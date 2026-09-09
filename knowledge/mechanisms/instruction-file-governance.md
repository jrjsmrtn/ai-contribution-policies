---
type: Practice
title: Governing the instruction file
description: An agent-instruction file is read at the start of every session, so it is a context budget rather than a document, and it grows by accretion. Two projects wrote rules for what may enter their own — systemd admits only what it has watched an agent get wrong, Zed requires three criteria and forbids drive-by edits — reaching the same principle in unrelated words.
resource: https://raw.githubusercontent.com/zed-industries/zed/main/.rules
tags:
  - ai-contribution
  - mechanism
  - maintenance
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:29:44Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:29:44Z'
stale_after: 2027-03-08
sources:
  - id: gov-systemd
    title: 'AGENTS.md (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md
  - id: gov-zed
    title: '.rules (zed-industries/zed, main) — Rules Hygiene'
    resource: https://raw.githubusercontent.com/zed-industries/zed/main/.rules
  - id: gov-agentskills-progressive
    title: 'Specification — Agent Skills (progressive disclosure and the token budget)'
    resource: https://agentskills.io/specification
---

**An instruction file is a budget, not a document.** It is read at the start of every session, before
anyone knows what the session is for, and everything in it is paid for whether or not it is relevant.
The Agent Skills specification states the same economics for skills — metadata at roughly 100 tokens
loaded for *every* skill at startup, full instructions only on activation, with a recommendation to
keep a `SKILL.md` under 500 lines.[^gov-agentskills-progressive]

Files like `AGENTS.md` have no such staging. They are loaded whole. And they grow the way checklists
grow: every plausible rule gets added, nothing is ever removed, and the cost is invisible because it
falls on a future session rather than on the person adding the line.

**Two projects in this bundle wrote a rule about what may enter their own file.** They share no text
and reach the same principle: *evidence before admission*.

## systemd admits only what it has watched fail

The rule is the second sentence of the file, before any content:

> This file provides guidance to AI coding agents when working with code in this repository. **Only
> add instructions to this file if you've seen an AI agent mess up that particular bit of logic in
> practice.**[^gov-systemd]

**The bar is an observed failure.** Not a plausible one, not a rule that seems prudent — one that
someone watched happen. It makes the file a record of things that have gone wrong rather than a
description of how the project works, which is a much smaller thing.

## Zed states criteria, and forbids the agent editing the file during work

[Zed](../projects/zed.md)'s `.rules` carries a *Rules Hygiene* section that opens with the economics
explicitly — *"These `.rules` files are read by every agent session. Keep them
high-signal."*[^gov-zed] — and then sets three tests:

> **New rules must meet all three criteria:** 1. **Non-obvious** — someone familiar with the codebase
> would still get it wrong without the rule. 2. **Repeatedly encountered** — it came up more than once
> (multiple hits in one session counts). 3. **Specific enough to act on** — a concrete instruction,
> not a vague principle.[^gov-zed]

Criterion 2 is systemd's rule. Criteria 1 and 3 are additions that attack different failure modes:
**1 excludes what the code already teaches**, and **3 excludes advice too general to change any
decision.**

Two further rules make it a process rather than a preference:

> **Avoid architectural descriptions of a crate** (module layout, data flow, key types). These go
> stale fast and the agent can gather them by reading the code. **Rules should be traps to avoid, not
> maps to follow.**[^gov-zed]

> Do **not** edit `.rules` inline during normal feature/fix work. … **Rules emerge from validated
> patterns, not one-off observations.** The workflow is: agent notes a pattern during a session; team
> validates it in code review; a dedicated commit adds the rule with context on *why* it
> exists.[^gov-zed]

**The agent is barred from amending its own instructions during ordinary work.** It may propose,
under a *"Suggested `.rules` additions"* heading in the pull request; a human decides. That is the
same separation [NetworkManager](../projects/networkmanager.md) draws for commit messages and review
replies, applied to the rules themselves.

Zed also scopes: *"Rules that apply to a single crate belong in that crate's own `.rules` file, not
the repo root"* — the only instance here of an instruction file being **split by blast radius** rather
than allowed to grow at the root.

## Traps, not maps

The sharpest line is Zed's, and it generalises past this bundle. **A map goes stale and duplicates
what the code already says; a trap encodes something the code cannot tell you** — that this
plausible-looking thing is wrong here. Architectural description is the most tempting content for one
of these files and the least durable, because the code is its own best description and drifts away
from any prose account of it.

systemd's file demonstrates the tension it is trying to manage: alongside the policy clauses it
carries build guidance about `meson`, `mkosi` and `grep -q`. Every one of those is a trap, and the
file has still grown to cover four unrelated subjects.

## What is established, and what is not

**Two independent implementations.** systemd's phrasing and Zed's share no wording, and neither cites
the other. Given how much else in this bundle spread by copying, **arriving at the same rule
separately is the finding** rather than the count.

**Zed's version is spreading, and by how much is not established.** GitHub code search returns dozens
of repositories carrying its *"High bar for new rules"* heading. Spot checks found most to be
re-uploads of the Zed codebase under new names rather than git forks, and the handful of genuinely
different projects had taken the heading without Zed's distinctive phrasing — adaptation rather than
verbatim copying. **The population was not enumerated; a rate limit stopped the check** and the number
is not claimed.

**⚠ Code search is not a reliable population estimate here, demonstrated rather than assumed.** The
only results for systemd's phrase *"Only add instructions to this file"* are **this bundle's own
records**, quoting it. systemd's `AGENTS.md` is not in the index. A search-derived count would have
reported one implementation and missed the other.

## What it does not solve

**It bounds what enters, not what stays.** Neither project describes removing a rule once the failure
it recorded stops happening, and both files will accumulate on a one-way ratchet unless something
prunes them. The private tracking bundle in this family uses *"past `stale_after` for two consecutive
review cycles → delete, don't carry"* for exactly this reason; nothing equivalent appears in an
instruction file here.

**It cannot be enforced by the thing it governs.** Zed's rule tells the agent not to edit `.rules`
during ordinary work; an agent that ignores the file ignores that clause too. It works because the
diff is reviewed by a human, which is the same foundation the
[review canary](review-canary.md) rests on.

**And neither rule addresses length directly.** Zed's `.rules` is 12 KB and
[cdxgen](../projects/cdxgen.md)'s ungoverned `AGENTS.md` is 36 KB — the criteria constrain what each
line must earn, not how many lines there may be.

## What to watch

Whether either project adds a **removal** rule, which is the missing half. Whether the split-by-scope
idea spreads, since it is the only structural answer to growth rather than a filter on it. And
whether any tool starts reporting the context cost of these files back to the person editing them —
today the cost is entirely invisible at the moment it is incurred, which is why the rules have to be
written down at all.

[^gov-systemd]: [AGENTS.md (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md)
[^gov-zed]: [.rules (zed-industries/zed, main) — Rules Hygiene](https://raw.githubusercontent.com/zed-industries/zed/main/.rules)
[^gov-agentskills-progressive]: [Specification — Agent Skills (progressive disclosure and the token budget)](https://agentskills.io/specification)
