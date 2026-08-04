---
type: Organization
title: Debian
description: Has no LLM policy; six competing General Resolution proposals ranging from prohibition to permissive were in discussion until 2026-08-08, with the vote still to come.
resource: https://www.debian.org/vote/2026/vote_002
tags:
  - ai-contribution
  - policy
  - distribution
  - undecided
  - in-progress
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T23:10:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T23:10:00Z'
stale_after: 2026-09-15
sources:
  - id: debian-gr-2026-002
    title: 'General Resolution: LLM usage in Debian (2026 vote_002)'
    resource: https://www.debian.org/vote/2026/vote_002
---

**Stance: undecided, and actively being decided.** Debian has **no policy on LLM-assisted
contributions**. A General Resolution — *"LLM usage in Debian"*, 2026 `vote_002` — was in its
discussion period **2026-07-23 to 2026-08-08**, with the ballot to follow.[^debian-gr-2026-002]

> ⚠ **This record has a short shelf life by construction.** `stale_after` is 2026-09-15, not the
> bundle's usual six months, because the subject is a vote in progress. Re-read the GR page rather
> than trusting this record after the ballot closes.

## Six proposals, not two

The interesting fact is the **shape of the disagreement**. This is not ban-versus-allow; it is six
distinct positions, and the middle four differ on questions most projects have not yet
noticed.[^debian-gr-2026-002]

| | Proposer | Position |
|---|---|---|
| **A** | Matthias Geiger | Forbid LLM-assisted contributions to Debian |
| **B** | Lucas Nussbaum | Allow, with conditions |
| **C** | Ian Jackson | Reject LLMs as far as practical |
| **D** | Pierre-Elliott Bécue | Accept, for Debian-specific work |
| **E** | Marc Haber | Responsible use — neither endorse nor prohibit |
| **F** | Tobias Frost | A cautious approach — discourage, trust judgement |

**A** covers *"packaging, native Debian software like lintian, documentation and translations"* but
**excludes upstream projects** — Debian would keep packaging software written with AI while barring
it from its own work. That carve-out is what makes a distribution-level ban tractable at all.

**C** contains the requirement no other project in this bundle has: *"messages to humans … must be
drafted solely by humans without LLM assistance."* Every other policy here governs **code**. Debian
is the first to put the *conversation* in scope — and in a project whose work is substantially
mailing-list discussion, that is the larger surface.

**B** and **D** both require disclosure and both forbid sending sensitive data to external AI
services; **B** additionally asks that bulk submissions be discussed beforehand. **E** and **F**
both decline to require disclosure — **E** encourages it, **F** encourages it *"as a courtesy"* —
and both rest on the position that existing quality standards already cover the problem.

## The axes a policy must decide

Debian's ballot is the most useful artifact in this bundle for anyone drafting a policy, because
six people wrote independently and converged on the same questions:

1. **Prohibit, discourage, or regulate?**
2. **Disclosure: mandatory, encouraged, or silent?**
3. **Does it cover prose and human communication, or only code?**
4. **Does it bind upstream, or only the project's own work?**
5. **May contributor data leave the project's infrastructure?**
6. **Is there a volume threshold?**

Any policy that does not answer all six leaves a gap someone will find.

## What a contributor must do

Until the vote resolves, **no rule binds**, and that is precisely when caution is cheapest — a
contribution made now may be judged under a rule adopted next month. Disclose AI assistance
voluntarily: it is required by **B** and **D**, encouraged by **E** and **F**, and mandated by
**C** — five of six ballot options. Volunteering it is the only choice that is safe under every
outcome.

## Re-verification notes

`https://www.debian.org/vote/2026/vote_002` carries the result once the ballot closes; Debian votes
are preferential, so the outcome may be a ranked result rather than a single winner, and **Further
Discussion** is always on the ballot — a "no decision" outcome is a real possibility, and would
leave this record's stance unchanged rather than superseded.

[^debian-gr-2026-002]: [General Resolution: LLM usage in Debian (2026 vote_002)](https://www.debian.org/vote/2026/vote_002)
