---
type: Organization
title: Debian
description: Adopted "Responsible Use of Generative AI" — neither endorses nor prohibits, holds AI-assisted work to the same standards, encourages but does not require disclosure. The prohibition option was dropped for missing the 3:1 majority this record derived from the Constitution before the vote page stated any. Officially declared 2026-08-30 with a 425-vote tally sheet.
resource: https://www.debian.org/vote/2026/vote_002
tags:
  - ai-contribution
  - policy
  - distribution
  - decided
  - permitted
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
  - by: claude/opus-5
    at: '2026-08-29T02:45:00Z'
  - by: claude/opus-5
    at: '2026-08-30T12:00:00Z'
stale_after: 2027-02-28
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
  - id: debian-gr-2026-002-results
    title: 'Results for LLM usage in Debian (automated publication, Devotee)'
    resource: https://lists.debian.org/debian-vote/2026/08/msg00360.html
  - id: debian-gr-2026-002-tally
    title: 'Tally sheet for the votes cast, GR 2026 vote_002 (425 votes)'
    resource: https://www.debian.org/vote/2026/vote_002_tally.txt
---

**Stance: decided and officially declared — generative AI is permitted, under the standards that
already applied.** The General Resolution *"LLM usage in Debian"*, 2026 `vote_002`, closed on
2026-08-28 23:59:59 UTC. **Option 5, "Responsible Use of Generative AI"** — Proposal **E** below — is
the sole member of the Schwartz set and **the declared winner**, defeating *None of the above* by 281
to 126.[^debian-gr-2026-002]

The official outcome, quorum arithmetic and the **tally sheet of 425 votes** were published on the
vote page on **2026-08-30**, roughly 36 hours after the ballot
closed.[^debian-gr-2026-002][^debian-gr-2026-002-tally] Quorum was **48.4897** — `Q = sqrt(1045)/2 =
16.163`, quorum `= 3Q` — against a current developer count of 1,045; **all eight proposals cleared
it**.[^debian-gr-2026-002]

> **This record carried the automated result for a day before the official one existed, and said so
> in place.** Devotee published the computed tally at 2026-08-29 00:01:45 UTC, describing itself as
> *"an automated, unofficial publication of vote results"* with official results *"to follow, sent in
> by the vote taker"*.[^debian-gr-2026-002-results] **Every figure in it matched the declaration**,
> which is the expected outcome — Devotee computes what the Secretary certifies — but the two were
> recorded as different kinds of claim while only one existed. The distinction cost nothing and would
> have mattered had they diverged.
>
> One figure did change: the unofficial message gave quorum as **47.244**, the declaration gives
> **48.4897**, computed against a slightly different developer count. The numbers above are the
> official ones.

## What Debian adopted

The adopted text is a **statement of position under Constitution §4.1(5)**, not a rule added to a
foundation document — and it says so, reserving the right to evolve *"as time passes without the
need to resort to future general resolutions."*[^debian-gr-2026-002]

> Debian neither endorses nor prohibits the use of generative AI tools in the development,
> maintenance, or documentation of software, packaging, documentation, and other media published
> within the Debian Project.[^debian-gr-2026-002]

**The operative move is that it adds no new rule.** Contributions must meet *"the same standards of
quality, correctness, maintainability, and legal compliance"* regardless of the tools used, and
*"The use of a generative AI tool does not diminish the contributor's responsibility for the work
they submit."* Contributors are expected to *"understand, review, test, and, where appropriate,
modify AI-assisted output"*, because *"Blindly accepting or uploading AI-generated material without
appropriate human review is inconsistent with Debian's established development
practices."*[^debian-gr-2026-002] It closes by affirming that generative AI is *"neither exempt from
nor subject to special rules beyond the standards already expected of Debian
contributors."*[^debian-gr-2026-002]

**Disclosure is encouraged and explicitly not required**, which puts Debian on the opposite side of
this axis from the kernel's required `Assisted-by:` trailer:

> We enourage our contributors to disclose whether a contribution was made with AI assitance, but do
> not require them to do so.[^debian-gr-2026-002]

*(Both misspellings — "enourage", "assitance" — are in the adopted text as published. They are
reproduced rather than silently corrected, because this is the operative wording of the position
Debian voted for.)*

Two concrete obligations sit underneath the general one:

- **Non-public material must not reach third-party AI services.** Confidential information, private
  communications, embargoed security information, cryptographic keys and credentials relating to the
  project, its infrastructure or its community may not be disclosed *"unless such disclosure has
  been explicitly authorized"*.[^debian-gr-2026-002]
- **Scale still needs consent.** Mass bug filing, large-scale code modification and other automated
  changes affecting many packages *"should seek prior discussion and consensus"* first, and *"Any
  such automated process should be overseen by a human who remains accountable for its behavior and
  output."*[^debian-gr-2026-002]

**It declines the legal question deliberately.** Debian *"does not seek to resolve these unsettled
legal questions through this General Resolution, nor does it adopt a position on whether AI-generated
output is, in whole or in part, copyrightable or derived from copyrighted works"* — leaving existing
licensing and copyright policy to apply unchanged.[^debian-gr-2026-002] That is the mirror image of
GCC, whose whole rule turns on the copyright threshold.

## The result, and the arithmetic this record predicted

The ballot carried nine options — the eight proposals below plus *None of the above*. All eight
reached quorum (47.244). Two were then dropped for failing their majority
requirement:[^debian-gr-2026-002-results]

```
Dropping option 1 because of majority. 0.560 (144/257) < 3
Dropping option 3 because of majority. 0.765 (176/230) < 1
```

**Option 1 is Proposal A, the prohibition, and the `3` it failed against is the supermajority this
record derived from the Constitution before the vote page stated any requirement at all.** It
finished at 0.56 against a threshold of 3 — not close. The reasoning recorded on 2026-08-05, that a
ballot where one option needs 3:1 and its rivals need a simple majority is not the even contest a
flat list suggests, is what the tally then confirmed.[^debian-constitution]

Option 3 (Proposal **C**, reject as far as practical) failed even a simple majority against *None of
the above*, at 0.765. Options 2, 4, 5, 6, 7 and 8 all passed theirs, and Option 5 beat each of them
head to head — Option 2 by 203–148, Option 6 by 210–130, Option 4 by 232–115.


## Eight proposals, not two

The interesting fact is the **shape of the disagreement**, and it survives the vote: this was not
ban-versus-allow but eight distinct positions, differing on questions most projects have not yet
noticed.[^debian-gr-2026-002] The ballot is kept here in full because a project drafting its own
policy learns more from the options Debian declined than from the one it adopted.

| | Proposer | Position |
|---|---|---|
| **A** | Matthias Geiger | Forbid — **by amending the Social Contract** |
| **B** | Lucas Nussbaum | Allow, with conditions *(amended twice)* |
| **C** | Ian Jackson | Reject LLMs as far as practical *(amended once)* |
| **D** | Pierre-Elliott Bécue | Accept, for Debian-specific work |
| **E** ✅ | Marc Haber | Responsible use — neither endorse nor prohibit — **adopted** |
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

**You may use generative AI, and you own the result.** Debian added no gate, no tag and no
declaration — what it added is an explicit statement that the existing bar applies unchanged. In
practice that means: review, test and understand anything a tool produced before you submit it, and
be ready to answer for its quality and licensing as if you had typed it.

Three things are firmer than the general permission, and they are where a contributor can actually
get this wrong:

1. **Do not paste non-public project material into third-party AI services** — embargoed security
   information, credentials, keys and private communications — without explicit authorisation.
2. **Do not run anything at scale without asking first.** Mass filing, mass patching and automated
   changes across many packages need prior discussion and consensus, and a named human accountable
   for the output.
3. **Disclosure is your choice.** Debian encourages it and does not require it, so omitting it
   breaks no rule here — but the projects Debian ships from may differ, and the kernel's
   `Assisted-by:` trailer *is* required by the document that governs ordinary patch submission.
   **A Debian contributor forwarding work upstream is bound by the upstream rule, not this one.**

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

**Checked 2026-08-29**, hours after the ballot closed. The result was read from the automated tally
on `debian-vote`, and Proposal E's operative text was read in full from the vote page — the adopted
wording is quoted here from that text, not from the summaries circulating in the press within the
hour.

**A prediction this record made was confirmed, which is worth more than the result.** The 3:1
supermajority for Proposal A was derived from the Constitution on 2026-08-05, at a time when the
vote page stated no majority requirement; the tally dropped Option 1 at 0.560 against exactly that
threshold. A derived claim that later matches the primary is the strongest evidence a record can
offer that its reasoning was sound.

**The declaration arrived on 2026-08-30 and this record was updated against it.** `stale_after`
returns to the bundle's six months, since the subject is now a settled decision rather than a vote in
progress. What would reopen it is Debian amending or superseding the statement, which Proposal E
explicitly contemplates — it reserves the right to evolve *"without the need to resort to future
general resolutions"*, so a change need not arrive through another GR and will not announce itself on
the vote page.

**Two corrections to where this record previously said to look**, both still worth keeping:

- **The vote page was not where the result appeared first.** This record said
  `https://www.debian.org/vote/2026/vote_002` *"carries the result once the ballot closes"*. Hours
  after closing it carried no outcome section, no tally sheet and no quorum log, while the result
  had been published on the `debian-vote` list. **Watch the list, then the page.**
- **The preferential-outcome caution did not apply.** The Schwartz set resolved to a single option,
  so there is no ranked result to interpret and *None of the above* placed last among the survivors.

[^debian-gr-2026-002]: [General Resolution: LLM usage in Debian (2026 vote_002)](https://www.debian.org/vote/2026/vote_002)
[^debian-constitution]: [Debian Constitution §4.1 — Foundation Documents and majority requirements](https://www.debian.org/devel/constitution)
[^debian-gr-2025-002]: [General Resolution: Interpretation of DFSG on Artificial Intelligence (AI) Models (2025 vote_002)](https://www.debian.org/vote/2025/vote_002)
[^debian-gr-2025-002-withdrawal]: [withdrawing Proposal A — Interpretation of DFSG on Artificial Intelligence (AI) Models](https://lists.debian.org/debian-vote/2025/05/msg00105.html)
[^debian-gr-2026-002-results]: [Results for LLM usage in Debian (automated publication, Devotee)](https://lists.debian.org/debian-vote/2026/08/msg00360.html)
[^debian-gr-2026-002-tally]: [Tally sheet for the votes cast, GR 2026 vote_002 (425 votes)](https://www.debian.org/vote/2026/vote_002_tally.txt)
