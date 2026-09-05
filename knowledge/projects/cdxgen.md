---
type: Organization
title: cdxgen
description: Has no contribution policy at all — no CONTRIBUTING file and no code of conduct — yet publishes a machine-readable AI-DECLARATION.md grading its own AI usage per source path against an external six-level scale. It is the only record here that discloses what the project did rather than governing what a contributor may do, and the only one whose disclosure is a parseable artifact rather than prose.
resource: https://github.com/cdxgen/cdxgen/blob/master/AI-DECLARATION.md
tags:
  - ai-contribution
  - policy
  - project
  - no-policy
  - disclosure
  - attribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-05T22:25:31Z'
verified:
  - by: claude/opus-5
    at: '2026-09-05T22:25:31Z'
stale_after: 2027-03-06
sources:
  - id: cdxgen-ai-declaration
    title: 'AI-DECLARATION.md (cdxgen/cdxgen, master)'
    resource: https://raw.githubusercontent.com/cdxgen/cdxgen/master/AI-DECLARATION.md
  - id: aideclaration-spec
    title: 'AI-DECLARATION.md — Open Standard for AI Usage Transparency, v0.1.2'
    resource: https://ai-declaration.md/en/0.1.2
  - id: cdxgen-agents
    title: 'AGENTS.md — cdxgen contributor guide for AI agents (cdxgen/cdxgen, master)'
    resource: https://raw.githubusercontent.com/cdxgen/cdxgen/master/AGENTS.md
  - id: cdxgen-readme
    title: 'README.md (cdxgen/cdxgen, master) — the declaration badge and the OWASP production-project statement'
    resource: https://raw.githubusercontent.com/cdxgen/cdxgen/master/README.md
  - id: owasp-devguide-contributing
    title: 'Providing content — OWASP Developer Guide (Use of AI)'
    resource: https://devguide.owasp.org/contributing/
---

**Stance: no contributor-facing rule of any kind, and a published self-declaration instead.** Every
other record in this bundle answers *what the project demands of you*. This one answers *what the
project did*, and it is the only record here whose answer is a machine-readable file rather than
prose.

cdxgen is the polyglot CycloneDX SBOM generator, *"an OWASP Foundation production
project"*.[^cdxgen-readme] It has **no `CONTRIBUTING.md` and no `CODE_OF_CONDUCT.md`** — absent from
all 2,326 entries of the tree, and reported as absent by GitHub's own community profile. There is
therefore no permission, no prohibition, no disclosure requirement and no trailer rule addressed to a
contributor.

## The declaration, in full

`AI-DECLARATION.md` is 400 bytes at the repository root, badged from the first line of the
README:[^cdxgen-ai-declaration]

```yaml
---
version: "0.1.2"
level: pair
components:
  lib/inventory/ciParsers: pair
  lib/inventory/table.js: pair
  lib: assist
  test: assist
  bin: assist
---
```

> Various models, such as Google Gemini, Qwen 3.5, GPT-5, and Claude Sonnet/Opus, were used. **Most
> changes were reviewed by both agents and maintainers.**[^cdxgen-ai-declaration]

**Two things no other record here supplies.** The disclosure is scoped **per source path**, so a
reader can tell that the CI parsers were written in partnership with a model while `bin/` was only
assisted. And it **names the models** — four of them, across three vendors — which the
[Linux kernel](linux-kernel.md) deliberately stopped doing and [GTK](gtk.md) forbids outright.

## A degree vocabulary, defined externally

The file cites `ai-declaration.md` v0.1.2,[^aideclaration-spec] which defines a **six-level ordinal
scale** built from the verbs *act* and *prompt*:

| Level | Definition |
|---|---|
| `none` | Human acts on the task alone with no AI involvement |
| `hint` | Human acts on the task and the AI surfaces suggestions passively |
| `assist` | Human prompts and the AI acts on **a part** of the task |
| `pair` | Human prompts as both human and AI act on the task **equally**; human understands internals clearly |
| `copilot` | Human prompts and AI acts on the **whole** task, prompting for permission or clarification |
| `auto` | Human prompts and AI acts **autonomously**, bringing the task to completion |

It also defines six **processes** — design, implementation, testing, documentation, review,
deployment — so involvement can differ by phase, with two structural rules: the global `level` must
be the highest present, and any process not listed is *"assumed to be `none`
implicitly."*[^aideclaration-spec]

**This is the finest-grained disclosure vocabulary in the bundle by a wide margin.** The overview's
[disclosure tags](../overview.md) record *that* AI was used, and at most *which tool*; QEMU's proposed
`AI-used-for:` records *where*. This records *how much*, on a defined scale, per path — and the scale
is versioned and maintained outside any single project, which none of the trailer conventions are.

The spec's own rationale inverts the usual argument for disclosure:

> This is not to discourage usage of LLM- and other code-generation … On the contrary, it is an
> enabler. **When you declare what parts of the code were, in fact, generated, a skeptic can
> immediately look into just those parts** to satisfy their urge to re-verify and
> double-check.[^aideclaration-spec]

Disclosure as **review triage** rather than as compliance or as warning. That is a fourth job for a
provenance signal, alongside the three the overview already separates.

## It is maintained, which is what distinguishes it from a badge

Three commits in four months, and the third is the one that matters:[^cdxgen-ai-declaration]

| Date | Change |
|---|---|
| 2026-04-15 | Added, `level: pair`, with `lib/helpers/ciParsers` at `pair` |
| 2026-04-22 | `lib/helpers/table.js` added at `pair` when a new pair-built file appeared |
| 2026-08-06 | Both paths rewritten `lib/helpers/*` → `lib/inventory/*`, following a refactor |

**The last commit changes no fact — it carries the declaration through a directory rename.** A badge
would have rotted silently there. This is the only evidence in the bundle of an AI-provenance claim
being *maintained against the code it describes*, and it is the answer to the obvious objection that
a self-declaration is unfalsifiable decoration.

## What it is not: `AGENTS.md` here is a codebase guide, not a policy

cdxgen carries a 36 KB `AGENTS.md` added 2026-04-11 and revised across 25 commits. Its opening line
sets the scope:

> This document helps AI coding agents (GitHub Copilot, Claude, Cursor, etc.) understand the cdxgen
> codebase conventions, architecture, and contribution rules so they can produce code that fits
> naturally with the existing style.[^cdxgen-agents]

Its content is engineering constraint — construct purls with `PackageURL`, never by concatenation;
route HTTP through `cdxgenAgent`; never emit raw secrets into BOM fields — and it contains **no
permission, prohibition, disclosure rule or trailer rule**.

**This is the same filename as [Asahi Linux](asahi-linux.md)'s and the opposite artifact.** Asahi's is
181 bytes and instructs the tool to refuse and redirect; cdxgen's is a 36 KB style guide that assumes
the tool will proceed. **The filename says nothing about whether a repository carries a policy** — a
caution worth holding, because `AGENTS.md` is increasingly where a reader looks first.

One clause inverts a rule three other records share. Under *Review feedback handling*, cdxgen tells
the agent to *"review feedback from automated code review or validation tools"*, to fix valid
comments in the same change, and to *"document why it was not applied"*
otherwise.[^cdxgen-agents] [GTK](gtk.md), [Kubernetes](kubernetes.md) and [Nerves](nerves.md) all
forbid routing review replies through a tool; cdxgen instructs it. The subject is not identical —
theirs is *replying to a human reviewer*, this is *acting on automated review output* — but no
document here draws that line, and a contributor moving between the two conventions would have to
infer it.

A second agent-facing file, `.github/copilot-instructions.md` (4.4 KB), covers similar ground with
**different text**. Two agent-facing documents that can drift, with nothing asserting they agree.

## No floor above it, either

cdxgen left the CycloneDX organisation for its own **`cdxgen`** GitHub org (styled *OWASP cdxgen*,
created 2025-12-09), so the CycloneDX org-level `CONTRIBUTING.md` — which requires DCO sign-off and
is silent on AI — **no longer governs it**. The `cdxgen` org publishes no `.github` defaults.

OWASP sets no foundation-level floor that reaches it. The nearest thing is the **OWASP Developer
Guide**, which does have a rule — *"if it is genuinely helpful to use generative AI then it must be
declared in any pull request or issue, failure to do so can result in the contribution being closed
or even deleted"*, and *"AI slop drains maintainers' time and is actively harmful to **this
project**"*[^owasp-devguide-contributing] — but that text scopes itself to the Developer Guide and
claims no reach over other OWASP projects.

**So OWASP is not a foundation of the kind this bundle records under `foundations/`.** The
[Linux Foundation](../foundations/linux-foundation.md) and its peers publish floors their projects
inherit; OWASP's projects each answer for themselves, and two of them have reached opposite
arrangements — one requiring declaration from contributors, one declaring on its own behalf and
requiring nothing.

## What a contributor must do

**Nothing is asked of you about AI, because nothing is written.** There is no disclosure route, no
trailer, no tag and no stated sanction — and equally no permission to point at. Read `AGENTS.md`
before submitting, because it is where the project's actual expectations live, but read it as a style
guide: it will tell you how to construct a purl and nothing about whether you may have had a model
write it. The declaration at the root describes the **maintainer's** work, not yours, and there is no
documented mechanism for a contributor to extend it to their own.

## Re-verification notes

**Fetch under `cdxgen/cdxgen`, not `CycloneDX/cdxgen`.** The old path still resolves by redirect, and
every URL in this record was re-fetched canonically and confirmed byte-identical. A future move would
break silently the same way.

Four artifacts move independently: the declaration, the spec it cites, `AGENTS.md`, and
`.github/copilot-instructions.md`. `git log -- AI-DECLARATION.md` is the cheapest check and the most
informative — **if the paths in it stop tracking the tree, the declaration has become a badge**, and
that transition is the finding to watch for.

Two gaps are left open rather than closed by inference. **Whether OWASP has any foundation-level AI
policy** was checked at the `OWASP/.github` defaults repository (absent) and against the Developer
Guide's self-scoped rule; `owasp.org` was not exhaustively searched, so this is an absence of found
evidence, not established absence. And **whether the spec is used outside cdxgen** is unestablished —
`ai-declaration.md` advertises a directory of adopters, which was not enumerated here. If the format
has spread, that changes this record from a curiosity to a convention, and it is the single most
consequential thing to re-check.

[^cdxgen-ai-declaration]: [AI-DECLARATION.md (cdxgen/cdxgen, master)](https://raw.githubusercontent.com/cdxgen/cdxgen/master/AI-DECLARATION.md)
[^aideclaration-spec]: [AI-DECLARATION.md — Open Standard for AI Usage Transparency, v0.1.2](https://ai-declaration.md/en/0.1.2)
[^cdxgen-agents]: [AGENTS.md — cdxgen contributor guide for AI agents (cdxgen/cdxgen, master)](https://raw.githubusercontent.com/cdxgen/cdxgen/master/AGENTS.md)
[^cdxgen-readme]: [README.md (cdxgen/cdxgen, master) — the declaration badge and the OWASP production-project statement](https://raw.githubusercontent.com/cdxgen/cdxgen/master/README.md)
[^owasp-devguide-contributing]: [Providing content — OWASP Developer Guide (Use of AI)](https://devguide.owasp.org/contributing/)
