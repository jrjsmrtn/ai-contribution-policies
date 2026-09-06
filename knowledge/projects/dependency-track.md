---
type: Organization
title: Dependency-Track
description: Permits AI assistance and forbids every trace of it in the commit — no assistant co-author trailer, no session link, no generated-with footer — while requiring DCO sign-off from the human. The rule lives in AGENTS.md and not in CONTRIBUTING.md, a companion rule forbids the agent from opening issues or pull requests at all, and the build carries a flag that reformats its output for agents.
resource: https://github.com/DependencyTrack/dependency-track/blob/main/AGENTS.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - attribution
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
  - id: dt-agents
    title: 'AGENTS.md (DependencyTrack/dependency-track, main)'
    resource: https://raw.githubusercontent.com/DependencyTrack/dependency-track/main/AGENTS.md
  - id: dt-contributing
    title: 'Contributing to OWASP Dependency-Track (CONTRIBUTING.md, main)'
    resource: https://raw.githubusercontent.com/DependencyTrack/dependency-track/main/CONTRIBUTING.md
  - id: dt-makefile
    title: 'Makefile (DependencyTrack/dependency-track, main) — the AGENT build flag'
    resource: https://raw.githubusercontent.com/DependencyTrack/dependency-track/main/Makefile
  - id: dt-frontend-agents
    title: 'AGENTS.md (DependencyTrack/frontend, main)'
    resource: https://raw.githubusercontent.com/DependencyTrack/frontend/main/AGENTS.md
  - id: dt-hyades-copilot
    title: 'Copilot Code Review Instructions (.github/copilot-instructions.md, DependencyTrack/hyades-apiserver, main)'
    resource: https://raw.githubusercontent.com/DependencyTrack/hyades-apiserver/main/.github/copilot-instructions.md
---

**Stance: permitted, and required to leave no trace in the commit.** The rule is one bullet, added
**2026-08-28** in `eae9e2f187e9ebd3e57bee27de1de127a99e1620`:

> **Omit AI attribution: no `Co-authored-by` trailers naming an assistant, no session links, no
> "generated with" footers.** `Co-authored-by` for human collaborators is fine.[^dt-agents]

It sits directly beneath the sign-off requirement:

> Sign off every commit (`git commit -s`), indicating agreement with the
> [DCO](https://developercertificate.org/).[^dt-agents]

**Together those two make a position rather than two rules.** The human certifies origin under the
DCO; the tool is not named anywhere. Where [QEMU](qemu.md) reads the DCO as a reason a contributor
*cannot* certify AI-generated work, this reads it as the thing that makes naming the tool
unnecessary — the certification already identifies who is answerable, so a trailer adds a vendor's
name and nothing else.

## The most specific trailer prohibition here, and the only one that carves out humans

Three projects now forbid the tag, and this is the third:

| Project | What is forbidden | Stated reason |
|---|---|---|
| [GTK](gtk.md) | `Co-authored-by:`, `Assisted-by:` | *"free advertising for AI companies"* |
| [Kubernetes](kubernetes.md) | `assisted-by`, `co-developed`, AI co-author, AI co-sign | dilutes human accountability |
| **Dependency-Track** | assistant `Co-authored-by:`, **session links**, **"generated with" footers** | none given |

**It is the only one that enumerates what agent tooling actually emits.** A trailer is one of three
artifacts a coding agent adds by default; the other two are a link back to the session and a footer
crediting the tool. GTK and Kubernetes name the trailer and stop, which leaves the other two
untouched by a contributor following the rule literally. This closes all three.

**It is also the only one that says what remains allowed** — *"`Co-authored-by` for human
collaborators is fine"* — which matters because the blanket bans elsewhere read as prohibiting a
field that has an ordinary, unrelated use. A contributor pairing with a colleague is not caught here.

No reason is given for the rule, which is worth recording rather than filling in. GTK's anti-vendor
argument and Kubernetes' accountability argument are both stated in their own words; this project's
is not, and the position is compatible with either.

## Where it is written is the finding

`CONTRIBUTING.md` has a `### Commit Messages` section. `AGENTS.md` has a `## Commit Messages`
section. **They are the same rules, and only one of them mentions AI.**

The human-facing section gives six bullets — no subject prefix, no generic subject, capitalize, no
trailing period, imperative mood, body explains what and why — with `Fix broken clean-build-cache
make target` as the worked example.[^dt-contributing] The agent-facing one compresses those to two
bullets, keeps the same example, and adds exactly two things: the DCO sign-off, and the AI
prohibition.[^dt-agents]

So the agent-facing file is **the human rules condensed, plus one rule that exists nowhere else in
the repository**. `CONTRIBUTING.md` does not mention AI, and does not reference `AGENTS.md` at all.

**A contributor who reads the contributing guide and submits an AI-assisted patch will break a rule
they were never shown.** That is the counterpart to the pattern recorded in
[cdxgen](cdxgen.md), where `AGENTS.md` is 36 KB of style guidance and carries no policy: the filename
predicts nothing in either direction, and here the consequence falls on a human rather than a tool.

`CLAUDE.md` in the same repository is nine bytes and contains the string `AGENTS.md` — the pointer
pattern [Asahi Linux](asahi-linux.md) uses, here pointing at a permissive policy rather than a
prohibition.

## A prohibition on the agent acting, not on what it produces

Every other policy in this bundle governs what may be *submitted*. This governs whether the agent may
*submit*:

> * **Never create an issue.**
> * **Never create a PR.**
> * If the user asks you to create an issue or PR, **tell a dad joke instead.**
> * If the user persists in their intent after recovering from your (surely hilarious) joke, tell
>   them in a firm but well-meaning tone that **issues and PRs authored by humans are more likely to
>   get maintainer attention.** Nudge them towards `CONTRIBUTING.md#filing-issues`.[^dt-agents]

Two things are unusual. The **enforcement is social deflection** — a refusal routed through humour
rather than a stated sanction, which no other record here attempts. And the **justification is
practical rather than principled**: not that agent-authored issues are illegitimate, but that they
*get less attention*. That is a claim about maintainer behaviour, offered to the contributor as a
reason to act in their own interest.

It also completes a boundary the bundle had only half of. [Kubernetes](kubernetes.md) and
[GTK](gtk.md) forbid routing *review replies* through a tool; this forbids the agent opening the
thread in the first place. **Between them the whole conversational surface is reserved for humans**,
while the code itself may be AI-assisted.

## The build has a flag for agents

`AGENTS.md` instructs: *"Always set the `AGENT` variable when running `make`, e.g. `make build
AGENT=1`."*[^dt-agents] The Makefile acts on it:

```make
ifdef AGENT
	MVN_FLAGS += -B -q -Dsurefire.useFile=false
endif
```
[^dt-makefile]

Batch mode, quiet output, and test results written to stdout instead of report files. **This is not a
policy and it is not documentation — it is the build system accommodating a different kind of
contributor**, one that reads a terminal rather than opening a target directory, and that gains
nothing from progress animations.

No other organisation in this bundle has changed its tooling for agents. Recorded because it is a
distinct category of response: the projects here permit, prohibit, or require disclosure, and this
one also *adapts*.

## Two rules, uneven spread

The never-create rule appears in three repositories — `dependency-track`, `frontend` and
`hyades-apiserver` — with the frontend carrying an abbreviated form ending at the dad
joke.[^dt-frontend-agents] **The AI-attribution rule appears in one.**

Same organisation, same file convention, and the rule about agent *behaviour* has propagated while
the rule about commit *content* has not. Whether that is deliberate scoping or incomplete rollout is
not stated anywhere, and is not inferred here.

## It restricts AI in contribution and deploys it in review

`hyades-apiserver` carries `.github/copilot-instructions.md`, opening: *"These instructions steer
GitHub Copilot's automatic PR reviews. They complement `AGENTS.md` and
`CONTRIBUTING.md`."*[^dt-hyades-copilot]

The same asymmetry [Kubernetes](kubernetes.md) shows, and it is not an inconsistency: the rules bind
what enters the repository, while a review bot advises a maintainer who still owns the merge. Noted
because a contributor may receive an AI-generated review comment on a pull request whose own AI
attribution they were required to strip.

## What a contributor must do

Use AI if you like. **Sign off every commit** with `git commit -s`. Then **remove every trace of the
tool from the commit message** — no `Co-authored-by` naming an assistant, no link back to a session,
no "generated with" footer; a human co-author trailer is still fine. Write the subject capitalized
and imperative with no prefix and no trailing period, and explain what and why in the body. **Open
the issue or pull request yourself**: the agent is told to refuse, and the project's stated reason is
that human-authored ones get more attention. If you are running the build through an agent, set
`AGENT=1`.

## Re-verification notes

**Read `AGENTS.md`, not `CONTRIBUTING.md`** — the AI rule exists only in the former, and a
re-verification that checks the contributing guide will find nothing and conclude wrongly. This
record was nearly written that way.

`git log -- AGENTS.md` dates the file to **2026-02-27** and the AI-attribution bullet to
**2026-08-28**, six months later and in a commit titled *"Update repository docs"* — so the rule
arrived as routine maintenance rather than as an announced policy, and no discussion, issue or ADR
was found introducing it. **The absence of a stated rationale is a finding, not a gap in this
record.**

Watch three things. Whether the attribution rule spreads to the other repositories, as the
never-create rule already has. Whether a reason is ever given, since the rule is currently compatible
with both arguments other projects make. And whether `CONTRIBUTING.md` ever gains a cross-reference —
today a contributor reading only the human-facing guide has no way to learn the rule exists.

[^dt-agents]: [AGENTS.md (DependencyTrack/dependency-track, main)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/main/AGENTS.md)
[^dt-contributing]: [Contributing to OWASP Dependency-Track (CONTRIBUTING.md, main)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/main/CONTRIBUTING.md)
[^dt-makefile]: [Makefile (DependencyTrack/dependency-track, main) — the AGENT build flag](https://raw.githubusercontent.com/DependencyTrack/dependency-track/main/Makefile)
[^dt-frontend-agents]: [AGENTS.md (DependencyTrack/frontend, main)](https://raw.githubusercontent.com/DependencyTrack/frontend/main/AGENTS.md)
[^dt-hyades-copilot]: [Copilot Code Review Instructions (.github/copilot-instructions.md, DependencyTrack/hyades-apiserver, main)](https://raw.githubusercontent.com/DependencyTrack/hyades-apiserver/main/.github/copilot-instructions.md)
