---
type: Organization
title: Rust
description: Has no adopted policy; an unusually developed draft for rust-lang/rust is open, permitting LLMs to analyse but not create, with a disclosure tier and a bounded experiment for LLM-created code.
resource: https://github.com/rust-lang/rust-forge/pull/1040
tags:
  - ai-contribution
  - policy
  - project
  - undecided
  - draft
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T23:45:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T23:45:00Z'
stale_after: 2026-11-04
sources:
  - id: rust-forge-1040
    title: 'Add an LLM policy for `rust-lang/rust` (rust-lang/rust-forge#1040)'
    resource: https://github.com/rust-lang/rust-forge/pull/1040
  - id: rust-rfc-3959
    title: 'Project-wide LLM policy (rust-lang/rfcs#3959)'
    resource: https://github.com/rust-lang/rfcs/pull/3959
  - id: rust-rfc-3950
    title: 'Add contribution policy for AI-generated work (rust-lang/rfcs#3950, closed)'
    resource: https://github.com/rust-lang/rfcs/pull/3950
---

**Stance: undecided — nothing adopted, but the draft is the most developed in this bundle.** As of
2026-08-04 Rust has **no merged LLM policy**. Three attempts are on record: RFC 3950 (closed,
unmerged)[^rust-rfc-3950], RFC 3959 *"Project-wide LLM policy"* (open)[^rust-rfc-3959], and
rust-forge #1040 *"Add an LLM policy for `rust-lang/rust`"* (open, last updated
2026-08-02)[^rust-forge-1040].

Quoted below is **proposed text from an open pull request**, not a rule in force. It is recorded
because it is the clearest articulation available of how a large project reasons about this — but a
contributor cannot be held to it, and it may change or die in review.

## The design principle

> It's fine to use LLMs to answer questions, analyze, distill, refine, check, suggest, review. But
> not to **create**.
>
> LLMs work best when used as a tool to write *better*, not *faster*.[^rust-forge-1040]

## The part worth stealing: it concedes it is unenforceable

Alone among the policies here, the draft states its own limits and then explains why it is still
worth writing:

> We are aware that many clauses in this policy are unenforceable. Our goal is *not* to catch every
> violation. Instead, our goal is to remove plausible deniability: to force a choice between
> following the policy and intentionally violating it.[^rust-forge-1040]

It cites **anti-money-laundering compliance** as the model.[^rust-forge-1040] That reframes the
whole question. [Git](git.md)'s *"reject anything that looks AI generated"* is a detection rule and
inherits detection's false-positive problem. Rust's is a **declaration rule**: it does not try to
tell, it makes not-telling a deliberate act. Any project drafting a policy should decide which of
the two it is writing, because they fail differently.

The draft says so directly elsewhere: *"It's not your job to play detective."*[^rust-forge-1040]

## A four-level scheme, not a binary

The draft grades by **who sees the output**, which is a sharper axis than "how much AI":

| | |
|---|---|
| ✅ **Allowed** | *"Any use of an LLM where you are the only one who sees the output"* — questions about a codebase, private summaries, private review of your own code, personal dev-tools, generating candidate solutions then *"writing something from scratch in your own style"* |
| ❌ **Banned** | Comments, issue bodies and PR descriptions *"originally created by an LLM"* from a personal account; LLM-created documentation, doc-comments, safety comments and **compiler diagnostics**; treating an LLM review as sufficient to merge; policies *"written such that an LLM is required to execute them"* |
| ⚠️ **With disclosure** | Machine translation, trivial changes, LLM-assisted bug discovery *"as long as you personally verify the bug"*, review bots |
| 🔨 **Moderation penalty** | Lying — a Code of Conduct violation |

The heuristic for anything unlisted:

> Using an LLM for your own personal use is likely allowed ✅ · Showing LLM output to another human
> without solicitation is likely banned ❌ · Making a decision that affects others based on LLM
> output requires disclosure ⚠️[^rust-forge-1040]

## Two clauses no other project here has

**Documentation must be authored for humans.** *"You must not only document where tests live with
an `AGENTS.md`. Documentation must be authored for humans primarily, and LLM documentation may only
summarize it, not add new detail."*[^rust-forge-1040] This is a constraint on the *project's own*
artifacts, not on contributions — a rule against the codebase drifting into a state only a machine
can navigate.

**Review bots are regulated rather than banned.** They must be pre-approved, must post from *"a
separate GitHub account that clearly marks them as an LLM"*, must be blockable through GitHub's
normal user-blocking (explicitly excluding app accounts that cannot be blocked), and their comments
*"**must not** be blocking"* — a human reviewer has to endorse a comment before it gates a PR, and
*"cannot treat it as a CI failure."*[^rust-forge-1040]

## The experiment, and its five named conditions

LLM-*created* code is permitted only under a bounded experiment *"meant to inform future
non-experimental policy, not to serve as the perpetual LLM usage policy"* — **pre-arranged**
(a named reviewer agreed *before* the PR was opened), **non-critical** (internal tooling yes; *"the
trait system, MIR building, or the query system"* no), **high-quality** (*"we are not interested in
'vibe-coded' PRs"*), **well-tested** (*"held to a higher standard than human-created PRs, because
LLMs make it easier to write tests"*; no test suite means write one or close the PR, with *"no
exceptions for 'writing the tests seems hard'"*), and **well-reviewed** (author and reviewer both
*"commit to fully understanding the code"*), all **with disclosure**.[^rust-forge-1040]

`rust-lang` organization members are exempt from *"non-critical"* — but the draft *"strongly
discourages"* using that exemption: *"LLMs are very very good at generating plausible-looking code,
and soundness is hard to test."*[^rust-forge-1040]

## What a contributor must do

Nothing is binding yet. If the draft lands: keep LLM output private, or disclose. Never post
generated prose from your own account. Do not open an LLM-written PR without arranging a reviewer
first — that is a precondition, not a formality, and it is the clause a well-meaning contributor is
most likely to miss.

## Re-verification notes

Check **merge state first**, before reading any text: `gh pr view 1040 --repo rust-lang/rust-forge`
and `gh pr view 3959 --repo rust-lang/rfcs`. A quotation from an open PR is a proposal; the same
words merged are a rule, and this record must not describe one as the other. If #1040 merges, the
policy will live at `forge.rust-lang.org` under `policies/llm-usage.md` — which **404s as of
2026-08-04**, itself a usable check.

[^rust-forge-1040]: [Add an LLM policy for `rust-lang/rust` (rust-lang/rust-forge#1040)](https://github.com/rust-lang/rust-forge/pull/1040)
[^rust-rfc-3959]: [Project-wide LLM policy (rust-lang/rfcs#3959)](https://github.com/rust-lang/rfcs/pull/3959)
[^rust-rfc-3950]: [Add contribution policy for AI-generated work (rust-lang/rfcs#3950, closed)](https://github.com/rust-lang/rfcs/pull/3950)
