---
type: Practice
title: Policy by copying
description: Most AI contribution policies here were adapted from another project's. Six copying events are dated and traceable, and what a copy drops is the enforcement, the currency and the clauses that cost something. A policy turns out to be an artifact with a supply chain, exhibiting unattributed reuse, licence ambiguity, a stale upstream and no notification channel. Two borrowers pin their citation to a commit SHA and the two pins behave oppositely, which is the honest account of what a pin buys — reproducibility, not correctness.
resource: https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md
tags:
  - ai-contribution
  - mechanism
  - policy-design
  - attribution
  - licensing
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-10T11:05:00Z'
verified:
  - by: claude/opus-5
    at: '2026-09-10T11:05:00Z'
stale_after: 2027-03-10
sources:
  - id: cp-ripgrep
    title: 'AI_POLICY.md — ripgrep AI policy (BurntSushi/ripgrep, master)'
    resource: https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md
  - id: cp-zed
    title: 'CONTRIBUTING.md (zed-industries/zed, main)'
    resource: https://raw.githubusercontent.com/zed-industries/zed/main/CONTRIBUTING.md
  - id: cp-systemd
    title: 'AGENTS.md (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md
  - id: cp-llvm
    title: 'LLVM AI Tool Use Policy (llvm/docs/AIToolPolicy.md, main)'
    resource: https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/docs/AIToolPolicy.md
  - id: cp-gnome-loupe
    title: 'Loupe no longer allows generative AI contributions (GNOME Discourse, 2025-02-26)'
    resource: https://discourse.gnome.org/t/loupe-no-longer-allows-generative-ai-contributions/27327
  - id: cp-macports
    title: 'macports-base pull request 420 — diff'
    resource: https://patch-diff.githubusercontent.com/raw/macports/macports-base/pull/420.diff
  - id: cp-kernel-rendered
    title: 'Coding assistants — Linux kernel documentation (rendered, released kernel)'
    resource: https://docs.kernel.org/process/coding-assistants.html
  - id: cp-gcc
    title: 'GCC AI policy'
    resource: https://gcc.gnu.org/ai-policy.html
---

**Very few of these policies were written from scratch.** Six copying events in this bundle are
dated and traceable, and reading them together says more about how a rule spreads than any single
record does: **what survives a copy is the prohibition, and what is dropped is the machinery that
made it work.**

## The six events

| Source | Borrower | Date | Attributed | What was dropped |
|---|---|---|:--:|---|
| Astral (`astral-sh/.github`, org default) | [ripgrep](../projects/ripgrep.md) | 2026-05-26 | ● SHA-pinned | scope — *"our projects"* → *"this project"* |
| [ripgrep](../projects/ripgrep.md) | [Zed](../projects/zed.md) | 2026-08-21 | ● SHA-pinned | — (but pinned to a superseded revision) |
| [Zed](../projects/zed.md) | [systemd](../projects/systemd.md) | 2026-09-03 | ○ | the canary's **check**, and the prose clause |
| [Fedora](../distributions/fedora.md) policy proposal | [LLVM](../projects/llvm.md) | — | ● licence-required | — (a partial view; the source is unpublished) |
| GNOME Loupe | ~a dozen GNOME modules | from 2025-02-26 | ◐ some | currency — the copies diverged |
| Linux kernel docs (rendered) | [MacPorts](../projects/macports.md) PR #420 | 2026-08-04 | ● cited | currency — the source had retired the rule |

● attributed · ◐ some copies attribute · ○ unattributed

The first three are one chain — **the only fully attributed lineage here**, four hops, each borrower
naming its lender until the last. Zed's credit is a single sentence: *"This policy was adapted from
[ripgrep's AI policy]"*, linked to an exact commit.[^cp-zed] ripgrep's own adaptation is visible as
one edit — it landed the policy and, the same day, committed *"s/our projects/this project in AI
policy"*, which turns an organisation-wide text into one project's rule. **That edit is where Zed's
pin lands on the wrong side**, as the next section shows.

## What a copy loses

**Enforcement is the first thing to go.** [systemd](../projects/systemd.md) took Zed's review canary
verbatim and did not take the CI job that checks it — the marker string appears in exactly one
file.[^cp-systemd] A canary nobody greps for is a canary that detects only what a reviewer would have
caught anyway; the detail is in [the review canary](review-canary.md).

**Then the clauses that cost something.** systemd also dropped the prose rule that the first three
hops all carry, keeping the attribution ban instead — see
[prose reserved to humans](prose-reserved-to-humans.md). A borrower takes the parts that are cheap to
state and leaves the parts that impose work.

**Then currency.** MacPorts cited `docs.kernel.org`, which renders a *released* kernel rather than
mainline, and so reproduced an attribution format the kernel had replaced **the day
before**.[^cp-macports] [^cp-kernel-rendered] The GNOME copies diverged too: the Loupe original does
not name Ollama, `libadwaita` added it on 2025-07-11 and five siblings carry it while the rest do
not. **A policy propagated by copy-paste diverges on exactly the detail a contributor needs** —
whether their tool is named — and nothing reconciles the copies.

**No carelessness is implied by any of this.** MacPorts cited a canonical-looking URL on the
project's own domain, which is what a careful person does. *What went wrong is that the URL was
stale, not that the author was.*

## Licensing decides whether a policy is adoptable or merely readable

This is the dimension the records only touch individually, and it splits three ways:

- **Explicitly free.** [GCC](../projects/gcc.md)'s policy is marked *"CC0 1.0 Universal"*[^cp-gcc] —
  the only policy here carrying an explicit public-domain dedication. ripgrep's repository is
  **Unlicense**, so Zed faced no attribution obligation and attributed anyway.
- **Attribution-bearing.** [LLVM](../projects/llvm.md) copied from Fedora's proposal, *"licensed
  under the Creative Commons Attribution 4.0 International License. This link serves as
  attribution."*[^cp-llvm] The only case here where the credit was **owed** rather than offered.
- **Unstated**, which is most of them. A `CONTRIBUTING.md` inherits its repository's licence, and a
  project's code licence is rarely a sensible licence for prose. Nobody has raised this, and every
  borrower above proceeded regardless.

**The LLVM case is the sharpest**, because the licence did work no other mechanism could: Fedora's
policy is in force and **unpublished**, so LLVM's attributed excerpt is the only view of that text
this bundle can reach. Licensing made a document readable that governance had not made public.

## Two pins, behaving oppositely

**Two of the six pin their citation to a commit SHA**, and comparing them is the most useful thing in
this concept, because they demonstrate both halves of what a pin does.

| Borrower | Pins | Pinned revision | Against the source today |
|---|---|---|---|
| [ripgrep](../projects/ripgrep.md) | `astral-sh/.github` `c5187e20…`[^cp-ripgrep] | still current | **byte-identical** (compared 2026-09-10) |
| [Zed](../projects/zed.md) | `BurntSushi/ripgrep` `f0cec341…`[^cp-zed] | **superseded** | differs — *"our projects"* vs *"this project"* |

**Zed pinned the wrong revision, and the pin is what makes that visible.** ripgrep added
`AI_POLICY.md` at `f0cec341`, `2026-05-26T04:02:44Z`, carrying Astral's organisation-wide wording
unedited; it corrected that to *"this project"* **8 hours 33 minutes later**, at `4857d6fa`,
`2026-05-26T12:36:15Z`. Zed adopted the policy on 2026-08-21 — three months after the fix — and
pinned the pre-fix commit.

Nothing turns on the three words. What the case establishes is the general property: **a pin
guarantees your reference resolves to the same bytes forever, and guarantees nothing about whether
those bytes are the ones the source stands behind.** ripgrep's pin happens to be to a live revision;
Zed's happens to be to a dead one; neither borrower can tell without comparing, and **neither is
notified**.

Everyone else cites a branch, a rendered page, or nothing. **MacPorts is what that costs**, and it
cost only a day's drift.

## The diffusion is social or organisational, never institutional

**GNOME is the clearest case and it bypassed the centre entirely.** One maintainer wrote a text for
Loupe, proposed it fleet-wide on Discourse — *"I'm in favor of adopting a similar policy for all
official GNOME software"*[^cp-gnome-loupe] — and a dozen modules copied it. **The GNOME handbook was
never amended and still says nothing.**

Astral is the opposite shape and equally non-institutional: an org-level default in
`astral-sh/.github` that every repository inherits and none overrides. Not a governance document
telling projects what to do — a file that applies unless someone shadows it.

**No project in this bundle acquired its AI policy through its own governance process except by
voting on one** ([Debian](../distributions/debian.md)) or by a board issuing one
([Asahi Linux](../projects/asahi-linux.md)). Everywhere else the rule arrived sideways.

## A policy is an artifact with a supply chain

Every failure mode this bundle's neighbours document in software shows up here, in prose:

| Software supply-chain failure | Its form in these six events |
|---|---|
| unattributed reuse | systemd taking Zed's canary without saying so |
| licence ambiguity | most policies carrying no stated licence for their text |
| a stale upstream | MacPorts copying from a rendered page a day out of date |
| a patch dropped in a fork | systemd taking the canary and leaving the check |
| no notification channel | none of the six can learn its source changed |
| a pinned dependency | ripgrep's SHA — the one case where drift is detectable |

That is not an analogy stretched for effect. **These documents are copied, adapted, licensed,
attributed and left to rot exactly like the code they govern**, and the practices that would help are
the ones the projects already apply to dependencies.

## What to watch

Whether GCC's CC0 policy acquires a borrower — it is licensed for copying and no copy is recorded
here. **Whether Zed repoints its pin**, which would be the first instance of a policy citation being
*maintained* rather than merely placed. Whether a third project pins at all. And whether the
rendered-docs hazard catches anyone else, since `docs.kernel.org` still serves the retired form.

[^cp-ripgrep]: [AI_POLICY.md — ripgrep AI policy (BurntSushi/ripgrep, master)](https://raw.githubusercontent.com/BurntSushi/ripgrep/master/AI_POLICY.md)
[^cp-zed]: [CONTRIBUTING.md (zed-industries/zed, main)](https://raw.githubusercontent.com/zed-industries/zed/main/CONTRIBUTING.md)
[^cp-systemd]: [AGENTS.md (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/AGENTS.md)
[^cp-llvm]: [LLVM AI Tool Use Policy (llvm/docs/AIToolPolicy.md, main)](https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/docs/AIToolPolicy.md)
[^cp-gnome-loupe]: [Loupe no longer allows generative AI contributions (GNOME Discourse, 2025-02-26)](https://discourse.gnome.org/t/loupe-no-longer-allows-generative-ai-contributions/27327)
[^cp-macports]: [macports-base pull request 420 — diff](https://patch-diff.githubusercontent.com/raw/macports/macports-base/pull/420.diff)
[^cp-kernel-rendered]: [Coding assistants — Linux kernel documentation (rendered, released kernel)](https://docs.kernel.org/process/coding-assistants.html)
[^cp-gcc]: [GCC AI policy](https://gcc.gnu.org/ai-policy.html)
