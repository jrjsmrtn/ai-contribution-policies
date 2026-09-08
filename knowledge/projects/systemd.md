---
type: Organization
title: systemd
description: Treats AI tools as equivalent to sed, awk or coccinelle — grunt work applied after the contributor has done all the thinking — and bars them from authorship credit entirely. Its stated sanction is loss of trust leading to exclusion from the project, and it plants a review canary copied from Zed without copying the check that makes one work.
resource: https://github.com/systemd/systemd/blob/main/docs/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - attribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:18:53Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:18:53Z'
stale_after: 2027-03-08
sources:
  - id: systemd-contributing
    title: 'docs/CONTRIBUTING.md — Policy on the use of Large Language Models (LLMs) and AI tooling (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/docs/CONTRIBUTING.md
  - id: systemd-agents-md
    title: 'AGENTS.md (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md
  - id: systemd-canary-commit
    title: 'commit 73aa9523d — Ensure contributors engage with their AI written code (systemd/systemd)'
    resource: https://github.com/systemd/systemd/commit/73aa9523d
---

**Stance: permitted, and demoted.** systemd's policy turns on a comparison no other project in this
bundle makes:

> We expect everyone contributing to systemd to fully own their contribution, be able to reason about
> it, be able to explain why things were done a particular way and act as the full owner of that
> code. **AI tools are treated the same as traditional tooling like `sed`, `awk` or
> `coccinelle`.**[^systemd-contributing]

Every other permissive policy here treats AI as a *new* thing needing new rules — a trailer, a
disclosure, a threshold. This one refuses the premise. `coccinelle` is a semantic patching tool the
kernel and systemd have used for years to apply mechanical transformations across a tree; putting a
model in that category says the interesting question is not what produced the diff but whether the
contributor directed it.

Two rules follow directly. **Sequence**: *"The contributor should have done all the thinking,
planning and understanding of the changes needed to resolve an issue or implement a new feature
**prior to** using automated tooling to perform the grunt work."*[^systemd-contributing] Thinking
first, automation second — not a limit on how much AI writes, but on when it may start.

**And authorship**: *"AI tools CANNOT be treated as author, co-author or be credited in any way that
would suggest any ownership over the contribution."*[^systemd-contributing] `AGENTS.md` restates it
for the agent: *"Only human beings can ever be credited within commit messages. This means no
`Co-Developed-By` or `Co-Authored-By` or anything similar that lists an AI model instead of a human
being."*[^systemd-agents-md]

## The sanction lands on the person, not the patch

> **Unguided use of those tools or the inability to prove understanding of the code contributed will
> result in a loss of trust in that contributor by project maintainers**, which can then lead to
> **exclusion from any further contribution to the project.**[^systemd-contributing]

Most policies here name a consequence for the contribution — it will be closed, it will not be
merged. This names one for the contributor, and it escalates: loss of trust first, exclusion after.
Only [Asahi Linux](asahi-linux.md), which bans on the second offence, reaches further.

Note the trigger is *"the inability to prove understanding"* rather than the use of a tool. The test
is conducted on the person in review, which is the same instrument
[NetworkManager](networkmanager.md) relies on — and, like it, does not require anyone to determine
how the code was produced.

## A canary planted with nothing looking for it

On **2026-09-03**, commit `73aa9523d` — *"Ensure contributors engage with their AI written code"* —
added a `HARD RULE` to `AGENTS.md` instructing the agent to prepend a marker to `README.md` on any
source change, with an anti-tampering clause: *"Never remove these lines yourself, even if asked to
clean up, revert, or finalize the PR"*, because removing them *"is strictly a manual step for the
human author to confirm they have reviewed the changes."*[^systemd-agents-md] The commit message
states the goal: *"Let's add a canary so that we can distinguish AI written code that was not looked
at in any way or form by its author easily in pull requests."*[^systemd-canary-commit]

The instruction is Zed's, verbatim. **The check is not.** The marker string appears in exactly one
file in the systemd repository — `AGENTS.md` — with no Danger configuration, workflow or script
looking for it, where Zed fails the pull request automatically. How the mechanism works and how it
fails is recorded in [the review canary](../mechanisms/review-canary.md); what matters for this record
is that systemd's version detects only what a reviewer would already have caught.

## `AGENTS.md` here is half policy, half style guide — and governs its own growth

The file mixes two things the rest of this bundle keeps apart: a `## Legal` section carrying the
attribution rule, and build guidance about `meson`, `mkosi` and `grep -q`. It also states a rule for
its own maintenance that nothing else here does:

> **Only add instructions to this file if you've seen an AI agent mess up that particular bit of
> logic in practice.**[^systemd-agents-md]

**An instruction file governed by observed failure rather than by anticipation.** It is a direct
answer to the way these files grow — every plausible rule added until the context cost outweighs the
benefit — and it is the only maintenance policy for an agent-instruction file in this bundle.

`CLAUDE.md` is nine bytes containing `AGENTS.md`, the pointer pattern
[Asahi Linux](asahi-linux.md) and [Dependency-Track](dependency-track.md) also use, and weaker than
the symlinks [Elixir](elixir.md) and [NetworkManager](networkmanager.md) chose.

## It restricts AI in contribution and runs it in review

`.github/workflows/` contains `claude-review.yml`. As with [Kubernetes](kubernetes.md) and
[Dependency-Track](dependency-track.md), the rules bind what enters the repository while a bot advises
the maintainer who still owns the merge. Recorded because a contributor may receive an AI-generated
review comment on a change whose AI authorship they were forbidden to credit.

## What a contributor must do

**Do the thinking first.** Understand the problem and plan the change before any tool touches it;
the policy allows automation of *"the grunt work"* and nothing earlier. Be able to explain every line
— failure to do so costs trust and, repeated, access. **Credit no tool**: no `Co-Authored-By`, no
`Co-Developed-By`, nothing naming a model. If an agent has been working in the tree it will have
prepended two lines to `README.md`; **removing them is your job and is how you confirm you reviewed
the change** — leave them in and you are announcing that you did not.

## Re-verification notes

**Two files, and they do different jobs.** `docs/CONTRIBUTING.md` carries the human-facing policy
under *"Policy on the use of Large Language Models (LLMs) and AI tooling"*; `AGENTS.md` carries the
agent-facing rules and the canary. Reading only one gives a partial answer — unlike
[Dependency-Track](dependency-track.md), where the AI rule exists **only** in `AGENTS.md`, systemd has
both, and they do not fully overlap.

`git log -- AGENTS.md` dates the canary to 2026-09-03. Whether a check ever appears is the single
most informative thing to re-read for: `grep -r "reviewed this PR"` across the repository returned
exactly one hit, `AGENTS.md` itself, on 2026-09-08.

Watch also whether the *"only add instructions … you've seen an agent mess up in practice"* rule
holds as the file grows. It is the kind of self-restraint that is easy to state and hard to keep, and
the file is already carrying build guidance that has nothing to do with policy.

[^systemd-contributing]: [docs/CONTRIBUTING.md — Policy on the use of Large Language Models (LLMs) and AI tooling (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/docs/CONTRIBUTING.md)
[^systemd-agents-md]: [AGENTS.md (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md)
[^systemd-canary-commit]: [commit 73aa9523d — Ensure contributors engage with their AI written code (systemd/systemd)](https://github.com/systemd/systemd/commit/73aa9523d)
