---
type: Organization
title: OpenInfra Foundation
description: Permits AI contributions across its projects under the most precise labelling scheme found — Assisted-By for predictive tools, Generated-By for generative ones, removable by reviewers after rework.
resource: https://openinfra.org/legal/ai-policy
tags:
  - ai-contribution
  - policy
  - foundation
  - permitted
  - disclosure
  - attribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T00:55:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T00:55:00Z'
stale_after: 2027-02-04
sources:
  - id: openinfra-ai-policy
    title: AI Generated Content Policy — OpenInfra Foundation
    resource: https://openinfra.org/legal/ai-policy
---

**Stance: permitted, with the most precise disclosure scheme in this bundle.** OpenInfra's *AI
Generated Content Policy* applies to all contributions committed to source revision control by
OpenInfra Foundation projects.[^openinfra-ai-policy]

## It settles the tag question by using both

Elsewhere in this bundle, three organisations use two different field names and nobody explains the
difference. OpenInfra uses **both, and the distinction is the point**:[^openinfra-ai-policy]

| Tag | For |
|---|---|
| `Assisted-By:` | **Predictive** AI — auto-complete style suggestions |
| `Generated-By:` | **Generative** AI — creating complete code artifacts, permitted *under limited circumstances* |

That is the missing semantics. The [Linux kernel](../projects/linux-kernel.md) and
[Ansible](../projects/ansible.md) chose `Assisted-by:`; the [ASF](apache-software-foundation.md)
chose `Generated-by:`. Read through OpenInfra's scheme, those are not competing spellings for one
concept — **they name two different degrees of authorship**, and a project that uses only one is
either restricting itself to that degree or collapsing a distinction it may later want.

Both labels must carry *explanatory context* about the tool used and the extent of AI
involvement.[^openinfra-ai-policy] So the tag is not a checkbox; it is a short provenance note.

## The label is mutable, which nothing else here allows

Reviewers should *"consider removing labels if substantial human reworking
occurs."*[^openinfra-ai-policy]

This is a genuinely different model of what a provenance tag *is*. Everywhere else the tag records
**history** — this is how the patch came to exist, permanently. Here it records a **current
property**: how much of what is about to be merged is machine-origin. Rework enough and the label
comes off.

Both readings are defensible, and they are incompatible. Anyone designing tagging for their own
project should decide which they mean before choosing a field name, because a mutable
history-tag is just an inaccurate one.

## What is forbidden

- Output from **proprietary models whose vendors claim rights over it**.
- Code or content with **incompatible licensing**.
- **Automated submissions**, except from documented automated processes such as release tooling or
  internationalization updates.[^openinfra-ai-policy]

The proprietary-model clause is sharper than the [Linux Foundation](linux-foundation.md)'s
*"should ensure the terms … do not place any contractual restrictions"*: it names the failing
condition rather than asking the contributor to assess compatibility.

## Obligations on both sides of the review

**Contributors** must review AI-generated code for correctness, security and licensing; add the
appropriate label with context; verify licence compatibility; confirm they have rights to submit the
output; treat AI-generated code as **untrusted** and debug it thoroughly; and sign off, taking full
responsibility.[^openinfra-ai-policy]

**Reviewers** must verify that a labelled change carries sufficient explanation, apply **heightened
scrutiny** to AI-assisted contributions, and evaluate technical *and legal* merits.[^openinfra-ai-policy]

That reviewer clause is rare. Most policies here place the entire burden on the submitter; OpenInfra
is explicit that a disclosed contribution is reviewed *differently*, which is what makes disclosure
consequential rather than ceremonial. Contributions must also align with the **Four Opens** and use
compatible open-source licences.[^openinfra-ai-policy]

## What a contributor must do

Decide honestly whether your tool was predictive or generative, and label accordingly — with a
sentence on what it did, not just a tool name. Treat the output as untrusted. Expect the label to
attract closer review, because that is its designed effect. Do not use a model whose vendor claims
rights over its output.

## Re-verification notes

Watch the two-tag distinction specifically: it is the most useful thing on the page and the most
likely to be simplified away. Also watch whether the *"limited circumstances"* qualifier on
generative tools is ever spelled out — as written it is the policy's one undefined term, and it
governs the case contributors most need answered.

[^openinfra-ai-policy]: [AI Generated Content Policy — OpenInfra Foundation](https://openinfra.org/legal/ai-policy)
