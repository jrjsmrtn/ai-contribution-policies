---
type: Organization
title: Fedora
description: Has an AI-assisted contributions policy in force since 2025-10-22 by unanimous Council vote — whose agreed text has no reachable canonical publication, so this record deliberately does not state what it says.
resource: https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-council-meeting.2025-10-22-14.01.log.html
tags:
  - ai-contribution
  - policy
  - distribution
  - in-force
  - unpublished
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T07:45:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T07:45:00Z'
stale_after: 2026-11-05
sources:
  - id: fedora-council-meeting-2025-10-22
    title: Fedora Council meeting log, 2025-10-22 — AI policy approval
    resource: https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-council-meeting.2025-10-22-14.01.log.html
  - id: fedora-council-policies
    title: Fedora Council Policies
    resource: https://docs.fedoraproject.org/en-US/council/policies/
  - id: fedora-communityblog-proposal
    title: 'Council Policy Proposal: Policy on AI-Assisted Contributions (the PROPOSAL, not the adopted text)'
    resource: https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/
---

> **This record states that Fedora has a policy and that it is in force. It deliberately does not
> state what the policy says**, because the adopted text has no reachable canonical publication and
> nobody has read it here. Every other record in this bundle quotes its subject; this one cannot,
> and saying so is the finding.

**Stance: a policy exists and binds, but is not published where a contributor can find it.**

## What is established

The Fedora Council approved the AI-Assisted Contributions policy on **2025-10-22**, by a recorded
vote of **+7, 0, 0**. Aoife Moloney: *"The Fedora Council have agreed to the latest revision of the
proposed ai policy."* The policy **takes effect immediately upon council approval**, with future
revisions through the established Policy Change Process.[^fedora-council-meeting-2025-10-22]

The agreed version was referenced in **Pagure ticket #542, comment 990415**. Publication to the
Fedora policies page was to happen via a Pagure pull request, with **Justin Wheeler assigned** to add
it to Fedora's official policies documentation, and summaries to follow on Discourse, the mailing
lists and the Community Blog.[^fedora-council-meeting-2025-10-22]

## What is not

**As of 2026-08-05 the policy is not on the Fedora Council Policies page.**[^fedora-council-policies]
That page carries the Council's other standing policies — meeting cadence, communication venues,
infrastructure stance, elections, event support — and no AI policy. That is roughly nine months after
approval, against an assigned action to publish it there.

The agreed text therefore exists, so far as can be established, **only as a comment on a ticket** —
and `pagure.io` was unreachable at the time of writing, from two independent networks.

## Why this is worth a record rather than an empty cell

Fedora did the governance well: an open proposal, weeks of public discussion on Discourse, revisions
in response to community feedback, and a recorded unanimous vote. The failure is at the last step,
and it is the one that matters to a contributor.

**A rule in force that cannot be read is not a rule anyone can follow.** Contributors are bound as of
2025-10-22 by a text whose canonical location is a ticket comment on a service that may be down. This
bundle exists because unsourced summaries of policies decay silently; Fedora is the case where the
*policy itself* has the same problem, upstream of any summary.

## The Community Blog post is the proposal, not the policy

A full policy text is published on the Community Blog.[^fedora-communityblog-proposal] **It must not
be treated as the adopted text.** The Council states it approved *"the latest revision"* after
*"incorporating feedback from our community into better revisions of the initial
proposal"*[^fedora-council-meeting-2025-10-22] — so the blog post is a superseded draft, and the
extent of the differences is not documented anywhere reachable.

Quoting it here would reproduce exactly the error this bundle was built to correct: presenting a
plausible, well-formatted, out-of-date text as the current position of an organisation.

## What a contributor must do

Assume a policy binds you, because one does. Secondary reporting consistently describes disclosure
via an `Assisted-by` tag, contributor accountability, and AI not being the sole or final arbiter in
review — but that is reporting, not the text, and this record does not adopt it. Ask on the Fedora
Council's Discourse category, or in `#council`, for the current canonical location before relying on
any published summary.

## Re-verification notes

Check, in this order:

1. **[Council Policies](https://docs.fedoraproject.org/en-US/council/policies/)** — where the Council
   resolved to put it. Its appearance there supersedes this record entirely and turns it into a
   normal one.
2. **Pagure ticket #542, comment 990415** — the agreed text, when `pagure.io` is reachable.
3. **`docs.fedoraproject.org`** is behind an Anubis proof-of-work challenge for non-browser clients,
   which returns **HTTP 200 with a challenge page for any path, including ones that do not exist**.
   A 200 from that host proves neither retrieval nor existence. This record's predecessor logged a
   fabricated council URL as "located, retrieval blocked" for exactly that reason.

[^fedora-council-meeting-2025-10-22]: [Fedora Council meeting log, 2025-10-22 — AI policy approval](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-council-meeting.2025-10-22-14.01.log.html)
[^fedora-council-policies]: [Fedora Council Policies](https://docs.fedoraproject.org/en-US/council/policies/)
[^fedora-communityblog-proposal]: [Council Policy Proposal: Policy on AI-Assisted Contributions (the PROPOSAL, not the adopted text)](https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/)
