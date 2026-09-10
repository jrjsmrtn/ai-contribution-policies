---
type: Organization
title: ripgrep
description: Welcomes LLM-assisted coding, forbids autonomous agents, and reserves every word addressed to a maintainer to humans — with hiding rather than closing as the sanction for generated comments. Its entire CONTRIBUTING.md is a pointer to that policy, and the policy itself is the middle hop of the only attributed lineage in this bundle.
resource: https://github.com/BurntSushi/ripgrep/blob/master/AI_POLICY.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - restricted
  - communication
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:29:44Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:29:44Z'
stale_after: 2027-03-08
sources:
  - id: rg-ai-policy
    title: 'AI Policy (AI_POLICY.md, BurntSushi/ripgrep, master)'
    resource: https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md
  - id: rg-contributing
    title: 'Contributing (CONTRIBUTING.md, BurntSushi/ripgrep, master)'
    resource: https://raw.githubusercontent.com/BurntSushi/ripgrep/master/CONTRIBUTING.md
  - id: astral-ai-policy
    title: 'AI Policy (AI_POLICY.md, astral-sh/.github, at commit c5187e20) — the source ripgrep adapted'
    resource: https://raw.githubusercontent.com/astral-sh/.github/c5187e200db51bfe11d56e13053d29bd3793fdd8/AI_POLICY.md
---

**Stance: permitted for code, refused for autonomous agents, and reserved to humans for every word
addressed to a maintainer.** Added **2026-05-26**, and the whole of `CONTRIBUTING.md` is 213 bytes
pointing at it:

> ## Use of AI
>
> All use of AI in contributions must follow the [AI Policy]. **Contributions not following the AI
> Policy will be closed.**[^rg-contributing]

A 68,000-star project whose contributing guide contains nothing but an AI policy reference and a
sanction. Whatever else contributing to ripgrep involves is not written down; this is.

## Responsibility is stated in both directions

> Using AI (i.e., LLMs) as tools for coding is welcome. A high bar is held for all contributions to
> this project. Moreover, **the project maintainers remain responsible for any code that is published
> as part of a release.** Contributors are expected to be responsible for any code they
> publish.[^rg-ai-policy]

**Almost every policy in this bundle places responsibility on the contributor and stops.** This one
names the maintainer's share first. That is not a softening — it is the argument for the high bar,
since the person who cannot refuse the consequences is the one setting the standard.

## The sanction for generated prose is hiding, not closing

> **AI should not be used to generate comments when communicating with maintainers.** Comments are
> expected to be written by humans. **Comments that are believed to be written by AI may be hidden
> without notice.**[^rg-ai-policy]

Hiding is a lighter and stranger instrument than the closures used elsewhere, and it fits the
offence: a generated comment wastes a reader's attention, so removing it from view is the remedy. It
is also the only sanction here that operates on a *belief* about authorship — no detection is claimed
and none is offered, which is honest about what a maintainer is actually doing.

The rule then reaches both directions of the conversation: *"If you are opening an issue, you should
be able to describe the problem in your own words"*, and for a pull request, *"you are expected to be
able to explain the proposed changes in your own words. This includes the pull request body and
responses to questions. **Do not copy responses from the AI when replying to questions from
maintainers.**"*[^rg-ai-policy]

## Autonomous agents are refused, with the same phrasing Zed later used

> This project requires **a human in the loop who understands the work produced by AI. Autonomous
> agents are not allowed to be used for contributing to this project.** Pull requests that appear in
> violation of this will be closed, perhaps without notice.[^rg-ai-policy]

[Zed](zed.md) carries this almost verbatim, and the reason is recorded below. **What did not carry
is Astral's justification** — the criticality argument is the clause dropped at this hop. Nine records
constrain autonomous agents and they constrain five different things; see
[human in the loop](../mechanisms/human-in-the-loop.md).

## Sharing model output, with a length limit nobody else states

> If you wish to include context from an interaction with AI in your comments, it must be **in a quote
> block** and **disclosed as such**. It must be accompanied by **human commentary explaining the
> relevance and implications** of the context. **Do not share long snippets.**[^rg-ai-policy]

Quote, label, interpret — the three-part recipe [Zed](zed.md) inherited — plus a fourth constraint
nobody else imposes: **brevity**. It is the only place in this bundle where the *volume* of quoted
model output is bounded, and it follows from the hiding sanction: the objection is to reader
attention being spent, and a long snippet spends more of it.

## Translation, with the emphasis on voice

> AI is useful when communicating as a non-native English speaker. If you are using AI to edit your
> comments for this purpose, please take the time to **ensure it reflects your own voice and ideas**.
> If using AI for translation, we recommend **writing in your native language and including the AI
> translation in a quote block.**[^rg-ai-policy]

The same construction [Zed](zed.md) uses and the same one [Nerves](nerves.md), [Perl](perl.md) and
[Elixir](elixir.md) arrive at independently — **the translation carve-out is the closest thing to a
consensus in this bundle.** ripgrep adds the part the others leave implicit: the test is whether the
result is still *your voice*, not whether a tool was used.

## The middle hop of the only attributed lineage here

The policy closes by naming its source, pinned to an exact commit:

> This policy was adapted from **[uv's AI policy]** —
> `astral-sh/.github` at `c5187e20…`[^rg-ai-policy]

**Pinning the citation to a SHA rather than to a branch is the careful choice**, and it is checkable:
the pinned text and the current `astral-sh/.github/AI_POLICY.md` were compared on 2026-09-08 and are
**byte-identical**, so nothing has drifted under the reference.[^astral-ai-policy]

That makes ripgrep the middle hop of a dated four-hop chain — tabulated, with the five other copying
events in this bundle, in [policy by copying](../mechanisms/policy-by-copying.md).

**The adaptation is visible in the commits.** ripgrep landed the policy at `f0cec341`
(`2026-05-26T04:02:44Z`) carrying Astral's *"our projects"* wording unedited, and corrected it to
*"this project"* **8 hours 33 minutes later** at `4857d6fa` — the single edit that turns an
organisation-wide text into one project's rule. That is the whole mechanics of adaptation in one
`sed` expression, and [Zed](zed.md)'s pinned citation landed on the wrong side of it.

And the reason it spreads is partly licensing: ripgrep is **Unlicense**, a public-domain dedication,
so downstream projects face no attribution obligation. [Zed](zed.md) attributed anyway. That is the
same property [GCC](gcc.md)'s CC0 policy has and, as there, **the licence is what makes the text
adoptable rather than merely readable.**

## What a contributor must do

Use an LLM to write code. **Do not let it run unattended** — autonomous-agent pull requests are
closed, perhaps without notice. **Write everything you say to a maintainer yourself**: the issue
description, the pull request body, and every reply. If you need to quote model output, put it in a
quote block, say what it is, explain why it matters, and keep it short. If English is not your first
language, write in your own and put the translation in a quote block — and make sure what comes out
is still your voice. Contributions that do not follow the policy are closed.

## Re-verification notes

Two files, and the small one matters: `AI_POLICY.md` is the policy, `CONTRIBUTING.md` is 213 bytes
that exist to point at it and state the sanction. `git log -- AI_POLICY.md` shows **two commits, both
2026-05-26** — the add, and the `s/our projects/this project` adaptation.

**Re-check the pin, not just the policy.** The citation names `astral-sh/.github` at a fixed SHA. Its
value as provenance depends on the pinned text remaining fetchable, and its value as *currency*
depends on whether the upstream has since moved — verified identical on 2026-09-08, which will not
stay true forever.

**Astral's policy is an org-level default and is now recorded** at
[Astral](../vendors/astral.md). It binds contributors to uv, ruff and their siblings from a single
`.github` repository, which makes it the closest thing in this bundle to a foundation floor published
by a company — and the origin of this one. **If that file changes, this record's currency claim goes
with it**, since the claim is that ripgrep's pinned text still matches upstream.

Watch whether the chain grows a fifth hop, and whether any of them starts citing ripgrep rather than
Astral — the point at which a lineage becomes a convention is when the borrowers stop agreeing on
who the source is.

[^rg-ai-policy]: [AI Policy (AI_POLICY.md, BurntSushi/ripgrep, master)](https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md)
[^rg-contributing]: [Contributing (CONTRIBUTING.md, BurntSushi/ripgrep, master)](https://raw.githubusercontent.com/BurntSushi/ripgrep/master/CONTRIBUTING.md)
[^astral-ai-policy]: [AI Policy (AI_POLICY.md, astral-sh/.github, at commit c5187e20) — the source ripgrep adapted](https://raw.githubusercontent.com/astral-sh/.github/c5187e200db51bfe11d56e13053d29bd3793fdd8/AI_POLICY.md)
