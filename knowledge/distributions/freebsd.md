---
type: Organization
title: FreeBSD
description: Has no formal AI policy — verified absent from the Committer's Guide; Core reported in 2025 that it was drafting one and that it tends not to use AI for code over licence concerns.
resource: https://www.freebsd.org/status/report-2025-04-2025-06/core/
tags:
  - ai-contribution
  - policy
  - distribution
  - undecided
  - no-policy
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T23:10:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T23:10:00Z'
stale_after: 2027-02-04
sources:
  - id: freebsd-core-2025q2
    title: FreeBSD Core Team — status report, 2025-04 to 2025-06
    resource: https://www.freebsd.org/status/report-2025-04-2025-06/core/
  - id: freebsd-committers-guide
    title: Committer's Guide — FreeBSD documentation
    resource: https://docs.freebsd.org/en/articles/committers-guide/
---

**Stance: no formal policy, drafting reported but not landed.** This record documents an **absence**,
and the absence is the finding.

The FreeBSD Core Team reported in its 2025-04 to 2025-06 status that *"Core is investigating setting up
a policy for LLM/AI usage (including but not limited to generating code)"*, that
*"we currently tend to not use it to generate code because of license concerns"*, and that
*"the discussion continues at the core session at BSDCan 2025 developer summit, and core is still
collecting feedback and working on the policy."*[^freebsd-core-2025q2]

Core stated the result would be added to the Contributors Guide.[^freebsd-core-2025q2] **As of
2026-08-04 it has not been**: the Committer's Guide contains no mention of AI, LLMs, generative
tooling or coding assistants.[^freebsd-committers-guide] That is roughly a year between "working on
the policy" and no published policy.

## Why the absence is worth a record

An empty entry in a survey is ambiguous — it can mean *no policy*, *policy not found*, or *nobody
looked*. Those are three different things to a contributor, and only the first is a fact about
FreeBSD. This record asserts the first, names where it looked, and dates the look.

The distinction matters more here than elsewhere because FreeBSD is routinely grouped with
[NetBSD](netbsd.md) and [Gentoo](gentoo.md) as a BSD/distribution that restricts AI code. NetBSD
and Gentoo have written rules. FreeBSD has a **disposition reported by Core in a status update** —
which is evidence of intent, not a rule a contributor can be held to, and not something Core has
committed to keeping.

## What FreeBSD does consider AI useful for

Core's own list: translations (*"which seems faster than doing the work manually"*), explaining long
or obscure documents, tracking down bugs, and understanding large code
bases.[^freebsd-core-2025q2] The reservation is specific to **generating code**, and its stated
ground is **licence concerns** — the same provenance argument [QEMU](../projects/qemu.md) and
[Git](../projects/git.md) make from the DCO, reached here without a DCO.

## What a contributor must do

No rule binds, so nothing is formally required. But Core has said in public that it tends not to
generate code with AI over licence concerns, and a policy is in progress: submitting bulk generated
code now is submitting into a stance that is known and unfavourable, before the rule that would
govern it exists. Ask on the relevant list first.

## Re-verification notes

Two places must both be checked, and checking only one produces a wrong answer:

1. **The Committer's Guide** (`docs.freebsd.org/en/articles/committers-guide/`) — where Core said
   the policy would land. Its presence there would supersede this record entirely.
2. **Quarterly status reports** (`freebsd.org/status/`) — where the intent was reported and where
   any change of intent would appear first.

A finding of "no policy" is only as good as its date. Re-check on the schedule, not on rumour.

[^freebsd-core-2025q2]: [FreeBSD Core Team — status report, 2025-04 to 2025-06](https://www.freebsd.org/status/report-2025-04-2025-06/core/)
[^freebsd-committers-guide]: [Committer's Guide — FreeBSD documentation](https://docs.freebsd.org/en/articles/committers-guide/)
