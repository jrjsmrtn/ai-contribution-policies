---
type: Practice
title: Agent-file pointers
description: Agent tools look for instructions under different filenames, so projects publish one file and point the other names at it. Every project in this bundle that does so uses a git symlink; the one that duplicated the content instead now maintains two documents that have already diverged. The byte counts that make symlinks look like small text files are a retrieval artifact.
resource: https://agents.md/
tags:
  - ai-contribution
  - mechanism
  - distribution
  - resolution
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:29:44Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:29:44Z'
stale_after: 2027-03-08
sources:
  - id: ptr-asahi-tree
    title: 'Repository tree, AsahiLinux/m1n1 at main — file modes for AGENTS.md, CLAUDE.md, GEMINI.md'
    resource: https://api.github.com/repos/AsahiLinux/m1n1/git/trees/main
  - id: ptr-elixir-tree
    title: 'Repository tree, elixir-lang/elixir at main — file mode for AGENTS.md'
    resource: https://api.github.com/repos/elixir-lang/elixir/git/trees/main
  - id: ptr-zed-tree
    title: 'Repository tree, zed-industries/zed at main — file modes for AGENTS.md, CLAUDE.md, GEMINI.md'
    resource: https://api.github.com/repos/zed-industries/zed/git/trees/main
  - id: ptr-osquery-cursor
    title: '.cursor/rules/build-format.mdc (osquery/osquery, master)'
    resource: https://raw.githubusercontent.com/osquery/osquery/master/.cursor/rules/build-format.mdc
  - id: ptr-cdxgen-agents
    title: 'AGENTS.md (cdxgen/cdxgen, master)'
    resource: https://raw.githubusercontent.com/cdxgen/cdxgen/master/AGENTS.md
  - id: ptr-cdxgen-copilot
    title: '.github/copilot-instructions.md (cdxgen/cdxgen, master)'
    resource: https://raw.githubusercontent.com/cdxgen/cdxgen/master/.github/copilot-instructions.md
---

**Different agents look for different filenames, and no specification says which.** `AGENTS.md`,
`CLAUDE.md`, `GEMINI.md`, `.rules`, `.github/copilot-instructions.md` — a project that wants its
instructions found by more than one tool has to answer for several names at once.

There are only two answers. **Publish once and point the other names at it, or publish the content
more than once.** Every project in this bundle that solves the problem takes the first; the one that
took the second has already drifted.

## The construction is a git symlink, in every case

| Project | Real file | Symlinked names |
|---|---|---|
| [Asahi Linux](../projects/asahi-linux.md) | `AGENTS.md` | `CLAUDE.md`, `GEMINI.md`[^ptr-asahi-tree] |
| [Zed](../projects/zed.md) | `.rules` | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`[^ptr-zed-tree] |
| [Elixir](../projects/elixir.md) | `CONTRIBUTING.md` | `AGENTS.md`[^ptr-elixir-tree] |
| [systemd](../projects/systemd.md) | `AGENTS.md` | `CLAUDE.md` |
| [Dependency-Track](../projects/dependency-track.md) | `AGENTS.md` | `CLAUDE.md` |
| [NetworkManager](../projects/networkmanager.md) | `AGENTS.md` | `CLAUDE.md` |

Git stores a symlink as mode `120000` with the target path as its content, so the whole mechanism
costs one tree entry per extra filename and **cannot drift by construction** — there is one document,
and the other names are aliases for it.

**Two variations are worth separating from the rest.** [Zed](../projects/zed.md) points three
agent-facing names at `.rules`, a filename that belongs to none of the tools, which decouples the
source of truth from any vendor's convention. And [Elixir](../projects/elixir.md) points the
agent-facing name at the **human-facing** document, so an agent and a contributor read identical text
and the project maintains one file rather than a human one and a machine one.

**NetworkManager's commit names the problem exactly**: *"AGENTS.md: add symlinks under the names other
agents look for"* (2026-09-04).

## The counter-example, and it has already diverged

[cdxgen](../projects/cdxgen.md) maintains **two real files**: `AGENTS.md` at 36,710 bytes[^ptr-cdxgen-agents]
and `.github/copilot-instructions.md` at 4,411 bytes,[^ptr-cdxgen-copilot] covering similar ground in
**different text**. Nothing asserts they agree, and at an eight-fold size difference they plainly do
not.

That is the predicted cost of the second answer, observed rather than hypothesised. It is not
negligence — Copilot's filename lives under `.github/` and a symlink there is a reasonable thing to
hesitate over — but it is the outcome the symlink construction exists to prevent.

## A retrieval hazard that produced a false finding in this bundle

`raw.githubusercontent.com` serves a symlink by returning **its target path as the file's content**.
A symlink named `CLAUDE.md` pointing at `AGENTS.md` therefore fetches as a 9-byte file containing the
string `AGENTS.md`, and looks exactly like a deliberately-written stub.

**This bundle recorded that mistake in six records before it was caught.** Asahi Linux's,
Dependency-Track's and systemd's `CLAUDE.md` files were described as *"nine-byte pointer files"*, and
contrasted unfavourably with the *"symlinks"* Elixir and NetworkManager had chosen — a distinction
between two things that are the same thing. The claim *"a pointer can go stale and a symlink cannot"*
was true in general and false about every example it was attached to.

**Check the mode, not the bytes**: `git ls-tree <ref> <path>` or the tree API returns `120000` for a
symlink and `100644` for a regular file. A fetch of the file contents cannot tell them apart, and the
fetched bytes are actively misleading because they look like a plausible stub.

This joins two hazards this bundle already documents — an Anubis challenge returning HTTP 200 with a
challenge page instead of the document, and `docs.kernel.org` serving a released kernel's retired
trailer format weeks after mainline changed it. **All three share a shape: the request succeeded, the
bytes were well-formed, and they did not mean what they appeared to mean.**

## One convention the construction does not reach

`.cursor/rules/` is a **directory** of `.mdc` files, not a single file, so there is no name to
symlink — [osquery](../projects/osquery.md) carries `.cursor/rules/build-format.mdc` alongside a
`.cursorignore`,[^ptr-osquery-cursor] and no amount of symlinking `AGENTS.md` would produce it. A project wanting to
answer that convention as well has to author separately, which is the duplication problem again in a
form the symlink cannot fix.

The format also does something none of the single-file conventions do. Its frontmatter carries
`alwaysApply: true`, and a field that can be true can be false: **the rule is conditionally
applied**, where `AGENTS.md` is loaded whole every time. That is the staging
[governing the instruction file](instruction-file-governance.md) says the single-file conventions
lack, present here as a format feature rather than as a discipline the maintainers have to keep.

**`.cursorignore` is a different artifact class again** — it tells the agent what *not* to read
(osquery excludes `libraries/` and `build/`). Every other file in this concept adds context; that one
subtracts it, and nothing else in this bundle does.

## What the mechanism does not solve

**Nothing obliges a tool to read any of these files.** The convention is that agents look for a name
they recognise; there is no specification requiring it, and a contributor pasting output from a chat
interface that never saw the repository is unaffected by every symlink in the tree.

**It does not settle which file should be canonical.** Pointing `AGENTS.md` at `CONTRIBUTING.md`
guarantees agents and humans read the same rules but forces one document to serve two audiences;
pointing `CLAUDE.md` at `AGENTS.md` keeps an agent-specific document at the cost of a second thing to
maintain. Both are defensible and the projects here split on it.

**And it multiplies reach without multiplying scrutiny.** One file now answers to three or four
names, so a change to it changes what every agent reads at once — which is the point, and also the
reason a repository-resident instruction file is worth treating as an unauthenticated instruction
channel rather than as documentation.

## What to watch

Whether `.github/copilot-instructions.md` starts being symlinked, which would remove the only
observed divergence. Whether Elixir's choice — pointing at the human document — spreads, since it is
the only variant that reduces the number of documents rather than the number of copies. And whether
any tool begins refusing to follow symlinks for instruction files, which would silently undo the
entire construction and is exactly the kind of change nothing in a repository would report.

[^ptr-asahi-tree]: [Repository tree, AsahiLinux/m1n1 at main — file modes for AGENTS.md, CLAUDE.md, GEMINI.md](https://api.github.com/repos/AsahiLinux/m1n1/git/trees/main)
[^ptr-elixir-tree]: [Repository tree, elixir-lang/elixir at main — file mode for AGENTS.md](https://api.github.com/repos/elixir-lang/elixir/git/trees/main)
[^ptr-zed-tree]: [Repository tree, zed-industries/zed at main — file modes for AGENTS.md, CLAUDE.md, GEMINI.md](https://api.github.com/repos/zed-industries/zed/git/trees/main)
[^ptr-osquery-cursor]: [.cursor/rules/build-format.mdc (osquery/osquery, master)](https://raw.githubusercontent.com/osquery/osquery/master/.cursor/rules/build-format.mdc)
[^ptr-cdxgen-agents]: [AGENTS.md (cdxgen/cdxgen, master)](https://raw.githubusercontent.com/cdxgen/cdxgen/master/AGENTS.md)
[^ptr-cdxgen-copilot]: [.github/copilot-instructions.md (cdxgen/cdxgen, master)](https://raw.githubusercontent.com/cdxgen/cdxgen/master/.github/copilot-instructions.md)
