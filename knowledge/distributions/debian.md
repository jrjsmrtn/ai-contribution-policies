---
type: Organization
title: Debian
description: Has no LLM policy; eight competing General Resolution proposals go to a ballot open 2026-08-15 to 2026-08-28 — and the prohibition option amends the Social Contract, so it needs a 3:1 majority the other seven do not.
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
  - by: claude/opus-5
    at: '2026-08-14T22:40:00Z'
stale_after: 2026-08-29
sources:
  - id: debian-gr-2026-002
    title: 'General Resolution: LLM usage in Debian (2026 vote_002)'
    resource: https://www.debian.org/vote/2026/vote_002
  - id: debian-constitution
    title: Debian Constitution §4.1 — Foundation Documents and majority requirements
    resource: https://www.debian.org/devel/constitution
  - id: debian-gr-2025-002
    title: 'General Resolution: Interpretation of DFSG on Artificial Intelligence (AI) Models (2025 vote_002)'
    resource: https://www.debian.org/vote/2025/vote_002
  - id: debian-gr-2025-002-withdrawal
    title: 'withdrawing Proposal A — Interpretation of DFSG on Artificial Intelligence (AI) Models'
    resource: https://lists.debian.org/debian-vote/2025/05/msg00105.html
---

**Stance: undecided, and about to be decided.** Debian has **no policy on LLM-assisted
contributions**. A General Resolution — *"LLM usage in Debian"*, 2026 `vote_002` — is now in its
**voting period, 2026-08-15 00:00:00 UTC to 2026-08-28 23:59:59 UTC**.[^debian-gr-2026-002]

> ⚠ **This record has a short shelf life by construction.** `stale_after` is set to the day after
> the ballot closes, not the bundle's usual six months, because the subject is a vote. Re-read the
> GR page rather than trusting this record once the result exists.
>
> **Re-checked 2026-08-14**, and four things had changed in nine days. The discussion period was
> **extended to 2026-08-13**, a week past the date this record carried. The voting period is now
> announced. **Two further proposals were added — G and H — making eight, not six.** And the vote
> page now **states the majority requirement itself**, which it did not before.

## Eight proposals, not two

The interesting fact is the **shape of the disagreement**. This is not ban-versus-allow; it is eight
distinct positions, and the middle ones differ on questions most projects have not yet
noticed.[^debian-gr-2026-002]

| | Proposer | Position |
|---|---|---|
| **A** | Matthias Geiger | Forbid — **by amending the Social Contract** |
| **B** | Lucas Nussbaum | Allow, with conditions *(amended twice)* |
| **C** | Ian Jackson | Reject LLMs as far as practical *(amended once)* |
| **D** | Pierre-Elliott Bécue | Accept, for Debian-specific work |
| **E** | Marc Haber | Responsible use — neither endorse nor prohibit |
| **F** | Tobias Frost | A cautious approach — discourage, trust judgement |
| **G** | Gard Spreemann | *"we disallow the output of generative AI as direct contributions"* — including messages, bug reports and patches |
| **H** | Holger Levsen | Encourage avoidance **on environmental grounds** — a position statement, not a rule |

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
page now states this directly — *"Proposal A needs a 3:1 majority, the other proposals need a simple
majority"*[^debian-gr-2026-002] — where before it stated no requirement at all and this record
derived it from the Constitution. **The derivation was right and is now sourced**, which is worth
recording: the earlier note said explicitly that it was read from the Constitution rather than the
ballot, and that caveat can now be dropped rather than quietly kept.

A ballot where one option needs 3:1 and its seven rivals need a simple majority is not the even
contest an eight-way list suggests, and any reading of the outcome has to account for it.

**Two options put human communication in scope, and no other organisation in this bundle does.**
**C** requires that *"messages to humans … must be drafted solely by humans without LLM
assistance."* **G** reaches the same surface from the other direction, disallowing generative output
in *"Submissions (messages, bug reports, patches, etc.) to the BTS, Salsa, mailing
lists."*[^debian-gr-2026-002] Every other policy in this bundle governs **code**. In a project whose
work is substantially mailing-list discussion, the conversation is the larger surface — and it is
now the position of two independent proposals rather than one, which is a change in the shape of the
disagreement, not only its size.

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
7. **On what grounds?** Added by **H**, which argues from **environmental cost** rather than from
   quality, licensing or provenance. Every other option in this ballot — and every other
   organisation in this bundle — reasons from the character of the output or its legal status. A
   policy resting on the cost of *producing* it is a different argument, and one a project could
   adopt while agreeing entirely about quality.

Any policy that does not answer the first six leaves a gap someone will find; the seventh decides
which coalition it can be argued to.

## What a contributor must do

Until the vote resolves, **no rule binds**, and that is precisely when caution is cheapest — a
contribution made now may be judged under a rule adopted this month. Disclose AI assistance
voluntarily. Every option that permits any use asks for disclosure in some form: **B** and **D**
require it, **E**, **F** and **H** encourage or appreciate it, and **C** goes further by requiring
human-drafted messages. The two that would disallow the contribution outright, **A** and **G**, make
disclosure moot rather than unwelcome. **Volunteering it is the only choice that is safe under every
outcome**, which was true of the six-option ballot and remains true of the eight.

## A prior AI vote, withdrawn — and why it is not recorded here

Debian put a different AI question to a General Resolution in 2025, `vote_002`, *"Interpretation of
DFSG on Artificial Intelligence (AI) Models"*, proposed by Mo Zhou with eight seconds and a
discussion period opening 2025-04-21.[^debian-gr-2025-002] Its single option asked whether models
released under a DFSG-compatible licence **without the original training data or program** are
DFSG-compliant, and answered no — such files *"can not be included in the "main" section of the
Debian archive"*, with the question of `non-free` left explicitly open.[^debian-gr-2025-002]

**It is out of scope for this bundle, and the omission is deliberate rather than an oversight.** The
subject is the licensing of AI models *as distributed artifacts* — whether a model may ship in
`main` — not how the project treats AI-authored *contributions*. Filing it here would widen the
bundle from contribution policy to model licensing, which the landscape bundle's territory adjoins.

**It was withdrawn by its proposer on 2025-05-08**, before reaching a ballot, and conditionally:
*"if the other proposals suddenly get enough sponsors in the last minute, the proposal A has to be
there. So this is a "conditional" withdraw, and I'm expecting the GR to be
canceled."*[^debian-gr-2025-002-withdrawal] The stated ground was readiness, not the merits:
*"Based on the overall discussions and feedbacks, we as a community is underprepared to vote on
this. Even if we vote, it is leading to a less convincing
result."*[^debian-gr-2025-002-withdrawal]

**What transfers is about process, not about either subject.** One of the proposer's reasons for
withdrawing was that his was the only option on the ballot — *"The lack of other options can make
the result less convincing"* — with an offer to coordinate the start so rival proposals could be
drafted without rushing.[^debian-gr-2025-002-withdrawal] Fifteen months later the LLM ballot carried
**eight** competing proposals. The defect named in 2025 is precisely the one the 2026 ballot does not
have, which is worth knowing for anyone reading that eight-way split as mere disagreement: in this
project a crowded ballot is the repaired condition, not the broken one.

*The two sources in this section were read 2026-08-29. That is not a re-verification of this
record's claims about the 2026 ballot, which remain as checked on 2026-08-14.*

## Re-verification notes

**Checked 2026-08-14.** What this pass confirmed directly: the status is *Voting*; the discussion
period ran to **2026-08-13**, not the 2026-08-08 this record carried; the ballot is open
**2026-08-15 to 2026-08-28**; there are **eight** proposals, G and H having been added; and the page
now states the majority requirement itself. The operative text of G and H was read, not inferred
from their titles.

**All eight quotations in this record were re-confirmed against the page in the same pass**, not
only the three added today. That distinction was worth closing rather than noting: five had been
carried forward from the 2026-08-05 check, and a quotation nobody has re-read is exactly the kind of
claim that reads as sourced while resting on an earlier session.

`https://www.debian.org/vote/2026/vote_002` carries the result once the ballot closes; Debian votes
are preferential, so the outcome may be a ranked result rather than a single winner, and **Further
Discussion** is always on the ballot — a "no decision" outcome is a real possibility, and would
leave this record's stance unchanged rather than superseded.

[^debian-gr-2026-002]: [General Resolution: LLM usage in Debian (2026 vote_002)](https://www.debian.org/vote/2026/vote_002)
[^debian-constitution]: [Debian Constitution §4.1 — Foundation Documents and majority requirements](https://www.debian.org/devel/constitution)
[^debian-gr-2025-002]: [General Resolution: Interpretation of DFSG on Artificial Intelligence (AI) Models (2025 vote_002)](https://www.debian.org/vote/2025/vote_002)
[^debian-gr-2025-002-withdrawal]: [withdrawing Proposal A — Interpretation of DFSG on Artificial Intelligence (AI) Models](https://lists.debian.org/debian-vote/2025/05/msg00105.html)
