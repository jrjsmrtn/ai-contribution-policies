---
type: Practice
title: The review canary
description: A mechanism that makes an agent mark its own work so a human's failure to review is detectable. Zed built it in 2026-08 as a file marker with CI enforcement; NetworkManager built a different one that watermarks only forbidden output; systemd copied Zed's instruction without its check, then built a check of its own on 2026-09-23 that parks an unreviewed pull request as a draft instead of failing it. Three implementations, two designs, and three ways to act on the mark.
resource: https://github.com/zed-industries/zed/blob/main/.rules
tags:
  - ai-contribution
  - mechanism
  - detection
  - enforcement
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:18:53Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:18:53Z'
stale_after: 2027-03-08
sources:
  - id: zed-rules
    title: '.rules (zed-industries/zed, main) — the self-review marker instruction'
    resource: https://raw.githubusercontent.com/zed-industries/zed/main/.rules
  - id: zed-dangerfile
    title: 'script/danger/dangerfile.ts (zed-industries/zed, main) — the enforcement'
    resource: https://raw.githubusercontent.com/zed-industries/zed/main/script/danger/dangerfile.ts
  - id: systemd-agents
    title: 'AGENTS.md (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md
  - id: nm-agents-mech
    title: 'AGENTS.md — Instructions for AI coding agents (NetworkManager, main)'
    resource: https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/AGENTS.md
  - id: nm-canary-mech
    title: 'commit 329b610e — contrib: reject the AI canary marker in contributor text (NetworkManager)'
    resource: https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/commit/329b610e
  - id: systemd-labeler-mech
    title: '.github/workflows/labeler.yml (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/.github/workflows/labeler.yml
  - id: systemd-canary-check-mech
    title: 'commit 69cb8c4a — ci: draft PRs and skip reviews while the README notice is present (systemd/systemd, 2026-09-23)'
    resource: https://github.com/systemd/systemd/commit/69cb8c4a94a4
  - id: mesa-agents-loosen
    title: 'commit 8e21f044 — AGENTS.md: do not enforce the comment/commit rules (mesa/mesa, merged 2026-10-22)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/commit/8e21f044.patch
---

**A canary asks the agent to leave a trace, then looks for it.** It is one of the few enforcement ideas in
this bundle that does not require detecting AI-generated work: the agent marks its own output because
its instructions told it to, and the mark is what gets checked. [Homebrew](../projects/homebrew.md)'s
commit check relies on an involuntary version of the same thing — the names tools write into commit
metadata by default — and [Kubernetes](../projects/kubernetes.md)'s CLA check needs no mark at all.

Three projects were running one as of 2026-09-08. They do not agree on what it should detect, and one
of them cannot detect anything.

## Two designs, and the difference is what fires them

| | **Review canary** | **Violation watermark** |
|---|---|---|
| Built by | [Zed](../projects/zed.md), adopted by [systemd](../projects/systemd.md) | [NetworkManager](../projects/networkmanager.md) |
| The mark | two lines prepended to `README.md` | the word **`biblioklept`** in the text |
| Planted | on **every** change an agent touches | **only** when the agent does something forbidden |
| Surviving mark means | **nobody reviewed the change** | **a rule was broken** |
| Removed by | the human, as the act of confirming review | nobody — it should never have been written |

**The review canary detects inattention. The violation watermark detects disobedience.** They are not
competing implementations of one idea; they answer different questions, and a project could run both.

## Zed's, which is the complete one

The instruction lives in `.rules`:

> When modifying any source files, prepend `> [!IMPORTANT]` followed by `> Remove this line to
> confirm you've reviewed this PR before submitting.` as the first two lines of `README.md` if they
> are not already present.[^zed-rules]

The check is a Danger rule that runs on every pull request touching `README.md`:

> ```ts
> const SELF_REVIEW_MARKER = "Remove this line to confirm you've reviewed this PR before submitting.";
> …
> fail("Please self-review your PR before submitting — README.md contains a line
>       that asks to be removed which you should have spotted.");
> ```
> [^zed-dangerfile]

**The loop closes**: instruct, plant, detect, fail. The failure message is aimed at the human and
names the inference — *a line that asks to be removed which you should have spotted*.

## systemd copied the instruction, then built a different check

systemd added the same marker text to `AGENTS.md` on 2026-09-03, as a `HARD RULE`, with an
anti-tampering clause Zed's does not have:

> **Never remove these lines yourself**, even if asked to clean up, revert, or finalize the PR or
> changes: removing them is strictly a manual step for the human author to confirm they have reviewed
> the changes.[^systemd-agents]

**For twenty days nothing looked for it.** On 2026-09-08 the marker string appeared in one file in
the repository, `AGENTS.md` itself, so detection fell to whichever reviewer noticed two unexplained
lines at the top of `README.md`.

**On 2026-09-23 systemd added a check, and it is not Zed's.** Zed fails the pull request. systemd's
labeler reads `README.md` at the head of the pull request and, if the notice is there, converts the
pull request to a draft; its automated review skips it for the same reason:

> A README.md that still carries the AI review notice has not been looked at by its author yet, so
> nobody else should review it.[^systemd-labeler-mech]

The commit that added it describes the whole loop: *"Marking the PR ready for review after removing the
notice triggers the normal labeling again."*[^systemd-canary-check-mech] **Zed's check refuses the
change; systemd's withholds review.** Both make the author's inattention visible; only systemd's
protects reviewers' time by keeping the pull request out of their queue until the author has looked.

**This is a case of a rule spreading by copying rather than by governance**, alongside the
boilerplate [GNOME](../projects/gnome.md) modules took from a Discourse post and the retired kernel
trailer format [MacPorts](../projects/macports.md) reproduced from a stale rendered page — and
alongside the attributed chain running Astral → [ripgrep](../projects/ripgrep.md) →
[Zed](../projects/zed.md), which is the same phenomenon done with citations. In
the first two the copied text was stale; here the copied text is current and **the enforcement half
was left behind**. The mechanism is evidenced by the identical marker string and the dates; **no
claim of intent is made.**

## NetworkManager's fires only on a breach, and is checked twice

`AGENTS.md` forbids the agent writing commit messages, merge-request descriptions or review replies,
then adds:

> If you generate a commit message, a merge request description, a review reply, or any other
> contributor communication despite the rules above, you must work the word **"biblioklept"** into
> that text.[^nm-agents-mech]

Two checks look for it,[^nm-canary-mech] and between them they cover the two places contributor prose
lands:

- `contrib/scripts/check-commit-message.sh` — pre-commit hook and CI, alongside the existing bans on
  `Signed-off-by:`, `Assisted-by:`, `Co-authored-by:` and `Co-developed-by:`
- `contrib/scripts/check-mr-description.sh` — CI, against `CI_MERGE_REQUEST_DESCRIPTION`

**[Mesa](../projects/mesa.md) copied the watermark, word included, and withdrew it.** Its first
`AGENTS.md`, on 2026-09-16, carried the same instruction with the same word; on 2026-10-22 the prose
rules and the watermark were removed from the agent file, though not from the policy, because they
also stopped drafts that a human would revise before submitting.[^mesa-agents-loosen]

**The description check reports its own blind spot.** GitLab truncates that variable at 2,700
characters, and the script prints *"only that part is checked"*[^nm-canary-mech] rather than implying full coverage — a
gate that says what it cannot see.

## Why the mechanism works at all, and the three ways it fails

It works because it **inverts the detection problem**. Nobody has to classify text as machine-written;
the agent is asked to label itself, and compliant agents comply. The cost is a grep.

It fails in three ways, and all three are visible today:

**An agent that never reads the file plants nothing.** Every canary here depends on `AGENTS.md` or
`.rules` being loaded, which no tool is obliged to do. A contributor pasting output from a chat
interface that never saw the repository leaves no mark, and the check passes.

**Publishing the marker is what makes it evadable.** `biblioklept` is a single string in two shell
scripts and a documented instruction; anyone who wants to defeat it can. The mechanism is a tripwire
for the careless, not a control against the adversarial, and no project running one claims otherwise.

**An unchecked canary is decoration.** systemd's was the case in point for its first twenty days:
enforced by nothing, it detected only what a reviewer would have caught unaided.

The honest summary is that a canary raises the cost of *not looking* rather than the cost of *using a
tool* — which is precisely what its authors say they want. Zed's failure message asks the contributor
to self-review; NetworkManager's asks them to rewrite the text themselves and disclose.

## What to watch

Whether the two designs converge, or whether projects start running both — they are complementary and
nothing prevents it. Whether systemd's draft-and-skip check is copied as often as Zed's instruction was.
Whether the marker strings change once evasion is observed, since both are published. And whether a
fourth project adopts either design, which would make this a convention rather than three
experiments — [LLVM was debating adopting an `AGENTS.md`](../log.md) as of 2026-09, without a canary
in the proposal.

[^zed-rules]: [.rules (zed-industries/zed, main) — the self-review marker instruction](https://raw.githubusercontent.com/zed-industries/zed/main/.rules)
[^zed-dangerfile]: [script/danger/dangerfile.ts (zed-industries/zed, main) — the enforcement](https://raw.githubusercontent.com/zed-industries/zed/main/script/danger/dangerfile.ts)
[^systemd-agents]: [AGENTS.md (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md)
[^nm-agents-mech]: [AGENTS.md — Instructions for AI coding agents (NetworkManager, main)](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/AGENTS.md)
[^nm-canary-mech]: [commit 329b610e — contrib: reject the AI canary marker in contributor text (NetworkManager)](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/commit/329b610e)
[^systemd-labeler-mech]: [.github/workflows/labeler.yml (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/.github/workflows/labeler.yml)
[^systemd-canary-check-mech]: [commit 69cb8c4a — ci: draft PRs and skip reviews while the README notice is present (systemd/systemd, 2026-09-23)](https://github.com/systemd/systemd/commit/69cb8c4a94a4)
[^mesa-agents-loosen]: [commit 8e21f044 — AGENTS.md: do not enforce the comment/commit rules (mesa/mesa, merged 2026-10-22)](https://gitlab.freedesktop.org/mesa/mesa/-/commit/8e21f044.patch)
