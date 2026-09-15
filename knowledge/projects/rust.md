---
type: Organization
title: Rust
description: Adopted an LLM usage policy for rust-lang/rust on 2026-08-05, and since 2026-09-15 lists six adopting repositories — rust, cargo, rustlings, mdBook, rustfmt and rust-clippy — still bound only to the five teams that ratified it, not the whole project. It allows LLMs to analyse but not create, bans LLM-created comments, docs and diagnostics, admits LLM-created code only under a bounded experiment with a circuit breaker, and says openly that many of its clauses are unenforceable. A project-wide committee could still supersede it.
resource: https://forge.rust-lang.org/policies/llm-usage.html
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - moderation
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T23:45:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T23:45:00Z'
  - by: claude/opus-5
    at: '2026-09-14T13:10:00Z'
  - by: claude/opus-5
    at: '2026-09-15T19:10:00Z'
stale_after: 2026-12-14
sources:
  - id: rust-llm-policy
    title: 'src/policies/llm-usage.md (rust-lang/rust-forge at 3eda0e9cfdd5)'
    resource: https://raw.githubusercontent.com/rust-lang/rust-forge/3eda0e9cfdd5059f7bccbd1e668c8a54ea5907f8/src/policies/llm-usage.md
  - id: rust-forge-1108
    title: 'Edit LLM policy — list adopting repositories (rust-lang/rust-forge#1108, merged 2026-09-15)'
    resource: https://github.com/rust-lang/rust-forge/pull/1108
  - id: rust-adopt-rust
    title: 'CONTRIBUTING.md (rust-lang/rust, main) — LLM policy section'
    resource: https://raw.githubusercontent.com/rust-lang/rust/main/CONTRIBUTING.md
  - id: rust-adopt-cargo
    title: 'CONTRIBUTING.md (rust-lang/cargo, master) — LLM policy section'
    resource: https://raw.githubusercontent.com/rust-lang/cargo/master/CONTRIBUTING.md
  - id: rust-adopt-rustlings
    title: 'CONTRIBUTING.md (rust-lang/rustlings, main) — LLM Usage Policy section'
    resource: https://raw.githubusercontent.com/rust-lang/rustlings/main/CONTRIBUTING.md
  - id: rust-adopt-mdbook
    title: 'CONTRIBUTING.md (rust-lang/mdBook, main) — LLM policy section'
    resource: https://raw.githubusercontent.com/rust-lang/mdBook/main/CONTRIBUTING.md
  - id: rust-adopt-rustfmt
    title: 'Contributing.md (rust-lang/rustfmt, main) — LLM policy section'
    resource: https://raw.githubusercontent.com/rust-lang/rustfmt/main/Contributing.md
  - id: rust-adopt-clippy
    title: 'CONTRIBUTING.md (rust-lang/rust-clippy, master) — LLM policy section'
    resource: https://raw.githubusercontent.com/rust-lang/rust-clippy/master/CONTRIBUTING.md
  - id: rust-forge-1040
    title: 'Add an LLM policy for `rust-lang/rust` (rust-lang/rust-forge#1040, merged 2026-08-05)'
    resource: https://github.com/rust-lang/rust-forge/pull/1040
  - id: rust-blog-adoption
    title: 'rust-lang/rust is adopting an LLM policy (Inside Rust Blog, Jynn Nelson, 2026-08-05)'
    resource: https://blog.rust-lang.org/inside-rust/2026/08/05/rust-langrust-is-adopting-an-llm-policy/
  - id: rust-rfc-3959
    title: 'Project-wide LLM policy (rust-lang/rfcs#3959, open)'
    resource: https://github.com/rust-lang/rfcs/pull/3959
  - id: rust-rfc-3950
    title: 'Add contribution policy for AI-generated work (rust-lang/rfcs#3950, closed)'
    resource: https://github.com/rust-lang/rfcs/pull/3950
---

**Stance: conditionally allowed in the repositories that have adopted it — six so far, all in
`rust-lang` — and nowhere else by this policy.** Pull request
rust-forge#1040, opened 2026-04-17, was merged on **2026-08-05** after 114 conversation comments and
reviews from dozens of participants.[^rust-forge-1040] The policy now lives on the Rust Forge. It
opens:

> Using LLMs while working on `rust-lang/rust`, and other repositories that have adopted this policy,
> is conditionally allowed, when done with care. LLMs are not a substitute for thought, and we do not allow them to be used in ways that risk losing our
> shared social and technical understanding of the project, nor in ways that hurt our goals of
> creating a strong community.[^rust-llm-policy]

**This record said "no adopted policy" when it was written on 2026-08-04. The merge came the next
day.** Its text had not changed between that reading and the merge — the file's history shows no
commit between 2026-07-20 and 2026-08-12 — so the rules described then were accurate; only their
status was wrong.

## Scope is the first thing to read

> This policy only applies to the repositories that have adopted it, and only to the teams that have
> ratified it: compiler, libs, types, rustdoc, bootstrap, and their subteams.[^rust-llm-policy]

**Until 2026-09-15 the first clause read *"only applies to `rust-lang/rust`"*.** That day PR 1108
generalised it and began listing adopters, noting that each already had text in its own contributing
guide.[^rust-forge-1108] All six were checked on 2026-09-15:

| Repository | Adoption text added to its contributing guide |
|---|---|
| `rust-lang/rust` | 2026-08-02 — three days before the Forge policy merged[^rust-adopt-rust] |
| `rust-lang/cargo` | 2026-08-08[^rust-adopt-cargo] |
| `rust-lang/rustlings` | 2026-08-11[^rust-adopt-rustlings] |
| `rust-lang/mdBook` | 2026-08-18[^rust-adopt-mdbook] |
| `rust-lang/rustfmt` | 2026-08-28, in `Contributing.md`[^rust-adopt-rustfmt] |
| `rust-lang/rust-clippy` | 2026-09-01[^rust-adopt-clippy] |

**So the policy spread repository by repository before its own text admitted it**, and the Forge page
caught up with the practice rather than leading it. The teams clause did not change: adoption widens
*where* the rules apply, not *who* ratified them.

Other `rust-lang` repositories, submodules, subtrees, crates.io dependencies, and teams that did not
ratify it — lang and edition are named — set their own policies. The announcement is explicit that
this is *"not an official stance on LLMs, and does not apply everywhere in the Rust
project"*.[^rust-blog-adoption]

**And it can be overtaken.** An earlier contribution-policy RFC was closed unmerged,[^rust-rfc-3950] a
project-wide policy is still an open RFC,[^rust-rfc-3959] and the policy
yields in advance: if a proposed LLM committee *"(or any similar dedicated project-wide body) is
formed, any policy it sets will take precedence over this policy."*[^rust-llm-policy] A contributor to
another Rust repository cannot assume this text applies, and a contributor here cannot assume it will
last.

## Why a policy, from a project that cannot agree

The announcement names three problems — polished work no longer signals effort, easier code
worsens review bandwidth (*"At the time of writing, there are 1,281 open PRs to
`rust-lang/rust`"*), and copy-pasting to and from a model wastes reviewers' time — and then explains
why the answer is a compromise rather than a stance:[^rust-blog-adoption]

> We do not have a benevolent dictator … Rust operates by consensus.

> Our choices are not "no policy" or "policy". Our choice is whether to have the policy be an
> unofficial list of moderation notes or something we stand by publicly.

The author adds, unusually, *"I do not think every rule in this policy is wholly good."* **A policy
adopted as the least-bad codification of moderation already happening** is a different artifact from
one adopted as a position, and this is the clearest instance of the first kind here.

## The rule, in one line

> It's fine to use LLMs to answer questions, analyze, distill, refine, check, suggest, review. But not
> to **create**.[^rust-llm-policy]

The policy grades uses with symbols, and the summary is compact:

| | |
|---|---|
| ✅ **Allowed** | private use — anything where you are the only one who sees the output — and clearly experimental PRs not meant for review |
| ❌ **Banned** | *"LLM-created comments, docs, or diagnostics. Replacing human judgement with LLM judgement. Requiring people to use an LLM to contribute."* |
| ⚠️ **With disclosure** | trivial changes, machine translation (*"allowed but discouraged"*), LLM-assisted bug discovery you personally verify, review bots, and LLM-created code under the experiment |
| 🔨 **Moderation penalty** | lying about LLM use |

The ban on comments covers issue bodies, PR descriptions and scripted voice or video, unless the model
output is *"clearly quoted and marked"* — and even then *"the content of the comment must stand on its
own even without the LLM content"*.[^rust-llm-policy] See
[prose reserved to humans](../mechanisms/prose-reserved-to-humans.md).

**Origin, not edit distance, decides.** *"No amount of editing can change how it was originally
created"*, and *"This policy makes no distinction between LLM output that comes from a chat interface
and output that comes from editor auto-completion."*[^rust-llm-policy]

## It concedes that it is unenforceable, and says why that is fine

> We are aware that many clauses in this policy are unenforceable. Our goal is *not* to catch every
> violation … Instead, our goal is to remove plausible deniability: to force a choice between
> following the policy and intentionally violating it.[^rust-llm-policy]

It cites anti-money-laundering compliance as the model. **That makes it a declaration rule rather than
a detection rule**, and the moderation section follows through: *"It's not your job to play
detective."* Then a sentence no other policy here writes down:

> Style is not evidence, and English-as-a-second-language speakers, neurodivergent people, and
> over-explainers are the most likely to be accused of writing like an LLM.[^rust-llm-policy]

That is the false-positive cost of a style test like [Git](git.md)'s, named by a project choosing not
to run one. Lying is the only clause that carries a Code of Conduct penalty — a warning, then a
possible ban — and harassing someone for using an LLM is ruled out in the same section.

## Two rules about the project, not the contributor

**Documentation must be written for humans.** A process may not be written *"such that an LLM is
required to execute them"*: *"you must not *only* document where tests live with an `AGENTS.md`.
Documentation must be authored for humans primarily, and LLM documentation may only summarize it, not
add new detail."*[^rust-llm-policy] A rule against a codebase drifting into a state only a machine can
navigate.

**Review bots are regulated, not banned.** They must be approved once by a maintainer, post from *"a
separate GitHub account that clearly marks them as an LLM"*, be blockable through ordinary GitHub
user-blocking, and never block a PR — *"reviewers must explicitly endorse an LLM comment before
blocking a PR"*, and cannot treat it as a CI failure.[^rust-llm-policy]

## LLM-created code: an experiment with a circuit breaker

Code *"originally created by an LLM"* is allowed only if it is **pre-arranged, non-critical,
high-quality, well-tested and well-reviewed, with disclosure**.[^rust-llm-policy] Pre-arranged means
a reviewer agreed before the PR was opened, and *"This must be the *same* reviewer who will be
assigned"*. Non-critical rules out soundness-sensitive areas such as *"the trait system, MIR building,
or the query system"*. Well-tested means *"a higher standard than human-created PRs, because LLMs make
it easier to write tests"*. Organisation members may ignore the non-critical clause, but are *"strongly
discouraged"* from doing so.

Every such PR carries an `llm-assisted` label and is posted to a private Zulip channel whose purpose
is to learn *whether the experiment is working*, not to gatekeep. And the experiment has a stop:

> If more than half of PRs merged in a 6-week window are LLM-created, we disallow merging new
> LLM-created PRs until we go back below 50%, with a minimum cooldown of 10 days.[^rust-llm-policy]

**No other record here caps AI-created work as a share of merges.** [Homebrew](homebrew.md) caps how
many AI-assisted pull requests one person may have open; Rust caps the proportion the project accepts.
The window matches the release cycle, and the policy *"strongly suggests"* automating the breaker to
avoid inconsistent enforcement.

## How it changes

Minor edits need an ordinary approval; a new or cancelled rule needs a Major Change Proposal from
**each** ratifying team. It can be dissolved by those teams, by a leadership council decision on
evidence of harm, or by the project-wide committee described above.[^rust-llm-policy] Post-merge edits
were small at first: a label name corrected on 2026-08-12 and wording changes on 2026-08-13 and
2026-08-14. On 2026-09-15 PR 1108 widened the scope wording and added the adopters list, merged with
one approving review — the procedure the policy sets for minor changes, not a Major Change Proposal.[^rust-forge-1108]

## What a contributor must do

Use an LLM privately as much as you like. Do not post its words as your own — not comments, PR
descriptions, docs, doc-comments or diagnostics. Disclose trivial changes, translations, LLM-found
bugs and review-bot output. For LLM-created code, find and agree with your reviewer **before** opening
the PR, stay out of soundness-critical areas, test beyond the usual bar, and expect the label. Never lie about it. This applies in the six adopting
repositories; everywhere else in the Rust project, check that repository's own rules.

## Re-verification notes

**Check RFC 3959 and the LLM committee first**, because either can supersede this record outright.
Then read the source file at the Forge's current commit rather than the rendered page; its history
dates every change. **Check the adopters list against each repository's contributing guide** — and
list the repository's files rather than guessing a filename: rustfmt's guide is `Contributing.md`,
which a probe for `CONTRIBUTING.md` misses. `stale_after` is three months for those reasons.

[^rust-llm-policy]: [src/policies/llm-usage.md (rust-lang/rust-forge at 3eda0e9cfdd5)](https://raw.githubusercontent.com/rust-lang/rust-forge/3eda0e9cfdd5059f7bccbd1e668c8a54ea5907f8/src/policies/llm-usage.md)
[^rust-forge-1040]: [Add an LLM policy for `rust-lang/rust` (rust-lang/rust-forge#1040, merged 2026-08-05)](https://github.com/rust-lang/rust-forge/pull/1040)
[^rust-blog-adoption]: [rust-lang/rust is adopting an LLM policy (Inside Rust Blog, Jynn Nelson, 2026-08-05)](https://blog.rust-lang.org/inside-rust/2026/08/05/rust-langrust-is-adopting-an-llm-policy/)
[^rust-rfc-3959]: [Project-wide LLM policy (rust-lang/rfcs#3959, open)](https://github.com/rust-lang/rfcs/pull/3959)
[^rust-rfc-3950]: [Add contribution policy for AI-generated work (rust-lang/rfcs#3950, closed)](https://github.com/rust-lang/rfcs/pull/3950)
[^rust-forge-1108]: [Edit LLM policy — list adopting repositories (rust-lang/rust-forge#1108, merged 2026-09-15)](https://github.com/rust-lang/rust-forge/pull/1108)
[^rust-adopt-rust]: [CONTRIBUTING.md (rust-lang/rust, main) — LLM policy section](https://raw.githubusercontent.com/rust-lang/rust/main/CONTRIBUTING.md)
[^rust-adopt-cargo]: [CONTRIBUTING.md (rust-lang/cargo, master) — LLM policy section](https://raw.githubusercontent.com/rust-lang/cargo/master/CONTRIBUTING.md)
[^rust-adopt-rustlings]: [CONTRIBUTING.md (rust-lang/rustlings, main) — LLM Usage Policy section](https://raw.githubusercontent.com/rust-lang/rustlings/main/CONTRIBUTING.md)
[^rust-adopt-mdbook]: [CONTRIBUTING.md (rust-lang/mdBook, main) — LLM policy section](https://raw.githubusercontent.com/rust-lang/mdBook/main/CONTRIBUTING.md)
[^rust-adopt-rustfmt]: [Contributing.md (rust-lang/rustfmt, main) — LLM policy section](https://raw.githubusercontent.com/rust-lang/rustfmt/main/Contributing.md)
[^rust-adopt-clippy]: [CONTRIBUTING.md (rust-lang/rust-clippy, master) — LLM policy section](https://raw.githubusercontent.com/rust-lang/rust-clippy/master/CONTRIBUTING.md)
