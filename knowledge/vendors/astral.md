---
type: Organization
title: Astral
description: Publishes the origin of the only attributed policy lineage in this bundle, as an organisation-wide default that every one of its repositories inherits and none overrides. It is the one vendor here whose policy binds contributors rather than staff, it justifies its human-in-the-loop rule by the criticality of what it maintains, and it is joining an AI lab while forbidding autonomous agents.
resource: https://github.com/astral-sh/.github/blob/main/AI_POLICY.md
tags:
  - ai-contribution
  - policy
  - vendor
  - permitted
  - restricted
  - communication
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:29:44Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:29:44Z'
stale_after: 2027-03-08
sources:
  - id: astral-policy
    title: 'AI Policy (AI_POLICY.md, astral-sh/.github, main)'
    resource: https://raw.githubusercontent.com/astral-sh/.github/main/AI_POLICY.md
  - id: astral-uv-contributing
    title: 'Contributing (CONTRIBUTING.md, astral-sh/uv, main)'
    resource: https://raw.githubusercontent.com/astral-sh/uv/main/CONTRIBUTING.md
  - id: astral-site
    title: 'Astral — High-performance Python tooling (astral.sh)'
    resource: https://astral.sh
---

**Stance: permitted for code, autonomous agents refused, all maintainer-facing prose reserved to
humans — published once and inherited everywhere.** Astral's policy lives in `astral-sh/.github`,
the repository GitHub uses for organisation-wide defaults, added **2026-03-13** as its first commit.

It is one of **three** files in that repository. The other two are `CODE_OF_CONDUCT.md` and
`SECURITY.md`. Whatever else Astral chose not to standardise across 86 repositories, it standardised
this.

## Inherited, not copied — and no project overrides it

Checked 2026-09-08 across the flagship repositories: **none carries its own `AI_POLICY.md`.**

| Repository | Stars | Own policy | `CONTRIBUTING.md` points at it |
|---|---|---|---|
| `uv` | 89,632 | inherits | yes |
| `ruff` | 49,551 | inherits | yes |
| `ty` | 19,645 | inherits | no |
| `rye` | 14,158 | inherits | no |
| `python-build-standalone` | 4,393 | inherits | no |

**One text, no drift, because there is only one copy.** That is the opposite arrangement to
[OWASP](../foundations/owasp.md), whose projects each answered the question separately and disagree,
and it is what an inherited floor looks like when it is actually inherited.

The pointer, where it exists, is terse and identical between `uv` and `ruff`: *"We **require all use
of AI in contributions to follow our [AI Policy]**. If your contribution does not follow the policy,
it will be closed."*[^astral-uv-contributing] **Three of the five surface no link at all** — the
org-level default still governs them, but a contributor reading only that repository's
`CONTRIBUTING.md` would not learn the policy exists.

## The criticality argument, which nobody else makes

> **Due to the foundational nature of our projects**, we require a human in the loop who understands
> the work produced by AI. **We do not allow autonomous agents to be used for contributing to our
> projects.** We will close any pull requests that we believe were created
> autonomously.[^astral-policy]

Every other project barring autonomous agents argues from review cost, provenance or accountability.
This argues from **what depends on the code**. `uv` and `ruff` sit under a large share of the Python
ecosystem's builds, and the claim is that the blast radius sets the bar — a position that would
justify a *different* answer for a less load-bearing project, and does not pretend otherwise.

It pairs with a responsibility clause stated in both directions, the sentence
[ripgrep](../projects/ripgrep.md) kept:

> **You remain responsible for any code you publish and we are responsible for any code we merge and
> release.**[^astral-policy]

## The rest of the text, and what its borrowers did with it

The remaining clauses are the ones the lineage carried:

- **Prose to humans**, sanctioned by hiding rather than closing — *"We may hide any comments that we
  believe are AI generated"* — and reaching issues, pull-request bodies and replies alike.
- **Quoted model output** must be in a quote block, disclosed, accompanied by human commentary on its
  relevance, and *"do not share long snippets."*
- **Translation** is welcomed with a voice test — *"please take the time to ensure it reflects your
  own voice and ideas"* — recommending you write in your native language and quote the machine
  output.[^astral-policy]

**This is the head of a four-hop chain**, three hops of which cite their source:

| | Date | Change made |
|---|---|---|
| **Astral** | 2026-03-13 | the original, organisation-scoped |
| [ripgrep](../projects/ripgrep.md) | 2026-05-26 | *"s/our projects/this project"*; added *"perhaps without notice"*; **dropped the criticality argument** |
| [Zed](../projects/zed.md) | 2026-08-21 | adapted again, cites ripgrep |
| [systemd](../projects/systemd.md) | 2026-09-03 | the canary only, unattributed, without its check |

ripgrep pinned its citation to a commit, and that pin was compared against this text on 2026-09-08
and found **byte-identical** — the policy has not moved since it began being copied.

**ripgrep also copied the `CONTRIBUTING.md` stub**, not just the policy: Astral's *"require all use of
AI … it will be closed"* becomes ripgrep's *"All use of AI in contributions must follow the AI Policy.
Contributions not following the AI Policy will be closed."* The delivery pattern travelled with the
text.

## The one vendor here whose policy binds the reader

The three other `vendors/` records — [Canonical](canonical.md), [Red Hat](red-hat.md),
[SUSE](suse.md) — publish policies for their **own employees**, and the [overview](../overview.md)
described this as the category where the policy *does not bind the reader*. **Astral breaks that.**
Its policy governs anyone opening a pull request against `uv` or `ruff`, employee or not.

It is filed here because the bundle files by **what an organisation is**, and Astral is a company, not
a project or a foundation. But the category now contains two different kinds of document, and the
distinction that matters to a reader is not who published it — it is **who it binds**.

## A fact recorded because it is checkable, not because it resolves anything

Astral's own site leads with *"Astral to join OpenAI as part of the Codex team"*,[^astral-site] and its
GitHub organisation describes itself as *"High-performance developer tools for the Python ecosystem,
from @OpenAI."*

**So the author of the most-copied AI contribution policy in this bundle is being acquired by an AI
lab, while forbidding autonomous agents in its own repositories.** No inference is drawn here about
whether the policy will change — the acquisition is an event, the policy is a text, and the text was
byte-identical to its 2026-03-13 original when checked. It is recorded because it is the single most
likely cause of this record needing to be re-read.

## What a contributor must do

Use an LLM to write code, and stay in the loop — **a pull request Astral believes was created
autonomously will be closed.** Describe issues in your own words; explain your pull request in your
own words, including replies to questions. Do not paste model output as a reply. If you quote model
output, use a quote block, say what it is, explain why it matters, and keep it short. If English is
not your first language, translate freely, but make sure the result is your voice. **The policy is not
in the repository you are contributing to** — it is one level up, in `astral-sh/.github`, and applies
whether or not that project's `CONTRIBUTING.md` mentions it.

## Re-verification notes

**One file governs 86 repositories.** `astral-sh/.github/AI_POLICY.md` is the only copy;
`git log` on it showed a single commit, *"Add an AI policy (#1)"*, 2026-03-13, when checked. A second
commit there would change the policy for every Astral project at once, and would silently invalidate
[ripgrep](../projects/ripgrep.md)'s currency claim, which rests on the pinned text still matching.

**Do not check a project repository to answer this.** None carries its own policy and three of five
do not link to it, so a per-repository sweep returns a false negative. Check the `.github`
repository.

Watch three things. Whether the OpenAI acquisition changes the text — an autonomous-agent prohibition
published by a subsidiary of an agent vendor is a position with visible tension, whatever its merits.
Whether the pointer stubs spread to the repositories that lack them. And whether any Astral project
ever overrides the default, which is the first thing that would turn this from a floor into a
starting point.

[^astral-policy]: [AI Policy (AI_POLICY.md, astral-sh/.github, main)](https://raw.githubusercontent.com/astral-sh/.github/main/AI_POLICY.md)
[^astral-uv-contributing]: [Contributing (CONTRIBUTING.md, astral-sh/uv, main)](https://raw.githubusercontent.com/astral-sh/uv/main/CONTRIBUTING.md)
[^astral-site]: [Astral — High-performance Python tooling (astral.sh)](https://astral.sh)
