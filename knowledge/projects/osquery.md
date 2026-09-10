---
type: Organization
title: osquery
description: Has no AI policy of its own and inherits the Linux Foundation's, which is guidance rather than a binding rule and is not in the policy list its charter actually binds contributors to. It is the bundle's clearest case of a large, active project where the foundation really is the whole answer — and the only one being extended to inventory AI agents on other people's machines while saying nothing about them in its own.
resource: https://github.com/osquery/foundation/blob/main/CHARTER.md
tags:
  - ai-contribution
  - policy
  - project
  - no-policy
  - cla
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-06T22:23:15Z'
verified:
  - by: claude/opus-5
    at: '2026-09-06T22:23:15Z'
stale_after: 2027-03-07
sources:
  - id: osquery-charter
    title: 'Technical Charter for OSQUERY a Series of LF Projects, LLC (osquery/foundation, CHARTER.md)'
    resource: https://raw.githubusercontent.com/osquery/foundation/main/CHARTER.md
  - id: lfprojects-policies
    title: 'Policies — LF Projects, LLC'
    resource: https://lfprojects.org/policies/
  - id: lf-generative-ai
    title: 'Guidance Regarding Use of Generative AI Tools for Open Source Software Development — The Linux Foundation'
    resource: https://www.linuxfoundation.org/legal/generative-ai
  - id: osquery-contributing
    title: 'Contributing to osquery (CONTRIBUTING.md, osquery/osquery, master)'
    resource: https://raw.githubusercontent.com/osquery/osquery/master/CONTRIBUTING.md
---

**Stance: nothing of its own, and what it inherits is weaker than it looks.** osquery has written no
AI policy, and unlike most silent projects in this bundle it sits under a foundation that has —
which makes it the cleanest test of what inheritance actually delivers.

## The absence is established

Across its **89** markdown files there is not one occurrence of *generative AI*, *LLM*, *GenAI*,
*AI-generated*, *AI-assisted*, *machine-generated*, *Copilot* or *ChatGPT*; the positive control,
*contribut*, matched **14** files, so the sweep was reading them.

**It does carry agent-instruction files, and an earlier version of this record said it did not.** The
first sweep looked for `.cursorrules`, the legacy single-file form, and missed
`.cursor/rules/build-format.mdc` and `.cursorignore`, which are the current directory convention. The
claim was narrowly true and broadly misleading; a re-sweep across every convention
(`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.rules`, `.cursor/`, `.windsurf`, `.clinerules`,
`.aider`, `.junie`, `.github/copilot-instructions.md`) found these two and nothing else.

**Neither carries policy.** `build-format.mdc` is CMake guidance — build in `build/`, set `-j` to the
core count, edit the right `CMakeLists.txt`, check formatting against `.clang-format` — and
`.cursorignore` excludes `libraries/` and `build/` from the agent's view. So the conclusion is
unchanged and its basis is now correct: osquery instructs agents about its **build system** and says
nothing about whether one may write a patch. It is another instance of the finding in
[agent-file pointers](../mechanisms/agent-file-pointers.md) that the filename predicts nothing about
whether a repository carries a policy. The same sweep across the 86 files of the `osquery/foundation` governance repository
returned zero, against a control of **81** files matching *osquery*.

`CONTRIBUTING.md` is 12.7 KB covering blueprints, pull requests, labels, milestones, releases, the
CLA and the Technical Steering Committee.[^osquery-contributing] It says nothing about AI.

## What it inherits, precisely

osquery is *"a Series of LF Projects, LLC"*, adopted 2019-06-14, and its charter binds participants
explicitly:

> Contributors will comply with the policies of LF Projects as may be adopted and amended by LF
> Projects, including, without limitation the policies listed at
> https://lfprojects.org/policies/[^osquery-charter]

**That list contains no AI policy.** It is Antitrust, General Rules of Operation, Privacy, Telemetry
Data Collection and Usage, and Trademark, plus a review policy for hosted project
tools.[^lfprojects-policies] [Valkey](valkey.md) reaches the same page from a website footer rather
than a charter and finds the same nothing, so **this is a pattern rather than one project's
oversight** — a binding and a signpost arriving at the same gap.

The [Linux Foundation](../foundations/linux-foundation.md)'s generative-AI text lives elsewhere, and
reads as guidance rather than obligation — the contributor *"should confirm"* permission for
third-party material and *"should provide notice and attribution"* — closing with:

> **Individual Linux Foundation projects may develop their own project-specific guidance** and
> recommendations regarding AI-generated content.[^lf-generative-ai]

So a contributor asking *"what am I bound to?"* and one asking *"what guidance exists?"* get
different answers. **The binding set has no AI clause; the AI text is advisory and invites the
project to write its own.** osquery has not.

This is worth stating carefully rather than as a gotcha: nothing here suggests the guidance is
*meant* to be optional, and the LF plainly intends it to reach its projects. The observation is only
that the charter's mandatory list and the guidance are different documents on different sites, and a
contributor following the charter literally will not arrive at the AI text.

## Why a silent project earns a record here

The [overview](../overview.md) warns that *"checking only the foundation is a reliable way to be
wrong about the project"*, on the reasoning that the more active a project is, the likelier it has
written its own rule. **osquery is the counter-example that keeps the warning honest**: 23,549 stars, a
funded foundation, a Technical Steering Committee, and steady maintenance — thirty commits across the
two months to 2026-08-25 — with no project-specific rule at all. For this project the foundation is
genuinely the whole answer.

It is also different in kind from the other silences here. Ash — swept and logged rather than
recorded, see [the bundle log](../log.md) — has no foundation above it, so its silence is total.
[MacPorts](macports.md) has an open, contested proposal. osquery has neither an argument in progress
nor a vacuum: it has a baseline it has simply never narrowed.

## The asymmetry worth recording

Two open issues propose osquery tables that inventory AI artifacts on an endpoint: **`ai_agent_skills`**
(#9044, opened 2026-08-07) and **`ai_assistant_chats`** (#9040, opened 2026-08-06).

**So the project is being extended to report which AI agents and skills are installed across a fleet,
while having no position on whether an agent may write its own code.** That is not a contradiction —
detection and contribution policy are different concerns — but it is the only case in this bundle
where a project's *subject matter* is the very artifact class it declines to govern in itself. If
either table ships, osquery becomes a way to answer the skill-distribution question empirically at
fleet scale, which is a supply-chain capability rather than a policy one.

## A mechanism that exists but is unexamined

Pull requests run **EasyCLA**, the Linux Foundation's contributor-licence service, observed passing
on merged PR #9058. [Kubernetes](kubernetes.md) turned exactly this class of check into the only
mechanical AI enforcement in this bundle, by enabling it **for co-authors** so that an AI listed as
one fails the check.

**Whether osquery's EasyCLA is configured that way is not established here** and was not tested. The
check exists; what it covers is unverified, and a reader should not assume the Kubernetes property
transfers.

## What a contributor must do

Nothing specific to AI is asked of you by osquery. **Sign the CLA** — EasyCLA gates pull requests,
and `CONTRIBUTING.md` describes the signoff check.[^osquery-contributing] Beyond that, the applicable
text is the Linux Foundation's guidance: satisfy yourself that any third-party material in a tool's
output may be contributed, and provide notice and attribution where it is.[^lf-generative-ai] There
is no disclosure requirement, no trailer, and no stated sanction.

## Re-verification notes

**Sweep both repositories, and sweep every agent-file convention.** `osquery/osquery` holds the code
and `CONTRIBUTING.md`; `osquery/foundation` holds the charter, the CLAs and the governance record.
⚠ **A probe for `.cursorrules` will report a false absence here** — the file is
`.cursor/rules/build-format.mdc`, and the legacy single-file name does not exist. A policy could appear in
either, and the charter is the only place the binding-policy question is answerable.

**A limit on the negative, stated because it bounds the claim.** The foundation's office-hours minutes
stop at `20220607`, and Discussions are disabled on the main repository. There is therefore no public
forum record in which a 2025 or 2026 decision would have appeared. **The silence is in the written
artifacts and is not evidence that nobody has discussed it.**

Three things would change this record: a project-specific rule, which the LF text explicitly invites;
an AI clause entering the `lfprojects.org` policy list, which would convert guidance into obligation
for every LF project at once; or either AI-inventory table merging, which would make the asymmetry
above concrete.

[^osquery-charter]: [Technical Charter for OSQUERY a Series of LF Projects, LLC (osquery/foundation, CHARTER.md)](https://raw.githubusercontent.com/osquery/foundation/main/CHARTER.md)
[^lfprojects-policies]: [Policies — LF Projects, LLC](https://lfprojects.org/policies/)
[^lf-generative-ai]: [Guidance Regarding Use of Generative AI Tools for Open Source Software Development — The Linux Foundation](https://www.linuxfoundation.org/legal/generative-ai)
[^osquery-contributing]: [Contributing to osquery (CONTRIBUTING.md, osquery/osquery, master)](https://raw.githubusercontent.com/osquery/osquery/master/CONTRIBUTING.md)
