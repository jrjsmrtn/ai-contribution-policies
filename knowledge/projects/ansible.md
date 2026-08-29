---
type: Organization
title: Ansible
description: Permits AI-assisted contributions org-wide under a published community policy using RFC 2119 keywords, with threshold-based disclosure via an Assisted-by tag and a named reporting address.
resource: https://docs.ansible.com/projects/ansible/latest/community/ai_policy.html
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
  at: '2026-08-04T23:45:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T23:45:00Z'
stale_after: 2027-02-04
sources:
  - id: ansible-ai-policy
    title: Ansible Community Policy for AI-Assisted Contributions
    resource: https://docs.ansible.com/projects/ansible/latest/community/ai_policy.html
---

**Stance: permitted, with threshold-based disclosure and an explicit maintainer veto.** Ansible has
a published, named policy — *Ansible Community Policy for AI-Assisted
Contributions*[^ansible-ai-policy] — and it is the most conventionally-drafted document in this
bundle: it defines its terms, states its scope, and uses **RFC 2119 keywords** (MUST, SHOULD, MAY),
so its requirements can be read off rather than inferred.

## Definition and scope, both stated

"AI" is *"technology that is generally built using the machine learning approach"*, covering
*"assistive tools, including those considered as autonomous and semi-autonomous, such as large
language models (LLMs), text or image generators, and agentic systems."*[^ansible-ai-policy]

Scope is **all public projects** under the `ansible`, `ansible-community` and `ansible-collections`
GitHub organizations, **and** public communication platforms — the Ansible Forum, official Matrix
channels, GitHub discussions.[^ansible-ai-policy] Like [Debian](../distributions/debian.md)'s
Proposal C, this reaches conversation and not only code.

**Sub-projects may differ**: individual projects *"may have their own AI policies that are more or
less restrictive."*[^ansible-ai-policy] So an org-level answer is not a project-level answer, and
checking the org policy alone can be wrong in either direction.

## The requirements

- Contributions *"MUST adhere to any specific project or platform standards, conventions and
  contributing guidelines."*
- *"Contributors are fully accountable for the contributions they make with or without AI
  assistance."*
- *"Any autonomous contributions submitted by AI tools MAY be rejected by resource maintainers
  without prior justification."*
- Disclosure *"SHOULD be explicitly disclosed by the author when a significant part of the
  contribution is taken from the AI tools output without significant changes. Grammar, spelling, and
  stylistic corrections do not need disclosure."*[^ansible-ai-policy]

The disclosure threshold is doing real work: it is keyed to **unmodified bulk**, not to whether a
tool was involved. Under it, heavy editing of generated output falls below the line — a materially
different rule from [Rust](rust.md)'s draft, where origin triggers disclosure regardless of how much
you rewrote.

The autonomous-agent clause is worth noting separately. It grants maintainers a veto *"without prior
justification"* — no argument required, no appeal named. That is a deliberate asymmetry against
volume.

## The tag is the kernel's

Contributors may use `Assisted-by: [tool name/version]` in commit messages or contribution
preambles.[^ansible-ai-policy]

**Two independent projects converged on `Assisted-by:`, then diverged on what it carries.** The
[Linux kernel](linux-kernel.md) once specified `Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1]
[TOOL2]`, and on 2026-08-03 **deliberately dropped the tool and model**, leaving the bare literal
`Assisted-by: LLM`, on the ground that naming them advertised proprietary vendors. Ansible still
asks for `[tool name/version]`.

So the same field name now encodes **opposite intentions**: Ansible wants to know which tool, the
kernel has decided it does not. The *value grammar* never matched and the gap has widened. Anyone
building tooling to emit or parse this should treat the tag as a loose convention rather than a
format, and anyone adopting it should copy the target project's grammar — and its reasoning — rather
than assume one.

## Enforcement has an address

Violations are reported to `ansible-community@redhat.com`.[^ansible-ai-policy] Most policies in this
bundle name no channel at all; a named address is the difference between a rule and a sentiment.

## What a contributor must do

Take responsibility. Follow the target project's own contributing guidelines — and check whether
that project has a stricter AI policy of its own. Disclose with `Assisted-by:` when a significant
part is unmodified tool output. Do not run autonomous agents against Ansible repositories: they may
be rejected on sight, and no one owes you a reason.

## Re-verification notes

The canonical path is `docs.ansible.com/projects/ansible/latest/community/ai_policy.html`. Note
that `docs.ansible.com/ansible/latest/community/…` is a **different documentation tree** and its
`development_process.html` contains no AI mention — reading that one and concluding "no policy"
would be wrong. Since sub-projects may set stricter rules, a complete answer for a given collection
requires checking that collection too.

[^ansible-ai-policy]: [Ansible Community Policy for AI-Assisted Contributions](https://docs.ansible.com/projects/ansible/latest/community/ai_policy.html)
