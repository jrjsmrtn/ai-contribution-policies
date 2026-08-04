---
type: Organization
title: curl
description: Accepts AI-assisted code that meets normal standards, but requires disclosure for AI-found security reports and bans submitters of fabricated ones outright.
resource: https://curl.se/dev/contribute.html
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - security
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T00:55:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T00:55:00Z'
stale_after: 2027-02-04
sources:
  - id: curl-contribute
    title: Contribute to curl — on AI use in curl
    resource: https://curl.se/dev/contribute.html
---

**Stance: permitted for code, tightly governed for security reports.** curl is the only project in
this bundle whose policy is shaped primarily by **inbound security reports** rather than by patches,
and that makes it the most useful record for anyone running a vulnerability-disclosure or bug-bounty
process.

## Code: allowed, on the existing bar

> We can accept code written with the help of AI into the project, but the code must still follow
> coding standards, be written clearly, be documented, feature test cases and adhere to all the
> normal requirements we have.[^curl-contribute]

And the memorable formulation of the standard:

> A basic rule of thumb is that if someone can spot that the contribution was made with the help of
> AI, you have more work to do.[^curl-contribute]

That is [Git](git.md)'s *"looks AI generated"* rejection restated as **a target for the contributor
rather than a trigger for the maintainer** — same observable, opposite direction. Git tells
maintainers what to reject; curl tells contributors what to fix. Worth noting for anyone drafting:
the identical criterion reads as hostile in one framing and as coaching in the other.

## Security reports: disclosure is mandatory

> If you asked an AI tool to find problems in curl, you **must** make sure to reveal this fact in
> your report.[^curl-contribute]

Note the modal. Everywhere else in this bundle disclosure is SHOULD ([Ansible](ansible.md)),
appreciated-not-required ([Python](python.md)), or tier-dependent ([Rust](rust.md)'s draft). Here it
is **MUST**, and it applies to a narrow, high-cost channel rather than to contributions at large.

Reporters must *"double-check the findings carefully before reporting them to us to validate that
the issues are indeed existing and working exactly as the AI says"*, because *"AI-based tools
frequently generate inaccurate or fabricated results."* Copying an AI report wholesale is
discouraged: they *"typically are too wordy and rarely to the point (in addition to the common
fabricated details)."*[^curl-contribute]

## The sanction is immediate and unusual

> We ban users immediately who submit made up fake reports to the project.[^curl-contribute]

No warning, no graduated response. That is the sharpest enforcement statement in the bundle, and it
is aimed at a specific economic problem: bug-bounty submissions cost the reporter almost nothing to
generate and cost maintainers real time to triage. A policy that only asks for *quality* does not
address an asymmetry that large; a policy that removes the submitter does.

## Translation is encouraged, with a caveat about perception

AI translation is permitted and encouraged for non-native speakers — though contributors may want to
disclose it, to avoid maintainers dismissing the work as low-quality.[^curl-contribute]

The caveat is honest about a second-order effect the other permissive policies do not mention:
machine-translated prose can *read* like generated slop, so disclosure protects the contributor
rather than the project. Compare [Zig](zig.md), which forbids LLM translation outright and instead
invites people to post in their own language.

## What a contributor must do

Write code that meets the ordinary bar; if it is recognisably machine-written, keep working. If you
used a tool to find a security issue, say so — this is a MUST — and reproduce the issue yourself
before reporting. Never forward an unverified finding: the penalty for a fabricated report is an
immediate ban.

## Re-verification notes

The AI section lives inside the general `contribute.html` page rather than in a dedicated policy
document, so it can move or be renamed without any redirect. Search the page text for `AI` rather
than relying on a fragment anchor. curl also publishes separately about AI-generated slop in its
bug-bounty programme; treat this page as the normative one and other writing as commentary.

[^curl-contribute]: [Contribute to curl — on AI use in curl](https://curl.se/dev/contribute.html)
