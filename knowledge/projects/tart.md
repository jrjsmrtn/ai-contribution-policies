---
type: Organization
title: Tart
description: Has no AI contribution policy and no agent-instruction file. The repository moved from Cirrus Labs to OpenAI in 2026-06, and the commit that recorded the move edited the contributing guide without adding anything about AI. Since 2026-01, four commits credit an AI model as co-author, three of them Claude and one Codex, under a guide that says nothing either way.
resource: https://raw.githubusercontent.com/openai/tart/main/CONTRIBUTING.md
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
  - id: tart-contributing
    title: 'CONTRIBUTING.md (openai/tart, main)'
    resource: https://raw.githubusercontent.com/openai/tart/main/CONTRIBUTING.md
  - id: tart-readme
    title: 'README.md (openai/tart, main)'
    resource: https://raw.githubusercontent.com/openai/tart/main/README.md
  - id: tart-license
    title: 'LICENSE (openai/tart, main)'
    resource: https://raw.githubusercontent.com/openai/tart/main/LICENSE
  - id: tart-move
    title: 'Update docs after OpenAI move (#1240), openai/tart commit 1ea60ef'
    resource: https://github.com/openai/tart/commit/1ea60ef420
  - id: tart-contributing-history
    title: 'Commit history of CONTRIBUTING.md (openai/tart, main)'
    resource: https://github.com/openai/tart/commits/main/CONTRIBUTING.md
---

**Stance: none stated, and the absence is measured rather than assumed.** Tart's
`CONTRIBUTING.md`[^tart-contributing] and all 26 Markdown files on `main`, including the `docs/` tree
the project site is built from, were read on 2026-10-09. They were searched for the whole words *AI*,
*LLM*, *generative*, *artificial intelligence*, *Copilot*, *Claude*, *Cursor*, *ChatGPT* and *Codex*.
**There were no matches**, while a control search of DuckDB's `CONTRIBUTING.md` found two. A search
for *agent* found only Tart's guest agent, launchd agents and a monitoring product.

The repository has no agent-instruction file in any of the conventions the survey tool checks. It
has no pull request template and no issue templates.

## What the contributing guide does say

There are four short sections: how to build, how to file an issue, a style rule (camel case and
SwiftFormat), and three steps for a pull request. The last of these is *"Wait for pull request to be
reviewed"*.[^tart-contributing] Nothing in the guide concerns who or what wrote the change.

## The move to OpenAI touched the guide and added no rule

`cirruslabs/tart` now redirects to `openai/tart`, and the README[^tart-readme] loads its images from the new location. The licence reads *"Copyright 2022-2026
OpenAI"*,[^tart-license] and the licence is FSL-1.1-ALv2. On 2026-06-06 the commit *"Update docs
after OpenAI move (#1240)"*[^tart-move] changed 27 files. The only change it made to
`CONTRIBUTING.md` was the issues URL, from `cirruslabs/tart` to `openai/tart`. **So the guide was
edited under its new owner, an AI vendor, and no AI rule was added.** The guide has three commits in
its history, and this is the most recent.[^tart-contributing-history]

## Practice: three models credited, from two vendors

A partial clone of `main` on 2026-10-09 contains 75 commits since 2025-10-01. The GitHub API returns
the same 75 for that window. **Four of these commits credit an AI model as co-author:**

| Date | Trailer | Other AI marker in the message |
|---|---|---|
| 2026-01-23 | `Co-authored-by: Claude Opus 4.5 <noreply@anthropic.com>` | none |
| 2026-02-25 | `Co-authored-by: Codex <codex@openai.com>` | a *Generated with Codex* line |
| 2026-07-17 | `Co-authored-by: Claude Fable 5 <noreply@anthropic.com>` | none |
| 2026-09-09 | `Co-authored-by: Claude Opus 5 <noreply@anthropic.com>` | none |

Three people authored them, one of them both the Codex commit and the first Claude commit. The Codex commit came before the move to OpenAI.
Every Claude trailer is a bare `Co-authored-by`: no commit carries `Assisted-by:`, and none mentions
Claude Code. A further commit, on 2026-07-16, has the subject prefix `[codex]` and no trailer. It is
not counted here, because the prefix does not say whether a model wrote the change.

**A trailer is a lower bound.** A trailer records that a contributor chose to add one. The guide asks
for none, so a commit without a trailer tells you nothing about whether a model was used.

## Orchard

[Orchard](orchard.md), Tart's orchestration layer, moved to OpenAI with it. It has no contributing
guide at all.

## What a contributor must do

**Nothing in writing binds you on AI.** Build with the signing script, follow SwiftFormat, and open a
pull request with a detailed description. Contributors have credited both Claude and Codex in
commits, so a trailer is not out of place. None is required.

## Re-verification notes

**Check whether `CONTRIBUTING.md` has changed.** Its history is short enough to read in full. Also
check whether `openai/tart` has gained a pull request template, an `AGENTS.md` or an `AI_POLICY.md`.
OpenAI has no organisation-wide `.github` repository: the API returned 404 on 2026-10-09. If one
appears, its default files apply to Tart. This record does not cover GitHub Discussions.

[^tart-contributing]: [CONTRIBUTING.md (openai/tart, main)](https://raw.githubusercontent.com/openai/tart/main/CONTRIBUTING.md)
[^tart-readme]: [README.md (openai/tart, main)](https://raw.githubusercontent.com/openai/tart/main/README.md)
[^tart-license]: [LICENSE (openai/tart, main)](https://raw.githubusercontent.com/openai/tart/main/LICENSE)
[^tart-move]: [Update docs after OpenAI move (#1240), openai/tart commit 1ea60ef](https://github.com/openai/tart/commit/1ea60ef420)
[^tart-contributing-history]: [Commit history of CONTRIBUTING.md (openai/tart, main)](https://github.com/openai/tart/commits/main/CONTRIBUTING.md)
