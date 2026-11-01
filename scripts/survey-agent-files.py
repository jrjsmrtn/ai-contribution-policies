#!/usr/bin/env python3
"""Enumerate the agent-instruction files a repository carries.

Usage: survey-agent-files.py <owner/repo>[:<ref>] ...
       survey-agent-files.py --conventions      # print the list and its provenance
       survey-agent-files.py --self-test

Why this exists
---------------
Twice on 2026-09-08/09 a record in `ai-contribution-policies` reported that a project carried no
agent-instruction files, and twice it was wrong, because the probe used a filename list
reconstructed from memory:

  * **osquery** was recorded as having none. It carries `.cursor/rules/build-format.mdc` and
    `.cursorignore`. The probe looked for `.cursorrules`, the *legacy single-file* name, and the
    current convention is a **directory**.
  * **LLVM** was reached for a different reason and turned out to carry
    `.github/instructions/*.instructions.md` with `applyTo:` glob frontmatter -- a convention no
    earlier probe had included at all.

Both are the same failure: **a pattern that matches less than you think, reported as an absence.**
The list below is the fix. It lives in one place, in code, so a sweep cannot quietly use a shorter
one.

It also reports the **git file mode**, because a third error came from reading bytes instead of
structure: `raw.githubusercontent.com` serves a symlink by returning its *target path* as the
content, so a symlinked `CLAUDE.md` fetches as a 9-byte file containing the string `AGENTS.md` and
looks exactly like a hand-written stub. Six records described symlinks as "nine-byte pointer files"
before that was caught. Mode `120000` is a symlink; `100644` is a regular file.

Provenance of the list
----------------------
Entries marked OBSERVED were seen in a repository during the 2026-08/09 surveys. Entries marked
GITIGNORE come from `llvm/llvm-project`'s `.gitignore` block titled "Coding assistants' stuff",
which is a major project's own enumeration of the conventions it wants excluded -- evidence rather
than recollection. **Nothing here is included on the strength of memory alone.**

This is a survey tool, not a gate: it exits 0 whatever it finds, because "carries an agent file" is
not a fault.
"""

from __future__ import annotations

import json
import subprocess
import sys

# (path-or-prefix, kind, provenance, note)
#   kind: "file"   -> exact path
#         "prefix" -> any tracked path starting with this
CONVENTIONS: list[tuple[str, str, str, str]] = [
    ("AGENTS.md",                        "file",   "OBSERVED",  "cross-vendor; agents.md"),
    ("CLAUDE.md",                        "file",   "OBSERVED",  "Claude Code"),
    ("GEMINI.md",                        "file",   "OBSERVED",  "Gemini CLI"),
    ("instructions.md",                  "file",   "GITIGNORE", "listed by LLVM; not yet observed"),
    (".rules",                           "file",   "OBSERVED",  "Zed"),
    (".cursorrules",                     "file",   "OBSERVED",  "Cursor, LEGACY single-file form"),
    (".cursorignore",                    "file",   "OBSERVED",  "Cursor; EXCLUDES context, does not add it"),
    (".cursor/",                         "prefix", "OBSERVED",  "Cursor, current form: rules/*.mdc with alwaysApply"),
    (".github/copilot-instructions.md",  "file",   "OBSERVED",  "Copilot, repository-wide"),
    (".github/instructions/",            "prefix", "OBSERVED",  "Copilot, path-scoped: *.instructions.md with applyTo globs"),
    (".agents/",                         "prefix", "OBSERVED",  "cross-client; .agents/skills/*/SKILL.md"),
    (".claude/",                         "prefix", "OBSERVED",  "skills/, settings.json, hooks"),
    (".gemini/",                         "prefix", "GITIGNORE", "listed by LLVM"),
    (".codex/",                          "prefix", "GITIGNORE", "listed by LLVM"),
    ("usage-rules.md",                   "file",   "OBSERVED",  "Hex/Elixir; consolidated into a consumer's AGENTS.md"),
    ("usage-rules/",                     "prefix", "OBSERVED",  "directory form of the above"),
    ("AI_POLICY.md",                     "file",   "OBSERVED",  "policy, not instructions: Perl, ripgrep, Astral"),
    ("AI-DECLARATION.md",                "file",   "OBSERVED",  "self-declaration, not instructions: cdxgen"),
]

MODE_NAMES = {"120000": "symlink", "100644": "file", "100755": "exec", "040000": "tree"}


def tree(spec: str) -> tuple[str, list[tuple[str, str]]]:
    repo, _, ref = spec.partition(":")
    if not ref:
        out = subprocess.run(["gh", "api", f"repos/{repo}", "--jq", ".default_branch"],
                             capture_output=True, text=True)
        ref = out.stdout.strip() or "main"
    out = subprocess.run(
        ["gh", "api", f"repos/{repo}/git/trees/{ref}?recursive=1",
         "--jq", r'.tree[]? | select(.type=="blob") | "\(.mode)\t\(.path)"'],
        capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip()[:200])
    rows = [tuple(l.split("\t", 1)) for l in out.stdout.splitlines() if "\t" in l]
    return ref, rows


def match(rows: list[tuple[str, str]]) -> list[tuple[str, str, str]]:
    """Return (path, mode, note) for every convention hit."""
    hits = []
    for path, kind, _prov, note in CONVENTIONS:
        for mode, p in rows:
            if (kind == "file" and p == path) or (kind == "prefix" and p.startswith(path)):
                hits.append((p, MODE_NAMES.get(mode, mode), note))
    return sorted(set(hits))


def self_test() -> int:
    rows = [("100644", "AGENTS.md"), ("120000", "CLAUDE.md"),
            ("100644", ".cursor/rules/build-format.mdc"), ("100644", "src/main.rs")]
    hits = match(rows)
    paths = {h[0] for h in hits}
    bad = 0
    for want in ("AGENTS.md", "CLAUDE.md", ".cursor/rules/build-format.mdc"):
        if want in paths:
            print(f"  ok   {want} matched")
        else:
            print(f"FAIL: {want} not matched"); bad += 1
    if "src/main.rs" in paths:
        print("FAIL: unrelated file matched"); bad += 1
    else:
        print("  ok   unrelated file not matched")
    sym = [h for h in hits if h[0] == "CLAUDE.md"]
    if sym and sym[0][1] == "symlink":
        print("  ok   symlink reported as symlink, not as a small file")
    else:
        print(f"FAIL: symlink not identified -> {sym}"); bad += 1
    # the osquery regression: .cursorrules must NOT be what finds .cursor/rules/
    legacy = [c for c in CONVENTIONS if c[0] == ".cursorrules"]
    current = [c for c in CONVENTIONS if c[0] == ".cursor/"]
    if legacy and current:
        print("  ok   both the legacy .cursorrules and the current .cursor/ are listed")
    else:
        print("FAIL: Cursor conventions incomplete"); bad += 1
    print("self-test PASSED" if not bad else f"self-test FAILED ({bad})")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    if argv and argv[0] == "--self-test":
        return self_test()
    if argv and argv[0] == "--conventions":
        print(f"{len(CONVENTIONS)} conventions checked:\n")
        for path, kind, prov, note in CONVENTIONS:
            print(f"  {path:34s} {kind:6s} {prov:9s} {note}")
        print("\nOBSERVED = seen in a repository during the 2026-08/09 surveys.")
        print("GITIGNORE = enumerated by llvm/llvm-project's 'Coding assistants' stuff' block.")
        return 0
    if not argv:
        print(f"usage: survey-agent-files.py <owner/repo>[:<ref>] ... | --conventions | --self-test",
              file=sys.stderr)
        return 2
    for spec in argv:
        try:
            ref, rows = tree(spec)
        except Exception as e:
            print(f"{spec}: {e}", file=sys.stderr)
            continue
        hits = match(rows)
        print(f"{spec.partition(':')[0]} @ {ref}  ({len(rows)} tracked files)")
        if not hits:
            print(f"  none of the {len(CONVENTIONS)} conventions present")
        for p, mode, note in hits:
            print(f"  {mode:8s} {p:44s} {note}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
