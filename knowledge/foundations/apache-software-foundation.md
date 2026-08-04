---
type: Organization
title: Apache Software Foundation
description: Permits generative-AI contributions to ASF projects under three licence-focused conditions, tells contributors not to second-guess vendor terms, and asks for a Generated-by commit token.
resource: https://www.apache.org/legal/generative-tooling.html
tags:
  - ai-contribution
  - policy
  - foundation
  - permitted
  - licensing
  - attribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T00:25:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T00:25:00Z'
stale_after: 2027-02-04
sources:
  - id: asf-generative-tooling
    title: Generative Tooling Guidance — The Apache Software Foundation
    resource: https://www.apache.org/legal/generative-tooling.html
---

**Stance: permitted, under licence-focused conditions, with a disclosure token.** The ASF's
*Generative Tooling Guidance* allows code, documentation and images produced with generative AI in
ASF project contributions, subject to conditions that are — like the
[Linux Foundation](linux-foundation.md)'s — about **rights in the output** rather than about tool
use.[^asf-generative-tooling]

## The conditions

1. **Tool terms must not conflict with the Open Source Definition.** *"The terms and conditions of
   the generative AI tool do not place any restrictions on use of the output that would be
   inconsistent with the Open Source Definition."*[^asf-generative-tooling]

2. **One of three must hold** for third-party material: the output is not copyrightable; or no
   third-party materials are included; or any that are included have permission and comply with the
   applicable licence terms.[^asf-generative-tooling]

3. **Due diligence has a defined bar.** *"A contributor obtains reasonable certainty that conditions
   2.2 or 2.3 are met if the AI tool itself provides sufficient information about output that may be
   similar to training data."*[^asf-generative-tooling]

Condition 3 is the pragmatic move. The obligation is otherwise unsatisfiable — a contributor cannot
audit a model's training data — so the ASF makes **the tool's own similarity reporting** the
evidence that discharges it. Like the LF, it makes a product feature part of compliance; unlike the
LF, it states what counts as *enough*.

## "Don't second guess vendor's terms of use"

> Don't second guess vendor's terms of use (TOU). Your usage of their tools is bound by the totality
> of the given TOU and you are not expected to go outside of the TOU text for further
> clarifications.[^asf-generative-tooling]

This is the single most contributor-friendly sentence in the bundle, and it is worth reading against
the [Linux Foundation](linux-foundation.md), which asks contributors to satisfy themselves that the
tool's terms are compatible but does not say how far that duty runs. The ASF **bounds the duty**:
read the TOU, take it at face value, stop. Two foundations, near-identical conditions, and only one
tells you when you are done.

## The tag is a third spelling

Contributors *"should indicate tooling used"*, including a `Generated-by: ` token in commit
messages, described as being for future machine-parsable tracking.[^asf-generative-tooling]

That makes **three field names across five organisations** for the same job:

| Field | Used by |
|---|---|
| `Assisted-by:` | [Linux kernel](../projects/linux-kernel.md) (`AGENT_NAME:MODEL_VERSION [TOOLS]`), [Ansible](../projects/ansible.md) (`[tool name/version]`) |
| `Generated-by:` | Apache Software Foundation |

The semantics differ too, not only the spelling — *assisted* and *generated* describe different
degrees of authorship, so a project could plausibly want both. Anyone building tooling should treat
this as an unsettled convention: emit what the target project asks for, and do not assume a parser
written for one will read the other.

## What a contributor must do

Read your tool's terms of use once, and take them at face value. Turn on similarity reporting if the
tool offers it — under condition 3 that reporting is what discharges your diligence obligation. Add
`Generated-by:` to the commit. Then check the specific ASF project, which may ask for more.

## Re-verification notes

The page is ASF **legal** guidance and applies across ASF projects, but individual projects publish
their own supplementary rules — Airflow, CouchDB, DataFusion and Kvrocks all have AI sections in
their contributor docs, so a project-level answer needs the project's own page as well. Watch the
`Generated-by:` token specifically: it is described as anticipating machine-parsable tracking, so
its grammar may be tightened later in a way that invalidates loosely-formatted trailers.

[^asf-generative-tooling]: [Generative Tooling Guidance — The Apache Software Foundation](https://www.apache.org/legal/generative-tooling.html)
