---
type: Organization
title: GCC
description: Declines legally significant LLM contributions — a copyright threshold rather than a volume or origin test — with named exceptions for test cases, marked insignificant changes, and accessibility tooling.
resource: https://gcc.gnu.org/ai-policy.html
tags:
  - ai-contribution
  - policy
  - project
  - restricted
  - dco
  - attribution
  - accessibility
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T07:30:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T07:30:00Z'
stale_after: 2027-01-15
sources:
  - id: gcc-ai-policy
    title: GNU Compiler Collection - AI Policy
    resource: https://gcc.gnu.org/ai-policy.html
  - id: gcc-contribute
    title: Contributing to GCC — Legal Prerequisites
    resource: https://gcc.gnu.org/contribute.html
---

**Stance: restricted, on a copyright threshold.** Adopted 2026-07-29 on a dedicated page.

> For the time being, the GNU Compiler Collection (GCC) policy is to decline any **legally
> significant** contributions which include LLM-generated content or are derived from LLM-generated
> content.[^gcc-ai-policy]

## The threshold is legal significance, and nothing else here uses it

Every other policy in this bundle draws its line somewhere else: origin ([Zig](zig.md)), appearance
([Git](git.md)), certifiability ([QEMU](qemu.md)), unmodified bulk ([Ansible](ansible.md)),
disclosure ([Rust](rust.md)'s draft). GCC's line is **the copyright threshold** — the same test that
decides whether a contribution needs a copyright assignment at all.

That makes the policy an extension of GCC's existing legal machinery rather than a new regime. Below
the threshold nothing much changes; above it, LLM-derived content is declined. It also means the
question *"is this AI-generated?"* is subordinate to *"is this legally significant?"* — a contributor
who already knows GCC's assignment rules already knows which of their patches are in scope.

## Three exceptions, each doing distinct work

- **Legally insignificant LLM content is acceptable** — *"as long as they meet the usual
  prerequisites for any contribution and the contribution is clearly marked."*[^gcc-ai-policy]
- **Test cases are exempt even when legally significant**: *"the GCC maintainers are free to accept
  legally significant contributions to test cases, generated in whole or in part by an
  LLM."*[^gcc-ai-policy] This is the only exception of its kind in the bundle, and it is coherent
  with the threshold logic — test cases are where generated volume is most useful and where a
  copyright defect is least likely to propagate into the shipped compiler.
- **Imported code is out of scope**: the policy *"does not apply to code which does not primarily
  belong to the GCC project, but is imported from other projects for convenience or to satisfy
  prerequisites (e.g. libsanitizer)."*[^gcc-ai-policy] GCC declines to impose its rule on upstreams
  it merely vendors — compare [Debian](../distributions/debian.md)'s Proposal A, which carves out
  upstreams for the same reason.

## The accessibility carve-out

No other policy here says this, and it is the clause most worth copying:

> This policy does not apply to a contributor's other uses of AI including the use of these tools to
> enable them to work with their own computing devices e.g. screen readers, text-to-speech, direct
> translations, spelling or grammar assistance, where the contributor verifies the output of the
> tool.[^gcc-ai-policy]

A blanket "no AI" rule silently taxes contributors who rely on assistive technology, and taxes
non-native speakers through the translation clause. GCC names both and puts them outside the policy
entirely — with one condition, that the contributor verifies the output.

## Transparency, and who may act

- *"The commit message for any contribution of LLM-generated content must include an `Assisted-by:`
  tag."*[^gcc-ai-policy]
- *"All contributions must be submitted by a human who understands the changes and is prepared to
  answer questions about them. The decision to include the contribution in the project must also be
  made by a human."*[^gcc-ai-policy]
- *"Only a human may provide the `Signed-off-by:` tag certifying the Developer Certificate of Origin
  (DCO). **An LLM may not commit code to the project repository.**"*[^gcc-ai-policy]

GCC is the **fourth** project here to land on `Assisted-by:`, after the
[Linux kernel](linux-kernel.md), [Ansible](ansible.md) and OpenInfra — with no shared specification
between them. It joins the kernel in reserving `Signed-off-by:` to humans, and goes further by
barring an LLM from committing at all: a rule about *agents with write access*, not just about
generated text.

## Permitted uses are enumerated

Research, analysis, bug discovery and reporting, patch review and debugging are all fine *"so long
as the output is not included in the contributions"* — with two qualifications worth noting: report
output *"should not be sent verbatim without due consideration"*, and patch review is *"supporting
human review, not replacing it."*[^gcc-ai-policy]

## It opens by protecting contributors, not the codebase

Alone in this bundle, the policy's first section is about people:

> First, all contributors should be treated with respect and kindness. There are strongly held and
> widely varying opinions regarding large language models (LLMs) and everyone should be presumed to
> be contributing in good faith. We welcome all contributors to the community even if they have not
> yet followed our policies; we should guide such contributors on how to do
> so.[^gcc-ai-policy]

That inverts the usual posture. Where [Git](git.md) tells maintainers what to reject and
[curl](curl.md) bans fabricated reporters outright, GCC's opening instruction is to *guide* a
contributor who has not complied. It is also a hedge against the enforcement problem
[Rust](rust.md)'s draft concedes: if the rule cannot be verified, the failure mode is suspicion, and
this is an explicit instruction not to treat contributors that way.

## The policy is CC0

*"This work is marked CC0 1.0 Universal."*[^gcc-ai-policy] It is the only policy in this bundle
released for reuse, so a project wanting a copyright-threshold rule can adopt the text outright
rather than draft one.

## What a contributor must do

Work out whether your change is **legally significant** by GCC's existing standard — the same
judgement that decides whether you need a copyright assignment. Above that line, do not submit
LLM-generated or LLM-derived content, except test cases. Below it, mark the contribution clearly.
Add `Assisted-by:` whenever LLM-generated content is included. Use AI freely for accessibility,
translation, research and review — verify the output. Never let a tool sign off or commit.

## Re-verification notes

The policy states its own next check: *"At the latest the policy will be reviewed at the start of
2027"*, and it *"is expected to evolve with the community or as the overall GNU Project position is
updated."*[^gcc-ai-policy] `stale_after` is set to 2027-01-15 for that reason, rather than the
bundle's usual six months — the source named the date.

**Watch the GNU Project position**, not only this page: the policy is explicitly downstream of it.
Note also that `contribute.html` carries GCC's legal prerequisites (copyright assignment *or* DCO,
with standing DCO records in `MAINTAINERS.yml`) and does **not** mention AI[^gcc-contribute] — the
AI policy lives only at `ai-policy.html`, so checking the contribution guide alone finds nothing.

[^gcc-ai-policy]: [GNU Compiler Collection - AI Policy](https://gcc.gnu.org/ai-policy.html)
[^gcc-contribute]: [Contributing to GCC — Legal Prerequisites](https://gcc.gnu.org/contribute.html)
