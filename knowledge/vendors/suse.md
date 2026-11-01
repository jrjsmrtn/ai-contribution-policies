---
type: Organization
title: SUSE
description: Its Open Source Policy binds employees, not contributors. Two SUSE-published versions disagree on whether AI pair programming is prohibited, the live page silent and the 2024 PDF forbidding it, and openSUSE's board recorded in 2025-10 that SUSE's internal policy had been updated to allow named AI tools. That update is not published.
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
  - by: claude/opus-5-5
    at: '2026-11-01T15:00:00Z'
stale_after: 2027-05-01
sources:
  - id: suse-policy-html
    title: SUSE Open Source Policy (live web version)
    resource: https://opensource.suse.com/legal/policy
  - id: suse-policy-pdf
    title: SUSE Open Source Policy, effective 2024-04 (PDF)
    resource: https://www.suse.com/siteassets/suse_open_source_policy2.pdf
  - id: opensuse-board-2025-10-27
    title: openSUSE Board meeting minutes, 2025-10-27 — openSUSE AI Code Assist Policy
    resource: https://en.opensuse.org/Archive:Board_meeting_2025-10-27
---

**Stance: contradictory across two published versions, apparently superseded by an unpublished
internal update, and binding on employees rather than contributors.**

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
`opensource.suse.com/legal/policy` returns **zero** matches for "pair programming" or "artificial
intelligence", while containing the sections that **bracket** the AI clause in the PDF — *Creating
new projects*, *Guiding Principles*, *codes of conduct*, and *Contributing to Open Source
Projects*.[^suse-policy-html] So the page is complete and the clause is genuinely absent, not
truncated in transit.

**SUSE has published nothing that says which is current.** Two SUSE-published documents describe one
policy and one of them has an AI prohibition.

## openSUSE's board says the prohibition has gone

The openSUSE board had held back its own AI policy to avoid contradicting SUSE's. Its minutes of
2025-10-27 record why it stopped waiting:[^opensuse-board-2025-10-27]

> To avoid conflicts we decided to wait on SUSE to publish its corporate policy. That policy has now
> been updated.

and, attributed in the minutes to a board member as *"Fair warning"*:

> Internal discussions are ongoing to open up more tools for use, but the policy now allows Gemini,
> Qwen 2.5 (3.0 coming), and GitHub Copilot. MCP is allowed for development, but not for use in
> production deployments without prior approval.[^opensuse-board-2025-10-27]

**This is the best evidence here that the PDF's prohibition is no longer in force**, and it explains
why the live page is silent. It is still second-hand: the minutes summarise what was said at a
meeting of a community board, and the updated internal policy they describe is not public. The live
page names a repository for proposed changes, `github.com/SUSE/open-source-policy`, which answered
HTTP 404 on 2026-11-01, so it is private or gone.[^suse-policy-html] This record does not state SUSE's
current rule as fact; it states what each source says.

## Why this matters beyond SUSE

*"SUSE bans AI pair programming"* is widely repeated, and it traces to the PDF. **By openSUSE's <!-- quote-ok: a secondary claim, quoted as the claim this record examines -->
account it stopped being true by 2025-10.** A reader relying on the live policy would find no such rule; a reader relying on the PDF
would find a flat prohibition. This is the failure this bundle exists to surface, occurring in the
source rather than in a summary of it — compare [Fedora](../distributions/fedora.md), whose adopted
policy has no reachable publication at all.

## What a contributor must do

If you are **not** a SUSE employee, this policy does not bind you; read the specific project's
contribution guidelines instead. If you **are**, your internal policy is the one that binds you, and
by openSUSE's account it now names the tools you may use. Nothing public tells an outsider which.

## Re-verification notes

Check **both** artifacts and compare them — that comparison is the finding, and reading either alone
gives a confident wrong answer:

1. `opensource.suse.com/legal/policy` — count occurrences of `pair programming`; do not skim.
2. `suse.com/siteassets/suse_open_source_policy2.pdf` — extract text and grep. It carries
   `Effective April 2024` verbatim.

Then two places that could settle what the comparison cannot:

3. The openSUSE board minutes after 2025-10-27, for the board's own AI policy and for anything more
   it reports about SUSE's.
4. `github.com/SUSE/open-source-policy`, named on the live page as where changes are reviewed. If it
   becomes public, it settles the question.

If the clause reappears on the live page, or the PDF is withdrawn or superseded, this record
resolves into an ordinary one. [openSUSE](../distributions/opensuse.md)'s board drafted a policy of its own,
with Fedora's as a baseline, and has not adopted it.

[^suse-policy-html]: [SUSE Open Source Policy (live web version)](https://opensource.suse.com/legal/policy)
[^suse-policy-pdf]: [SUSE Open Source Policy, effective 2024-04 (PDF)](https://www.suse.com/siteassets/suse_open_source_policy2.pdf)
[^opensuse-board-2025-10-27]: [openSUSE Board meeting minutes, 2025-10-27 — openSUSE AI Code Assist Policy](https://en.opensuse.org/Archive:Board_meeting_2025-10-27)
