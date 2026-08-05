---
type: Organization
title: SUSE
description: Its Open Source Policy binds employees, not contributors — and two SUSE-published versions disagree on whether AI pair programming is prohibited, with the live page silent and the 2024 PDF forbidding it.
resource: https://opensource.suse.com/legal/policy
tags:
  - ai-contribution
  - policy
  - vendor
  - employee-binding
  - contradictory
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T07:50:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T07:50:00Z'
stale_after: 2026-11-05
sources:
  - id: suse-policy-html
    title: SUSE Open Source Policy (live web version)
    resource: https://opensource.suse.com/legal/policy
  - id: suse-policy-pdf
    title: SUSE Open Source Policy, effective 2024-04 (PDF)
    resource: https://www.suse.com/siteassets/suse_open_source_policy2.pdf
---

**Stance: contradictory across two published versions — and binding on employees rather than
contributors.**

## It governs SUSE staff, not people contributing to SUSE projects

> The policy applies to SUSE employees. It is our hope that it serves as an inspiration for our
> partners, customers and users to follow the same model.[^suse-policy-html]

The PDF says the same: *"The audience of this policy is mainly SUSE employees. However, we hope the
policy … might also serve as inspiration for others implementing open source
policies."*[^suse-policy-pdf]

**This is the vendor pattern, and it inverts every other category in this bundle.** A distribution,
project or foundation policy tells *you* what you may submit. A vendor policy tells *its own staff*
what they may do. A contributor to a SUSE-run project is not bound by this document at all — the
project's own contribution guidelines govern them.

## The two versions disagree

**The 2024-04 PDF prohibits it**, under its own heading:

> **AI pair programming**
>
> AI pair programming must not be used.
>
> The legal constructs around AI pair programming with respect to licensing and potential violations
> are not resolved.[^suse-policy-pdf]

**The live web policy does not contain it.** Checked by counting rather than reading:
`opensource.suse.com/legal/policy` returns **zero** matches for *"pair programming"* or *"artificial
intelligence"*, while containing the sections that **bracket** the AI clause in the PDF — *Creating
new projects*, *Guiding Principles*, *codes of conduct*, and *Contributing to Open Source
Projects*.[^suse-policy-html] So the page is complete and the clause is genuinely absent, not
truncated in transit.

**Which is current is not established here.** Two SUSE-published documents describe one policy and
one of them has an AI prohibition. Possible readings — the clause was removed and the PDF is a stale
artifact; the PDF is authoritative and the web version is abridged; or the two were never
synchronised. Nothing reachable settles it.

## Why this matters beyond SUSE

*"SUSE bans AI pair programming"* is widely repeated, and it traces to the PDF. **It may no longer be
true.** A reader relying on the live policy would find no such rule; a reader relying on the PDF
would find a flat prohibition. This is the failure this bundle exists to surface, occurring in the
source rather than in a summary of it — compare [Fedora](../distributions/fedora.md), whose adopted
policy has no reachable publication at all.

## What a contributor must do

If you are **not** a SUSE employee, this policy does not bind you; read the specific project's
contribution guidelines instead. If you **are**, the two versions disagree and the safe reading is
the stricter one, pending clarification from SUSE.

## Re-verification notes

Check **both** artifacts and compare them — that comparison is the finding, and reading either alone
gives a confident wrong answer:

1. `opensource.suse.com/legal/policy` — count occurrences of `pair programming`; do not skim.
2. `suse.com/siteassets/suse_open_source_policy2.pdf` — extract text and grep. It carries
   `Effective April 2024` verbatim.

If the clause reappears on the live page, or the PDF is withdrawn or superseded, this record
resolves into an ordinary one. A public policy repository would settle it, but the live page links
to none.

[^suse-policy-html]: [SUSE Open Source Policy (live web version)](https://opensource.suse.com/legal/policy)
[^suse-policy-pdf]: [SUSE Open Source Policy, effective 2024-04 (PDF)](https://www.suse.com/siteassets/suse_open_source_policy2.pdf)
