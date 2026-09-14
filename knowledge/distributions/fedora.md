---
type: Organization
title: Fedora
description: Permits AI-assisted contributions under a Council policy approved 2025-10-22 and published two days later — MUST take responsibility, MUST disclose when a significant part is taken from a tool unchanged, with an Assisted-by trailer as the recommended method. It also forbids AI as the final judge of a contribution or of a person's standing. This record said the policy was unpublished from 2026-08-05 to 2026-09-14; it never was.
resource: https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/
tags:
  - ai-contribution
  - policy
  - distribution
  - in-force
  - permitted
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T07:45:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T07:45:00Z'
  - by: claude/opus-5
    at: '2026-09-14T13:10:00Z'
stale_after: 2027-03-14
sources:
  - id: fedora-ai-policy
    title: 'AI-Assisted Contributions Policy — Fedora Council (v1.0, 2025-10-24)'
    resource: https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/
  - id: fedora-ai-policy-src
    title: 'council/modules/ROOT/pages/policy/ai-contribution-policy.adoc (forge.fedoraproject.org council/docs, main)'
    resource: https://forge.fedoraproject.org/council/docs/raw/branch/main/council/modules/ROOT/pages/policy/ai-contribution-policy.adoc
  - id: fedora-ai-policy-commit
    title: 'council/docs commit 823e93b640 — Add AI-Assisted Contributions Policy (2025-10-24)'
    resource: https://forge.fedoraproject.org/council/docs/commit/823e93b640dea2205d6df2bc51586552a52898d7
  - id: fedora-council-nav
    title: 'council/modules/ROOT/nav.adoc (forge.fedoraproject.org council/docs, main)'
    resource: https://forge.fedoraproject.org/council/docs/raw/branch/main/council/modules/ROOT/nav.adoc
  - id: fedora-council-meeting-2025-10-22
    title: Fedora Council meeting log, 2025-10-22 — AI policy approval
    resource: https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-council-meeting.2025-10-22-14.01.log.html
  - id: fedora-council-policies
    title: 'Fedora Council — Additional Policies (the page this record checked on 2026-08-05)'
    resource: https://docs.fedoraproject.org/en-US/council/policies/
---

**Stance: permitted, with accountability and threshold disclosure.** The Fedora Council approved the
AI-Assisted Contributions Policy on **2025-10-22** by a recorded vote of **+7, 0,
0**,[^fedora-council-meeting-2025-10-22] and it was added to the Council documentation on
**2025-10-24**.[^fedora-ai-policy-commit] The published text carries `v1.0, 2025-10-24`, and a
2026-01-15 commit added that version line without changing the rules — the two revisions differ
only in the version line and an author attribute, compared on 2026-09-14.[^fedora-ai-policy-src]

## ⚠ Correction: this record was wrong for six weeks, and wrong from its first day

From 2026-08-05 to 2026-09-14 this record said the policy *"has no reachable canonical
publication"* and deliberately declined to state what it said. **The policy had been published for
more than nine months when that was written.**

The cause was the page checked. The record looked at `council/policies/`,[^fedora-council-policies] which the Council's own
navigation labels **"Additional Policies"**; the AI policy sits under a separate **"Council
Policies"** heading at `council/policy/ai-contribution-policy/`.[^fedora-council-nav] At the time,
the docs site also sat behind an Anubis challenge and the Pagure ticket holding the agreed text was
unreachable, so the page that did load looked like confirmation. **An absence was recorded from one
list, when the site had two.** On 2026-09-14 the policy page fetched without a challenge and its
source fetched from `forge.fedoraproject.org`.

The earlier record's refusal to quote the Community Blog proposal as policy was right, and remains
right: that post is the proposal, not the adopted text.

## The policy

> You *MAY* use AI assistance for contributing to Fedora, as long as you follow the principles
> described below.[^fedora-ai-policy]

Four principles follow, in RFC 2119 language.

**Accountability** — *"You *MUST* take the responsibility for your contribution. Contributing to Fedora
means vouching for the quality, license compliance, and utility of your submission. … The contributor
is always the author and is fully accountable for the entirety of these
contributions."*[^fedora-ai-policy]

**Transparency** — a threshold, not a blanket rule:

> You *MUST* disclose the use of AI tools when the significant part of the contribution is taken from
> a tool without changes. You *SHOULD* disclose the other uses of AI tools, where it might be useful.
> Routine use of assistive tools for correcting grammar and spelling, or for clarifying language, does
> not require disclosure.[^fedora-ai-policy]

That is close to [Ansible](../projects/ansible.md)'s wording — significant unmodified output, with
grammar and spelling exempt — with Fedora's *MUST* where Ansible has *SHOULD*. Which text came first,
and whether one drew on the other, is not established here.

**Disclosure goes where authorship goes.** *"For contributions tracked in git, the recommended method
is an `Assisted-by:` commit message trailer"*; elsewhere, document preambles, design-file metadata,
translation notes or a wiki category.[^fedora-ai-policy] The two examples are *"`Assisted-by: generic
LLM chatbot`"* and *"`Assisted-by: ChatGPTv5`"* — so Fedora recommends the trailer with a model named,
the form the [Linux kernel](../projects/linux-kernel.md) dropped as *"free advertising"*. See
[the Assisted-by trailer](../mechanisms/assisted-by-trailer.md).

**Contribution and community evaluation** — a limit on reviewers and on the project, not only on
contributors:

> You *MUST NOT* use AI as the sole or final arbiter in making a substantive or subjective judgment on
> a contribution, nor may it be used to evaluate a person's standing within the community (e.g., for
> funding, leadership roles, or Code of Conduct matters).[^fedora-ai-policy]

Automated technical validation — CI, tests, spam filtering — is excluded, and *"The final
accountability for accepting a contribution, even if implemented by an automated system, always
rests with the human contributor who authorizes the action."* **Few policies here say anything about
AI judging people**; this one rules it out for funding, leadership and conduct decisions by name.

**Large-scale initiatives** are out of scope: work that *"may significantly change the ways the
project operates or lead to exponential growth in contributions"* must be discussed with the Council
separately. Suspected violations go to the Council through private tickets.[^fedora-ai-policy]

## Governance, which was done well throughout

An open proposal, public discussion, revisions in response to it, a recorded unanimous vote, and
publication two days later by the person assigned to publish it.[^fedora-council-meeting-2025-10-22]
[^fedora-ai-policy-commit] **Every step of Fedora's process worked; this bundle's check of it did
not.**

[LLVM](../projects/llvm.md) credits *"the Fedora project policy proposal"* for part of its own text.
That is the proposal, not this adopted version, and the two have not been compared here.

## What a contributor must do

Take responsibility for everything you submit, including its licence. If a significant part came from
an AI tool unchanged, disclose it — in git, with an `Assisted-by:` trailer. Disclose other uses where
useful; grammar and spelling help needs no disclosure. If you review or decide things in Fedora, do not
let an AI make the final call on a contribution, and do not use one to judge a person. Take any
large-scale AI initiative to the Council first.

## Re-verification notes

**Read the source, and read the navigation before concluding anything is absent.** The policy's source
is `ai-contribution-policy.adoc` in `council/docs` on `forge.fedoraproject.org`; its commit history
dates every change. The Council's `nav.adoc` lists which pages exist and under which heading — the
check this record skipped. Anubis has been seen on `docs.fedoraproject.org`; when it appears, the
forge source is the route.

[^fedora-ai-policy]: [AI-Assisted Contributions Policy — Fedora Council (v1.0, 2025-10-24)](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/)
[^fedora-ai-policy-src]: [council/modules/ROOT/pages/policy/ai-contribution-policy.adoc (forge.fedoraproject.org council/docs, main)](https://forge.fedoraproject.org/council/docs/raw/branch/main/council/modules/ROOT/pages/policy/ai-contribution-policy.adoc)
[^fedora-ai-policy-commit]: [council/docs commit 823e93b640 — Add AI-Assisted Contributions Policy (2025-10-24)](https://forge.fedoraproject.org/council/docs/commit/823e93b640dea2205d6df2bc51586552a52898d7)
[^fedora-council-nav]: [council/modules/ROOT/nav.adoc (forge.fedoraproject.org council/docs, main)](https://forge.fedoraproject.org/council/docs/raw/branch/main/council/modules/ROOT/nav.adoc)
[^fedora-council-meeting-2025-10-22]: [Fedora Council meeting log, 2025-10-22 — AI policy approval](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-council-meeting.2025-10-22-14.01.log.html)
[^fedora-council-policies]: [Fedora Council — Additional Policies (the page this record checked on 2026-08-05)](https://docs.fedoraproject.org/en-US/council/policies/)
