---
type: Organization
title: QEMU
description: Still prohibits AI-generated contributions — verified 2026-08-30 against master — on the ground that the DCO cannot be satisfied when the copyright status of LLM output is unsettled. A relaxation patch has been pending since 2026-05-28 which would permit AI in revert-cheap areas (tests, docs, mechanical changes, small fixes) and add an "AI-used-for" trailer.
resource: https://www.qemu.org/docs/master/devel/code-provenance.html
tags:
  - ai-contribution
  - policy
  - project
  - restricted
  - dco
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T22:30:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T22:30:00Z'
  - by: claude/opus-5
    at: '2026-08-30T05:00:00Z'
stale_after: 2026-11-30
sources:
  - id: qemu-relax-proposal
    title: '[PATCH] docs/devel: relax policy on AI-generated contributions (Paolo Bonzini, qemu-devel, 2026-05-28)'
    resource: https://lists.nongnu.org/archive/html/qemu-devel/2026-05/msg07614.html
  - id: qemu-code-provenance
    title: Code provenance — QEMU developer documentation
    resource: https://www.qemu.org/docs/master/devel/code-provenance.html
---

**Stance: prohibited, with an exceptions process.** QEMU *"requires that contributors refrain from
using AI content generators on patches intended to be submitted to the project, and will decline
any contribution if use of AI is either known or suspected."*[^qemu-code-provenance]

## The reasoning is DCO compliance, not distaste

This is the most transferable part of the policy. QEMU requires the **Developer's Certificate of
Origin**, which obliges a contributor to understand the copyright and licence status of what they
submit. The project's position is that for AI generators *"the copyright and license status of the
output is ill-defined with no generally accepted, settled legal foundation"*, so *"how contributors
could comply with DCO terms (b) or (c) … is unclear"*, and the project *"is not willing or able to
accept the legal risks of non-compliance."*[^qemu-code-provenance]

The consequence: this policy is downstream of DCO mechanics, so any project requiring a DCO faces
the same question whether or not it has written an answer.

## Scope and named tools

Copilot, ChatGPT, Claude, Code Llama, *"and code/content generation agents which are built on top
of such tools."*[^qemu-code-provenance]

## Exceptions exist and are documented

The project *"welcomes discussion on any exceptions to this policy, or more general revisions"*,
via the `qemu-devel` mailing list with details of a proposed tool, model or usage scenario;
accepted exceptions are listed on the policy page itself. It also states the policy *"may evolve as
AI tools mature and the legal situation is clarified."*[^qemu-code-provenance]

## What a contributor must do

Do not use AI generators on patches for QEMU. To propose an exception, take a concrete
tool-and-scenario case to `qemu-devel` **before** writing the patch — an exception granted after
the fact does not exist.

## A proposal to relax it has been pending since 2026-05-28

**The prohibition above is still in force** — verified against `master` on 2026-08-30 — but it is
under active challenge, and the challenge is the more interesting document.

Paolo Bonzini (Red Hat) posted *"[PATCH] docs/devel: relax policy on AI-generated
contributions"*.[^qemu-relax-proposal] **It concedes the legal question rather than answering it:**

> The concern that motivated the policy is unchanged, and it is worth stating precisely: the DCO is
> about whether the submitter has the legal right to contribute the code, not about "creative
> expression". The copyright and license status of LLM output remains unsettled, so that question is
> still open. **What has shifted is the balance of risk**[^qemu-relax-proposal]

The two grounds offered are that projects accepting AI content *"have not run into serious legal
trouble so far"*, and that Red Hat has assessed the risk as acceptable — **immediately qualified by
the distinction this bundle records elsewhere**: *"a community of individual developers does not have
the legal backing of a company, and even an unfounded dispute would be a long-lasting distraction
from work on QEMU."*[^qemu-relax-proposal] A Red Hat engineer citing Red Hat's own risk assessment,
and then noting it does not transfer to the community, is [the vendor/community
boundary](../vendors/red-hat.md) argued from the inside.

**It would scope permission by blast radius, not by legal significance:**

> permit AI assistance where the ramifications of copyright violations are at least easy to revert
> and unlikely to spread: **tests, documentation, mechanical changes, and small bug fixes**. Core
> code that other things depend on, and that cannot simply be thrown away once a problem is noticed
> long after the fact, stays off-limits without prior agreement from a
> maintainer.[^qemu-relax-proposal]

[GCC](gcc.md) draws its line at *legal significance*, [GTK](gtk.md) at the *shape* of the change;
this draws it at **how cheaply a mistake can be undone**. Three projects, three different axes for
the same "where is AI acceptable" question.

## The clearest statement in this bundle of why review cost is the real problem

> AI lowers the cost of producing a patch but **does nothing to lower the cost of understanding and
> reviewing one; if anything it raises it, since a reviewer can no longer assume that the submitter
> has reasoned through every line.** The limits above work just as much to keep the volume of review
> work sustainable.[^qemu-relax-proposal]

Five other projects here give reviewer bandwidth as their motive — [GNOME](gnome.md), the
[Linux wireless maintainer](linux-kernel.md), the kernel's `generated-content.rst`,
[Nerves](nerves.md), [MacPorts](macports.md) — but they state it as a *fact about volume*. **This
states the mechanism**: the reviewer's prior about the submitter has changed, so the same diff now
costs more to review than it used to. That is why volume caps and "be able to explain it" rules keep
appearing together across otherwise unrelated policies.

## A fourth trailer, with a different job

The patch would introduce **`AI-used-for:`**, recording *where* AI was used rather than *that* it was
used — and it says explicitly why that differs from the tag everyone else reaches for:

> The standard is slightly different from the more usual "Assisted-by", **which doubles as a check
> that the author has read the policy.**[^qemu-relax-proposal]

**That reframes what an attribution trailer is for.** `Assisted-by:` functions as a *compliance
signal* — its presence proves you found the rule. `AI-used-for:` is meant to be *information for the
reviewer*, telling them which parts to read hardest. A project choosing between them is choosing
between proving compliance and directing attention, and no other record here makes that distinction.

Added to the [kernel](linux-kernel.md)'s `Assisted-by: LLM`, [Nerves](nerves.md)'s
`Assisted-by: AGENT_NAME:MODEL_VERSION` and [GTK](gtk.md)'s outright prohibition, that is **four
positions on commit-message attribution**, of which three are in force and one is proposed.

The proposal keeps the DCO intact regardless: *"use of AI does not relax any other contribution
requirement: authors still comply with the DCO and take responsibility for the whole patch via
Signed-off-by."*[^qemu-relax-proposal]

## Re-verification notes

**Checked 2026-08-30: the prohibition stands.** `docs/devel/code-provenance.rst` on `master` still
reads *"Current QEMU project policy is to DECLINE any contributions which are believed to include or
derive from AI generated content."* The file's last change was 2026-05-22 — **before** the relaxation
patch of 2026-05-28 — so the patch has not landed after three months, and the exceptions section
still lists no exceptions.

**`stale_after` shortened from 2027-02-04 to 2026-11-30.** A live proposal to reverse the stance is
exactly the condition under which a six-month expiry is too long: had this record not been re-checked
opportunistically, a merge would have gone unnoticed for five months. Watch
`git log -- docs/devel/code-provenance.rst`, which dates every change, and the `qemu-devel` thread.

The exceptions list is *on the policy page*, so re-verification means reading to the end rather
than confirming the headline. The page is versioned documentation (`docs/master/devel/`), so its
git history is the audit trail.

[^qemu-relax-proposal]: [[PATCH] docs/devel: relax policy on AI-generated contributions (Paolo Bonzini, qemu-devel, 2026-05-28)](https://lists.nongnu.org/archive/html/qemu-devel/2026-05/msg07614.html)
[^qemu-code-provenance]: [Code provenance — QEMU developer documentation](https://www.qemu.org/docs/master/devel/code-provenance.html)
