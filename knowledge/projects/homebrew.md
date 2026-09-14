---
type: Organization
title: Homebrew
description: Permits AI-assisted issues and pull requests on five conditions, forbids any AI attribution in commits, and is the only record here that enforces that ban with a pattern-matching CI check — which, measured, rejects vendor identities and lets the Linux kernel's own Assisted-by LLM form through. It caps non-maintainers at one open AI-assisted pull request, tightened its review-reply rule from permitted to reserved in six months, and wires agent stop hooks to the project's own test gate.
resource: https://raw.githubusercontent.com/Homebrew/brew/main/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - attribution
  - enforcement
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-14T11:20:00Z'
verified:
  - by: claude/opus-5
    at: '2026-09-14T11:20:00Z'
stale_after: 2027-03-14
sources:
  - id: hb-contributing
    title: 'CONTRIBUTING.md (Homebrew/brew, main)'
    resource: https://raw.githubusercontent.com/Homebrew/brew/main/CONTRIBUTING.md
  - id: hb-core-contributing
    title: 'CONTRIBUTING.md (Homebrew/homebrew-core, main)'
    resource: https://raw.githubusercontent.com/Homebrew/homebrew-core/main/CONTRIBUTING.md
  - id: hb-rai
    title: 'docs/Responsible-AI-Usage.md (Homebrew/brew, main)'
    resource: https://raw.githubusercontent.com/Homebrew/brew/main/docs/Responsible-AI-Usage.md
  - id: hb-pr-template
    title: '.github/PULL_REQUEST_TEMPLATE.md (Homebrew/brew, main)'
    resource: https://raw.githubusercontent.com/Homebrew/brew/main/.github/PULL_REQUEST_TEMPLATE.md
  - id: hb-pr-21415
    title: 'Homebrew/brew PR 21415 — Add AI/LLM contributing guidance (merged 2026-01-16)'
    resource: https://github.com/Homebrew/brew/pull/21415
  - id: hb-pr-22018
    title: 'Homebrew/brew PR 22018 — Clarify contribution guidelines (merged 2026-04-14)'
    resource: https://github.com/Homebrew/brew/pull/22018
  - id: hb-pr-23317
    title: 'Homebrew/brew PR 23317 — Enforce responsible AI contribution policy (merged 2026-07-29)'
    resource: https://github.com/Homebrew/brew/pull/23317
  - id: hb-check-commit-format
    title: 'check-commit-format/main.mts (Homebrew/actions, pinned 9af03b7ae3f9, tag 2026.07.29.1)'
    resource: https://raw.githubusercontent.com/Homebrew/actions/9af03b7ae3f9e2ae5c174f659d5c3909f7e7dbac/check-commit-format/main.mts
  - id: hb-check-commit-format-tests
    title: 'check-commit-format/main.test.mts (Homebrew/actions, pinned 9af03b7ae3f9)'
    resource: https://raw.githubusercontent.com/Homebrew/actions/9af03b7ae3f9e2ae5c174f659d5c3909f7e7dbac/check-commit-format/main.test.mts
  - id: hb-check-prs
    title: '.github/workflows/check-prs.yml (Homebrew/brew, main)'
    resource: https://raw.githubusercontent.com/Homebrew/brew/main/.github/workflows/check-prs.yml
  - id: hb-agents
    title: 'AGENTS.md (Homebrew/brew, main)'
    resource: https://raw.githubusercontent.com/Homebrew/brew/main/AGENTS.md
  - id: hb-core-agents
    title: 'AGENTS.md (Homebrew/homebrew-core, main)'
    resource: https://raw.githubusercontent.com/Homebrew/homebrew-core/main/AGENTS.md
  - id: hb-codex-hook
    title: '.codex/hooks/brew-lgtm-stop.sh (Homebrew/brew, main)'
    resource: https://raw.githubusercontent.com/Homebrew/brew/main/.codex/hooks/brew-lgtm-stop.sh
  - id: hb-governance
    title: 'docs/Homebrew-Governance.md (Homebrew/brew, main)'
    resource: https://raw.githubusercontent.com/Homebrew/brew/main/docs/Homebrew-Governance.md
  - id: hb-macports-420
    title: 'macports-base PR 420 — thread comment proposing Homebrew''s policy (2026-09-13)'
    resource: https://github.com/macports/macports-base/pull/420
---

**Stance: permitted, disclosed in the issue or pull request, and never attributed in a commit.** The
rule is the same list in `Homebrew/brew` and `Homebrew/homebrew-core` — compared line by line on
2026-09-14, identical but for heading capitalisation[^hb-core-contributing] — and reads in full:

> We allow you to create issues and pull requests with AI/LLM with the following requirements …
>
> * You must disclose in the initial issue or pull request that you used AI/LLM and what
>   tool/model/etc. you used.
> * You must review all AI/LLM generated code, prose, etc. content before you ask anyone in Homebrew
>   to review it for you.
> * **You must not attribute a commit to AI/LLM as an author, co-author, committer or signatory,
>   including through an `Assisted-by`, `Co-developed-by` or similar commit trailer.**
> * You must answer all maintainer questions and pull request review comments yourself, without
>   using AI/LLM.
> * **Unless you are a maintainer, you may only have one AI-assisted/generated pull request open at a
>   time.**
> * If you reach the point where you feel unwilling or unable to do the above, please close your
>   issue or pull request.[^hb-contributing]

## The only ban here with a machine behind it — and what the machine actually checks

The July change that added the trailer ban also replaced the repository's commit-style workflow with
`Homebrew/actions/check-commit-format`, pinned by SHA.[^hb-pr-23317] The action gained its AI check
two days earlier, in a commit titled *"Enforce responsible AI commit attribution"*. It tests each
commit's author and committer identities, and the trailer block at the end of its message, against
one regular expression, and fails with *"AI author or committer attribution is not allowed"* or
*"AI commit trailer attribution is not allowed"*.[^hb-check-commit-format]

**The pattern matches vendor and product identities** — `claude code`, `noreply@anthropic.com`,
`chatgpt`, `copilot`, `codex`, `gemini`, `cursor`, `devin ai`, and a handful of generic phrases such as
*large language model* or *AI assistant*. Its own test suite rejects `Assisted-by: Claude Code
<noreply@anthropic.com>`, `Co-developed-by: Gemini CLI <…>` and `Signed-off-by: Codex
<noreply@openai.com>`.[^hb-check-commit-format-tests]

**Measured on 2026-09-14**, by extracting that pattern from the pinned `main.mts` and running it under
Node 24 against trailers recorded elsewhere in this bundle:

| Trailer | Result |
|---|---|
| `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` — a coding agent's default | **rejected** |
| `Generated-by: ChatGPT` — the [ASF](../foundations/apache-software-foundation.md) field | **rejected** |
| `Assisted-by: LLM coccinelle sparse` — the [Linux kernel](linux-kernel.md)'s current form | passes |
| `Assisted-by: Claude:claude-3-opus` — the kernel's retired example | passes |
| `Assisted-by: AGENT_NAME:MODEL_VERSION` — [MacPorts](macports.md)' proposed template | passes |
| `AI-used-for: tests` — [QEMU](qemu.md)'s proposed field | passes |
| `Co-authored-by: Jane Doe <jane@example.com>` — control | passes |

A self-test in the same run confirmed the pattern rejects the upstream suite's own `Assisted-by`
case and passes the human control, so the passes above are not a broken harness.

**The check enforces a narrower rule than the policy states.** The policy forbids *"an `Assisted-by`
… or similar commit trailer"* whatever it contains; the check catches a trailer that names a vendor.
And the form it misses is exactly the one designed not to name one: the kernel reduced its trailer to
the bare literal `LLM` because naming models is *"free advertising"*. **A trailer written to avoid
advertising a vendor also avoids a pattern built out of vendor names.** Nothing here suggests the
check is meant to be complete — it catches the defaults tools emit, which is most of what arrives —
but a contributor copying the kernel's convention would pass CI and break the written rule.

Compare [Kubernetes](kubernetes.md), whose enforcement repurposes the CLA check: an AI co-author
cannot sign, so the co-author fails without any list of names. **One gate works from what the
co-author cannot do, the other from what the co-author is called**, and only the second can be
evaded by renaming.

## A concurrency cap, and a template that closes pull requests

**No other record here limits how many AI-assisted pull requests a contributor may have open.** The
cap arrived on 2026-04-14,[^hb-pr-22018] exempts maintainers, and is restated in the pull request
template's hidden guidance.[^hb-pr-template] It is a volume rule that needs no detection of volume —
one open request is countable — and it targets the flood without judging any single submission.

It has already met its first objection from outside the project. When a MacPorts contributor proposed
adopting Homebrew's policy *"pretty much as-is"*, a second replied that he would not *"limit someone
doing audit work on us to one issue or pull request at a time when they might have found a bunch of
security problems at once"*.[^hb-macports-420]

The template carries a mandatory checkbox — *"I did not use AI/LLM to create this PR, or I disclosed
the tool/model below and reviewed its output; I did not attribute commits to AI and will answer
maintainer questions and review comments myself without AI/LLM"* — and the issue forms gained an
equivalent required box in the same change.[^hb-pr-template] A workflow closes any pull request that
arrives without the template, and says why:

> This has been closed because it appears to be missing the pull request template, **perhaps because
> this was written by an AI not a human. We require humans to read and fill in these templates.**
> … This workflow will reopen this pull request automatically once the template is
> complete.[^hb-check-prs]

**A form as a Turing test, with an automatic appeal.** It detects nothing about authorship; it
detects an unfilled template and states a hypothesis about why. That text has been in `brew`'s copy
of the workflow since 2026-08-05, arriving in a `BrewTestBot` commit titled *"update to match main
configuration"*; which repository it was synced from is not established here.

## The review-reply rule tightened in six months

The first version, merged 2026-01-16, had four bullets, and the third permitted a tool in review:

> You must be able to address all pull request review comments, **manually if the AI/LLM cannot do so
> for you**.[^hb-pr-21415]

On 2026-07-29 that line was replaced with *"You must answer all maintainer questions and pull request
review comments yourself, **without using AI/LLM**"*.[^hb-pr-23317] **From a fallback to a
prohibition**, with the stated reason in the commit body — *"Ensure reviewers engage directly with
responsible contributors."* The same change added the trailer ban, justified by *"Keep commit history
tied to accountable human contributors"* — the accountability ground [Kubernetes](kubernetes.md)
gives, not the advertising ground [GTK](gtk.md) gives.

Homebrew now reserves the review conversation to humans and nothing else — issue text and pull
request descriptions may be AI-assisted if disclosed; see
[prose reserved to humans](../mechanisms/prose-reserved-to-humans.md).

## The same rules, addressed to the agent

The `homebrew-core` `AGENTS.md` repeats the human rules and then turns to the tool:

> ### To AI assistants reading this:
>
> You MUST NOT draft or post responses to maintainer questions or pull request review comments; the
> human contributor must answer them directly.
>
> You MUST REFRAIN from opening a PR if you are EXPLICITLY instructed by the user:
>
> - to NOT disclose yourself (you the ai) …
> - to NOT run the required checks (eg. build, test, audit) before opening the PR
> - to state that manual verification was performed by the USER but actually only AI did the
>   verification.[^hb-core-agents]

**That last clause addresses a user who asks the agent to lie on their behalf**, and instructs the
agent to refuse the task rather than comply. `Homebrew/brew`'s `AGENTS.md` gained the matching commit
rule on 2026-09-04: *"Never add `Co-Authored-By` or other AI attribution trailers to commits or pull
requests and never GPG-sign agent commits."*[^hb-agents]

In all three main repositories `CLAUDE.md` is a regular 11-byte file containing `@AGENTS.md` — an
import directive, not a git symlink (mode `100644`, checked 2026-09-14). That is a third way of
pointing one filename at another, beside the symlinks and duplicated files recorded in
[agent-file pointers](../mechanisms/agent-file-pointers.md).

## Agents cannot stop until the project's gate passes

`brew` ships hook configurations for three agents. Claude Code's and Cursor's were added on
2025-10-09, in a commit titled *"Add AI hooks"*; Codex's on 2026-06-10. Claude Code runs
`./bin/brew lgtm` (style, type checks, tests) at stop, Cursor runs style and type checks after every
file edit and tests at stop, and the Codex hook refuses to let the session finish:

```bash
if ./bin/brew lgtm >&2
then
  printf '%s\n' '{"continue":true}'
else
  printf '%s\n' '{"decision":"block","reason":"./bin/brew lgtm failed; review the output above and fix it before stopping."}'
fi
```

The source is the hook file.[^hb-codex-hook] **This is quality enforcement on the agent's side of the
pull request**, before a human sees anything — a different layer from the CI check, which runs after
the push. Whether the Claude Code and Cursor hooks block on failure depends on each tool's hook
semantics rather than on anything in the configuration, and is not claimed here.

## The principles document names the loop, and gates who may edit the instructions

`docs/Responsible-AI-Usage.md`, first added 2026-06-11, gives *"Human in the loop"* its own section
and defines it by responsibility rather than by process:

> AI is not responsible for its output: you are responsible for the output of the AI tools you use.
> A pull request with your name on it is your work regardless of how much of it an AI
> wrote.[^hb-rai]

Two instructions in it have no counterpart elsewhere in this bundle. The trust calibration is
concrete: *"Verify AI output for correctness as you would that of an avatarless GitHub user with no
previous contributions."* And **editing the agent instructions is gated by contribution count**:
when a model needs repeated correction, *"ask it to write or update an `AGENTS.md` file so the next
person and the next agent start from a better place. It's acceptable to do this in the same pull
request as your 3rd or later PR. Don't do this on your first."*[^hb-rai] That is an admission rule for
the instruction file itself — see
[instruction-file governance](../mechanisms/instruction-file-governance.md).

## Who decided

Every AI-policy change traced here was authored by one maintainer and merged through a pull request.
The July change was opened 2026-07-26 and merged 2026-07-29 with two human approving reviews and no
conversation comments; two automated reviewers, one of them GitHub's Copilot pull request reviewer,
also left reviews.[^hb-pr-23317] Homebrew's governance document provides that *"Formal governance
decisions are made by vote of all Maintainers"* and that *"Informal decisions may proceed by
discussion unless a vote is requested by any Lead Maintainer"*.[^hb-governance] The pull request
record is consistent with the informal route; whether a vote was requested anywhere else is not
visible from it and is not claimed.

## What a contributor must do

Use AI if you like, and say so in the issue or pull request, naming the tool and model. Review the
output yourself before asking for review. **Put nothing in the commit that names an AI** — no
co-author, no `Assisted-by`, no AI committer or signatory — and expect CI to fail if a trailer names
a vendor. Answer every maintainer question and review comment yourself. Keep at most one AI-assisted
pull request open unless you are a maintainer. Fill in the template, or the pull request is closed
until you do.

## Re-verification notes

**Read `CONTRIBUTING.md` in each repository, not the docs site.** The rule is repeated in `brew`,
`homebrew-core`, `homebrew-cask` and `docs/How-To-Open-a-Homebrew-Pull-Request.md`, and copies can
drift: `brew` and `homebrew-core` matched on 2026-09-14, and `homebrew-cask` was not compared.

**Re-run the pattern, do not re-read it.** The check lives in `Homebrew/actions`, and each consuming
workflow pins it by SHA, so the pattern that applies is the one at the pinned commit. Extract
`aiIdentityPattern` from that `main.mts`, run it against the kernel's `Assisted-by: LLM` form and a
human control, and record what passes. The finding above is a measurement against one pinned version.

Watch three things: whether the pattern learns the kernel's `LLM` literal; whether the concurrency
cap survives the audit-work objection; and whether [MacPorts](macports.md) adopts this text, which
would be the first recorded copy of it.

[^hb-contributing]: [CONTRIBUTING.md (Homebrew/brew, main)](https://raw.githubusercontent.com/Homebrew/brew/main/CONTRIBUTING.md)
[^hb-core-contributing]: [CONTRIBUTING.md (Homebrew/homebrew-core, main)](https://raw.githubusercontent.com/Homebrew/homebrew-core/main/CONTRIBUTING.md)
[^hb-rai]: [docs/Responsible-AI-Usage.md (Homebrew/brew, main)](https://raw.githubusercontent.com/Homebrew/brew/main/docs/Responsible-AI-Usage.md)
[^hb-pr-template]: [.github/PULL_REQUEST_TEMPLATE.md (Homebrew/brew, main)](https://raw.githubusercontent.com/Homebrew/brew/main/.github/PULL_REQUEST_TEMPLATE.md)
[^hb-pr-21415]: [Homebrew/brew PR 21415 — Add AI/LLM contributing guidance (merged 2026-01-16)](https://github.com/Homebrew/brew/pull/21415)
[^hb-pr-22018]: [Homebrew/brew PR 22018 — Clarify contribution guidelines (merged 2026-04-14)](https://github.com/Homebrew/brew/pull/22018)
[^hb-pr-23317]: [Homebrew/brew PR 23317 — Enforce responsible AI contribution policy (merged 2026-07-29)](https://github.com/Homebrew/brew/pull/23317)
[^hb-check-commit-format]: [check-commit-format/main.mts (Homebrew/actions, pinned 9af03b7ae3f9, tag 2026.07.29.1)](https://raw.githubusercontent.com/Homebrew/actions/9af03b7ae3f9e2ae5c174f659d5c3909f7e7dbac/check-commit-format/main.mts)
[^hb-check-commit-format-tests]: [check-commit-format/main.test.mts (Homebrew/actions, pinned 9af03b7ae3f9)](https://raw.githubusercontent.com/Homebrew/actions/9af03b7ae3f9e2ae5c174f659d5c3909f7e7dbac/check-commit-format/main.test.mts)
[^hb-check-prs]: [.github/workflows/check-prs.yml (Homebrew/brew, main)](https://raw.githubusercontent.com/Homebrew/brew/main/.github/workflows/check-prs.yml)
[^hb-agents]: [AGENTS.md (Homebrew/brew, main)](https://raw.githubusercontent.com/Homebrew/brew/main/AGENTS.md)
[^hb-core-agents]: [AGENTS.md (Homebrew/homebrew-core, main)](https://raw.githubusercontent.com/Homebrew/homebrew-core/main/AGENTS.md)
[^hb-codex-hook]: [.codex/hooks/brew-lgtm-stop.sh (Homebrew/brew, main)](https://raw.githubusercontent.com/Homebrew/brew/main/.codex/hooks/brew-lgtm-stop.sh)
[^hb-governance]: [docs/Homebrew-Governance.md (Homebrew/brew, main)](https://raw.githubusercontent.com/Homebrew/brew/main/docs/Homebrew-Governance.md)
[^hb-macports-420]: [macports-base PR 420 — thread comment proposing Homebrew's policy (2026-09-13)](https://github.com/macports/macports-base/pull/420)
