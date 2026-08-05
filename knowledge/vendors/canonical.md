---
type: Organization
title: Canonical
description: Requires a Harmony-based CLA and has no AI-contribution policy — its contributor documentation is silent, while it publicly plans to ship AI-co-authored code in Ubuntu.
resource: https://ubuntu.com/project/docs/contributors/
tags:
  - ai-contribution
  - policy
  - vendor
  - no-policy
  - cla
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T07:50:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T07:50:00Z'
stale_after: 2026-11-05
sources:
  - id: ubuntu-contributors
    title: Contributing to Ubuntu Development — contributor documentation
    resource: https://ubuntu.com/project/docs/contributors/
  - id: canonical-cla
    title: Contributor Licence Agreement — Ubuntu and Canonical Legal
    resource: https://canonical.com/legal/contributors
---

**Stance: no AI-contribution policy, and a CLA that has nothing to say about AI either.**

## The absence is verified, and the search path is wide

Ubuntu's contributor documentation contains **no mention** of AI, LLMs, generative tooling or coding
assistants across its eighteen sections — bug triaging, QA and testing, debugging, bug fixing,
building, updating, merging, uploading and sponsorship, new packages, stable release updates,
accessibility, documentation, and the rest.[^ubuntu-contributors]

This is a stronger absence than a single-file check. The documentation covers the whole contribution
path, including the sponsorship queue where an AI-assistance rule would most naturally sit, and says
nothing.

## The CLA is the binding instrument, and it is silent

Canonical **requires a Contributor Licence Agreement**, based on the Harmony framework. It licenses
rather than assigns:

> you're giving us a licence, but you still own the copyright — so you retain the right to modify
> your code and use it in other projects.[^canonical-cla]

There is **no AI-related term in it**.[^canonical-cla] So a contributor to a Canonical project signs
an agreement about copyright and patents that is entirely silent on whether the work may be
AI-assisted — the [CLA](https://github.com/jrjsmrtn/software-supply-chain-landscape/blob/main/knowledge/provenance/cla.md)
instrument does not carry that question, and Canonical has not added it elsewhere.

Worth noting for anyone comparing: a **CLA is a heavier instrument than a DCO** and Canonical uses
one, so the barrier to contributing is already higher than at most projects here — and it still
does not answer the AI question.

## The tension worth recording

Canonical has publicly stated it intends to **ship AI-co-authored code in Ubuntu**, framing this as
following projects like the Linux kernel that now have governing policies, and has said it does not
want AI used carelessly or to produce "slop".

Those are statements about **product strategy and internal practice**, not a contribution policy —
and this record does not treat them as one. But the gap is real: Canonical plans to *produce*
AI-assisted code while publishing nothing about *receiving* it. A contributor cannot infer from a
roadmap what will be accepted in a merge proposal.

## The vendor pattern, third variant

Three vendors, three shapes: [SUSE](suse.md) binds its **employees** by policy (in one of two
published versions), [Red Hat](red-hat.md) publishes a **disposition** and defers to each community,
and Canonical publishes **neither** — while operating the heaviest inbound instrument of the three.

The common thread is that a vendor's rules govern its own staff, not contributors. Where the vendor
also runs a community — Fedora for Red Hat, openSUSE for SUSE, Ubuntu for Canonical — **the
community's policy is the one that binds a contributor**, and it is a separate document with a
separate adoption process.

## What a contributor must do

Sign the CLA — that part is not optional and is worth checking against your employer before you
start, since a CLA can be a hard stop. On AI assistance, **nothing is published**, so disclose
voluntarily and ask in the sponsorship queue or on the relevant Ubuntu Matrix channel. An absent
policy is not permission, and Canonical's stated intent to ship AI-assisted code says nothing about
what it will accept from outside.

## Re-verification notes

Two places, both needed:

1. **`ubuntu.com/project/docs/contributors/`** — where a contribution rule would live. Note this URL
   is the redirect target; `documentation.ubuntu.com/project/contributors/` 301s to it.
2. **`canonical.com/legal/contributors`** — the CLA. An AI clause added *there* would bind every
   contributor at once and is the higher-leverage change to watch.

A Canonical policy is more likely to appear as a CLA amendment than as a documentation section,
because the CLA is the instrument contributors actually sign.

[^ubuntu-contributors]: [Contributing to Ubuntu Development — contributor documentation](https://ubuntu.com/project/docs/contributors/)
[^canonical-cla]: [Contributor Licence Agreement — Ubuntu and Canonical Legal](https://canonical.com/legal/contributors)
