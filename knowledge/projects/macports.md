---
type: Organization
title: MacPorts
description: Has no adopted AI policy, but its unmerged proposal is already practice. An open pull request would require an Assisted-by trailer in the kernel's retired model-named form, and since the day it opened 316 commits in macports-ports have carried that form, 313 of them by one committer, while reviewers point contributors at the draft. The kernel page it cites has since changed format, and a participant proposes Homebrew's ban on the trailer instead.
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
  - by: claude/opus-5
    at: '2026-09-15T13:30:00Z'
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
  - id: macports-dev-announcement
    title: 'macports-dev — Proposed contributing document (Joshua Root, 2026-08-04)'
    resource: https://lists.macports.org/pipermail/macports-dev/2026-August/046853.html
  - id: macports-dev-trac-anubis
    title: 'macports-dev — Heads-up: MacPorts Trac now behind Anubis AI crawler protection (2026-06-15)'
    resource: https://lists.macports.org/pipermail/macports-dev/2026-June/046795.html
  - id: macports-users-vapor
    title: 'macports-users — New Port request: Vapor.code filed, what else is needed? (2026-08-16)'
    resource: https://lists.macports.org/pipermail/macports-users/2026-August/054373.html
  - id: macports-ports-34081-review
    title: 'macports-ports PR 34081 — review comment pointing to macports-base PR 420 (2026-08-17)'
    resource: https://github.com/macports/macports-ports/pull/34081#issuecomment-5312375408
  - id: macports-ports-34661-review
    title: 'macports-ports PR 34661 — review comment pointing to macports-base PR 420 (2026-09-15)'
    resource: https://github.com/macports/macports-ports/pull/34661#issuecomment-5679177293
  - id: macports-ports-34661-reply
    title: 'macports-ports PR 34661 — contributor switches to Assisted-by (2026-09-15)'
    resource: https://github.com/macports/macports-ports/pull/34661#issuecomment-5679976280
  - id: macports-ports-assisted-search
    title: 'GitHub commit search, macports-ports, "Assisted-by" (316 results on 2026-09-15)'
    resource: https://api.github.com/search/commits?q=repo:macports/macports-ports+%22Assisted-by%22
  - id: macports-ports-first-assisted
    title: 'macports-ports commit a89d64e444 — first Assisted-by trailer (2026-08-04)'
    resource: https://github.com/macports/macports-ports/commit/a89d64e444682be47db2f243576e8c0bcf1d51d1
  - id: macports-ports-coauthored-search
    title: 'GitHub commit search, macports-ports, noreply@anthropic.com (183 results on 2026-09-15)'
    resource: https://api.github.com/search/commits?q=repo:macports/macports-ports+%22noreply%40anthropic.com%22
  - id: macports-base-coauthored-search
    title: 'GitHub commit search, macports-base, noreply@anthropic.com (8 results on 2026-09-15)'
    resource: https://api.github.com/search/commits?q=repo:macports/macports-base+%22noreply%40anthropic.com%22
  - id: macports-pr-420-bundle-comment
    title: 'macports-base PR 420 — comment by this bundle''s maintainer on the kernel format change (2026-09-14)'
    resource: https://github.com/macports/macports-base/pull/420#issuecomment-5664987148
---

**Stance: undecided. This record describes a proposal, not a rule.** MacPorts has no adopted AI
policy. Pull request **#420**, *"Add CONTRIBUTING.md"*, was opened by Joshua Root on **2026-08-04**
and was **still open and unmerged** when re-checked on 2026-09-15.[^macports-pr-420] It is recorded
here because of what it demonstrates, not because it binds anyone.

> ⚠ **No written rule is in force, but the draft is already applied.** No merged document binds a
> MacPorts contributor today. Reviewers have nonetheless asked contributors to follow #420, and
> hundreds of commits already do. Re-read the PR before relying on any of this.

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
same commit, and the diff fetched on 2026-09-15 still specifies `AGENT_NAME:MODEL_VERSION`. What the
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
kernel changed the format, with a control string confirming the search worked, and none mentioned
it. **Later that day this bundle's maintainer posted a comment pointing it out**,[^macports-pr-420-bundle-comment]
so from 2026-09-14 the thread does contain the correction; that involvement is disclosed here.

**The evidence supports the mechanism, not intent.** No carelessness is implied: the PR cites a
canonical-looking URL on the kernel's own domain, which is what a careful person does. *What went
wrong is that the URL was stale, not that the author was.* The copying is set against the bundle's
other copying events in [policy by copying](../mechanisms/policy-by-copying.md).

## The proposal is already practice

**The trailer the PR proposes is already in the ports tree, in the format the PR names.** A GitHub commit
search of `macports-ports` on 2026-09-15 returned **316 commits** with an `Assisted-by:` trailer, and
every one has a trailer line rather than a passing mention.[^macports-ports-assisted-search]

- **None predates the proposal.** The first is `a89d64e444`, committed 2026-08-04 at 21:13 UTC, about
  seven hours after #420 was opened.[^macports-ports-first-assisted] 303 followed in August and 13 in
  September, the latest on 2026-09-14.
- **313 of the 316 are by one committer, `herbygillot`**, and **315 use the kernel's retired
  `AGENT:MODEL` form** — 309 of them `Assisted-by: Claude:claude-opus-5`. The other three come from
  three other contributors: `Claude:fable-5 [claude-code]`, `Google Search AI:Version of 2026-08-21`,
  and the free-text `ChatGPT 5.6 Luna`.
- **Before that, the same committer used `Co-Authored-By`.** The same search for `noreply@anthropic.com`
  returned **183 commits** with a `Co-Authored-By` trailer naming Anthropic, from 2026-02-15 to
  2026-08-16, 178 of them by `herbygillot`.[^macports-ports-coauthored-search] The 106 made from
  2026-08-04 onward carry **both** trailers; none after 2026-08-16 carries `Co-Authored-By`.
- **`macports-base`**, where #420 lives, has no `Assisted-by` commits but **8 commits co-authored with
  Anthropic**, all by `herbygillot` between 2026-03-15 and 2026-05-12, committed by `jmroot`,
  `neverpanic` or `herbygillot`.[^macports-base-coauthored-search]

**So the switch in the ports tree followed the proposal within hours, and follows its wording exactly —
the retired format included.** The PR body calls the trailer *"the emerging de facto standard"*; inside
MacPorts, the measured practice is overwhelmingly one committer's commit history, adopted the day the
proposal appeared. This record draws no conclusion about intent from the timing; the dates and counts
are what can be checked.

## Reviewers already apply it

**Twice, a contributor has been pointed at the unmerged draft in review.**

1. **Vapor toolbox, August.** On 2026-08-16 a contributor wrote to macports-users: *"I did something
   with the help of Googles AI"*, linking the conversation.[^macports-users-vapor] On the resulting pull
   request, `ryandesign` — a MacPorts committer, with about 29,700 commits committed in the ports tree —
   wrote on 2026-08-17: *"We're still working out the exact wording, but we would
   like changes that were created with the assistance of AI to be marked as such. Please see here for
   the current recommendations"*, linking #420.[^macports-ports-34081-review] The merged commit carries
   `Assisted-by: Google Search AI:Version of 2026-08-21`.
2. **QtPass, September.** A contributor who describes themself as QtPass's upstream maintainer opened
   an update whose description credited Claude Code. On 2026-09-15 `herbygillot` — a public member of the MacPorts GitHub organisation and the committer of
   about 29,800 ports commits — commented: *"While still
   being discussed, MacPorts is leaning towards AI or LLM -assisted contributions to needing to be marked
   with `Assisted-By`, and not `Co-Authored-By`"*, linking #420.[^macports-ports-34661-review] Within the
   hour the contributor *"switched the trailer to Assisted-by: Claude:claude-fable-5-1 [Claude Code] per
   macports-base#420"*[^macports-ports-34661-reply] — the retired kernel format, adopted **the day after**
   #420's thread was told the kernel had dropped it. That pull request was still open on 2026-09-15.

**An unmerged draft is functioning as review guidance, and it carries its stale format into commits.**
This is the copying hazard in [policy by copying](../mechanisms/policy-by-copying.md) one step further
along: a rendered page's superseded rule entered a draft, and the draft is now entering the tree.

## Discussion was asked for on the list, and happened on GitHub

The PR body asks: *"Please discuss on macports-dev in order to reach a wider audience."*[^macports-pr-420]
The author's announcement to that list on 2026-08-04 says *"I've opened a PR that adds a
CONTRIBUTING.md"* and *"Please have a look and make your opinions known here on the list."*[^macports-dev-announcement]

**No one replied on the list.** The macports-dev archives for 2026-08 (38 messages) and 2026-09
(15 messages) were read in full on 2026-09-15, and #420 appears only in the announcement. Every comment
and review is on GitHub instead. Subject indexes for macports-dev since 2024 and macports-users since
2025 carry no other thread on AI contributions. The one other AI-related subject is operational: on
2026-06-15 Trac was put behind Anubis *"due to continued hammering by AI crawler bots that ignore
robots.txt"*[^macports-dev-trac-anubis] — a response to crawlers, not a rule about contributions.

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

**If that proposal were taken, MacPorts would move from requiring the trailer to forbidding it** —
a trailer 316 commits in its ports tree already carry —
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

**No written rule binds you**, because the PR has not merged: you are responsible for your
contribution and must have the right to license it. **In practice, expect a reviewer to ask for an
`Assisted-by` trailer if you used AI**, citing #420; the examples accepted so far name the tool and
model, in the format the kernel has abandoned. If #420 merges, read the merged text rather than this
record — the trailer clause is its most contested part, and the most recent proposal in the thread
would reverse it.

## Re-verification notes

The proposal lives in an open pull request, so **its state is the thing most likely to change**:
check whether #420 merged, and if so which trailer clause survived, if any. `stale_after` stays three
months for that reason.

**Search the thread, do not skim it.** It is long and drifts into whether MacPorts should retire Trac
for GitHub issues, which is out of scope here. Search the PR body, comments and reviews for
`Assisted-by`, `Homebrew` and the kernel's `LLM` form, with a control string known to be present.

**Re-fetch the rendered kernel page and record the version it renders.** The finding above depends on
two dated observations of it, and a third would show whether it has moved again.

**Re-measure the practice, not just the proposal.** Re-run the commit searches for `Assisted-by` and
`noreply@anthropic.com` in `macports-ports` and `macports-base`, and record totals, authors and
formats; a change in who writes the trailer, or in its format, is the signal. Check #420's timeline
for cross-references — that is how both review citations were found.

**Read the mailing lists too.** `lists.macports.org/pipermail/` serves macports-dev and macports-users
to plain `curl`. Search subjects **and** bodies: the Vapor disclosure was only findable in a body. A
subject index that mentions Anubis is not a challenge page — check for challenge markup, not the word.

[^macports-pr-420]: [macports-base PR #420 — Add CONTRIBUTING.md (open, jmroot)](https://github.com/macports/macports-base/pull/420)
[^macports-pr-420-diff]: [macports-base PR #420 — proposed CONTRIBUTING.md, diff](https://patch-diff.githubusercontent.com/raw/macports/macports-base/pull/420.diff)
[^macports-kernel-rendered]: [AI Coding Assistants — The Linux Kernel documentation (rendered; 7.3.0-rc3 on 2026-09-14)](https://docs.kernel.org/process/coding-assistants.html)
[^macports-dev-announcement]: [macports-dev — Proposed contributing document (Joshua Root, 2026-08-04)](https://lists.macports.org/pipermail/macports-dev/2026-August/046853.html)
[^macports-dev-trac-anubis]: [macports-dev — Heads-up: MacPorts Trac now behind Anubis AI crawler protection (2026-06-15)](https://lists.macports.org/pipermail/macports-dev/2026-June/046795.html)
[^macports-users-vapor]: [macports-users — New Port request: Vapor.code filed, what else is needed? (2026-08-16)](https://lists.macports.org/pipermail/macports-users/2026-August/054373.html)
[^macports-ports-34081-review]: [macports-ports PR 34081 — review comment pointing to macports-base PR 420 (2026-08-17)](https://github.com/macports/macports-ports/pull/34081#issuecomment-5312375408)
[^macports-ports-34661-review]: [macports-ports PR 34661 — review comment pointing to macports-base PR 420 (2026-09-15)](https://github.com/macports/macports-ports/pull/34661#issuecomment-5679177293)
[^macports-ports-34661-reply]: [macports-ports PR 34661 — contributor switches to Assisted-by (2026-09-15)](https://github.com/macports/macports-ports/pull/34661#issuecomment-5679976280)
[^macports-ports-assisted-search]: [GitHub commit search, macports-ports, "Assisted-by" (316 results on 2026-09-15)](https://api.github.com/search/commits?q=repo:macports/macports-ports+%22Assisted-by%22)
[^macports-ports-first-assisted]: [macports-ports commit a89d64e444 — first Assisted-by trailer (2026-08-04)](https://github.com/macports/macports-ports/commit/a89d64e444682be47db2f243576e8c0bcf1d51d1)
[^macports-ports-coauthored-search]: [GitHub commit search, macports-ports, noreply@anthropic.com (183 results on 2026-09-15)](https://api.github.com/search/commits?q=repo:macports/macports-ports+%22noreply%40anthropic.com%22)
[^macports-base-coauthored-search]: [GitHub commit search, macports-base, noreply@anthropic.com (8 results on 2026-09-15)](https://api.github.com/search/commits?q=repo:macports/macports-base+%22noreply%40anthropic.com%22)
[^macports-pr-420-bundle-comment]: [macports-base PR 420 — comment by this bundle's maintainer on the kernel format change (2026-09-14)](https://github.com/macports/macports-base/pull/420#issuecomment-5664987148)
