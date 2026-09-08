---
type: Organization
title: Zed
description: Welcomes LLM-assisted coding, refuses autonomous agents outright, and reserves all maintainer-facing communication to humans — a policy it adapted from ripgrep's and says so. It built the review canary the rest of this bundle now copies, is the only project enforcing one in CI, and governs its own agent-instruction file with three admission criteria.
resource: https://github.com/zed-industries/zed/blob/main/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - restricted
  - communication
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:18:53Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:18:53Z'
stale_after: 2027-03-08
sources:
  - id: zed-contributing
    title: 'CONTRIBUTING.md — AI Policy (zed-industries/zed, main)'
    resource: https://raw.githubusercontent.com/zed-industries/zed/main/CONTRIBUTING.md
  - id: zed-rules-file
    title: '.rules (zed-industries/zed, main)'
    resource: https://raw.githubusercontent.com/zed-industries/zed/main/.rules
  - id: zed-danger
    title: 'script/danger/dangerfile.ts (zed-industries/zed, main)'
    resource: https://raw.githubusercontent.com/zed-industries/zed/main/script/danger/dangerfile.ts
  - id: ripgrep-ai-policy
    title: 'AI Policy (AI_POLICY.md, BurntSushi/ripgrep, master) — the source Zed adapted'
    resource: https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md
---

**Stance: LLM-assisted coding welcome, autonomous agents refused, prose reserved to humans.** Zed is a
company-backed editor with an outside contributor base, and its policy binds contributors rather than
staff — which is why it is filed here and not under `vendors/`.

> We welcome the use of LLMs for coding, but we hold a high bar for all contributions, and **we expect
> a human in the loop who genuinely understands the work an LLM produces** on their behalf. For that
> reason, **we don't accept contributions from autonomous agents**. Pull requests that appear to
> violate this may be closed, sometimes without notice.[^zed-contributing]

The autonomous-agent refusal is the sharp edge. [Perl](perl.md) and
[Dependency-Track](dependency-track.md) bar agents from *opening* issues and pull requests;
this bars the *mode of work* — a human may use a model, a model may not be left to run. The sanction
is stated and deliberately unceremonious: *closed, sometimes without notice.*

## It says where it came from

> This policy was **adapted from [ripgrep's AI policy]**.[^zed-contributing]

That single sentence makes Zed the only record in this bundle whose policy **cites its own source**.
ripgrep's text carries the same three moves — a high bar with the maintainer remaining responsible,
communication reserved to humans (*"Comments that are believed to be written by AI may be hidden
without notice"*), and *"Autonomous agents are not allowed to be used for contributing to this
project"*.[^ripgrep-ai-policy]

This bundle has now documented four cases of a rule spreading by copying. In
[GNOME](gnome.md)'s and [MacPorts](macports.md)'s the copied text was stale and the copying
unattributed; in [systemd](systemd.md)'s the text was current and the enforcement was left behind.
**This is the first where the borrower names the lender**, which is the difference between a
convention forming and a rumour propagating.

## The most generous translation clause here, and a disclosure recipe

Most policies that permit translation say only that it is permitted. Zed says how:

> If you're a non-native English speaker using an LLM to thoroughly edit or translate your messages to
> the maintainers, we'd encourage you to **put the machine translation in a quote block and include
> the original text in your native language after it**.[^zed-contributing]

**That is the only clause in this bundle that treats a contributor's own language as evidence rather
than noise** — the original is kept so a reader can check what the machine did to it.

The same shape governs sharing model output:

> If you think it's helpful/necessary to **share context from a chat with an LLM**, please put the
> **relevant part of it** in a quote block, **disclose it as AI-generated**, and add your own
> commentary explaining **why it's relevant and what you take from it**.[^zed-contributing]

Three requirements — quote it, label it, and say what you make of it. [Asahi Linux](asahi-linux.md)
forbids pasting model output into community channels outright; Zed permits it on condition the
contributor does the interpretive work. **Both are answers to the same complaint**, that unlabelled
model output transfers reading cost to the reader.

And the reason given for the prose rule is the redundancy argument, put more bluntly than anywhere
else: *"The readers are humans, and we'd like to hear from you, not from a model **(we have models at
home)**."*[^zed-contributing] [Elixir](elixir.md) and [Asahi Linux](asahi-linux.md) reach the same
premise independently.

## It built the canary, and it is the only project checking one

`.rules` carries the instruction — buried at line 16 in a list of Rust conventions rather than in a
policy section — telling the agent to prepend a self-review marker to `README.md` on any source
change.[^zed-rules-file] `script/danger/dangerfile.ts` then fails any pull request where that marker
appears in the `README.md` diff.[^zed-danger]

**Zed is the origin of the design and, with [NetworkManager](networkmanager.md)'s different one, one
of only two projects whose canary is actually enforced** — [systemd](systemd.md) copied the
instruction without the check. The mechanism, its two designs and its failure modes are recorded in
[the review canary](../mechanisms/review-canary.md).

## `.rules` governs its own growth, with criteria

Zed writes down what may enter its agent-instruction file, and the reasoning generalises past this
project:

> **New rules must meet all three criteria:** 1. **Non-obvious** — someone familiar with the codebase
> would still get it wrong without the rule. 2. **Repeatedly encountered** — it came up more than
> once. 3. **Specific enough to act on** — a concrete instruction, not a vague
> principle.[^zed-rules-file]

> Avoid architectural descriptions of a crate. These go stale fast and the agent can gather them by
> reading the code. **Rules should be traps to avoid, not maps to follow.**[^zed-rules-file]

And the file may not be edited during ordinary work: an agent that notices a pattern must propose it
under a *"Suggested `.rules` additions"* heading in the pull request description, with reviewers
deciding — *"Rules emerge from validated patterns, not one-off observations."*[^zed-rules-file]

**Two projects in this bundle now govern their agent-instruction files, and they agree.**
[systemd](systemd.md)'s rule is *"only add instructions to this file if you've seen an AI agent mess
up that particular bit of logic in practice"* — Zed's criterion 2, arrived at separately. Both are
answers to context cost: a file read at the start of every session is a budget, and anything
speculative in it is spent for nothing.

`AGENTS.md` and `CLAUDE.md` are each six bytes containing `.rules` — the pointer pattern, here aimed
at a third filename rather than at `AGENTS.md`.

## What a contributor must do

Use an LLM to write code if you like, but **stay in the loop**: understand what it produced, and do
not hand the work to an autonomous agent — pull requests that look like you did may be closed without
notice. **Write your own issue text, pull request description and review replies.** If English is not
your first language you may translate, but quote the machine output and include your original beneath
it. If model output is genuinely useful context, quote it, label it as AI-generated, and explain what
you take from it. **If an agent has touched the tree it will have added two lines to `README.md`;
delete them yourself** — that deletion is how you confirm you reviewed the change, and CI fails the
pull request if the lines survive.

## Re-verification notes

**Three files.** `CONTRIBUTING.md` holds the policy, `.rules` holds the agent instructions and the
canary, `script/danger/dangerfile.ts` holds the enforcement. `AGENTS.md` and `CLAUDE.md` are pointers
and carry nothing.

`git log -- .rules` dates the marker instruction to **2026-08-21** (#62945) and shows it being
**restored on 2026-08-28** (#63384, *"Restore the rule"*) — so it was removed at some point in
between. **Why it was removed and restored is not established here**, and is the most interesting
unanswered question about this record: a canary that was briefly reverted may have met an objection
worth knowing about.

Watch whether the ripgrep attribution survives edits, since it is the only provenance line in this
bundle and would be easy to lose in a rewrite. And watch the `.rules` admission criteria against the
file's actual growth — it is 12 KB already, and the discipline it describes is easier to write than
to keep.

[^zed-contributing]: [CONTRIBUTING.md — AI Policy (zed-industries/zed, main)](https://raw.githubusercontent.com/zed-industries/zed/main/CONTRIBUTING.md)
[^zed-rules-file]: [.rules (zed-industries/zed, main)](https://raw.githubusercontent.com/zed-industries/zed/main/.rules)
[^zed-danger]: [script/danger/dangerfile.ts (zed-industries/zed, main)](https://raw.githubusercontent.com/zed-industries/zed/main/script/danger/dangerfile.ts)
[^ripgrep-ai-policy]: [AI Policy (AI_POLICY.md, BurntSushi/ripgrep, master) — the source Zed adapted](https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md)
