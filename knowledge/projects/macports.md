---
type: Organization
title: MacPorts
description: Has no adopted AI policy. An open, contested pull request would require an Assisted-by trailer "in the format recommended by the Linux kernel developers" — but the format it copies was retired by the kernel one day before the PR opened, and the page it cites still serves the superseded form. The trailer's premise is being argued against in the thread.
resource: https://github.com/macports/macports-base/pull/420
tags:
  - ai-contribution
  - policy
  - project
  - draft
  - attribution
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-29T14:20:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-29T14:20:00Z'
stale_after: 2026-11-29
sources:
  - id: macports-pr-420
    title: 'macports-base PR #420 — Add CONTRIBUTING.md (open, jmroot)'
    resource: https://github.com/macports/macports-base/pull/420
  - id: macports-pr-420-diff
    title: 'macports-base PR #420 — proposed CONTRIBUTING.md, diff'
    resource: https://patch-diff.githubusercontent.com/raw/macports/macports-base/pull/420.diff
---

**Stance: undecided. This record describes a proposal, not a rule.** MacPorts has no adopted AI
policy. Pull request **#420**, *"Add CONTRIBUTING.md"*, was opened by Joshua Root on **2026-08-04**
and was **still open and unmerged** when checked on 2026-08-29.[^macports-pr-420] It is recorded here
because of what it demonstrates, not because it binds anyone.

> ⚠ **Nothing below is in force.** If you are contributing to MacPorts today, no written AI rule
> applies. Re-read the PR before relying on any of this.

## What it proposes

> If an LLM or other automated tool was used to generate a contribution in whole or part, an
> `Assisted-by:` tag **in the format recommended by the Linux kernel developers** must be present in
> the Git commit message.
>
>     Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]
>
> This information must be disclosed for all contributions.[^macports-pr-420-diff]

Plus a responsibility clause — contributors certify they *"have the legal right"* to contribute and
that the material *"can be distributed under the project's license"* — and one rule about agents:
*"Please do not use agents or similar software to open pull requests or tickets without human
supervision."*[^macports-pr-420-diff]

## The format it adopts was retired the day before it was proposed

This is the finding, and it is checkable in three steps.

The PR cites `docs.kernel.org/process/coding-assistants.html#attribution` as its
authority.[^macports-pr-420-diff] The [Linux kernel](linux-kernel.md) **replaced**
`AGENT_NAME:MODEL_VERSION` with the bare literal `LLM` in mainline on **2026-08-03**, because naming
models *"provides free advertising to proprietary software companies"*. This PR opened **2026-08-04**,
one day later, specifying the retired form.

**And the page it cites still serves that retired form** — `docs.kernel.org` renders a released
kernel rather than mainline, and on 2026-08-29 it still showed `AGENT_NAME:MODEL_VERSION` and the
`Claude:claude-3-opus` example.

**This is the documented instance of a hazard the rest of this bundle could otherwise only describe
in the abstract**: a rendered documentation site outliving the source it renders, and a second
project copying the superseded rule from it in good faith. No carelessness is implied — the PR cites
a canonical-looking URL on the project's own domain, which is exactly what a careful person does.
*What went wrong is that the URL was stale, not that the author was.*

**The evidence supports the mechanism, not intent.** The PR cites that page and reproduces the format
that page serves; whether the author consulted mainline is unknown and not claimed.

## The premise itself is contested in the thread

The PR body calls the trailer *"what appears to be the emerging de facto standard for tagging AI
use."*[^macports-pr-420] **This bundle's evidence is that no such standard exists.** The same trailer
is required without the model by the kernel, required *with* the model by [Nerves](nerves.md), and
forbidden outright by [GTK](gtk.md) — three mutually exclusive rules, all live.

A reviewer reached a related conclusion from first principles rather than from the corpus:

> what is the purpose of "assisted-by" or "co-authored-by" for LLMs? The author of the commit is
> responsible for its contents. … the "assisted-by" line also looks a bit hacked together, eg.
> mentioning Claude twice, and **I don't see what the format of `MODEL_VERSION` is supposed to be
> exactly**, other than a solitary example.[^macports-pr-420]

*"Mentioning Claude twice"* is a precise reading of the retired example, `Assisted-by:
Claude:claude-3-opus`, where agent and model name the same vendor — **a critique of the very
ambiguity the kernel resolved by deleting the field.** The reviewer arrives at the kernel's own
conclusion without knowing the kernel had already reached it, which is some evidence the format was
the problem rather than its documentation.

Two counter-positions follow, both of which appear elsewhere in this bundle:

- **Move disclosure to review.** *"The correct place for disclosure is at the time of review in the
  PR, we can add an additional item to the existing checklist for this."*[^macports-pr-420] That is
  [GTK](gtk.md)'s arrangement exactly — disclose in the merge request, keep it out of the commit
  trailer.
- **Disclosure will stop being informative.** *"almost all code going forward is going to be written
  by AI and so it's not necessarily interesting information any longer; we can mostly just assume
  that everything is AI assisted. The important part … is that a human is **responsible** for the
  output."*[^macports-pr-420] No adopted policy in this bundle takes that position; it is the
  strongest stated case here for *not* requiring disclosure at all.

## Supervision, not prohibition

The one agent rule attracted a refinement worth recording, because it separates two things most
policies conflate:

> asking your AI to pull something is not the same as having it do it without supervision and is
> okay … The problem is having someone mindlessly run an AI against the repo without supervision and
> inundate us with low quality requests … creating work for human beings.[^macports-pr-420]

**Reviewer bandwidth again**, from a fifth independent project — after [GNOME](gnome.md), the
[Linux wireless maintainer](linux-kernel.md), the kernel's `generated-content.rst` and
[Nerves](nerves.md). It is now the most frequently stated reason for an AI rule in this corpus.

## What a contributor must do

**Nothing specific to AI is required today**, because the PR has not merged. The existing
expectations still apply: you are responsible for your contribution and must have the right to
license it. If #420 merges in its current form you would add an `Assisted-by:` trailer — but check
the merged text rather than this record, since the trailer clause is the most contested part of the
proposal and the format it currently names is one the kernel has abandoned.

## Re-verification notes

The proposal lives in an open pull request, so **its state is the thing most likely to change**:
check whether #420 merged, and if so with which trailer clause. `stale_after` is three months rather
than six for that reason.

Two live leads sit in the thread. The reviewer cites the **Kubernetes** contribution guidance
(*"Open Source Maintainership in the Age of AI"*, kubernetes.dev, 2026-06-26) on human accountability
— not yet a record in this bundle. And the discussion repeatedly drifts to retiring Trac in favour of
GitHub, which is out of scope here but explains why the thread is long.

[^macports-pr-420]: [macports-base PR #420 — Add CONTRIBUTING.md (open, jmroot)](https://github.com/macports/macports-base/pull/420)
[^macports-pr-420-diff]: [macports-base PR #420 — proposed CONTRIBUTING.md, diff](https://patch-diff.githubusercontent.com/raw/macports/macports-base/pull/420.diff)
