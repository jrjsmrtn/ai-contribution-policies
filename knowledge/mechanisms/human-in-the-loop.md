---
type: Practice
title: Human in the loop
description: The most-copied phrase in these policies and the least defined. Nine records use it or bar autonomous agents, and they govern five different things — the mode of work, the act of publishing, maintainer discretion, where in the tracker, and a level you declare. None of them can detect autonomy, so each substitutes an observable proxy, and the three outright prohibitions all hedge their verbs. A Linux wireless maintainer supplies the counter-case where the human was in the loop and it made no difference.
resource: https://raw.githubusercontent.com/astral-sh/.github/main/AI_POLICY.md
tags:
  - ai-contribution
  - mechanism
  - policy-design
  - enforcement
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-10T13:40:00Z'
verified:
  - by: claude/opus-5
    at: '2026-09-10T13:40:00Z'
stale_after: 2027-03-10
sources:
  - id: hitl-astral
    title: 'AI_POLICY.md (astral-sh/.github, main)'
    resource: https://raw.githubusercontent.com/astral-sh/.github/main/AI_POLICY.md
  - id: hitl-ripgrep
    title: 'AI_POLICY.md — ripgrep AI policy (BurntSushi/ripgrep, master)'
    resource: https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md
  - id: hitl-zed
    title: 'CONTRIBUTING.md (zed-industries/zed, main)'
    resource: https://raw.githubusercontent.com/zed-industries/zed/main/CONTRIBUTING.md
  - id: hitl-llvm
    title: 'LLVM AI Tool Use Policy (llvm/docs/AIToolPolicy.md, main)'
    resource: https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/docs/AIToolPolicy.md
  - id: hitl-ansible
    title: 'Ansible community AI policy'
    resource: https://docs.ansible.com/projects/ansible/latest/community/ai_policy.html
  - id: hitl-aideclaration
    title: 'AI-DECLARATION.md specification v0.1.2'
    resource: https://ai-declaration.md/en/0.1.2
  - id: hitl-kernel-wireless
    title: 'linux-wireless — maintainer response to AI-assisted syzbot fixes'
    resource: https://lore.kernel.org/linux-wireless/3b6c46b6d79f3a0e0ded2967db3cfd469314b05c.camel@sipsolutions.net/T/
---

***"A human in the loop"* is the most-copied phrase in this bundle and the least defined.** Nine
records use it or bar autonomous agents, and reading them side by side shows they are not making the
same rule — they are governing five different things and calling it one.

## The five things the phrase governs

| Record | What is actually constrained | The rule |
|---|---|---|
| [Astral](../vendors/astral.md) | the **mode of work** | *"We do not allow autonomous agents"*[^hitl-astral] |
| [ripgrep](../projects/ripgrep.md) | the mode of work | the same sentence, scope-edited[^hitl-ripgrep] |
| [Zed](../projects/zed.md) | the mode of work | *"we don't accept contributions from autonomous agents"*[^hitl-zed] |
| [LLVM](../projects/llvm.md) | the act of **publishing** | bans agents that *"take action in our digital spaces without human approval"*[^hitl-llvm] |
| [Ansible](../projects/ansible.md) | **maintainer discretion** | autonomous contributions *"MAY be rejected … without prior justification"*[^hitl-ansible] |
| [Elixir](../projects/elixir.md) | **where in the tracker** | no agents on issues without the *Contributions Welcome* label |
| [Perl](../projects/perl.md) | the act of **opening a thread** | an agent may not create an issue or a pull request |
| [Dependency-Track](../projects/dependency-track.md) | the act of opening a thread | *"Never create an issue. Never create a PR"* |
| [cdxgen](../projects/cdxgen.md) | **a level you declare** | `auto` is a disclosure value, not a prohibition[^hitl-aideclaration] |

**The same mode of work is a bannable offence in three projects and a disclosable attribute in a
fourth.** cdxgen's scale defines `auto` as *"Human prompts and AI acts autonomously, bringing the
task to completion"* and asks you to record it per path. Nothing in this bundle is a sharper
disagreement about the same behaviour.

## Nobody forbids autonomy, because nobody can detect it

**Read the three prohibitions for their verbs.** Astral closes pull requests *"we believe were
created autonomously"*.[^hitl-astral] ripgrep closes those *"that appear in violation"*.[^hitl-ripgrep]
Zed closes those *"that appear to violate this"*.[^hitl-zed] All three hedge, and they hedge in the
operative clause.

That is not sloppiness; it is the honest form of the rule. **Autonomy is a fact about a process that
happened somewhere else**, and the artifact that arrives carries no evidence of it. So every record
here substitutes something observable:

| Record | The observable proxy |
|---|---|
| Astral, ripgrep, Zed | a submission that *looks* autonomous, judged by a maintainer |
| LLVM | something **published** in project spaces without approval |
| Ansible | nothing — the maintainer's veto needs no finding of fact |
| Elixir | the **label** on the issue |
| Perl, Dependency-Track | **who opened** the thread |
| cdxgen | the contributor's own **declaration** |

**LLVM's is the only one that is fully observable and fully specified**, and it gets there by
relocating the rule: not *do not use an autonomous agent*, but *nothing acts in our spaces without a
human approving it*. It then permits what the blunt version would forbid — *"an opt-in review tool
that keeps a human in the loop is acceptable"*[^hitl-llvm] — which is why LLVM can run review tooling
while banning the GitHub `@claude` agent by name.

**Ansible's is the only one that needs no detection at all**, because it is a veto rather than a
prohibition: *"MAY be rejected … without prior justification."*[^hitl-ansible] No argument required,
no appeal named. A deliberate asymmetry against volume, and the only instance here of a policy that
declines to define the thing it is refusing.

## The reason did not travel

**Astral is the only one that says why**, and it argues from what depends on the code:

> **Due to the foundational nature of our projects**, we require a human in the loop who understands
> the work produced by AI.[^hitl-astral]

`uv` and `ruff` sit under a large share of the Python ecosystem's builds, and the claim is that the
blast radius sets the bar — a position that would justify a *different* answer for a less
load-bearing project, and does not pretend otherwise.

**ripgrep and Zed carry the rule and not the argument.** The criticality clause is the piece dropped
at the first hop of the lineage, which is the pattern
[policy by copying](policy-by-copying.md) records: **the borrower keeps the prohibition and leaves
the reasoning that bounded it.** A rule inherited without its justification cannot be applied to a
case its author would have decided differently.

## The counter-case, from a maintainer who had one

A Linux wireless maintainer refused a series of syzbot-derived fixes, and his objection is the
sharpest thing said about this phrase anywhere in the bundle — because in his case **the human was in
the loop**:

> *"the human in the loop should actually take a step back from that and ask what the semantics of
> the code should be"*[^hitl-kernel-wireless]

An LLM asked for a targeted fix produces a targeted fix. A human who reviews it confirms it fixes the
report. **Both did their job and the patch was still wrong**, because nobody asked the question one
level up. He is explicit that he cannot supply that himself — *"I really cannot make that judgement
call myself for every single issue like that … Need the contributors to do
that."*[^hitl-kernel-wireless]

**A human in the loop is a necessary condition that eight of these records treat as a sufficient
one.** The phrase names a presence; the failure it is meant to prevent is an absence of judgement,
and presence does not imply it.

## What to watch

Whether any project defines the term — none does, and the cdxgen scale is the only vocabulary here
precise enough to. Whether LLVM's relocation spreads, since *published without approval* is the only
version of this rule a project can enforce without guessing. Whether the criticality argument is ever
picked up by a project that is **not** foundational, which would be the first sign the phrase has
detached from its reason entirely. And whether any of the three prohibitions is ever observed to
close a pull request — the sanction is stated in all three and recorded in none.

[^hitl-astral]: [AI_POLICY.md (astral-sh/.github, main)](https://raw.githubusercontent.com/astral-sh/.github/main/AI_POLICY.md)
[^hitl-ripgrep]: [AI_POLICY.md — ripgrep AI policy (BurntSushi/ripgrep, master)](https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md)
[^hitl-zed]: [CONTRIBUTING.md (zed-industries/zed, main)](https://raw.githubusercontent.com/zed-industries/zed/main/CONTRIBUTING.md)
[^hitl-llvm]: [LLVM AI Tool Use Policy (llvm/docs/AIToolPolicy.md, main)](https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/docs/AIToolPolicy.md)
[^hitl-ansible]: [Ansible community AI policy](https://docs.ansible.com/projects/ansible/latest/community/ai_policy.html)
[^hitl-aideclaration]: [AI-DECLARATION.md specification v0.1.2](https://ai-declaration.md/en/0.1.2)
[^hitl-kernel-wireless]: [linux-wireless — maintainer response to AI-assisted syzbot fixes](https://lore.kernel.org/linux-wireless/3b6c46b6d79f3a0e0ded2967db3cfd469314b05c.camel@sipsolutions.net/T/)
