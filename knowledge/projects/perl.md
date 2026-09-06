---
type: Organization
title: Perl
description: Draws its lines by artifact type rather than by tool or disclosure — code may be accepted, documentation will not, prose is grounds for dismissal, and agents are barred from every communication channel. It is the only policy here where documentation is governed more strictly than code, and the only one bounding contribution by what the contributor could have written unaided.
resource: https://github.com/Perl/perl5/blob/blead/AI_POLICY.md
tags:
  - ai-contribution
  - policy
  - project
  - restricted
  - disclosure
  - communication
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-06T22:23:15Z'
verified:
  - by: claude/opus-5
    at: '2026-09-06T22:23:15Z'
stale_after: 2027-03-07
sources:
  - id: perl-ai-policy
    title: 'AI Usage Policy (AI_POLICY.md, Perl/perl5, blead)'
    resource: https://raw.githubusercontent.com/Perl/perl5/blead/AI_POLICY.md
  - id: perl-contributing
    title: 'Contributing to perl (CONTRIBUTING.md, Perl/perl5, blead)'
    resource: https://raw.githubusercontent.com/Perl/perl5/blead/CONTRIBUTING.md
---

**Stance: differentiated by what you are contributing, not by whether a tool was used.** Perl gives
AI its own file — `AI_POLICY.md`, added **2026-07-30** in a single commit titled *"Add our AI
policy"* — and `CONTRIBUTING.md` routes contributors to it alongside the code of conduct: *"Please be
mindful of `CODE_OF_CONDUCT.md` and `AI_POLICY.md`."*[^perl-contributing]

Almost every other policy in this bundle asks one question — *may you use a tool, and must you say
so?* This asks a different one for each kind of thing you might submit.

## Five artifact types, five answers

| What you are contributing | Rule |
|---|---|
| **Code** | *"may be accepted"* — subject to the competence bound below |
| **Documentation and other non-code** | *"will not be accepted"* |
| **Prose in any channel** | *"grounds for dismissing a contribution out of hand"*, with two exceptions |
| **Reading the codebase** | *"up to the contributor and does not require disclosure"* |
| **Agent participation** | *"strictly prohibited"* in every channel |

**Documentation is governed more strictly than code, and that inverts what most projects assume.**
Elsewhere the reasoning runs that prose is low-risk and code is where correctness and provenance
bite; here generated documentation *"will not be accepted"* while generated code *"may
be"*.[^perl-ai-policy] The unstated premise is that Perl's documentation is part of the deliverable
rather than a description of it, and that a fluent-but-wrong page costs more than a patch a reviewer
can test.

## The competence bound, which no other policy states

> **Do not use an LLM to write code that you could not (with sufficient time available) have written
> yourself.** Perl is a complicated codebase with many implicit abstraction layers implemented in a
> fairly low-level language; it requires significant familiarity to successfully judge the quality of
> a large patch. Do not expect a submission to be accepted if you do not sufficiently understand
> design decisions to defend them in detail, **or if you would not be able to maintain your changes
> over the long run yourself**.[^perl-ai-policy]

Three distinct obligations in one paragraph, and only the middle one is common. *Defend the design in
detail* is the [Kubernetes](kubernetes.md) rule — explain it or the PR closes. The other two are new
here: a **capability test** applied before the fact, and a **maintenance commitment** extending after
the merge.

That last one is the sharpest idea in the record. Every other policy governs the moment of
submission; this one asks whether you will still be able to look after the code in a year. It is a
plausible answer to the review-cost problem stated across six projects in this bundle — the cost is
not only reviewing the patch, it is owning it afterwards.

## Agents are barred from the channels, and prose from the discourse

> **Non-human interaction in the project is strictly prohibited.** AI agents must not create issues or
> pull requests, post to the mailing list, or otherwise participate in any project communication
> channels.[^perl-ai-policy]

That is the same axis [Dependency-Track](dependency-track.md) covers with *"Never create an issue.
Never create a PR"* — but stated as a **project rule** rather than as an instruction to the tool, and
extended past the forge to the mailing list and *"any project communication channels"*. Between them
the bundle now has both halves: a rule addressed to humans about what agents may do, and an
instruction addressed to agents about what they may do.

Generated prose is separately disallowed, *"grounds for dismissing a contribution out of hand"*, with
**two exceptions that exist nowhere else**:

1. *"LLM-generated security analysis that has been verified by a qualified human prior to
   submission"*
2. *"LLM use for translation of human-written messages"*[^perl-ai-policy]

The translation carve-out matches [Nerves](nerves.md) and [Elixir](elixir.md), and is becoming the
one exception projects converge on — it is the case where refusing AI excludes people rather than
protecting the project. **The security-analysis exception is unique**, and notable for what it
concedes: that a model may find something a human would not, provided a qualified human checks it
first.

The Perl Steering Council *"may make further exceptions on a case-by-case basis"*, with a request
attached rather than a rule — *"we strongly urge you to make an effort to curb the verbosity of
LLM-generated text."*[^perl-ai-policy]

## Disclosure, and a scope boundary drawn by ownership

> The fact that AI was used to generate any part of any contribution or communication **must be
> disclosed**. Accountability for any contribution lies with the contributor who submitted
> it.[^perl-ai-policy]

No form is prescribed — no trailer, no template — which puts Perl with the majority of disclosure
rules here and against [Kubernetes](kubernetes.md), which supplies the sentence.

The closing paragraph draws a boundary no other record has:

> The same rules apply to the modules owned by the Perl core. **Dual-life modules owned by their
> authors can make other decisions**, but we strongly urge them to communicate their policies to us
> and to their users.[^perl-ai-policy]

Perl's distribution contains modules maintained independently and shipped with core. The policy
follows **ownership rather than the repository**, so a file inside the same tarball may be governed
by someone else's rule — and the project asks those owners to publish theirs. That is the only place
in this bundle where a policy acknowledges it does not cover everything it ships.

## What a contributor must do

**Do not let an agent open the issue, the pull request or the mailing-list message** — that is
prohibited outright, not merely discouraged. Write your own prose; if English is not your first
language you may use a model to translate what you wrote, but not to write it. **Do not submit
generated documentation.** You may submit AI-assisted code, but only code you could have written
yourself given time, that you can defend design decision by design decision, and that you are
prepared to maintain. **Disclose the use, in any part of any contribution or communication.** Review
generated comments and cut the verbose ones.

## Re-verification notes

The policy is its own file at the repository root, so `git log -- AI_POLICY.md` is the whole history
— **one commit, 2026-07-30**. A rule this differentiated arriving fully formed in a single commit
suggests it was drafted elsewhere; no proposal, PPC or steering-council minute was located, and none
is claimed.

Watch two things. **Whether the documentation prohibition softens** — it is the most unusual clause
and the one most likely to meet pressure, since generated documentation is what contributors most
often offer. And **whether any dual-life module publishes its own policy**, which the core explicitly
requested; that would be the first instance in this bundle of a policy propagating by request rather
than by copying.

[^perl-ai-policy]: [AI Usage Policy (AI_POLICY.md, Perl/perl5, blead)](https://raw.githubusercontent.com/Perl/perl5/blead/AI_POLICY.md)
[^perl-contributing]: [Contributing to perl (CONTRIBUTING.md, Perl/perl5, blead)](https://raw.githubusercontent.com/Perl/perl5/blead/CONTRIBUTING.md)
