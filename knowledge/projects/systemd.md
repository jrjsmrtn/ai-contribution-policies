---
type: Organization
title: systemd
description: Permits AI-assisted contributions the contributor understands and owns, bars AI from author or co-author credit, and forbids letting AI speak for the contributor, with a warning and then a ban. The policy was rewritten on 2026-10-03 from jj's, keeping systemd's credit ban and dropping jj's disclosure trailer. Its review canary, copied from Zed without a check, has had one since 2026-09-23 that turns an unreviewed pull request into a draft.
resource: https://github.com/systemd/systemd/blob/main/docs/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - attribution
  - lineage
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:18:53Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:18:53Z'
  - by: claude/opus-5-5
    at: '2026-10-31T12:00:00Z'
stale_after: 2027-04-30
sources:
  - id: systemd-contributing
    title: 'docs/CONTRIBUTING.md — Policy on the use of Large Language Models (LLMs) and AI tooling (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/docs/CONTRIBUTING.md
  - id: systemd-contributing-0908
    title: 'docs/CONTRIBUTING.md before the 2026-10-03 rewrite (systemd/systemd, commit 57f0f540)'
    resource: https://raw.githubusercontent.com/systemd/systemd/57f0f540b50248c0fb51eee551084a27383c213a/docs/CONTRIBUTING.md
  - id: systemd-policy-rewrite
    title: 'commit 643b9318 — Extend the AI policy a bit (systemd/systemd, 2026-10-03)'
    resource: https://github.com/systemd/systemd/commit/643b93185cdb
  - id: systemd-violation-templates
    title: 'commit bb9e9571 — CONTRIBUTING: Add template for LLM violation (systemd/systemd, 2026-10-27)'
    resource: https://github.com/systemd/systemd/commit/bb9e9571c3e6
  - id: systemd-jj-policy
    title: 'AI_POLICY.md (jj-vcs/jj, commit 9a00709a) — the text systemd names as its inspiration'
    resource: https://raw.githubusercontent.com/jj-vcs/jj/9a00709a22c47bf1df776dca198986382eb2c2ac/AI_POLICY.md
  - id: systemd-agents-md
    title: 'AGENTS.md (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md
  - id: systemd-canary-commit
    title: 'commit 73aa9523d — Ensure contributors engage with their AI written code (systemd/systemd)'
    resource: https://github.com/systemd/systemd/commit/73aa9523d
  - id: systemd-canary-check
    title: 'commit 69cb8c4a — ci: draft PRs and skip reviews while the README notice is present (systemd/systemd, 2026-09-23)'
    resource: https://github.com/systemd/systemd/commit/69cb8c4a94a4
  - id: systemd-labeler
    title: '.github/workflows/labeler.yml (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/.github/workflows/labeler.yml
  - id: systemd-claude-review
    title: '.github/workflows/claude-review.yml (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/.github/workflows/claude-review.yml
---

**Stance: permitted, provided you understand it, own it and speak for yourself.** The policy section
of `docs/CONTRIBUTING.md` opens: *"You may use generative AI and LLM tools ("AI") to help create
contributions, as long as you review and edit what they produce so it follows the project
guidelines."*[^systemd-contributing] Four numbered rules follow:

1. *"You are the author."* *"Do not list AI tools as author or co-author, or credit them in any way
   that suggests ownership."*[^systemd-contributing]
2. *"You must understand what you contribute."* *"If you cannot explain the code you contributed, your
   contribution will not be merged and any further pull requests will likely not get
   reviewed."*[^systemd-contributing]
3. *"You must speak for yourself."* *"Do not let an AI agent open pull requests or post for you."* AI
   may help draft commit messages and descriptions, if the result is reviewed and edited; the rule
   names the *"AI voice"* to avoid.[^systemd-contributing]
4. *"You are responsible for licensing."*[^systemd-contributing]

The sanction is graded and lands on the person: *"The first time maintainers find that you let AI
communicate for you, or that you posted AI-written text without reviewing it, you get a warning. The
second time, you are banned from the project."*[^systemd-contributing] Since 2026-10-27 the file
carries the two messages maintainers paste for each step, because *"The policy requires a warning
before a ban"*.[^systemd-violation-templates]

## Rewritten on 2026-10-03, from jj

This record was first written on 2026-09-08 against a different policy. That version's premise was
*"AI tools are treated the same as traditional tooling like `sed`, `awk` or
`coccinelle`"*; it required the contributor to have done all the thinking *"prior to using automated
tooling to perform the grunt work"*, and its sanction was *"a loss of trust in that contributor by
project maintainers"*.[^systemd-contributing-0908] None of that wording survives.

The commit that replaced it says *"Inspired by the text from"* jj's `AI_POLICY.md`, and that it
relaxes the language on design and writing: *"It's fine if AI designed it and wrote it, but you as the
author are supposed to fully understand and be able to answer questions about it."*[^systemd-policy-rewrite]
The opening sentence and the first three rule headings follow jj closely. jj opens *"You are welcome to
use generative AI and LLM tools ("AI") to help create contributions as long as you review and edit
what it produces to follow the project guidelines"*, and names the same *"AI voice"*.[^systemd-jj-policy]
`CONTRIBUTING.md` itself does not mention jj; only the commit message does.

**What systemd did not take is jj's one disclosure rule.** jj asks: *"If a substantial part of your
contribution is generated by AI, please disclose this by adding an `Assisted-by` trailer at the end of
the commit message."*[^systemd-jj-policy] systemd kept its own ban on crediting AI in any way. A
copy that inverts the source's attribution rule is a different policy wearing the same headings; see
[policy by copying](../mechanisms/policy-by-copying.md). It also dropped jj's allowance for machine
translation, and added the warning-then-ban sanction and the licensing rule, neither of which jj has.

## The canary now has a check

On 2026-09-03, commit `73aa9523d` added a `HARD RULE` to `AGENTS.md` telling the agent to prepend a
notice to `README.md` on any source change, and never to remove it: *"removing them is strictly a
manual step for the human author to confirm they have reviewed the changes."*[^systemd-agents-md] The
commit message gives the goal: *"Let's add a canary so that we can distinguish AI written code that
was not looked at in any way or form by its author easily in pull requests."*[^systemd-canary-commit]
The instruction is [Zed](zed.md)'s, and when this record was first written nothing in the repository
looked for the marker.

**Since 2026-09-23 something does**, and it is not Zed's design. Commit `69cb8c4a`: *"Until that
happens nobody else should look at the PR: convert it to a draft, don't add the please-review label,
and don't start a Claude review."*[^systemd-canary-check] The labeler reads `README.md` at the head of
the pull request and converts it to a draft if the notice is there:[^systemd-labeler]

> A README.md that still carries the AI review notice has not been looked at by its author yet, so
> nobody else should review it.

The automated review workflow skips the pull request for the same reason.[^systemd-claude-review]
Zed fails the pull request; systemd parks it and withholds review until the author removes the notice
and marks it ready. See [the review canary](../mechanisms/review-canary.md).

## `AGENTS.md` governs its own growth

`AGENTS.md` carries the credit rule for the agent, *"Only human beings can ever be credited within
commit messages."*, and a rule for its own maintenance: *"Only add instructions to this file if you've
seen an AI agent mess up that particular bit of logic in practice."*[^systemd-agents-md] See
[governing the instruction file](../mechanisms/instruction-file-governance.md). It has since gained
Varlink review guidance and an instruction to run `clang-tidy`, and on 2026-09-09 it was licensed
MIT-0. `CLAUDE.md` is a git symlink to it (mode `120000`); see
[agent-file pointers](../mechanisms/agent-file-pointers.md).

## It restricts AI in contribution and runs it in review

`.github/workflows/claude-review.yml` runs an AI review on pull requests from trusted contributors,
or on request.[^systemd-claude-review] As in [Kubernetes](kubernetes.md) and
[Dependency-Track](dependency-track.md), a contributor may get an AI-written review of a change whose
AI authorship they may not credit.

## What a contributor must do

Understand everything you submit and be ready to explain it. Credit no tool: no `Co-Authored-By`, no
`Co-Developed-By`, nothing naming a model. Write your own issues, comments, pull requests and mailing
list posts; if AI helped draft a commit message or description, edit it into the project's style. If
an agent has prepended the notice to `README.md`, remove it yourself and mark the pull request ready:
until you do, it stays a draft and nobody reviews it.

## Re-verification notes

**Read `docs/CONTRIBUTING.md` and `AGENTS.md` together**: the first carries the rules for people, the
second the credit rule and the canary for agents. `git log` on both is short enough to read in full.
Watch whether the credit ban and jj's disclosure trailer stay opposed, and whether the canary check
moves from parking a pull request to failing it.

**Corrections made on 2026-10-31.** This record described the policy as it stood on 2026-09-08, which
the rewrite of 2026-10-03 replaced, and said nothing looked for the canary, which stopped being true
on 2026-09-23. The earlier wording is quoted above from the commit before the rewrite.

[^systemd-contributing]: [docs/CONTRIBUTING.md — Policy on the use of Large Language Models (LLMs) and AI tooling (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/docs/CONTRIBUTING.md)
[^systemd-contributing-0908]: [docs/CONTRIBUTING.md before the 2026-10-03 rewrite (systemd/systemd, commit 57f0f540)](https://raw.githubusercontent.com/systemd/systemd/57f0f540b50248c0fb51eee551084a27383c213a/docs/CONTRIBUTING.md)
[^systemd-policy-rewrite]: [commit 643b9318 — Extend the AI policy a bit (systemd/systemd, 2026-10-03)](https://github.com/systemd/systemd/commit/643b93185cdb)
[^systemd-violation-templates]: [commit bb9e9571 — CONTRIBUTING: Add template for LLM violation (systemd/systemd, 2026-10-27)](https://github.com/systemd/systemd/commit/bb9e9571c3e6)
[^systemd-jj-policy]: [AI_POLICY.md (jj-vcs/jj, commit 9a00709a) — the text systemd names as its inspiration](https://raw.githubusercontent.com/jj-vcs/jj/9a00709a22c47bf1df776dca198986382eb2c2ac/AI_POLICY.md)
[^systemd-agents-md]: [AGENTS.md (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md)
[^systemd-canary-commit]: [commit 73aa9523d — Ensure contributors engage with their AI written code (systemd/systemd)](https://github.com/systemd/systemd/commit/73aa9523d)
[^systemd-canary-check]: [commit 69cb8c4a — ci: draft PRs and skip reviews while the README notice is present (systemd/systemd, 2026-09-23)](https://github.com/systemd/systemd/commit/69cb8c4a94a4)
[^systemd-labeler]: [.github/workflows/labeler.yml (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/.github/workflows/labeler.yml)
[^systemd-claude-review]: [.github/workflows/claude-review.yml (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/.github/workflows/claude-review.yml)
