#!/usr/bin/env python3
"""Detect changes in the primary sources a knowledge bundle cites. ADR-0013.

WHY
  `stale_after` catches a record that has aged. It cannot catch a policy that changed last week.
  On 2026-09-14 three records in ai-contribution-policies were wrong with every gate green: Rust
  had adopted its policy, Fedora's had been published all along, Asahi Linux had rewritten its
  own. Rust's and Fedora's `stale_after` were still seven weeks away. This fetches every source the
  bundle cites, fingerprints what it says, and reports what moved since the last run.
  It edits nothing. A change is a reason to re-read a primary, never a verdict about it.

WHAT COUNTS AS A CHANGE
  * URLs pinned to a commit (a 40-hex SHA, /commit/<sha>, ?id=<sha>) are not fetched: they
    cannot move.
  * GitHub pull requests and issues are fingerprinted by STATE (open/closed, merged, head SHA),
    not by page text, so a new comment is not a change and a merge is. That is the signal the
    Rust record needed.
  * GitHub tree listings are fingerprinted by path, file mode and type, so a commit elsewhere in the
    repository is not a change and a symlink becoming a regular file is. Commit searches are
    fingerprinted by their result count.
  * Everything else is fetched with curl and hashed as text. HTML is first reduced to its main
    content: <aside>, <nav>, <footer> and blocks marked as asides, sidebars or related links are
    dropped, then the largest <article> or <main> is used when it holds enough of the page. Measured
    2026-09-15 on the 63 HTML sources: it removed sidebar, navigation, build-timestamp and
    star-count churn, no page kept under 30% of its text, and all 47 quotations the bundle
    attributes to those pages survived.

HONEST LIMITS
  * A page that differs between two fetches seconds apart is marked VOLATILE the first time it
    is seen and is never reported as changed. Slower noise (relative dates, rotating banners)
    will still show as CHANGED, so the report prints the lines that moved and a person decides.
  * A challenge page (Anubis) is BLOCKED, never a change. HTTP 200 proves the server answered,
    not that the document arrived.
  * The first run only records a baseline, and says so. When the fingerprinting itself changes,
    NORMALISER is bumped and every source is re-baselined silently on the next run, reported as
    REBASELINED rather than CHANGED.
  * State lives outside the repository: it is derived, disposable, and machine-local.
    Delete the state directory to re-baseline everything.

USAGE
  check-primary-drift.py [--state-dir DIR] [--summary-file F] [--no-save] KNOWLEDGE_DIR...
  check-primary-drift.py --self-test
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import difflib
import hashlib
import html
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("check-primary-drift: PyYAML is required")

# NOT a browser-like user agent, measured 2026-09-14. With "Mozilla/5.0 (…)" the first baseline
# run lost 16 of 138 sources: Anubis served a challenge page on docs/forge.fedoraproject.org,
# git.kernel.org and gitlab.freedesktop.org, and gitlab.gnome.org answered HTTP 406. The same
# URLs returned the documents with this user agent. Anubis challenges clients that claim to be
# browsers; a tool that says what it is gets the file.
UA = "bundle-source-watch/1.0"
IMMUTABLE_SHA = re.compile(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")
IMMUTABLE_PATH = re.compile(r"/commit/[0-9a-f]{7,40}(?:[/?#]|$)|[?&]id=[0-9a-f]{7,40}(?:&|$)")
GH_STATE = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/(pull|issues)/(\d+)/?$")
GH_API = re.compile(r"^https://api\.github\.com/(.+)$")
# Bot walls seen on cited hosts: Anubis ("Making sure you're not a bot"), Cloudflare ("Just a
# moment"), and on lists.debian.org a Varnish proof-of-work page titled "I Challenge Thee" that sets a
# pow_challenge cookie — missed by the first baseline run on 2026-09-14, which stored it as the
# document and reported the real page as a change on the next run.
#
# Match the MARKUP of a challenge page, never a bare word. Until 2026-09-15 this matched "anubis"
# anywhere, which would report any policy page that merely mentions Anubis as BLOCKED; it surfaced
# when a MacPorts mailing-list index titled "Trac now behind Anubis AI crawler protection" tripped the
# same pattern. The markers below were taken from real challenge pages served that day.
CHALLENGE = re.compile(
    r"id=\"anubis_challenge\"|/\.within\.website/x/cmd/anubis/"      # Anubis
    r"|<title>\s*making sure you(?:'|&#39;|’)re not a bot"            # Anubis, title
    r"|<title>\s*just a moment"                                        # Cloudflare
    r"|<title>\s*i challenge thee|pow_challenge=",                      # Varnish proof of work
    re.I)
NORMALISER = 2   # bump whenever fingerprinting changes; a stored mismatch re-baselines, never reports
TREE_PATH = re.compile(r"^repos/[^/]+/[^/]+/git/trees/")
BLOCK_OPEN = re.compile(r"(?is)<(aside|nav|footer|div|section)\b([^>]*)>")
DROP_CLASS = re.compile(r'(?is)\bclass\s*=\s*["\'][^"\']*\b(?:aside|sidebar|related|more-like-this)\b')
DROP_DATA = re.compile(r'(?is)\bdata-[a-z-]+\s*=\s*["\'](?:more-like-this|related[^"\']*)["\']')
DEFAULT_STATE = pathlib.Path(__file__).resolve().parent.parent / ".okf" / "cache" / "source-watch" / "primary"
WORKERS = 8


def collect_sources(knowledge_dirs) -> dict[str, set[str]]:
    cited: dict[str, set[str]] = {}
    for d in knowledge_dirs:
        root = pathlib.Path(d)
        if not (root / "index.md").is_file():  # <!-- historical-filename: names the SIBLING bundle layout; no knowledge/ in this repo since ADR-0005 -->
            raise SystemExit(f"check-primary-drift: {d} is not a bundle root (no index.md)")  # <!-- historical-filename: names the SIBLING bundle layout; no knowledge/ in this repo since ADR-0005 -->
        for p in sorted(root.rglob("*.md")):
            if p.name in ("index.md", "log.md"):  # <!-- historical-filename: names the SIBLING bundle layout; no knowledge/ in this repo since ADR-0005 -->
                continue
            text = p.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                continue
            try:
                fm = yaml.safe_load(text.split("---\n", 2)[1]) or {}
            except yaml.YAMLError as e:
                raise SystemExit(f"check-primary-drift: cannot parse frontmatter in {p}: {e}")
            for s in fm.get("sources") or []:
                url = (s or {}).get("resource")
                if url:
                    cited.setdefault(url, set()).add(f"{root.parent.name}/{p.relative_to(root)}")
    return cited


def classify(url: str) -> str:
    if IMMUTABLE_SHA.search(url) or IMMUTABLE_PATH.search(url):
        return "immutable"
    if GH_STATE.match(url):
        return "gh-state"
    if GH_API.match(url):
        return "gh-api"
    return "page"


def normalise(text: str) -> str:
    lines = (re.sub(r"[ \t ]+", " ", line).strip() for line in text.splitlines())
    return "\n".join(line for line in lines if line)


def visible_text(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript|svg|template)\b.*?</\1\s*>", " ", raw)
    raw = re.sub(r"(?s)<!--.*?-->", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h[1-6]|tr|pre|blockquote|section|article|header|footer)\s*>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return normalise(html.unescape(raw))


def _matching_close(raw: str, tag: str, pos: int):
    depth = 1
    for m in re.compile(rf"(?is)<(/?){tag}\b[^>]*>").finditer(raw, pos):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return m.end()
    return None


def drop_blocks(raw: str) -> str:
    """Remove navigation, footers and sidebar-like blocks, nesting-aware."""
    out, i = [], 0
    while True:
        m = BLOCK_OPEN.search(raw, i)
        if not m:
            out.append(raw[i:])
            return "".join(out)
        tag, attrs = m.group(1).lower(), m.group(2)
        if tag in ("aside", "nav", "footer") or DROP_CLASS.search(attrs) or DROP_DATA.search(attrs):
            out.append(raw[i:m.start()])
            end = None if attrs.rstrip().endswith("/") else _matching_close(raw, tag, m.end())
            i = end if end is not None else m.end()
        else:
            out.append(raw[i:m.end()])
            i = m.end()


def _outermost(raw: str, tag: str):
    found, depth, start = [], 0, None
    for m in re.finditer(rf"(?is)<(/?){tag}\b[^>]*>", raw):
        if not m.group(1):
            if depth == 0:
                start = m.end()
            depth += 1
        elif depth:
            depth -= 1
            if depth == 0 and start is not None:
                found.append(raw[start:m.start()])
    return found


def page_text(raw: str) -> str:
    """The text that identifies a page's content, with page furniture removed."""
    full = visible_text(raw)
    cleaned = drop_blocks(re.sub(r"(?is)<(script|style|noscript|svg|template)\b.*?</\1\s*>", " ", raw))
    for tag in ("article", "main"):
        best = max((visible_text(e) for e in _outermost(cleaned, tag)), key=len, default="")
        if len(best) >= 200 and len(best) >= 0.2 * len(full):
            return best
    trimmed = visible_text(cleaned)
    return trimmed if len(trimmed) >= 200 and len(trimmed) >= 0.2 * len(full) else full


def reduce_gh(path: str, data):
    """Keep the part of a GitHub API response that carries the signal."""
    if TREE_PATH.match(path) and isinstance(data, dict) and isinstance(data.get("tree"), list):
        return sorted(({"path": e.get("path"), "mode": e.get("mode"), "type": e.get("type")} for e in data["tree"]),
                      key=lambda e: e["path"] or "")
    if path.startswith("search/") and isinstance(data, dict) and "total_count" in data:
        return {"total_count": data["total_count"], "incomplete_results": data.get("incomplete_results")}
    return data


def gh_json(path: str, jq: str | None) -> dict:
    cmd = ["gh", "api", path] + (["--jq", jq] if jq else [])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except (OSError, subprocess.TimeoutExpired) as e:
        return {"status": "error", "detail": f"gh: {e}"}
    if r.returncode != 0:
        last = (r.stderr.strip().splitlines() or ["failed"])[-1]
        return {"status": "error", "detail": f"gh api: {last[:160]}"}
    try:
        data = json.loads(r.stdout)
        return {"status": "ok", "text": json.dumps(data if jq else reduce_gh(path, data), sort_keys=True, indent=1)}
    except json.JSONDecodeError:
        return {"status": "ok", "text": normalise(r.stdout)}


def curl_text(url: str) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        body = pathlib.Path(tmp) / "body"
        try:
            r = subprocess.run(
                ["curl", "-sSL", "--max-time", "45", "--retry", "1", "-A", UA,
                 "-o", str(body), "-w", "%{http_code}\t%{content_type}", url],
                capture_output=True, text=True, timeout=120)
        except (OSError, subprocess.TimeoutExpired) as e:
            return {"status": "error", "detail": f"curl: {e}"}
        if r.returncode != 0:
            return {"status": "error", "detail": f"curl exit {r.returncode}: {r.stderr.strip()[:120]}"}
        code, _, ctype = r.stdout.partition("\t")
        raw = body.read_bytes().decode("utf-8", "replace") if body.exists() else ""
    if CHALLENGE.search(raw[:50000]):
        return {"status": "blocked", "detail": f"challenge page (HTTP {code})"}
    if code != "200":
        return {"status": "error", "detail": f"HTTP {code}"}
    looks_html = "html" in ctype.lower() or raw.lstrip()[:100].lower().startswith(("<!doctype", "<html"))
    text = page_text(raw) if looks_html else normalise(raw)
    if not text:
        return {"status": "error", "detail": "empty body"}
    return {"status": "ok", "text": text}


def fetch_live(url: str) -> dict:
    kind = classify(url)
    if kind == "gh-state":
        owner, repo, what, num = GH_STATE.match(url).groups()
        if what == "pull":
            return gh_json(f"repos/{owner}/{repo}/pulls/{num}",
                           "{state, merged: (.merged_at != null), merged_at, head: .head.sha, draft}")
        return gh_json(f"repos/{owner}/{repo}/issues/{num}", "{state, state_reason}")
    if kind == "gh-api":
        return gh_json(GH_API.match(url).group(1), None)
    return curl_text(url)


def snippet(old: str, new: str, limit: int = 12) -> list[str]:
    moved = [line for line in difflib.unified_diff(old.splitlines(), new.splitlines(), lineterm="", n=0)
             if line[:1] in "+-" and not line.startswith(("+++", "---"))]
    shown = [line if len(line) <= 160 else line[:157] + "..." for line in moved[:limit]]
    if len(moved) > limit:
        shown.append(f"... {len(moved) - limit} more changed line(s)")
    return shown or ["(no stored text to compare; the fingerprint changed)"]


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def run(knowledge_dirs, state_dir, fetch, save=True, now=None, pause=2.0, workers=WORKERS) -> dict:
    now = now or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    state_dir = pathlib.Path(state_dir)
    texts = state_dir / "text"
    index_path = state_dir / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {}

    cited = collect_sources(knowledge_dirs)
    if not cited:
        raise SystemExit("check-primary-drift: no cited sources found — refusing to report a clean result")

    rep = {k: [] for k in ("changed", "new", "rebaselined", "volatile", "blocked", "error", "unchanged")}
    rep["immutable"] = sorted(u for u in cited if classify(u) == "immutable")
    live = sorted(u for u in cited if classify(u) != "immutable")

    with cf.ThreadPoolExecutor(workers) as ex:
        first = dict(zip(live, ex.map(fetch, live)))
    def current(entry):
        return bool(entry.get("hash")) and entry.get("normaliser") == NORMALISER
    fresh = [u for u in live if first[u]["status"] == "ok" and not current(index.get(u) or {})]
    second = {}
    if fresh:
        if pause:
            time.sleep(pause)
        with cf.ThreadPoolExecutor(workers) as ex:
            second = dict(zip(fresh, ex.map(fetch, fresh)))

    for u in live:
        r, prev = first[u], (index.get(u) or {})
        item = {"url": u, "records": sorted(cited[u])}
        entry = dict(prev)
        entry.update(kind=classify(u), records=item["records"], last_checked=now, status=r["status"])
        if r["status"] != "ok":
            entry["detail"] = r.get("detail", "")
            rep[r["status"]].append({**item, "detail": entry["detail"]})
            index[u] = entry
            continue
        entry.pop("detail", None)
        h = sha256(r["text"])
        tfile = texts / (hashlib.sha1(u.encode("utf-8")).hexdigest() + ".txt")
        entry["normaliser"] = NORMALISER
        if not current(prev):
            s = second.get(u) or {}
            volatile = s.get("status") == "ok" and sha256(s["text"]) != h
            if prev.get("hash"):
                entry.update(hash=h, volatile=volatile)
                rep["rebaselined"].append({**item, "volatile": volatile})
            else:
                entry.update(hash=h, first_seen=now, last_changed=now, volatile=volatile)
                rep["new"].append({**item, "volatile": volatile})
        elif prev.get("volatile"):
            entry["hash"] = h
            rep["volatile"].append(item)
        elif h != prev["hash"]:
            old = tfile.read_text(encoding="utf-8") if tfile.exists() else ""
            rep["changed"].append({**item, "since": prev.get("last_changed") or prev.get("first_seen"),
                                   "diff": snippet(old, r["text"])})
            entry.update(hash=h, last_changed=now)
        else:
            rep["unchanged"].append(item)
        index[u] = entry
        if save:
            texts.mkdir(parents=True, exist_ok=True)
            tfile.write_text(r["text"], encoding="utf-8")

    rep["retired"] = sorted(u for u in index if u not in cited)
    for u in rep["retired"]:
        index.pop(u)
    if save:
        state_dir.mkdir(parents=True, exist_ok=True)
        tmp = index_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(index, indent=1, sort_keys=True), encoding="utf-8")
        tmp.replace(index_path)
    rep.update(cited=len(cited), checked=len(live), when=now)
    return rep


def print_report(rep: dict) -> None:
    print(f"=== primary-source drift, {rep['when']} ===")
    print(f"sources: {rep['cited']} cited, {len(rep['immutable'])} pinned to a commit (not fetched), "
          f"{rep['checked']} checked")
    if rep["changed"]:
        print(f"\nCHANGED ({len(rep['changed'])}) — re-read these primaries before trusting the records:")
        for c in rep["changed"]:
            print(f"  {c['url']}")
            print(f"    records: {', '.join(c['records'])}")
            print(f"    last changed before this: {c['since']}")
            for line in c["diff"]:
                print(f"      {line}")
    for key, title in (("blocked", "BLOCKED — a challenge page, not the document"), ("error", "UNREACHABLE")):
        if rep[key]:
            print(f"\n{title} ({len(rep[key])}):")
            for c in rep[key]:
                print(f"  {c['url']} — {c['detail']} [{', '.join(c['records'])}]")
    if rep["new"]:
        vol = [c for c in rep["new"] if c["volatile"]]
        print(f"\nBASELINED ({len(rep['new'])}) — first sight, nothing to compare yet"
              + (f"; {len(vol)} volatile" if vol else ""))
        for c in vol:
            print(f"  volatile: {c['url']}")
    if rep["rebaselined"]:
        vol = [c for c in rep["rebaselined"] if c["volatile"]]
        print(f"\nREBASELINED ({len(rep['rebaselined'])}) — fingerprinting changed (normaliser {NORMALISER}); "
              "stored afresh, no change reported" + (f"; {len(vol)} volatile" if vol else ""))
        for c in vol:
            print(f"  volatile: {c['url']}")
    if rep["volatile"]:
        print(f"\nVOLATILE ({len(rep['volatile'])}) — differed between fetches seconds apart; changes ignored")
    if rep["retired"]:
        print(f"\nRETIRED ({len(rep['retired'])}) — no longer cited, dropped from state")
    print(f"\nunchanged: {len(rep['unchanged'])}")


def summary(rep: dict) -> str:
    names = sorted({r.rsplit("/", 1)[-1].removesuffix(".md") for c in rep["changed"] for r in c["records"]})
    parts = []
    if rep["changed"]:
        more = "…" if len(names) > 6 else ""
        parts.append(f"{len(rep['changed'])} source(s) changed: {', '.join(names[:6])}{more}")
    unreachable = len(rep["blocked"]) + len(rep["error"])
    if unreachable:
        parts.append(f"{unreachable} unreachable")
    if rep["new"] and not rep["changed"] and not rep["unchanged"] and not rep["volatile"] and not rep["rebaselined"]:
        parts.append(f"baseline recorded for {len(rep['new'])} sources")
    if rep["rebaselined"] and not rep["changed"]:
        parts.append(f"fingerprints refreshed for {len(rep['rebaselined'])} sources")
    return "; ".join(parts) or "no primary-source changes"


def self_test() -> int:
    checks = 0

    def ok(cond, msg):
        nonlocal checks
        checks += 1
        if not cond:
            raise AssertionError(msg)

    with tempfile.TemporaryDirectory() as tmp:
        bundle = pathlib.Path(tmp) / "fixture-bundle" / "knowledge"
        (bundle / "projects").mkdir(parents=True)
        (bundle / "index.md").write_text("# fixture\n")  # <!-- historical-filename: names the SIBLING bundle layout; no knowledge/ in this repo since ADR-0005 -->
        pinned = "https://example.com/pinned/" + "a" * 40
        u = {"page": "https://example.com/policy", "pr": "https://github.com/example/repo/pull/1",
             "vol": "https://example.org/volatile", "blk": "https://example.net/blocked"}

        def record(name, srcs):
            items = "".join(f"  - id: s{i}\n    title: t\n    resource: {s}\n" for i, s in enumerate(srcs))
            (bundle / "projects" / f"{name}.md").write_text(
                f"---\ntype: Organization\ntitle: {name}\nsources:\n{items}---\nbody\n")

        record("alpha", [u["page"], pinned, u["vol"]])
        record("beta", [u["pr"], u["blk"], u["page"]])
        world = {"page": "Policy v1\nMUST disclose.", "pr": '{"state": "open", "merged": false}'}
        calls = {"vol": 0}
        fetched = []

        def fake(url):
            fetched.append(url)
            if url == u["page"]:
                return {"status": "ok", "text": world["page"]}
            if url == u["pr"]:
                return {"status": "ok", "text": world["pr"]}
            if url == u["vol"]:
                calls["vol"] += 1
                return {"status": "ok", "text": f"Generated at request {calls['vol']}"}
            if url == u["blk"]:
                return {"status": "blocked", "detail": "challenge page (HTTP 200)"}
            raise AssertionError(f"unexpected fetch of {url}")

        state = pathlib.Path(tmp) / "state"
        r1 = run([bundle], state, fake, pause=0)
        ok(pinned not in fetched, "a commit-pinned URL was fetched")
        ok(r1["immutable"] == [pinned], "a commit-pinned URL was not reported as skipped")
        ok(not r1["changed"], "the baseline run reported changes")
        ok({c["url"] for c in r1["new"]} == {u["page"], u["pr"], u["vol"]}, "baseline did not cover every reachable source")
        ok([c["url"] for c in r1["new"] if c["volatile"]] == [u["vol"]], "volatility misdetected")
        ok([c["url"] for c in r1["blocked"]] == [u["blk"]], "a challenge page was not reported as blocked")
        page_new = next(c for c in r1["new"] if c["url"] == u["page"])
        ok(page_new["records"] == ["fixture-bundle/projects/alpha.md", "fixture-bundle/projects/beta.md"],
           "a source cited by two records lost one of them")

        r2 = run([bundle], state, fake, pause=0)
        ok(not r2["changed"], f"a quiet run reported changes: {r2['changed']}")
        ok([c["url"] for c in r2["volatile"]] == [u["vol"]], "a volatile page was reported as something else")
        ok(summary(r2) == "1 unreachable", f"quiet-run summary wrong: {summary(r2)!r}")

        world["page"] = "Policy v2\nMUST NOT disclose."
        world["pr"] = '{"state": "closed", "merged": true}'
        r3 = run([bundle], state, fake, pause=0)
        ok({c["url"] for c in r3["changed"]} == {u["page"], u["pr"]},
           f"planted changes not both reported: {[c['url'] for c in r3['changed']]}")
        page_change = next(c for c in r3["changed"] if c["url"] == u["page"])
        ok(any("MUST NOT disclose" in line for line in page_change["diff"]), "a change was reported without what moved")
        ok(u["blk"] not in {c["url"] for c in r3["changed"]}, "a blocked source was reported as changed")
        ok(summary(r3).startswith("2 source(s) changed: alpha, beta"), f"change summary wrong: {summary(r3)!r}")

        record("beta", [u["page"]])
        r4 = run([bundle], state, fake, pause=0)
        ok(set(r4["retired"]) == {u["pr"], u["blk"]}, f"uncited sources not retired: {r4['retired']}")

        before = (state / "index.json").read_text()
        world["page"] = "Policy v3"
        r5 = run([bundle], state, fake, save=False, pause=0)
        ok([c["url"] for c in r5["changed"]] == [u["page"]], "a change was missed under --no-save")
        ok((state / "index.json").read_text() == before, "--no-save wrote state")

        empty = pathlib.Path(tmp) / "empty" / "knowledge"
        empty.mkdir(parents=True)
        (empty / "index.md").write_text("# empty\n")  # <!-- historical-filename: names the SIBLING bundle layout; no knowledge/ in this repo since ADR-0005 -->
        try:
            run([empty], pathlib.Path(tmp) / "state2", fake, pause=0)
            ok(False, "a bundle citing nothing reported a clean result")
        except SystemExit:
            ok(True, "")

        base = ('<html><body><nav>Home Docs Blog</nav><div role="main"><article class="post">'
                '<h1>AI policy</h1><p>' + "Contributors MUST disclose AI assistance. " * 10 + '</p>'
                '<div class="col aside"><div data-rhdc-block="more-like-this"><h3>{side}</h3></div></div>'
                '</article></div><footer>Last build: {ts}</footer></body></html>')
        pa = page_text(base.format(side="Related post one", ts="2026-09-14 11:50"))
        pb = page_text(base.format(side="A different related post", ts="2026-09-15 17:50"))
        ok(pa == pb, "sidebar or footer churn changed the page fingerprint")
        ok("MUST disclose" in pa and "Related post" not in pa and "Last build" not in pa and "Home Docs" not in pa,
           "main-content extraction kept page furniture or lost the policy text")
        ok(page_text(base.replace("MUST disclose", "MUST NOT disclose").format(side="x", ts="y")) != pa,
           "a change inside the article did not change the fingerprint")
        bare = "<html><body><p>" + "A short policy page with no article or main element. " * 8 + "</p></body></html>"
        ok("no article or main element" in page_text(bare), "a page without article or main lost its text")
        tp = "repos/o/r/git/trees/main"
        t1 = {"sha": "a" * 40, "tree": [{"path": "AGENTS.md", "mode": "120000", "type": "blob", "sha": "1" * 40, "url": "u1"}]}
        t2 = {"sha": "b" * 40, "tree": [{"path": "AGENTS.md", "mode": "120000", "type": "blob", "sha": "2" * 40, "url": "u2"}]}
        t3 = {"sha": "c" * 40, "tree": [{"path": "AGENTS.md", "mode": "100644", "type": "blob", "sha": "2" * 40, "url": "u2"}]}
        ok(reduce_gh(tp, t1) == reduce_gh(tp, t2), "per-commit tree SHAs changed a tree fingerprint")
        ok(reduce_gh(tp, t1) != reduce_gh(tp, t3), "a symlink becoming a regular file was lost")
        sp = "search/commits?q=repo:o/r+x"
        ok(reduce_gh(sp, {"total_count": 5, "incomplete_results": False, "items": [{"score": 1}]})
           == reduce_gh(sp, {"total_count": 5, "incomplete_results": False, "items": [{"score": 2}]}),
           "search result ordering changed a search fingerprint")
        ok(reduce_gh(sp, {"total_count": 5, "incomplete_results": False})
           != reduce_gh(sp, {"total_count": 6, "incomplete_results": False}), "a new matching commit was not reflected")
        nb = pathlib.Path(tmp) / "norm-bundle" / "knowledge"
        (nb / "p").mkdir(parents=True)
        (nb / "index.md").write_text("# n\n")  # <!-- historical-filename: names the SIBLING bundle layout; no knowledge/ in this repo since ADR-0005 -->
        (nb / "p" / "x.md").write_text("---\ntype: Organization\ntitle: x\nsources:\n  - id: s\n    title: t\n"
                                       "    resource: https://example.com/norm\n---\nbody\n")
        txt = {"v": "Policy text A"}
        fetch_norm = lambda url: {"status": "ok", "text": txt["v"]}
        ns = pathlib.Path(tmp) / "state-norm"
        run([nb], ns, fetch_norm, pause=0)
        idx = json.loads((ns / "index.json").read_text())
        for e in idx.values():
            e["normaliser"] = NORMALISER - 1
        (ns / "index.json").write_text(json.dumps(idx))
        txt["v"] = "Policy text A, fingerprinted by a newer normaliser"
        rn = run([nb], ns, fetch_norm, pause=0)
        ok(not rn["changed"] and [c["url"] for c in rn["rebaselined"]] == ["https://example.com/norm"],
           "a fingerprinting change was reported as a change in the source")
        rq = run([nb], ns, fetch_norm, pause=0)
        ok(not rq["changed"] and not rq["rebaselined"] and len(rq["unchanged"]) == 1, "the run after re-baselining was not quiet")
        ok(classify("https://git.kernel.org/x/patch/?id=816d9992d9ed434ec52cfbd63080d518e535a41b") == "immutable", "kernel patch URL not pinned")
        ok(classify("https://gitlab.gnome.org/GNOME/gtk/-/commit/e76acf1c991a") == "immutable", "short commit URL not pinned")
        ok(classify("https://github.com/rust-lang/rfcs/pull/3959") == "gh-state", "PR URL not state-tracked")
        ok(classify("https://raw.githubusercontent.com/o/r/main/AGENTS.md") == "page", "branch file treated as pinned")
        ok(CHALLENGE.search("<title>Making sure you're not a bot!</title>") is not None, "Anubis page not recognised")
        ok(CHALLENGE.search('<script id="anubis_challenge" type="application/json">') is not None,
           "Anubis challenge markup not recognised")
        ok(CHALLENGE.search("<title>Heads-up: MacPorts Trac now behind Anubis AI crawler protection</title>"
                            "<pre>Visitors will see a proof-of-work JavaScript prompt [1]: https://anubis.techaro.lol/</pre>") is None,
           "a page that merely mentions Anubis was treated as a challenge page")
        ok(CHALLENGE.search("<title>I Challenge Thee</title><script>document.cookie.match(/pow_challenge=/)") is not None,
           "Varnish proof-of-work page not recognised")
        ok("mozilla" not in UA.lower(), "the user agent claims to be a browser, which Anubis-protected hosts challenge")
        ok("secret" not in visible_text("<p>a</p><script>secret()</script><style>x{}</style>"), "script text leaked into the fingerprint")

    print(f"self-test OK ({checks} checks; every planted fault was reported)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Report changes in a bundle's cited primary sources.")
    ap.add_argument("bundles", nargs="*", help="bundle knowledge/ directories")
    ap.add_argument("--state-dir", default=os.environ.get("SOURCE_WATCH_PRIMARY_STATE", str(DEFAULT_STATE)))
    ap.add_argument("--summary-file", help="write a one-line summary here, for the notification")
    ap.add_argument("--no-save", action="store_true", help="report without updating state")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        try:
            return self_test()
        except AssertionError as e:
            print(f"self-test FAILED: {e}", file=sys.stderr)
            return 1
    if not a.bundles:
        ap.error("give at least one bundle knowledge/ directory")
    for tool in ("curl", "gh"):
        if not shutil.which(tool):
            print(f"check-primary-drift: {tool} not on PATH — cannot check sources", file=sys.stderr)
            return 1
    rep = run(a.bundles, a.state_dir, fetch_live, save=not a.no_save)
    print_report(rep)
    if a.summary_file:
        pathlib.Path(a.summary_file).write_text(summary(rep) + "\n", encoding="utf-8")
    unreachable = len(rep["blocked"]) + len(rep["error"])
    if rep["checked"] and unreachable * 2 > rep["checked"]:
        print(f"check-primary-drift: {unreachable} of {rep['checked']} sources unreachable — "
              "the check did not do its job", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
