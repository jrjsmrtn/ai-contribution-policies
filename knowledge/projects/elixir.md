---
type: Organization
title: Elixir
description: Permits AI with restraint, and argues for it from a premise no other project states — the maintainers already have AI, so what they want is the human behind the agent. It gates agent work by issue label, requires automated changes be paired with adversarial agents whose job is to invalidate them, and forbids an agent adding a Signed-off-by because only a human can certify the DCO.
resource: https://github.com/elixir-lang/elixir/blob/main/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - dco
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-06T22:23:15Z'
verified:
  - by: claude/opus-5
    at: '2026-09-06T22:23:15Z'
stale_after: 2027-03-07
sources:
  - id: elixir-contributing
    title: 'Contributing to Elixir (CONTRIBUTING.md, elixir-lang/elixir, main) — Using AI and coding agents'
    resource: https://raw.githubusercontent.com/elixir-lang/elixir/main/CONTRIBUTING.md
---

**Stance: permitted, with restraint argued from an unusual premise.** The guidance arrived
**2026-04-15** and was extended **2026-05-04**, and it opens by explaining why moderation is asked
for at all:

> While we allow the use of AI on contributions and discussions, please be mindful when doing so.
> **Generally speaking, Elixir maintainers already have access to AI** (like many other developers).
> Therefore, if we need the feedback or help of a coding agent, we can request so ourselves. For this
> reason, **we often find the point of view of the human behind the agent more
> valuable**.[^elixir-contributing]

Every other project here justifies restraint by cost, risk or provenance. **This one argues from
redundancy**: the output is not scarce, so submitting it adds nothing the maintainer could not have
produced. [Asahi Linux](asahi-linux.md) makes the same observation to ban pasted model output from
support channels — *"others also have access to the same models as you do"* — and reaches a
prohibition; Elixir reaches a request for judgement. **Same premise, opposite instruments.**

## Agent work is gated by issue label

> **Do not use coding agents to tackle existing issues unless they have the "Contributions Welcome"
> label.**[^elixir-contributing]

No other policy in this bundle scopes agent work by *where in the tracker* it happens. It is a
mechanical boundary made of machinery the project already ran, in the way
[GCC](gcc.md) reused a copyright threshold and [Asahi](asahi-linux.md) an existing ban — and it
targets the specific failure of agents swarming open issues, without needing to detect anything.

The complement is stated too: if you propose a feature on the mailing list and it is accepted, *"you
may use coding agents to implement it"*.[^elixir-contributing] **Agreement first, agent second** —
the same ordering [Perl](perl.md) asks for with its issue-before-PR rule, here applied specifically
to agent work.

## The adversarial-pairing requirement, which is unique

> When automating AI usage on the Elixir codebase for performance improvements, security fixes, or
> correctness changes to the compiler or type system, **pair it with a separate set of agents whose
> job is to argue against and try to invalidate any proposed change**. And treat their approval as
> advisory: **a human must still validate it** before opening issues or pull
> requests.[^elixir-contributing]

**Nothing else in this bundle requires a red team.** Other policies tell a contributor to verify
their own work — [Kubernetes](kubernetes.md)'s *"do not leave the first review to the reviewers"* is
the closest — but this specifies the *method*, and specifies that the method's output does not count
as approval.

Two things make it more than a curiosity. It scopes itself to the highest-risk surfaces (compiler,
type system, security, performance) rather than to all contributions, so the cost lands where the
blast radius is. And it treats agreement between agents as **evidence rather than authority**, which
is the correct epistemics and is stated plainly in a way most human review processes never bother to.

## The DCO gets an explicit answer

> **AI agents MUST NOT add `Signed-off-by` tags. Only humans can legally certify the Developer
> Certificate of Origin (DCO).** The human submitter is responsible for: reviewing all AI-generated
> code; ensuring compliance with licensing requirements; **adding their own `Signed-off-by` tag** to
> certify the DCO; taking full responsibility for the contribution; **disclosing use of AI for
> comments and code contributions**.[^elixir-contributing]

This is the clearest DCO statement in the bundle, and it resolves the question a third way. Where
[QEMU](qemu.md) reasons that a contributor *cannot* certify AI-generated work and prohibits it, and
[Dependency-Track](dependency-track.md) requires the human sign and the tool go unnamed, Elixir
separates the two acts: **the agent may write, only the human may certify**, and the certification is
what carries responsibility.

Note what it does *not* say. There is no prohibition on an AI co-author trailer and no required
attribution format — only that the sign-off is a human act. Disclosure is required *"for comments and
code contributions"*, with no form prescribed.

## Discussions, and the line through them

> When it comes to discussions, using AI to help express yourself is welcome, but **avoid directly
> copy and pasting AI generated content**. If there is a language barrier, use AI to translate,
> review, and improve your text, but **do not use AI to respond on your
> behalf**.[^elixir-contributing]

The translation carve-out again — [Nerves](nerves.md) and [Perl](perl.md) draw the same line — and
the same underlying distinction: **AI on your own words is assistance, AI instead of your words is
substitution.** The rule is a boundary rather than a ban, which is why it needs a human to apply it.

## `AGENTS.md` is a symlink, and that is the point

The repository's `AGENTS.md` is a **git symlink** to `CONTRIBUTING.md` — mode `120000`, added
2026-06-15 in a commit titled *"Symlink AGENTS.md to CONTRIBUTING.md"*.

Symlinking is the settled construction — [Asahi Linux](asahi-linux.md),
[Dependency-Track](dependency-track.md), [systemd](systemd.md), [NetworkManager](networkmanager.md)
and [Zed](zed.md) all do it. **What is distinctive here is the target.** The others point one
agent-facing filename at another; Elixir points the agent-facing filename at the **human-facing**
document, so an agent and a contributor are guaranteed to read the same text and the project
maintains one file rather than two. See [agent-file pointers](../mechanisms/agent-file-pointers.md).

## What a contributor must do

Use AI if you like, then ask whether what you are about to send is something the maintainer could
have generated themselves — they can. **Do not point an agent at an open issue unless it carries
"Contributions Welcome"**; get agreement on the mailing list first for anything else. If you are
automating changes to the compiler, type system, security or performance, **run adversarial agents
against your own change** and treat their approval as advice, not a verdict. Write your own
discussion posts; translate with AI if you need to, but do not let it reply for you. **Add your own
`Signed-off-by` and never let an agent add one.** Disclose AI use in comments and code.

## Re-verification notes

The policy lives in `CONTRIBUTING.md` under *"Using AI and coding agents"* and *"AI contributions"*.
**Read the repository copy** — `git log -- CONTRIBUTING.md` dates the first AI guidance to
2026-04-15 and the extension to 2026-05-04.

**Check that `AGENTS.md` is still a symlink** rather than assuming it: `git ls-tree main AGENTS.md`
shows mode `120000` today. If it is ever replaced by a regular file, the guarantee described above is
gone and the two documents can drift.

Watch the adversarial-pairing clause. It is the most demanding requirement in this bundle and the
hardest to verify from outside — a maintainer cannot tell from a diff whether the red team ran — so
whether it survives as written, gains an enforcement mechanism, or quietly relaxes is the most
informative thing this record can be re-read for.

[^elixir-contributing]: [Contributing to Elixir (CONTRIBUTING.md, elixir-lang/elixir, main) — Using AI and coding agents](https://raw.githubusercontent.com/elixir-lang/elixir/main/CONTRIBUTING.md)
