---
type: Organization
title: Kubernetes
description: Permits AI assistance, requires disclosure in the PR description, and forbids the Assisted-by and co-developed trailers — the second project here to ban that tag, for the opposite reason to GTK. It is also the only record with a mechanical enforcement hook, since the CLA check is enabled for co-authors and an AI co-author cannot sign one.
resource: https://www.kubernetes.dev/docs/guide/pull-requests/#ai-guidance
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - attribution
  - cla
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-30T05:20:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-30T05:20:00Z'
stale_after: 2027-02-28
sources:
  - id: k8s-ai-guidance
    title: 'contributors/guide/pull-requests.md — AI Guidance (kubernetes/community, master)'
    resource: https://raw.githubusercontent.com/kubernetes/community/master/contributors/guide/pull-requests.md
  - id: k8s-maintainership-blog
    title: 'Open source maintainership in the age of AI (Kevin Hannon, kubernetes.dev, 2026-06-26)'
    resource: https://www.kubernetes.dev/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/
---

**Stance: permitted, disclosed in the pull request, and never in a commit trailer.** The policy was
added on **2025-11-08**, substantially revised **2026-04-01**, and gained its worked example
**2026-04-15** — making it one of the oldest AI policies in this bundle, predating most of the
projects that have since reached the same conclusions independently.

> Using AI tools to help write your PR is acceptable, but as the author, you are responsible for
> understanding every change. If you used AI tools in preparing your PR, **you must disclose this in
> the description of your PR**. For example, including "This PR was written in part with the
> assistance of generative AI," in the PR description is
> sufficient.[^k8s-ai-guidance]

Supplying the sentence is a small thing that matters: **the disclosure rules elsewhere in this
bundle are mostly obligations without a template**, and a contributor who does not know what
compliance looks like tends either to over-disclose or to skip it.

## The second prohibition of `Assisted-by:` — for the opposite reason to GTK's

> Listing AI tooling as a co-author, co-signing commits using an AI tool, or using the
> `assisted-by`, `co-developed` or similar commit trailer **is not allowed**.[^k8s-ai-guidance]

[GTK](gtk.md) also forbids that trailer, and the two give incompatible reasons:

| Project | Trailer | Stated reason |
|---|---|---|
| [GTK](gtk.md) | forbidden | it is *"free advertising for AI companies"* |
| **Kubernetes** | forbidden | it **dilutes human accountability** |

The blog puts the second reason plainly: *"This isn't about diminishing AI's role as a tool — it's
about maintaining clear accountability. **If something breaks, there needs to be a human who
understands why and can fix it.**"*[^k8s-maintainership-blog]

**So the same rule is reached from anti-vendor sentiment and from accountability, and neither
argument implies the other.** With the [kernel](linux-kernel.md) requiring the tag without the model,
[Nerves](nerves.md) requiring it with the model, and [QEMU](qemu.md) proposing a different field
entirely, that is **five positions on commit-message attribution**, two of which agree on the rule
and disagree on why.

## The only mechanical enforcement in this bundle

Every other policy here is enforced by review — a maintainer noticing, judging, refusing. Kubernetes
found a hook that runs before a human looks:

> The CNCF provides a tool for verifying the contributor license agreements on each pull request.
> **AI agents are not able to solve these contributor license agreements** so one enforcement the
> project made is to **enable the CLA check for co-authors**. This provides a flag to reviewers that
> the PR is not ready to merge.[^k8s-maintainership-blog]

**It repurposes an existing legal instrument as a technical gate.** Listing an AI as co-author now
makes an automated check fail, because the co-author cannot sign the CLA. Nothing has to be detected
and no maintainer has to adjudicate — the prohibition enforces itself, and it does so using
machinery the project already ran for unrelated reasons.

That is worth contrasting with the [DCO](qemu.md) arguments elsewhere. Other projects reason about
whether an AI *can* satisfy a certification; Kubernetes turns the fact that it **cannot** into the
enforcement mechanism.

## Sanctions are stated, and stated twice

Most policies here describe expectations. This one names the consequence, in both places where it
applies:[^k8s-ai-guidance]

- *"Reviewers may ask questions about your AI-assisted code, and if you cannot explain why a change
  was made, **the PR will be closed**."*
- *"When responding to review comments, you must do so without relying on AI tools. Reviewers want to
  engage directly with you, not with generated responses. If you do not engage directly with
  reviewers, **the PR will be closed**."*

The second is the same rule [GTK](gtk.md) writes as *"Do NOT feed the review feedback to an
LLM/GenAI tool"* and the [Linux wireless maintainer](linux-kernel.md) enforced unilaterally by
refusing to *"argue with an LLM"* — here with the outcome spelled out in advance.

## Two limits nobody else states this bluntly

> **Large AI generated PRs and AI generated commit messages are not allowed.**[^k8s-ai-guidance]

A volume cap and a prose ban in nine words. [Nerves](nerves.md) reaches the same place with a more
carefully drawn line (*"translate or tighten your own writing is fine"*); Kubernetes simply forbids
generated commit messages outright.

> **Do not leave the first review of AI generated changes to the reviewers.** Verify the changes
> (code review, testing, etc.) before submitting your PR.[^k8s-ai-guidance]

**That is the review-cost problem stated as a contributor obligation rather than a maintainer
complaint.** [QEMU](qemu.md) explains the mechanism — a reviewer can no longer assume the submitter
reasoned through every line — and this is the corresponding duty: the first review is yours.

## The policy exists to end an argument, not only to prevent bad patches

A motive no other record here gives:

> This seems mundane and bureaucratic but **there were many PRs that derailed into discussions around
> AI usage**. The AI policy helps steer the conversation around the project's stance on AI and
> provides a clear signal to contributors on how to use these tools
> responsibly.[^k8s-maintainership-blog]

The cost being avoided is **the recurring meta-argument in every pull request**, not the AI content
itself. That reframes what a written policy is for: even a policy nobody consults has value if it
stops the same debate reopening on each contribution — which is an argument for writing one down
*before* you have a strong opinion.

## It governs AI on the contribution side while adopting it on the review side

Recorded because the asymmetry is real and easy to misread. Contributors may not use AI to respond
to reviews; meanwhile the project has **institutionally adopted AI review tooling** — a documented
process for evaluating new AI PR tools, GitHub Copilot via CNCF-provided maintainer access, and
CodeRabbit rolled out to several projects during 2026 — the post says `mid 2026` and gives no
sharper date — with `Kueue`, `JobSet` and `Agent-Sandbox` as early adopters.[^k8s-maintainership-blog]

**This is not inconsistency.** The rules bind *accountability for submitted work*; a review bot
advises a maintainer who remains responsible for the merge. But it is the only record here where a
project both restricts AI in contribution and deploys it in review, and a contributor could
reasonably be surprised to have an AI-assisted review comment land on a PR whose AI-assisted reply
would be forbidden.

The stated blocker for the Copilot rollout is worth noting for anyone planning similar tooling:
review requests depended on *contributors* holding licences, so *"automated reviews of pull requests
was out of reach for the community"* — demonstrating *"the need for organization control rather than
relying on contributors having access."*[^k8s-maintainership-blog]

## What a contributor must do

Use AI if you like, then verify the result yourself — code review, testing, understanding — **before**
submitting. Put one sentence in the **PR description** saying AI helped; the project supplies the
wording. Add **no** trailer, no AI co-author, no AI co-sign — the CLA check will fail and flag the PR
regardless. Keep the PR small and write the commit messages yourself. Answer reviewers personally: if
you cannot explain a change, or you route replies through a tool, the PR is closed.

## Re-verification notes

The policy is the *"AI Guidance"* section of `contributors/guide/pull-requests.md` in
`kubernetes/community`, rendered at `kubernetes.dev/docs/guide/pull-requests/#ai-guidance`. **Read the
repository copy** — `git log -- contributors/guide/pull-requests.md` dates every revision, and the
rendered site cannot show you when a rule changed.

The blog post carries the reasoning and the enforcement detail but is a **secondary account by one
maintainer**; every rule quoted above comes from the guide itself.

Watch for the trailer clause, which is the most consequential for cross-project contributors — the
same tag is required by the kernel and Nerves and forbidden here and by GTK — and for whether the CLA
co-author check spreads, since it is the only enforcement mechanism in this bundle that does not
depend on a maintainer noticing.

[^k8s-ai-guidance]: [contributors/guide/pull-requests.md — AI Guidance (kubernetes/community, master)](https://raw.githubusercontent.com/kubernetes/community/master/contributors/guide/pull-requests.md)
[^k8s-maintainership-blog]: [Open source maintainership in the age of AI (Kevin Hannon, kubernetes.dev, 2026-06-26)](https://www.kubernetes.dev/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/)
