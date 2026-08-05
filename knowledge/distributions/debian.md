---
type: Organization
title: Debian
description: Has no LLM policy; six competing General Resolution proposals in discussion until 2026-08-08 — and the prohibition option amends the Social Contract, so it needs a 3:1 majority the other five do not.
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
  - by: claude/opus-5
    at: '2026-08-05T07:25:00Z'
stale_after: 2026-09-15
sources:
  - id: debian-gr-2026-002
    title: 'General Resolution: LLM usage in Debian (2026 vote_002)'
    resource: https://www.debian.org/vote/2026/vote_002
  - id: debian-constitution
    title: Debian Constitution §4.1 — Foundation Documents and majority requirements
    resource: https://www.debian.org/devel/constitution
---

**Stance: undecided, and actively being decided.** Debian has **no policy on LLM-assisted
contributions**. A General Resolution — *"LLM usage in Debian"*, 2026 `vote_002` — was in its
discussion period **2026-07-23 to 2026-08-08**, with the ballot to follow.[^debian-gr-2026-002]

> ⚠ **This record has a short shelf life by construction.** `stale_after` is 2026-09-15, not the
> bundle's usual six months, because the subject is a vote in progress. Re-read the GR page rather
> than trusting this record after the ballot closes.
>
> **Re-checked 2026-08-05**: still *In Discussion*, closing **2026-08-08**; the **voting period is
> not yet announced**. Since first recorded, Proposal B has been amended twice and Proposal C once,
> and Proposal A is now framed as a Social Contract amendment — see below.

## Six proposals, not two

The interesting fact is the **shape of the disagreement**. This is not ban-versus-allow; it is six
distinct positions, and the middle four differ on questions most projects have not yet
noticed.[^debian-gr-2026-002]

| | Proposer | Position |
|---|---|---|
| **A** | Matthias Geiger | Forbid — **by amending the Social Contract** |
| **B** | Lucas Nussbaum | Allow, with conditions *(amended twice)* |
| **C** | Ian Jackson | Reject LLMs as far as practical *(amended once)* |
| **D** | Pierre-Elliott Bécue | Accept, for Debian-specific work |
| **E** | Marc Haber | Responsible use — neither endorse nor prohibit |
| **F** | Tobias Frost | A cautious approach — discourage, trust judgement |

**A is not an ordinary ballot option.** It adds a clause to the **Social Contract**:

> **6. Works Created through the use of Large Language Models (LLMs)**
>
> We will not allow direct contributions to Debian written with the use or assistance of large
> language models (LLMs) or other generative AI tools.[^debian-gr-2026-002]

*"Direct contributions"* means *"packaging, native Debian software like lintian, documentation and
translations written by Debian contributors, and official Debian web
resources"*[^debian-gr-2026-002] — **excluding upstream projects**, so Debian would keep packaging
software written with AI while barring it from its own work. That carve-out is what makes a
distribution-level ban tractable at all.

**The Social Contract is a Foundation Document, and the Constitution requires a 3:1 majority to
supersede one** (§4.1(5.2) names it; §4.1(5.3) sets the threshold).[^debian-constitution] The vote
page states no majority requirement for any option, so this is read from the Constitution rather
than from the ballot — but it means **A must clear a supermajority the other five do not**. A ballot
where one option needs 3:1 and its rivals need a simple majority is not the even contest a
six-way list suggests, and any reading of the outcome has to account for it.

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
[^debian-constitution]: [Debian Constitution §4.1 — Foundation Documents and majority requirements](https://www.debian.org/devel/constitution)
