---
type: Organization
title: QEMU
description: Machine emulator whose code-provenance policy requires contributors to refrain from AI content generators, grounded in an inability to satisfy the DCO, with a documented exceptions process.
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
stale_after: 2027-02-04
sources:
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

## Re-verification notes

The exceptions list is *on the policy page*, so re-verification means reading to the end rather
than confirming the headline. The page is versioned documentation (`docs/master/devel/`), so its
git history is the audit trail.

[^qemu-code-provenance]: [Code provenance — QEMU developer documentation](https://www.qemu.org/docs/master/devel/code-provenance.html)
