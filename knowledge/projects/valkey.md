---
type: Organization
title: Valkey
description: Has no AI contribution policy and runs an AI reviewer anyway — one briefed to flag missing DCO sign-offs, to detect changes needing TSC consensus, and to escalate any edit to the governance document. Its agent file bars the agent from pushing to the upstream repository at all, a write-scope rule no other record here states, and its TSC holds explicit authority over policy matters it has not exercised on AI.
resource: https://raw.githubusercontent.com/valkey-io/valkey/unstable/.github/copilot-instructions.md
tags:
  - ai-contribution
  - project
  - no-policy
  - review-tooling
  - dco
  - governance
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-10T16:30:00Z'
verified:
  - by: claude/opus-5
    at: '2026-09-10T16:30:00Z'
stale_after: 2027-03-10
sources:
  - id: vk-copilot
    title: 'Valkey Project Instructions (.github/copilot-instructions.md, valkey-io/valkey, unstable)'
    resource: https://raw.githubusercontent.com/valkey-io/valkey/unstable/.github/copilot-instructions.md
  - id: vk-core-instructions
    title: 'Valkey Core Engine Review Standards (.github/instructions/core-engine.instructions.md, unstable)'
    resource: https://raw.githubusercontent.com/valkey-io/valkey/unstable/.github/instructions/core-engine.instructions.md
  - id: vk-agents
    title: 'AGENTS.md (valkey-io/valkey, unstable)'
    resource: https://raw.githubusercontent.com/valkey-io/valkey/unstable/AGENTS.md
  - id: vk-governance
    title: 'GOVERNANCE.md (valkey-io/valkey, unstable)'
    resource: https://raw.githubusercontent.com/valkey-io/valkey/unstable/GOVERNANCE.md
  - id: vk-contributing
    title: 'CONTRIBUTING.md (valkey-io/valkey, unstable)'
    resource: https://raw.githubusercontent.com/valkey-io/valkey/unstable/CONTRIBUTING.md
  - id: vk-site
    title: 'valkey.io — project site and footer'
    resource: https://valkey.io/
  - id: vk-lfprojects
    title: 'Policies — LF Projects, LLC'
    resource: https://lfprojects.org/policies/
  - id: vk-lf-genai
    title: 'Generative AI policy — The Linux Foundation'
    resource: https://www.linuxfoundation.org/legal/generative-ai
---

**Stance: none stated, and the absence is measured rather than assumed.** `AGENTS.md`,
`CONTRIBUTING.md`,[^vk-contributing] `.github/copilot-instructions.md`, `README.md`, `GOVERNANCE.md` and
`DEVELOPMENT_GUIDE.md` were fetched on 2026-09-10 and scanned for *AI*, *LLM*, *generative* and
*artificial intelligence*: **zero occurrences across all six**, against a control run of the same
scan over the Kubernetes contributor guide, which returned 16.

That is the whole of Valkey's position on AI-authored contributions. **What makes the record worth
writing is everything the project does with AI regardless.**

## It has no policy on AI in contribution and briefs an AI to review contributions

`.github/copilot-instructions.md` is not an agent-authoring guide. It opens *"You are an expert code
reviewer for the Valkey project"*[^vk-copilot] and is a brief for a review bot — and three of its
five sections hand that bot work that is not about code:

> **DCO:** **Flag missing** `Signed-off-by: Name <email>` in commits. Every commit needs
> it.[^vk-copilot]

**An AI is checking the certification instrument that several projects here insist only a human can
satisfy.** The [Linux kernel](linux-kernel.md) and [Elixir](elixir.md) both state that *"Only humans
can legally certify the Developer Certificate of Origin"*; Valkey has an agent verify that a human
did. Nothing is inconsistent — checking that a line is present is not certifying anything — but it is
the first instance in this bundle of AI touching the DCO at all, and it lands on the opposite side of
the instrument from every argument in [certifying origin](../mechanisms/certifying-origin.md).

> Flag PRs that appear to be **"Technical Major Decisions" requiring TSC consensus** … **Action:**
> Comment mentioning **@core-team** that this appears to require TSC review and ask if consensus was
> reached in a linked Issue.[^vk-copilot]

> **ANY change to `GOVERNANCE.md`** requires special attention — comment mentioning **@core-team** for
> review.[^vk-copilot]

**The bot is a governance tripwire.** It is told to recognise fundamental datastructure changes, new
APIs, compatibility breaks and new external libraries, and to route them to the committee. Elsewhere
in this bundle AI review is scoped to code quality; here it is pointed at *who has to decide this*.

**Note what it is not told.** The brief never mentions AI-authored contributions, so the reviewer is
briefed to check sign-offs, governance scope and documentation — and not to notice the thing the
project has no rule about.

## The asymmetry runs the other way from every other record

[Kubernetes](kubernetes.md), [systemd](systemd.md), [Dependency-Track](dependency-track.md) and
[LLVM](llvm.md) all **restrict AI in contribution while running it in review**, and each record notes
the tension. **Valkey restricts nothing and runs it in review anyway** — including on its governance
document.

[LLVM](llvm.md) is the useful contrast because it drew the line explicitly: automated review tools
that publish without human review are banned, an opt-in tool that keeps a human in the loop is fine.
Valkey's brief tells the bot to *comment* and *mention @core-team* — publication into the project's
own space — with no stated human gate. Whether one exists in the workflow configuration is not
visible from the instruction file, and is not claimed here.

## A write-scope rule addressed to the agent

`AGENTS.md` is otherwise an ordinary codebase guide — build targets, test layout, a strong style rule
that unit tests be written *"in minimal C++"* with no STL. Its last line is not ordinary:

> **Always push to the user's fork. Never push to the upstream `valkey-io/valkey` repository. Never
> push directly to `unstable`.** If a user fork does not exist, ask the contributor to create
> one.[^vk-agents]

**No other record here bounds where an agent may write.** [Perl](perl.md) and
[Dependency-Track](dependency-track.md) bar an agent from *opening* issues and pull requests;
[Elixir](elixir.md) bars it from unlabelled issues. This assumes the agent has push capability and
constrains the destination — a rule that only makes sense once agents hold credentials, which is a
different threat model from the one every policy in this bundle was written for.

It is also a rule with no consequence attached and no enforcement named. Branch protection would
enforce it; the instruction file is not evidence that any exists.

## Path-scoped review instructions with a stated exclusion

Three files under `.github/instructions/` carry `applyTo` globs — core engine, integration tests,
utils. The core-engine one scopes itself to `src/**/*.{c,h,cpp,hpp}` and `valkey.conf`, and states the
carve-out in prose as well: *"Apply these standards to core engine C code. Do NOT apply to `deps/`
(vendored dependencies)."*[^vk-core-instructions]

**Excluding vendored code from AI review is the same boundary `AGENTS.md` draws for contributors** —
*"Treat vendored dependency code under `deps/` as special-case changes"*.[^vk-agents] The project
applies one rule to humans and machines alike, which is unusual here; most instruction files diverge
from the contributor guidance they sit beside.

## The foundation pointer leads somewhere with no AI policy — the second instance

valkey.io states *"The project is backed by the Linux Foundation"* and its footer reads *"Valkey and
the Valkey logo are trademarks of LF Projects, LLC … For other policies, please see
lfprojects.org."*[^vk-site]

**`lfprojects.org/policies/` was fetched on 2026-09-10 — 128 KB, and zero occurrences of *AI*, *LLM*,
*generative* or *artificial intelligence*.**[^vk-lfprojects] The Linux Foundation's generative-AI
guidance lives at a different domain under a different entity,[^vk-lf-genai] and the pointer does not
reach it.

**This is the second instance of a gap [osquery](osquery.md) documented as one**, and the two differ
in strength: osquery's *charter* binds participants to those policies, while Valkey's *website
footer* points at them. **A binding and a signpost both arrive at a page with nothing on AI**, which
is what makes it a pattern rather than one project's oversight — see
[the Linux Foundation](../foundations/linux-foundation.md) for why inheritance is thinner than it
looks.

## The authority exists and has not been used

`GOVERNANCE.md` gives the Technical Steering Committee oversight of *"all technical, project,
approval, and **policy** matters for Valkey"*[^vk-governance] — a named body with explicit standing to
issue one. It has not.

That is the [OWASP](../foundations/owasp.md) shape: **the machinery is present, mandatory and
unpointed.** Whether that is a decision or an omission is not stated anywhere and is not inferred
here; what is checkable is that the body exists, the authority is written down, and the AI question
has not reached it.

## What a contributor must do

**Nothing is required about AI, because nothing is written.** Sign off every commit — the DCO is
enforced and a bot is briefed to flag its absence. Push to your own fork. Expect an automated
reviewer to comment, and expect it to escalate to `@core-team` if your change looks like a technical
major decision or touches `GOVERNANCE.md`. Follow the vendored-code boundary: `deps/` is a
special case for you and out of scope for the reviewer.

## Re-verification notes

**Check the TSC first.** A policy would arrive through that body, and `GOVERNANCE.md` is where its
existence would show. `git log -- GOVERNANCE.md` dates any change, and the bot is briefed to flag
those, so the project's own tooling surfaces the file that matters.

Then re-run the scan across all six files rather than reading one: this record's finding is an
**absence**, and an absence is only as good as the set of places checked. The
`survey-agent-files.py` helper enumerates the conventions.

Watch three things. Whether the review brief ever gains an AI clause — it is the natural place, since
it is already the file describing what the bot should notice. Whether the write-scope rule in
`AGENTS.md` acquires a sanction or branch protection. And whether `lfprojects.org/policies/` ever
carries an AI policy, which would resolve the inheritance gap for this project and
[osquery](osquery.md) at the same time.

[^vk-copilot]: [Valkey Project Instructions (.github/copilot-instructions.md, valkey-io/valkey, unstable)](https://raw.githubusercontent.com/valkey-io/valkey/unstable/.github/copilot-instructions.md)
[^vk-core-instructions]: [Valkey Core Engine Review Standards (.github/instructions/core-engine.instructions.md, unstable)](https://raw.githubusercontent.com/valkey-io/valkey/unstable/.github/instructions/core-engine.instructions.md)
[^vk-agents]: [AGENTS.md (valkey-io/valkey, unstable)](https://raw.githubusercontent.com/valkey-io/valkey/unstable/AGENTS.md)
[^vk-governance]: [GOVERNANCE.md (valkey-io/valkey, unstable)](https://raw.githubusercontent.com/valkey-io/valkey/unstable/GOVERNANCE.md)
[^vk-contributing]: [CONTRIBUTING.md (valkey-io/valkey, unstable)](https://raw.githubusercontent.com/valkey-io/valkey/unstable/CONTRIBUTING.md)
[^vk-site]: [valkey.io — project site and footer](https://valkey.io/)
[^vk-lfprojects]: [Policies — LF Projects, LLC](https://lfprojects.org/policies/)
[^vk-lf-genai]: [Generative AI policy — The Linux Foundation](https://www.linuxfoundation.org/legal/generative-ai)
