---
type: Organization
title: Orchard
description: Has no contributing guide, so it has no AI contribution policy either. The repository moved to OpenAI with Tart, and its README still points to the Cirrus Labs location. Two commits from 2026-01 and 2026-02 credit Codex as co-author, both by one of the repository's two code owners.
resource: https://github.com/openai/orchard
tags:
  - ai-contribution
  - project
  - no-policy
  - attribution
status: stable
generated:
  by: claude/opus-5-5
  at: '2026-10-09T21:40:00Z'
verified:
  - by: claude/opus-5-5
    at: '2026-10-09T21:40:00Z'
stale_after: 2027-04-09
sources:
  - id: orch-readme
    title: 'README.md (openai/orchard, main)'
    resource: https://raw.githubusercontent.com/openai/orchard/main/README.md
  - id: orch-development
    title: 'DEVELOPMENT.md (openai/orchard, main)'
    resource: https://raw.githubusercontent.com/openai/orchard/main/DEVELOPMENT.md
  - id: orch-codeowners
    title: 'CODEOWNERS (openai/orchard, main)'
    resource: https://raw.githubusercontent.com/openai/orchard/main/.github/CODEOWNERS
  - id: orch-license
    title: 'LICENSE (openai/orchard, main)'
    resource: https://raw.githubusercontent.com/openai/orchard/main/LICENSE
---

**Stance: none stated, and there is no contributing guide where one could be stated.** Orchard
orchestrates [Tart](tart.md) virtual machines across a cluster. On 2026-10-09 its repository
contained two Markdown files, `README.md`[^orch-readme] and `DEVELOPMENT.md`.[^orch-development]
Neither contains *AI*, *LLM*, *generative*, *artificial intelligence*, *Copilot*, *Claude*, *Cursor*,
*ChatGPT* or *Codex* as a whole word. A control search of DuckDB's `CONTRIBUTING.md` found two
matches. The repository has no pull request template, no issue templates and no agent-instruction
file in any of the conventions the survey tool checks.

`DEVELOPMENT.md` is a single paragraph about regenerating protobuf code. Orchard's user
documentation lives in Tart's repository, under `docs/orchard/`, and the Tart record covers that
search too.

## Ownership

The licence reads *"Copyright 2023-2026 OpenAI"*[^orch-license] and the licence is FSL-1.1-ALv2,
the same as Tart's. **The README was not updated for the move.** It still loads its image from
`cirruslabs/orchard` and sends questions to `cirruslabs/orchard` issues.[^orch-readme] GitHub
redirects both to the new location. `CODEOWNERS` names two maintainers for every
path.[^orch-codeowners]

## Practice: Codex, before the move

A partial clone of `main` on 2026-10-09 contains 99 commits since 2025-10-01. The GitHub API returns
the same 99 for that window, and 24 of them are Dependabot's. **Two commits credit Codex as
co-author:**

- 2026-01-22, *Add pagination support for listing VM events (#386)*: a `Co-authored-by: Codex
  <codex@openai.com>` trailer, a second human co-author, and a *Generated with Codex* line.
- 2026-02-05, *Refactor listing VMs (#399)*: the same trailer and the same line.

**Both were authored by one of the two code owners**, and both came before the move to OpenAI. No
commit in the window names any other AI tool. **A trailer is a lower bound:** nothing asks for one,
so a commit without a trailer tells you nothing about whether a model was used.

## What a contributor must do

**Nothing in writing binds you on AI, or on anything else.** There is no contributing guide. Follow
`DEVELOPMENT.md` if you change a `.proto` file. A maintainer has credited Codex in commits, so a
trailer is not out of place. None is required.

## Re-verification notes

**Check whether a `CONTRIBUTING.md` has appeared**, and whether the README now points to `openai/`.
Updating the README would be the first edit that shows the move. OpenAI had no organisation-wide
`.github` repository on 2026-10-09; if one appears, its default files apply here.

[^orch-readme]: [README.md (openai/orchard, main)](https://raw.githubusercontent.com/openai/orchard/main/README.md)
[^orch-development]: [DEVELOPMENT.md (openai/orchard, main)](https://raw.githubusercontent.com/openai/orchard/main/DEVELOPMENT.md)
[^orch-codeowners]: [CODEOWNERS (openai/orchard, main)](https://raw.githubusercontent.com/openai/orchard/main/.github/CODEOWNERS)
[^orch-license]: [LICENSE (openai/orchard, main)](https://raw.githubusercontent.com/openai/orchard/main/LICENSE)
