---
type: Organization
title: Nerves
description: Permits AI assistance, reserves all human-facing writing to the contributor with a precise line between tightening your own prose and writing in your place, and requires an Assisted-by trailer naming the model — the exact format the Linux kernel retired eleven days earlier. Uses no Signed-off-by at all.
resource: https://github.com/nerves-project/nerves/blob/main/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - attribution
  - communication
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-29T14:05:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-29T14:05:00Z'
stale_after: 2027-02-28
sources:
  - id: nerves-contributing
    title: 'CONTRIBUTING.md — AI-assisted contributions (nerves-project/nerves, main)'
    resource: https://raw.githubusercontent.com/nerves-project/nerves/main/CONTRIBUTING.md
  - id: nerves-newsletter
    title: 'Nerves Newsletter, 2026-08-20 issue — "Nerves sets an AI policy" (Lars Wikman)'
    resource: https://underjord.io/nerves-newsletter.html
---

**Stance: permitted, with the contributor accountable and all human-facing writing reserved to
humans.** The section landed in `CONTRIBUTING.md` on **2026-08-14** and was announced six days later.
It opens on a sentence that carries the whole policy:

> Contributions are made by people, not tools.[^nerves-contributing]

## It requires the trailer format the kernel had just retired

    Assisted-by: AGENT_NAME:MODEL_VERSION

with the worked example `Assisted-by: Claude Code:claude-opus-5`.[^nerves-contributing]

**That is the [Linux kernel](linux-kernel.md)'s superseded grammar.** The kernel dropped
`AGENT_NAME:MODEL_VERSION` for the bare literal `LLM` on **2026-08-03**, because naming models
*"provides free advertising to proprietary software companies"*. Nerves adopted the retired form on
**2026-08-14**, eleven days later.

So one trailer now carries three incompatible rules across this bundle:

| Project | Rule | Reasoning |
|---|---|---|
| [Linux kernel](linux-kernel.md) | **required**, model **not** named | naming vendors is free advertising |
| [GTK](gtk.md) | **forbidden** entirely | the trailer itself is free advertising |
| **Nerves** | **required**, model **named** | credit the tools used |

**A hazard worth naming, and a claim deliberately not made.** `docs.kernel.org` still served
`AGENT_NAME:MODEL_VERSION` and the `Claude:claude-3-opus` example when checked on 2026-08-29 — it
renders a released kernel, not mainline. A project copying the kernel's convention from the rendered
documentation would get exactly the format Nerves uses. **That the stale page and the adopted format
match is checkable; that one caused the other is not, and is not claimed here.** Nerves may simply
have decided the model is worth recording — a defensible position the kernel itself held until this
month, and its policy cites no external authority at all.

**That the route exists is no longer hypothetical**, which sharpens rather than settles the question.
[MacPorts](macports.md) proposed the same retired format on 2026-08-04, explicitly *"in the format
recommended by the Linux kernel developers"* and citing the stale rendered page. **Nerves cites
nothing, so the same inference cannot be drawn about it** — the two cases look alike and only one is
evidenced.

**It also drops the other kernel instrument**: *"Do not add `Signed-off-by` tags. Nerves does not use
them."*[^nerves-contributing] That is a **fifth** destination for the DCO in this bundle, alongside
the kernel's bar-the-agent, QEMU's unsatisfiable, the Linux Foundation's not-invoked and
[NetworkManager](networkmanager.md)'s abolition.

## The sharpest line on communication in this bundle

> Pull request titles, descriptions, issue reports, commit messages, and review discussions should be
> written by the contributor. **Using AI to translate or tighten your own writing is fine. Using it to
> write in your place is not.**[^nerves-contributing]

Several projects restrict AI in communication — Debian's Proposals **C** and **G**,
[TeX Live](../distributions/tex-live.md), [NetworkManager](networkmanager.md). **None of them splits
*assist* from *substitute* this cleanly**, and the distinction is what makes the rule enforceable
against the objection that non-native speakers need help: tightening your own sentence is explicitly
allowed, and so is translation.

It extends to volume as well as authorship, with a line that inverts the usual assumption about who
should be talking to a model:

> Do not submit lengthy AI-generated summaries, explanations, or code walkthroughs. **Reviewers can
> chat with an LLM on their own time about your contributions, if they desire** — it is more
> important that the submitter convey their own understanding in their own
> words.[^nerves-contributing]

## Rules aimed at agents, and at agent configuration

Most policies here regulate generated text. Nerves regulates the **workflow around the agent**, and
two of these have no counterpart in this bundle:[^nerves-contributing]

- *"Comment on an open issue before pointing a coding agent at it."* — coordination *before* the
  work, not disclosure after it, which is the only rule here that tries to prevent duplicated agent
  effort rather than review it.
- *"Don't add AI tool configuration such as `AGENTS.md` or `CLAUDE.md` without asking first."* —
  **the only rule in this bundle governing the agent-instruction files themselves** as a class of
  contribution.
- *"Verify claims before making them. Unconfirmed bug reports, and especially unconfirmed security
  reports, cost maintainers a lot of time."* — the same target as [GTK](gtk.md)'s ban on fabricated
  benchmarks and reproducers: the **evidence** offered for a change, not the change.
- *"Keep the change focused. Delete unrelated refactoring, speculative abstractions, defensive error
  handling, and comments that restate the code."* — a shape constraint like GTK's, and it names the
  specific artifacts generation tends to add.
- *"Review AI-generated code as carefully as you would review a stranger's, and confirm that it
  compiles, runs, and is tested before sending it."*

## Friction is the point, and the reason is review bandwidth

The announcement gives the reasoning the policy file does not. It was written *"through discussion in
the core team around many, many .. many instances of our use of LLMs, drive-by contributions via
LLMs, thoughtful contributions via LLMs"*, and states the motive plainly: *"Friction is kind of the
point."* One well-meaning person with agents can *"completely saturate the bandwidth of the Nerves
core team in terms of review and feedback."*[^nerves-newsletter]

**That is review bandwidth again** — the same ground [GNOME](gnome.md) gives (*"to reduce the strain
on volunteer reviewers"*), the same one the [Linux wireless maintainer](linux-kernel.md) gave for
refusing compliant patches, and the one the kernel's `generated-content.rst` opens with. **Four
independent projects, one motive.** It is now the most common stated reason for an AI rule in this
bundle — more common than licensing, copyright or output quality.

The project is explicit that this is not opposition: *"We are not inherently against it … The project
doesn't take a hard stance in that because you'll do what you do."*[^nerves-newsletter]

> ⚠ **The newsletter is a source a third party cannot fetch.** It was received by email; underjord.io
> publishes no per-issue archive, so the `resource` above is the newsletter's home page rather than
> the issue. Every claim about **what the policy says** is taken from the public `CONTRIBUTING.md`
> instead. The quotations in this section are rationale, not rule, and are marked as such.

## Copied into every repository — on purpose, and not quite completely

> There is a copy in every official nerves repo to hopefully **encourage agents to surface this** as
> well as help people find it.[^nerves-newsletter]

**A novel motive for duplication.** [GNOME](gnome.md)'s modules copied a policy between themselves and
the copies drifted; Nerves replicates deliberately, and the stated reason is that an agent reading one
repository should encounter the rule without being pointed at a central document. **The policy is
written partly for the tools it governs.**

Spot-checked on 2026-08-29 across four `nerves-project` repositories: `nerves_bootstrap`,
`ssh_subsystem_fwup` and `ring_logger` all carry the section with the same trailer format;
**`nerves_system_br` has no `CONTRIBUTING.md` at all.** The rollout is real and the *"every"* is an
overstatement — worth knowing before relying on any single repository to surface the rule.

## What a contributor must do

Use AI if you like, then review its output as you would a stranger's, and confirm it compiles, runs
and is tested. **Write your own** PR title, description, issue report, commit message and review
replies — translating or tightening your own words is fine, having a tool write in your place is not.
Do not paste in generated summaries or walkthroughs. Comment on an issue before pointing an agent at
it, keep the change focused, and verify any claim you make, especially a security one. Add
`Assisted-by: AGENT_NAME:MODEL_VERSION`; add **no** `Signed-off-by`. Do not add an `AGENTS.md` or
`CLAUDE.md` without asking.

## Re-verification notes

The policy is the *"AI-assisted contributions"* section of `CONTRIBUTING.md` in
`nerves-project/nerves`; `git log -- CONTRIBUTING.md` dates it to commit `28dc3f77` on 2026-08-14.
Because copies are replicated across repositories, **check the canonical one** — divergence between
copies is what happened to GNOME's shared text within months.

Watch the trailer clause specifically. It is the most likely thing here to change, because the format
it mandates was retired by the project that invented it, and because a contributor working across
Nerves, the kernel and GTK is subject to three mutually exclusive rules about the same tag.

[^nerves-contributing]: [CONTRIBUTING.md — AI-assisted contributions (nerves-project/nerves, main)](https://raw.githubusercontent.com/nerves-project/nerves/main/CONTRIBUTING.md)
[^nerves-newsletter]: [Nerves Newsletter, 2026-08-20 issue — "Nerves sets an AI policy" (Lars Wikman)](https://underjord.io/nerves-newsletter.html)
