---
type: Organization
title: GTK
description: Permits AI assistance under six named requirements, requires disclosure in the issue or merge request — and forbids the Assisted-by and Co-authored-by trailers because they are "free advertising for AI companies". That is the same argument the Linux kernel used to narrow the very trailer GTK bans, three months earlier. It also binds maintainers, not only contributors.
resource: https://gitlab.gnome.org/GNOME/gtk/-/blob/main/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - attribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-29T04:05:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-29T04:05:00Z'
stale_after: 2027-02-28
sources:
  - id: gtk-contributing
    title: 'CONTRIBUTING.md — AI Contribution Policy (GTK, main)'
    resource: https://gitlab.gnome.org/GNOME/gtk/-/raw/main/CONTRIBUTING.md
  - id: gtk-commit-guidelines
    title: 'commit e76acf1c — Write down AI contribution guidelines'
    resource: https://gitlab.gnome.org/GNOME/gtk/-/commit/e76acf1c991a
  - id: gtk-commit-free-ad
    title: 'commit 247617cd — Mention the "free ad" motivation'
    resource: https://gitlab.gnome.org/GNOME/gtk/-/commit/247617cdc7b9
---

**Stance: permitted, tightly conditioned, and disclosed in prose rather than in a trailer.** GTK
wrote its AI contribution policy on **2026-04-03**, after discussion *"among the core GTK
contributors"*.[^gtk-commit-guidelines] It opens by stating a preference rather than a rule:

> GTK is a project by humans for humans. We prefer contributions that are produced by human
> creativity, we expect a human to take full responsibility for each contribution, and we will take
> more joy in reviewing contributions when there's people at the other end of the line to stand by
> their changes.[^gtk-contributing]

## It forbids the trailer the Linux kernel requires

This is the sharpest direct contradiction in this bundle, and both sides argue it the same way.

> Always disclose the use of LLM/GenAI tools when creating an issue or a merge request. **Do not
> include trailers like "Co-authored-by:" or "Assisted-by:" in commit messages, since they serve as
> free advertising for AI companies.**[^gtk-contributing]

The [Linux kernel](linux-kernel.md) **requires** `Assisted-by:`, and narrowed it on 2026-08-03 from
naming the model to the bare literal `LLM` on the ground that identifying models *"provides free
advertising to proprietary software companies"*. **Same premise, opposite instrument**: the kernel
kept the trailer and stripped the vendor from it; GTK removed the trailer and moved the disclosure
into the merge request.

**GTK got there first.** The *"free ad"* motivation was added to this file on
**2026-04-03**;[^gtk-commit-free-ad] the kernel's commit was authored 2026-07-01 and reached mainline
2026-08-03. *No influence is claimed here* — the dates are recorded because they are checkable and
the direction of travel is not. What the pair establishes is narrower and firmer: **an
anti-vendor-advertising argument does not determine an attribution mechanism.** A project drafting
one should decide the instrument separately from the premise, because two serious projects took this
premise to incompatible rules.

It also means **the trailer is not portable**. A contributor who learned `Assisted-by:` from the
kernel and applies it here is violating GTK's policy by following another project's; the same tag is
mandatory in one tree and forbidden in another.

## Six requirements, and what each is actually for

> 1. Use AI as a tool. Verify behavior, correctness, and compatibility yourself prior to submitting
>    your contribution. **Do not ask the maintainers to do this for you.**
> 2. Keep changes narrow and limited. Do **NOT** use LLM/GenAI tools to generate broad rewrites,
>    large refactorings, or style changes.
> 3. Do **NOT** submit generated code, documentation, or tests that you don't understand.
> 4. Do **NOT** fabricate benchmarks, bug reports, test results, code samples, or reproducers.
> 5. Do **NOT** include private code, credentials, tokens, or any other confidential material.
> 6. Respect the licensing and attribution requirements.[^gtk-contributing]

Two of these are not found elsewhere in this bundle. **Rule 2 caps the *shape* of the change**, not
its volume — no broad rewrites, refactorings or style changes — which targets the failure the
[Linux wireless maintainer](linux-kernel.md) described as *"sprinkling checks all over the code
disregarding the architecture"*. A volume threshold counts lines; this one bounds blast radius.

**Rule 4 governs fabricated evidence rather than generated code.** Benchmarks, bug reports, test
results and reproducers are the artifacts a reviewer uses *to check the code*, and a hallucinated
reproducer corrupts the review rather than the patch. Every other policy here regulates the
contribution; this regulates the case made for it.

## The review conversation is protected from both ends

> ### Reviews
> 1. Describe your changes, and the verification steps.
> 2. Be prepared to explain all the changes yourself.
> 3. Do **NOT** feed the review feedback to an LLM/GenAI tool.[^gtk-contributing]

That third rule is the contributor-side half of what the wireless maintainer refused from the other
side — *"I will absolutely not … argue with an LLM"*. Berg declined to be on one end of that
exchange; **GTK forbids the contributor from creating it.** Read together, the two describe the same
failure from opposite chairs, and GTK is the only policy here that closes it by rule.

## It binds maintainers, not only contributors

> ### Maintainers expectations
> 1. Review LLM/GenAI-assisted contributions more strictly than any other contribution.
> 2. Require reproducibility in fixes and tests.
> 3. Reject changes that appear to be unverified LLM/GenAI output.
> 4. **Reject comments and feedback that appear to be LLM/GenAI output.**[^gtk-contributing]

Almost every record in this bundle regulates the submitter alone. The kernel's `generated-content.rst`
*enumerates* maintainer discretion — what a maintainer **may** do; GTK **instructs** — what a
maintainer is expected to do. The difference matters to a contributor: under the kernel's wording a
strict maintainer is exercising a choice, under GTK's a lenient one is departing from policy.

The fourth item extends the rule past code into **review commentary**, which pairs with the
prohibition on feeding feedback to a tool: both ends of the review must be human.

## The closing argument

> A COMPUTER CAN NEVER BE HELD ACCOUNTABLE.
> THEREFORE A COMPUTER MUST NEVER MAKE A MAINTENANCE DECISION.[^gtk-contributing]

An IBM training slide from 1979, used here as the whole rationale in two lines. It is the
accountability argument [NetworkManager](networkmanager.md) makes in prose — *"A tool cannot certify
that for you"* — and the kernel makes procedurally by forbidding an agent to sign off.

## Where this sits relative to GNOME

GTK is hosted in the [GNOME](gnome.md) group and **diverges sharply from its sibling modules.** Seven
of them share a boilerplate that bans LLM contributions outright; GTK permits them under conditions.
Neither position comes from GNOME's project handbook, which says nothing about AI at all. **The
policy that binds you is the one in the repository you are sending to**, not the one belonging to the
umbrella the repository sits under.

## What a contributor must do

Verify the work yourself before submitting — behaviour, correctness, compatibility — and do not hand
that job to the maintainer. Keep the change narrow: no tool-driven rewrites or refactors. Submit
nothing you cannot explain, and never fabricate a benchmark, test result or reproducer. **Disclose
the tool use in the issue or merge request, and do not put it in a commit trailer** — the opposite of
the kernel's requirement. Handle review yourself, and do not route the feedback through a tool.

## Re-verification notes

The policy is the *"AI Contribution Policy"* section of `CONTRIBUTING.md` in `GNOME/gtk`; read the
`/-/raw/` path, since the GitLab blob view renders client-side and answers HTTP 200 with the file
text absent. `git log -- CONTRIBUTING.md` dates every change: the guidelines landed 2026-04-03 across
several same-day commits, with a further wording pass on 2026-04-27.

Watch for the trailer clause specifically. It is the one rule here that **contradicts another
project's requirement**, so it is both the most consequential for a cross-project contributor and the
most likely to be revisited if a shared convention emerges.

[^gtk-contributing]: [CONTRIBUTING.md — AI Contribution Policy (GTK, main)](https://gitlab.gnome.org/GNOME/gtk/-/raw/main/CONTRIBUTING.md)
[^gtk-commit-guidelines]: [commit e76acf1c — Write down AI contribution guidelines](https://gitlab.gnome.org/GNOME/gtk/-/commit/e76acf1c991a)
[^gtk-commit-free-ad]: [commit 247617cd — Mention the "free ad" motivation](https://gitlab.gnome.org/GNOME/gtk/-/commit/247617cdc7b9)
