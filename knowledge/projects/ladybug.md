---
type: Organization
title: Ladybug
description: Has no AI contribution policy, and its contributing guide has not been touched since 2025-10-16. It carries an AGENTS.md that is a build-and-test guide with no policy in it, and since 2026-04 fifteen commits credit Claude as co-author, under a guide that says nothing either way. The database was formerly Kuzu, whose repository is archived.
resource: https://raw.githubusercontent.com/LadybugDB/ladybug/main/CONTRIBUTING.md
tags:
  - ai-contribution
  - project
  - no-policy
  - attribution
  - agent-file
status: stable
generated:
  by: claude/sonnet-5-5
  at: '2026-10-03T12:00:00Z'
verified:
  - by: claude/sonnet-5-5
    at: '2026-10-03T12:00:00Z'
stale_after: 2027-04-03
sources:
  - id: lb-contributing
    title: 'CONTRIBUTING.md (LadybugDB/ladybug, main)'
    resource: https://raw.githubusercontent.com/LadybugDB/ladybug/main/CONTRIBUTING.md
  - id: lb-agents
    title: 'AGENTS.md (LadybugDB/ladybug, main)'
    resource: https://raw.githubusercontent.com/LadybugDB/ladybug/main/AGENTS.md
  - id: lb-readme
    title: 'README.md (LadybugDB/ladybug, main)'
    resource: https://raw.githubusercontent.com/LadybugDB/ladybug/main/README.md
  - id: lb-pr-template
    title: 'Pull request template (.github/docs/pull_request_template.md, LadybugDB/ladybug, main)'
    resource: https://raw.githubusercontent.com/LadybugDB/ladybug/main/.github/docs/pull_request_template.md
  - id: lb-dev-guide
    title: 'Build Ladybug from source — developer guide, docs.ladybugdb.com'
    resource: https://docs.ladybugdb.com/developer-guide/
  - id: lb-agents-history
    title: 'Commit history of AGENTS.md (LadybugDB/ladybug, main)'
    resource: https://github.com/LadybugDB/ladybug/commits/main/AGENTS.md
  - id: lb-contributing-history
    title: 'Commit history of CONTRIBUTING.md (LadybugDB/ladybug, main)'
    resource: https://github.com/LadybugDB/ladybug/commits/main/CONTRIBUTING.md
  - id: lb-kuzu
    title: 'kuzudb/kuzu — the repository Ladybug continues'
    resource: https://github.com/kuzudb/kuzu
---

**Stance: none stated, and the absence is measured rather than assumed.** The repository's
`CONTRIBUTING.md`,[^lb-contributing] `AGENTS.md`,[^lb-agents] `README.md`,[^lb-readme] pull request
template,[^lb-pr-template] five issue templates and `CODEOWNERS` were fetched on 2026-10-03 and scanned for
the whole words *AI*, *LLM*, *generative*, *artificial intelligence*, *Copilot*, *Claude* and *Cursor*:
**zero occurrences across all eleven**, against a control run of the same scan over DuckDB's
`CONTRIBUTING.md`, which returned four. The seven files `AGENTS.md` points at under `docs/` were scanned
with *agent* added; two hits, neither a policy — an extension named `llm` in a list, and a pointer
back to `AGENTS.md`. The developer guide the README sends contributors to[^lb-dev-guide] has a
*Contributing Changes* section that is only about submodule pull requests, and no AI term outside a
navigation label.

That is the whole of Ladybug's written position on AI-authored contributions. **What makes the record
worth writing is the practice the guide never mentions.**

## What the contributing guide does say

Six bullets and a thanks, none about authorship. The closest is a size rule:

> Avoid large pull requests - they are much less likely to be merged as they are incredibly hard to
> review.[^lb-contributing]

and a reservation of discretion — *"We reserve full and final discretion over whether or not we will merge
a pull request."*[^lb-contributing] The reviewer-burden concern that other projects here express as an AI
rule is present only as a general one.

**The guide has not been edited since 2025-10-16.**[^lb-contributing-history] It still says *"Do not
commit/push directly to the master branch"* while the default branch is `main`, so it has not been read
against the repository since the rename. Everything below happened after its last revision.

## Practice: Claude is credited as co-author, and nothing asks for it

A partial clone of `main` on 2026-10-03 (`--shallow-since=2025-10-01`, 1,294 commits) counts **15 commits
with a `Co-Authored-By:` trailer naming `noreply@anthropic.com`** — about 1.2 percent.

- **Dates:** first on 2026-04-02, last on 2026-09-08; by month, 1 in 2026-04, 6 in 2026-07, 7 in 2026-08
  and 1 in 2026-09, none between.
- **Authors:** five git author names; one accounts for 10 of the 15.
- **Four model strings:** `Claude Fable 5` (8), `Claude Opus 4.8` (5), `Claude Opus 4.6 (1M context)`
  (1) and `Claude Fable 5.1` (1). Every one is a bare `Co-Authored-By`; none carries `Assisted-by:` or a
  *Generated with* line, and no commit message mentions Claude Code.
- **A second AI tool appears, once and by name.** Two further trailers read `Copilot Autofix powered by
  AI`, GitHub's automated fix suggestions; the other three name people. The first scan terms above do not
  catch these, because the trailer is a name and not a phrase the files use.

**A trailer is a lower bound.** It records a contributor who chose to leave one; the guide asks for none,
so a commit without one says nothing about whether a model was used. The probe was checked: a planted
string absent from every commit returned zero.

## The agent file is a build guide

`AGENTS.md` is a 2,660-byte regular file (mode `100644`) headed *"Ladybug Agent Guidelines"*: build
commands, test commands, formatting and linting, and a list of further documents. It names no policy,
makes no demand of an agent about attribution or disclosure, and links nothing about contribution.
The survey tool found no other agent-instruction file on `main` — no `CLAUDE.md`, no Copilot
instructions, no Cursor rules. See [agent-file pointers](../mechanisms/agent-file-pointers.md).

It dates from 2025-11-03 and has been edited eight times since, by two accounts, one of them seven of the
eight.[^lb-agents-history] **It predates the first Claude trailer by five months**, so the project
published instructions for agents before any commit credited one, and has never published a rule for what
they may do.

## Lineage

The README says *"The database was formerly known as Kuzu."*[^lb-readme] The repository was created
2025-10-07, three days before `kuzudb/kuzu`'s last push; Kuzu's repository is archived.[^lb-kuzu] The
contributing guide's history runs through a `kuzu` → `ladybug` rename commit, so the guide descends from
Kuzu's. **Whether Kuzu had an AI policy was not checked**, so this record does not say Ladybug
inherited or dropped one.

## What a contributor must do

**Nothing written binds you on AI.** Discuss changes with the core team first, open a pull request from a
fork, add tests, and keep it small. Ladybug reserves discretion to decline any pull request. Other
contributors have credited Claude in commits, so a trailer is not out of place, and none is required.

## Re-verification notes

**The absence covers the repository and the documentation site, not the project's Discord.** The
contributing guide names the Discord server as the place for *"real-time communication with the core
team"*[^lb-contributing] and a rule could be stated there. It is not machine-readable and was not read.
GitHub Discussions was not checked either.

**Check whether `CONTRIBUTING.md` has been edited** — the date above is the clearest signal. A first AI
sentence, or an `AI_POLICY.md`, ends this record's stance. Count trailers from a clone, not from search:
search undercounted DuckDB by more than two thirds.

[^lb-contributing]: [CONTRIBUTING.md (LadybugDB/ladybug, main)](https://raw.githubusercontent.com/LadybugDB/ladybug/main/CONTRIBUTING.md)
[^lb-agents]: [AGENTS.md (LadybugDB/ladybug, main)](https://raw.githubusercontent.com/LadybugDB/ladybug/main/AGENTS.md)
[^lb-readme]: [README.md (LadybugDB/ladybug, main)](https://raw.githubusercontent.com/LadybugDB/ladybug/main/README.md)
[^lb-pr-template]: [Pull request template (.github/docs/pull_request_template.md, LadybugDB/ladybug, main)](https://raw.githubusercontent.com/LadybugDB/ladybug/main/.github/docs/pull_request_template.md)
[^lb-dev-guide]: [Build Ladybug from source — developer guide, docs.ladybugdb.com](https://docs.ladybugdb.com/developer-guide/)
[^lb-agents-history]: [Commit history of AGENTS.md (LadybugDB/ladybug, main)](https://github.com/LadybugDB/ladybug/commits/main/AGENTS.md)
[^lb-contributing-history]: [Commit history of CONTRIBUTING.md (LadybugDB/ladybug, main)](https://github.com/LadybugDB/ladybug/commits/main/CONTRIBUTING.md)
[^lb-kuzu]: [kuzudb/kuzu — the repository Ladybug continues](https://github.com/kuzudb/kuzu)
