---
type: Organization
title: MacPorts
description: Has no adopted AI policy. An open, contested pull request would require an Assisted-by trailer "in the format recommended by the Linux kernel developers" — in the form the kernel retired the day before it was written. The rendered kernel page it cites has since caught up and now contradicts it, nobody in the thread has noticed, and a participant has proposed replacing the whole section with Homebrew's policy, which forbids the trailer.
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
  - by: claude/opus-5
    at: '2026-09-14T11:20:00Z'
stale_after: 2026-12-14
sources:
  - id: macports-pr-420
    title: 'macports-base PR #420 — Add CONTRIBUTING.md (open, jmroot)'
    resource: https://github.com/macports/macports-base/pull/420
  - id: macports-pr-420-diff
    title: 'macports-base PR #420 — proposed CONTRIBUTING.md, diff'
    resource: https://patch-diff.githubusercontent.com/raw/macports/macports-base/pull/420.diff
  - id: macports-kernel-rendered
    title: 'AI Coding Assistants — The Linux Kernel documentation (rendered; 7.3.0-rc3 on 2026-09-14)'
    resource: https://docs.kernel.org/process/coding-assistants.html
---

**Stance: undecided. This record describes a proposal, not a rule.** MacPorts has no adopted AI
policy. Pull request **#420**, *"Add CONTRIBUTING.md"*, was opened by Joshua Root on **2026-08-04**
and was **still open and unmerged** when re-checked on 2026-09-14.[^macports-pr-420] It is recorded
here because of what it demonstrates, not because it binds anyone.

> ⚠ **Nothing below is in force.** If you are contributing to MacPorts today, no written AI rule
> applies. Re-read the PR before relying on any of this.

Neither `macports-base` nor `macports-ports` carries any of the agent-instruction files this bundle
surveys for (`survey-agent-files.py`, 2026-09-14).

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

**The proposed text has not changed since this record was first written.** The PR carries one commit,
authored 2026-08-04 and last committed 2026-08-17; a force-push on 2026-09-02 left the head at the
same commit, and the diff fetched on 2026-09-14 still specifies `AGENT_NAME:MODEL_VERSION`. What the
commit said before its 2026-08-17 amendment cannot be retrieved from the pull request and is not
claimed.

## The format it adopts was retired the day before it was written

The PR cites `docs.kernel.org/process/coding-assistants.html#attribution` as its
authority.[^macports-pr-420-diff] The [Linux kernel](linux-kernel.md) **replaced**
`AGENT_NAME:MODEL_VERSION` with the bare literal `LLM` in mainline on **2026-08-03**, because naming
models *"provides free advertising to proprietary software companies"*. The PR's commit was authored
**2026-08-04**, one day later.

**On 2026-08-29 the cited page still served the retired form** — `docs.kernel.org` renders a released
kernel rather than mainline, and it showed `AGENT_NAME:MODEL_VERSION` and the `Claude:claude-3-opus`
example. **On 2026-09-14 it no longer did**: the page rendered `7.3.0-rc3` and specified
`Assisted-by: LLM [TOOL1] [TOOL2]`.[^macports-kernel-rendered]

So the hazard has passed through both of its stages. A rendered page outlived its source long enough
for a second project to copy the superseded rule in good faith; then the page caught up, and **the
proposal now cites, as its authority, a page that contradicts it.** Nothing announced either change.
The body, 19 comments and 9 reviews on the PR were searched on 2026-09-14 for any mention that the
kernel changed the format, with a control string confirming the search worked: **none mentions it.**

**The evidence supports the mechanism, not intent.** No carelessness is implied: the PR cites a
canonical-looking URL on the kernel's own domain, which is what a careful person does. *What went
wrong is that the URL was stale, not that the author was.* The copying is set against the bundle's
other copying events in [policy by copying](../mechanisms/policy-by-copying.md).

## The argument in the thread

**The author's case is provenance.** Asked what the trailer is for: *"In short, enabling provenance
analysis. Putting an LLM in `Co-authored-by` is generally discouraged, BTW."* And on moving
disclosure to review: *"Yes, but tagging commits is also useful."* He points to Apache, FreeBSD,
Linux, LLVM, SciPy and SDL as projects whose discussions are *"well worth reading"*, and summarises:
*"I've seen more that have decided to allow it with tagging and clear statements that the human bears
responsibility. Almost none have allowed it with no tagging or restrictions."*[^macports-pr-420]

**The main objection is that the signal is poor and the cost is real.** A reviewer who opened the
debate on 2026-08-20 — reading the retired example as *"mentioning Claude twice"* and asking what
`MODEL_VERSION` is supposed to be — came back after checking the projects named:

> Only the Linux project requires disclosure in commit messages. Apache recommends `Generated-by` but
> doesn't seem to require it. SciPy requires disclosure with details in the PR … LLVM does not require
> it in the commit message.[^macports-pr-420]

He names three harms: statistics that matter more to companies than to open-source projects;
*"lowering standards as I feel developers are more accepting of some sloppiness if it's known that an
LLM wrote it"*; and a commit log *"littered with 'Claude', basically providing free advertising to AI
companies"*.[^macports-pr-420] The last is the reason [GTK](gtk.md) bans the trailer and the kernel
removed the model from it — reached here independently, in a thread that does not know the kernel
reached it too. His conclusion is that the draft is *"too focused on LLMs and their disclosure, but
not enough on what's expected from contributions"*, a view a third participant endorsed on
2026-09-07.

**The sharpest exchange was about who bans AI at all.** One participant called projects that
disallow LLM-generated code *"kooks"* and asserted that *"There is no legitimate license concern.
That has already been ruled on in several court cases in the US"*. That is a participant's claim,
cited to no ruling, and is recorded as a claim. The author replied that *"not merging AI-generated
code"* is not *"banning all use of AI"* and posted a non-exhaustive list of thirteen projects that
restrict it — among them [QEMU](qemu.md), [Zig](zig.md), GIMP, libxml2, OpenJDK, pkgconf, SDL and
Typst.[^macports-pr-420] Several on that list have no record here; they are leads, not evidence.

**Two further positions** from earlier in the thread still stand: that disclosure belongs in the PR
checklist rather than the commit, which is GTK's arrangement; and that *"we can mostly just assume
that everything is AI assisted. The important part … is that a human is **responsible**"*, which no
adopted policy in this bundle takes.[^macports-pr-420] A later comment asks whether the document is
meant to govern `macports-ports` as well, since it says *"code bases"* in the plural; the PR does not
say.

## The latest proposal is to adopt a policy that forbids the trailer

On 2026-09-13 the same reviewer quoted [Homebrew](homebrew.md)'s five requirements in full —
disclosure in the issue or pull request, self-review, **no AI attribution in commits including
`Assisted-by`**, answering reviewers without AI, and one open AI-assisted pull request for
non-maintainers — and wrote: *"I would recommend adopting this pretty much as-is."* The reply the
same day accepted the review requirement and objected to the concurrency cap, for audit work that
finds several problems at once.[^macports-pr-420]

**If that proposal were taken, MacPorts would move from requiring the trailer to forbidding it**
without passing through any intermediate position — which is the non-portability
[the Assisted-by trailer](../mechanisms/assisted-by-trailer.md) describes, arriving inside one
project's review. It is a proposal in a comment, not a change to the PR.

## Supervision, not prohibition

The one agent rule attracted a refinement worth keeping, because it separates two things most
policies conflate:

> asking your AI to pull something is not the same as having it do it without supervision and is
> okay … The problem is having someone mindlessly run an AI against the repo without supervision and
> inundate us with low quality requests … creating work for human beings.[^macports-pr-420]

That is reviewer bandwidth, the reason most often given for an AI rule in this corpus — see
[human in the loop](../mechanisms/human-in-the-loop.md) for how differently projects draw the same
line.

## What a contributor must do

**Nothing specific to AI is required today**, because the PR has not merged. The existing
expectations still apply: you are responsible for your contribution and must have the right to
license it. If #420 merges, read the merged text rather than this record. The trailer clause is the
most contested part of the proposal, the format it names is one the kernel has abandoned, and the
most recent proposal in the thread would reverse it.

## Re-verification notes

The proposal lives in an open pull request, so **its state is the thing most likely to change**:
check whether #420 merged, and if so which trailer clause survived, if any. `stale_after` stays three
months for that reason.

**Search the thread, do not skim it.** It is long and drifts into whether MacPorts should retire Trac
for GitHub issues, which is out of scope here. Search the PR body, comments and reviews for
`Assisted-by`, `Homebrew` and the kernel's `LLM` form, with a control string known to be present.

**Re-fetch the rendered kernel page and record the version it renders.** The finding above depends on
two dated observations of it, and a third would show whether it has moved again.

[^macports-pr-420]: [macports-base PR #420 — Add CONTRIBUTING.md (open, jmroot)](https://github.com/macports/macports-base/pull/420)
[^macports-pr-420-diff]: [macports-base PR #420 — proposed CONTRIBUTING.md, diff](https://patch-diff.githubusercontent.com/raw/macports/macports-base/pull/420.diff)
[^macports-kernel-rendered]: [AI Coding Assistants — The Linux Kernel documentation (rendered; 7.3.0-rc3 on 2026-09-14)](https://docs.kernel.org/process/coding-assistants.html)
