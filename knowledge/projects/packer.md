---
type: Organization
title: Packer
description: Has no AI contribution policy. Since 2026-07 it has carried an AGENTS.md that tells an agent how to work in the repository, including that it must not commit or open pull requests unless asked, but says nothing about disclosure, attribution or who is responsible for the result. Three commits since 2026-04 credit an AI tool as co-author, two of them release commits co-authored by Copilot.
resource: https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md
tags:
  - ai-contribution
  - project
  - no-policy
  - agent-file
  - attribution
  - cla
status: stable
generated:
  by: claude/opus-5-5
  at: '2026-10-09T21:40:00Z'
verified:
  - by: claude/opus-5-5
    at: '2026-10-09T21:40:00Z'
stale_after: 2027-04-09
sources:
  - id: pk-contributing
    title: '.github/CONTRIBUTING.md (hashicorp/packer, main)'
    resource: https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md
  - id: pk-agents
    title: 'AGENTS.md (hashicorp/packer, main)'
    resource: https://raw.githubusercontent.com/hashicorp/packer/main/AGENTS.md
  - id: pk-agents-pr
    title: 'chore: added an AGENTS.md (#13668), hashicorp/packer'
    resource: https://github.com/hashicorp/packer/pull/13668
  - id: pk-pr-template
    title: '.github/PULL_REQUEST_TEMPLATE.md (hashicorp/packer, main)'
    resource: https://raw.githubusercontent.com/hashicorp/packer/main/.github/PULL_REQUEST_TEMPLATE.md
  - id: pk-org-defaults
    title: 'hashicorp/.github — organisation default community files'
    resource: https://github.com/hashicorp/.github
  - id: pk-license
    title: 'LICENSE (hashicorp/packer, main)'
    resource: https://raw.githubusercontent.com/hashicorp/packer/main/LICENSE
---

**Stance: none stated, and the absence is measured rather than assumed.** On 2026-10-09 these files
were read: `.github/CONTRIBUTING.md`,[^pk-contributing] the pull request template,[^pk-pr-template] all
five issue templates and their `config.yml`, the README, and the `CODE_OF_CONDUCT.md`, `SECURITY.md`
and README in HashiCorp's organisation-wide `.github` repository.[^pk-org-defaults] They were searched
for the whole words *AI*, *LLM*, *generative*, *artificial intelligence*, *Copilot*, *Claude*,
*Cursor*, *ChatGPT* and *Codex*. **There were no matches**, while a control search of DuckDB's
`CONTRIBUTING.md` found two. The project's documentation site was not searched.

Packer is licensed BUSL-1.1, with IBM named as licensor.[^pk-license] The contributing guide asks for
a CLA, not a sign-off: *"If this is your first contribution to Packer you will be asked to sign the
CLA."*[^pk-contributing] The guide does not say whether the CLA covers code that a model wrote.

## The agent file governs the agent, not the contribution

`AGENTS.md` is a 9,242-byte regular file. It is the only agent-instruction file the survey tool found;
there is no `CLAUDE.md` and no Copilot instructions. It calls itself *"the repo-specific operating
contract"*[^pk-agents] and is written to the agent, not to the person using it. Three of its rules bear on contribution:

- **It limits what the agent may do on its own.** *"Do not commit, branch, push, or open PRs unless
  explicitly requested."*[^pk-agents] It also asks the agent to confirm before it changes the plugin
  SDK boundary, HCL2 template parsing, the command surface, CI and release workflows, or
  security-relevant behaviour.
- **It confines the agent to the repository.** *"Do not read from, write to, or execute files outside
  the workspace"*,[^pk-agents] and the list that follows names `/tmp`, `~` and `/etc`.
- **It requires a handoff report.** The completion checklist ends with *"Final handoff states what
  changed, what was validated"*, plus any remaining risk.[^pk-agents]

**It says nothing about disclosure, trailers, or responsibility.** No line tells the agent, or the
contributor, to state that a model was used, to add or omit a trailer, or that the human submitting
the change answers for it. The handoff report goes to the person running the agent, not to the
reviewer. A contributor who follows the file in full owes the project nothing about AI use.

The file was added in a single pull request on 2026-07-06, by the account that also merged
it. The pull request has no description,[^pk-agents-pr] and it is the only commit to touch the file.
See [governing the instruction file](../mechanisms/instruction-file-governance.md).

## Practice: Copilot on releases, Claude on a feature

A partial clone of `main` on 2026-10-09 contains 124 commits since 2025-10-01. The GitHub API returns
the same 124 commits for that window. A first, shallower clone had only 93, so this count was checked
against the API. **Three commits credit an AI tool as co-author:**

| Date | Commit | Trailer |
|---|---|---|
| 2026-04-24 | *Bump version to 1.15.2 and update changelog for release (#13618)* | `Co-authored-by: Copilot <copilot@github.com>`, three times |
| 2026-04-27 | *version: cut release v1.15.3* | `Co-authored-by: Copilot <copilot@github.com>` |
| 2026-08-10 | *hcl2template: pass user variable values to plugins as packer_user_variables (#13686)* | `Co-authored-by: Claude Fable 5 <noreply@anthropic.com>` |

The two Copilot commits are release preparation, authored by two accounts. One of them is the account
that added `AGENTS.md`. The Claude commit is a behaviour change from a third account, and it came
after `AGENTS.md`. **A trailer is a lower bound:** nothing asks for one, so a
commit without a trailer tells you nothing about whether a model was used.

## What a contributor must do

**Nothing in writing binds you on AI.** Sign the CLA on your first pull request and follow the pull
request template. If you work with an agent, `AGENTS.md` sets rules for the agent: no commits or
pull requests unless you ask, nothing outside the repository, and regenerate generated code rather
than editing it. Commits on `main` have credited Copilot and Claude. No trailer is required.

## Re-verification notes

**Check `AGENTS.md` first.** It is the file most likely to gain a disclosure or attribution rule,
because it already sets rules for commits and pull requests. Then check `CONTRIBUTING.md` and the
pull request template. The documentation at developer.hashicorp.com was not read. Packer plugins live in separate repositories and were not surveyed.

[^pk-contributing]: [.github/CONTRIBUTING.md (hashicorp/packer, main)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/CONTRIBUTING.md)
[^pk-agents]: [AGENTS.md (hashicorp/packer, main)](https://raw.githubusercontent.com/hashicorp/packer/main/AGENTS.md)
[^pk-agents-pr]: [chore: added an AGENTS.md (#13668), hashicorp/packer](https://github.com/hashicorp/packer/pull/13668)
[^pk-pr-template]: [.github/PULL_REQUEST_TEMPLATE.md (hashicorp/packer, main)](https://raw.githubusercontent.com/hashicorp/packer/main/.github/PULL_REQUEST_TEMPLATE.md)
[^pk-org-defaults]: [hashicorp/.github — organisation default community files](https://github.com/hashicorp/.github)
[^pk-license]: [LICENSE (hashicorp/packer, main)](https://raw.githubusercontent.com/hashicorp/packer/main/LICENSE)
