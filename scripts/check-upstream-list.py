#!/usr/bin/env python3
"""Report what changed in melissawm/open-source-ai-contribution-policies since the last run. ADR-0013.

WHY
  That list is a LEAD list for ai-contribution-policies and nothing more (see the bundle's
  CLAUDE.md): no entry counts as evidence until its primary has been read. But it is updated by
  many people, and on 2026-09-14 a one-off diff against it surfaced three records of ours that
  had gone wrong before any gate could notice. This makes that diff routine.
  It reports; it never edits a record.

WHAT IT REPORTS
  commits since the last-seen SHA; policy-table rows added, removed or changed (link or
  "AI/LLMs allowed?" column); entries added to or removed from "Ongoing discussions" — and, for
  each, whether it touches a record we already have. A touched record is a re-verification
  prompt. An untouched addition is a lead.

STATE
  One JSON file holding the last-seen commit SHA, outside the repository. Seed it with
  --baseline <sha>. With no state and no baseline, the first run records HEAD, reports nothing,
  and says so rather than pretending the list is unchanged.

USAGE
  check-upstream-list.py [--bundle KNOWLEDGE_DIR] [--state FILE] [--baseline SHA]
                         [--summary-file F] [--no-save]
  check-upstream-list.py --self-test
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import unicodedata

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("check-upstream-list: PyYAML is required")

REPO = "melissawm/open-source-ai-contribution-policies"
HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_BUNDLE = HERE.parent / "knowledge"
DEFAULT_STATE = HERE.parent / ".okf" / "cache" / "source-watch" / "upstream-list.json"

# Where their row name differs from our record title. Authored judgement, established on
# 2026-09-14 by reading both sides — not a fuzzy match, which produced a false positive then.
NAME_ALIASES = {"cpython": "python", "gentoolinux": "gentoo", "openinfra": "openinfrafoundation",
                "ruff": "astral", "ty": "astral", "uv": "astral"}
HOST_ALIASES = {"gitlab.gnome.org": "gnome", "gjs.guide": "gnome"}


def norm(name: str) -> str:
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    name = re.sub(r"\(.*?\)", " ", name)
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def section(lines, heading):
    start = next((i for i, line in enumerate(lines) if line.startswith(heading)), None)
    if start is None:
        return None
    end = next((i for i, line in enumerate(lines) if i > start and line.startswith("## ")), len(lines))
    return lines[start:end]


def parse_readme(text: str):
    lines = text.splitlines()
    table = section(lines, "## Policies")
    if table is None:
        raise ValueError("no '## Policies' section — the README's shape changed")
    rows = {}
    for line in table:
        if not line.startswith("[") or "|" not in line:
            continue
        m = re.match(r"\[(.+?)\]\((\S+?)\)", line)
        if not m:
            continue
        cells = [c.strip() for c in line.split("|")]
        rows[m.group(1)] = {"urls": re.findall(r"\]\((\S+?)\)", line),
                            "allowed": cells[2] if len(cells) > 2 else ""}
    if not rows:
        raise ValueError("the Policies table parsed to zero rows — the README's shape changed")
    disc = section(lines, "## Ongoing discussions") or []
    discussions = sorted({m.group(1) for line in disc for m in [re.match(r"- \[(.+?)\]\(", line)] if m})
    return rows, discussions


def our_records(knowledge) -> dict[str, str]:
    out = {}
    for p in sorted(pathlib.Path(knowledge).rglob("*.md")):
        if p.name in ("index.md", "log.md"):  # <!-- historical-filename: names the SIBLING bundle layout; no knowledge/ in this repo since ADR-0005 -->
            continue
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        fm = yaml.safe_load(text.split("---\n", 2)[1]) or {}
        if fm.get("type") == "Organization" and fm.get("title"):
            out[norm(fm["title"])] = str(p.relative_to(knowledge))
    if not out:
        raise ValueError(f"no Organization records under {knowledge}")
    return out


def match(name: str, row: dict, ours: dict) -> str | None:
    key = norm(name)
    key = NAME_ALIASES.get(key, key)
    if key in ours:
        return ours[key]
    for url in row.get("urls", []):
        host = re.sub(r"^https?://([^/]+).*$", r"\1", url).lower().removeprefix("www.")
        if HOST_ALIASES.get(host) in ours:
            return ours[HOST_ALIASES[host]]
    return None


def diff(old_rows, new_rows, old_disc, new_disc) -> dict:
    return {
        "added": sorted(set(new_rows) - set(old_rows), key=str.lower),
        "removed": sorted(set(old_rows) - set(new_rows), key=str.lower),
        "changed": sorted((n for n in set(old_rows) & set(new_rows) if old_rows[n] != new_rows[n]), key=str.lower),
        "disc_added": sorted(set(new_disc) - set(old_disc), key=str.lower),
        "disc_removed": sorted(set(old_disc) - set(new_disc), key=str.lower),
    }


def gh(*args) -> str:
    r = subprocess.run(["gh", "api", *args], capture_output=True, text=True, timeout=90)
    if r.returncode != 0:
        last = (r.stderr.strip().splitlines() or ["failed"])[-1]
        raise RuntimeError(f"gh api {args[0]}: {last}")
    return r.stdout


def readme_at(sha: str) -> str:
    url = f"https://raw.githubusercontent.com/{REPO}/{sha}/README.md"
    r = subprocess.run(["curl", "-sSfL", "--max-time", "60", url], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(f"README at {sha[:12]}: curl exit {r.returncode}")
    return r.stdout


def describe(name, row_old, row_new, ours):
    hit = match(name, row_new or row_old, ours)
    tag = f"ours: {hit}" if hit else "lead"
    bits = []
    if row_old and row_new:
        if row_old["allowed"] != row_new["allowed"]:
            bits.append(f"allowed {row_old['allowed'] or '?'} -> {row_new['allowed'] or '?'}")
        if row_old["urls"] != row_new["urls"]:
            gone = [u for u in row_old["urls"] if u not in row_new["urls"]]
            came = [u for u in row_new["urls"] if u not in row_old["urls"]]
            bits += [f"- {u}" for u in gone] + [f"+ {u}" for u in came]
    elif row_new:
        bits.append(f"allowed {row_new['allowed'] or '?'}; {row_new['urls'][1] if len(row_new['urls']) > 1 else row_new['urls'][0]}")
    return tag, bits


def write_state(path: pathlib.Path, sha: str, save: bool):
    if not save:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    path.write_text(json.dumps({"repo": REPO, "sha": sha, "checked_at": now}, indent=1) + "\n", encoding="utf-8")


def run_live(bundle, state_path: pathlib.Path, baseline, save) -> str:
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    old = state.get("sha") or baseline
    head = gh(f"repos/{REPO}/commits/HEAD", "--jq", ".sha").strip()
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise RuntimeError(f"unexpected HEAD value {head!r}")
    print(f"=== upstream lead list ({REPO}), {dt.datetime.now(dt.timezone.utc):%Y-%m-%dT%H:%M:%SZ} ===")
    if not old:
        print(f"no state and no --baseline: recorded HEAD {head[:12]} as the baseline; nothing compared")
        write_state(state_path, head, save)
        return "upstream list: baseline recorded"
    if old == head:
        print(f"no new commits since {head[:12]}")
        write_state(state_path, head, save)
        return "upstream list: no new commits"
    commits = gh(f"repos/{REPO}/compare/{old}...{head}", "--jq",
                 '.commits[] | "\\(.commit.committer.date[0:10]) \\(.sha[0:10]) \\(.commit.message | split("\\n")[0])"')
    commit_lines = [c for c in commits.splitlines() if c.strip()]
    o_rows, o_disc = parse_readme(readme_at(old))
    n_rows, n_disc = parse_readme(readme_at(head))
    ours = our_records(bundle)
    d = diff(o_rows, n_rows, o_disc, n_disc)
    print(f"{old[:12]} -> {head[:12]}: {len(commit_lines)} commit(s); table {len(o_rows)} -> {len(n_rows)} rows")
    for c in commit_lines[:30]:
        print(f"  {c}")
    touched = 0
    for key, title in (("changed", "CHANGED ROWS"), ("added", "ADDED ROWS"), ("removed", "REMOVED ROWS")):
        if not d[key]:
            continue
        print(f"\n{title} ({len(d[key])}):")
        for name in d[key]:
            tag, bits = describe(name, o_rows.get(name), n_rows.get(name), ours)
            touched += tag.startswith("ours")
            print(f"  {name}  [{tag}]")
            for b in bits:
                print(f"      {b}")
    for key, title in (("disc_added", "ONGOING DISCUSSIONS ADDED"), ("disc_removed", "ONGOING DISCUSSIONS REMOVED")):
        if d[key]:
            print(f"\n{title}: {', '.join(d[key])}")
    if not any(d.values()):
        print("\nno changes to the policy table or the discussions list")
    write_state(state_path, head, save)
    return (f"upstream list: {len(d['added'])} added, {len(d['changed'])} changed, "
            f"{len(d['removed'])} removed; {touched} touch our records")


OLD_FIXTURE = """# list

## Policies

Project | Policy link | AI/LLMs allowed? | Disclosure required? | Copyright? | Human in loop? | Notes
--- | --- | --- | --- | --- | --- | ---
[CPython](https://github.com/python/cpython) | [Policy](https://devguide.python.org/ai) | Yes | Yes | - | - |
[Foo](https://foo.example) | [Policy](https://foo.example/policy) | No | - | - | - |
[Gone](https://gone.example) | [Policy](https://gone.example/policy) | No | - | - | - |

## Ongoing discussions

- [Debian](https://www.debian.org/): [vote](https://lists.example.org/vote)

## Other references
"""

NEW_FIXTURE = OLD_FIXTURE.replace(
    "[CPython](https://github.com/python/cpython) | [Policy](https://devguide.python.org/ai) | Yes",
    "[CPython](https://github.com/python/cpython) | [Policy](https://devguide.python.org/ai) | No",
).replace(
    "[Gone](https://gone.example) | [Policy](https://gone.example/policy) | No | - | - | - |\n",
    "[Loupe](https://gitlab.gnome.org/GNOME/loupe) | [Policy](https://gitlab.gnome.org/GNOME/loupe/policy) | No | - | - | - |\n",
).replace(
    "- [Debian](https://www.debian.org/): [vote](https://lists.example.org/vote)",
    "- [Blender](https://www.blender.org/): [thread](https://devtalk.example.org/t/1)",
)


def self_test() -> int:
    checks = 0

    def ok(cond, msg):
        nonlocal checks
        checks += 1
        if not cond:
            raise AssertionError(msg)

    o_rows, o_disc = parse_readme(OLD_FIXTURE)
    n_rows, n_disc = parse_readme(NEW_FIXTURE)
    ok(len(o_rows) == 3 and len(n_rows) == 3, "fixture rows parsed wrongly")
    d = diff(o_rows, n_rows, o_disc, n_disc)
    ok(d["added"] == ["Loupe"], f"added row missed: {d['added']}")
    ok(d["removed"] == ["Gone"], f"removed row missed: {d['removed']}")
    ok(d["changed"] == ["CPython"], f"changed row missed: {d['changed']}")
    ok(d["disc_added"] == ["Blender"] and d["disc_removed"] == ["Debian"], "discussion changes missed")
    ok(not any(diff(o_rows, o_rows, o_disc, o_disc).values()), "identical READMEs reported a difference")
    ours = {"python": "projects/python.md", "gnome": "projects/gnome.md"}
    ok(match("CPython", n_rows["CPython"], ours) == "projects/python.md", "the CPython alias did not reach our record")
    ok(match("Loupe", n_rows["Loupe"], ours) == "projects/gnome.md", "a GNOME-hosted row did not reach our GNOME record")
    ok(match("Foo", n_rows["Foo"], ours) is None, "an unrelated row matched one of our records")
    ok(norm("Apache® Software Foundation (ASF)") == "apachesoftwarefoundation", "name normalisation drifted")
    for broken, why in (("# no table here\n", "missing section"),
                        ("## Policies\n\nProject | Link\n--- | ---\n\n## Ongoing discussions\n", "empty table")):
        try:
            parse_readme(broken)
            ok(False, f"a README with a {why} parsed as valid")
        except ValueError:
            ok(True, "")
    print(f"self-test OK ({checks} checks; every planted change was reported)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Report changes in the upstream AI-policy lead list.")
    ap.add_argument("--bundle", default=str(DEFAULT_BUNDLE), help="our bundle's knowledge/ directory")
    ap.add_argument("--state", default=os.environ.get("SOURCE_WATCH_UPSTREAM_STATE", str(DEFAULT_STATE)))
    ap.add_argument("--baseline", help="commit SHA to compare against when there is no state yet")
    ap.add_argument("--summary-file")
    ap.add_argument("--no-save", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        try:
            return self_test()
        except AssertionError as e:
            print(f"self-test FAILED: {e}", file=sys.stderr)
            return 1
    for tool in ("gh", "curl"):
        if not shutil.which(tool):
            print(f"check-upstream-list: {tool} not on PATH", file=sys.stderr)
            return 1
    if a.baseline and not re.fullmatch(r"[0-9a-f]{40}", a.baseline):
        ap.error("--baseline must be a full 40-character commit SHA")
    try:
        line = run_live(a.bundle, pathlib.Path(a.state), a.baseline, not a.no_save)
    except (RuntimeError, ValueError) as e:
        print(f"check-upstream-list: {e}", file=sys.stderr)
        line = f"upstream list: FAILED ({e})"
        if a.summary_file:
            pathlib.Path(a.summary_file).write_text(line + "\n", encoding="utf-8")
        return 1
    if a.summary_file:
        pathlib.Path(a.summary_file).write_text(line + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
