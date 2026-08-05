---
type: Organization
title: Red Hat
description: Publishes a disposition rather than a policy — AI-assisted upstream contribution is treated as normal, subject to each community's own rules, with no located contribution policy of its own.
resource: https://www.redhat.com/en/blog/ai-assisted-development-supercharging-open-source-way
tags:
  - ai-contribution
  - policy
  - vendor
  - employee-binding
  - no-policy
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T07:50:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T07:50:00Z'
stale_after: 2027-02-05
sources:
  - id: redhat-ai-assisted-dev
    title: 'AI-assisted development: Supercharging the open source way (Red Hat blog)'
    resource: https://www.redhat.com/en/blog/ai-assisted-development-supercharging-open-source-way
  - id: redhat-when-bots-commit
    title: 'When bots commit: AI-generated code in open source projects (Red Hat blog, 2025-04-01)'
    resource: https://www.redhat.com/en/blog/when-bots-commit-ai-generated-code-open-source-projects
---

**Stance: permissive disposition, no located policy.** Red Hat publishes a position on AI-assisted
contribution but, so far as this record can establish, **no contribution policy document** — nothing
with the standing of [SUSE](suse.md)'s Open Source Policy or [GCC](../projects/gcc.md)'s
`ai-policy.html`.

## What is actually published

The operative sentence, on Red Hat's own blog:

> Every line of code, whether written by a human or with the assistance of an AI, must be subject to
> rigorous review, testing, and validation.[^redhat-ai-assisted-dev]

Around it: an *"upstream first"* philosophy, that *"using the best available technology is part of
that"*, that human oversight remains critical, and that contributions must adhere to *"standards and
practices of each unique community."*[^redhat-ai-assisted-dev]

That last clause is the substantive one, and it is a **deferral**. Red Hat does not set a rule that
travels with its engineers; it directs them to the receiving project's rule. So the question *"may a
Red Hat engineer send you AI-assisted code?"* resolves to *"what does **your** project's policy
say?"* — which is the correct answer, and also means Red Hat's position adds no constraint of its
own.

## A widely-repeated claim this record does not adopt

Secondary sources describe Red Hat as having *"guidelines for AI-based open source contribution for
their staff … based on 3 principles."* **No such enumeration appears in either Red Hat post read
here.**[^redhat-ai-assisted-dev][^redhat-when-bots-commit] The claim may be true and the document
elsewhere; it is not recorded because it was not found.

The second post — *When bots commit*, 2025-04-01, by Huzaifa Sidhpurwala, Senior Principal Product
Security Engineer — is **industry guidance rather than Red Hat policy**: rigorous review, licence
compliance checks, security testing, addressed to organisations generally.[^redhat-when-bots-commit]
Reading it as Red Hat's staff policy is a category error, and an easy one to make from a search
result.

## The vendor pattern

Like [SUSE](suse.md), whatever Red Hat has governs **its own people**, not contributors to
Red Hat-sponsored projects. Fedora's policy binds Fedora contributors and is
[recorded separately](../distributions/fedora.md); it is not Red Hat's, even though Red Hat sponsors
Fedora. Conflating a vendor with the communities it sponsors gets both wrong.

## What a contributor must do

Nothing here binds you. If you are contributing **to** a Red Hat-sponsored project, read that
project's policy — Fedora's, Ansible's, or the specific repository's. If you are a Red Hat engineer
contributing upstream, the published position points you at the receiving community's rules, so that
is the document to read.

## Re-verification notes

The gap to close is whether an internal or published **staff guideline** exists with the "three
principles" structure secondary sources describe. Places to look that were not exhausted: Red Hat's
legal or open-source-program pages, and any `CONTRIBUTING` convention shared across Red Hat-run
repositories.

Treat blog posts as **statements of position, not policy** — they carry an author and a date rather
than an adoption process, and a later post can contradict an earlier one without superseding
anything.

[^redhat-ai-assisted-dev]: [AI-assisted development: Supercharging the open source way (Red Hat blog)](https://www.redhat.com/en/blog/ai-assisted-development-supercharging-open-source-way)
[^redhat-when-bots-commit]: [When bots commit: AI-generated code in open source projects (Red Hat blog, 2025-04-01)](https://www.redhat.com/en/blog/when-bots-commit-ai-generated-code-open-source-projects)
