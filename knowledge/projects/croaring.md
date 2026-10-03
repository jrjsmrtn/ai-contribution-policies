---
type: Organization
title: CRoaring
description: Permits any tooling under a human-in-the-loop rule copied from LLVM, with LLVM's labelling requirement softened to encouragement and its ban on autonomous agents, violations process and exceptions left out. Three months later it wrote a second document aimed at the other side — an AGENTS.md telling agents that AI-generated deserialization bug reports are bogus. No commit in the last year credits an AI tool.
resource: https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/AI_USAGE_POLICY.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - lineage
  - agent-file
  - bug-reports
status: stable
generated:
  by: claude/sonnet-5-5
  at: '2026-10-03T13:00:00Z'
verified:
  - by: claude/sonnet-5-5
    at: '2026-10-03T13:00:00Z'
stale_after: 2027-04-03
sources:
  - id: cr-policy
    title: 'AI_USAGE_POLICY.md (RoaringBitmap/CRoaring, master)'
    resource: https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/AI_USAGE_POLICY.md
  - id: cr-agents
    title: 'AGENTS.md (RoaringBitmap/CRoaring, master)'
    resource: https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/AGENTS.md
  - id: cr-security
    title: 'SECURITY.md (RoaringBitmap/CRoaring, master)'
    resource: https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/SECURITY.md
  - id: cr-pr-template
    title: 'Pull request template (.github/pull_request_template.md, RoaringBitmap/CRoaring, master)'
    resource: https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/.github/pull_request_template.md
  - id: cr-readme
    title: 'README.md (RoaringBitmap/CRoaring, master)'
    resource: https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/README.md
  - id: cr-policy-history
    title: 'Commit history of AI_USAGE_POLICY.md (RoaringBitmap/CRoaring, master)'
    resource: https://github.com/RoaringBitmap/CRoaring/commits/master/AI_USAGE_POLICY.md
  - id: cr-agents-history
    title: 'Commit history of AGENTS.md (RoaringBitmap/CRoaring, master)'
    resource: https://github.com/RoaringBitmap/CRoaring/commits/master/AGENTS.md
  - id: cr-llvm-policy
    title: 'AIToolPolicy.md (llvm/llvm-project at 6695f1d97f, the revision in force on 2026-03-23)'
    resource: https://raw.githubusercontent.com/llvm/llvm-project/6695f1d97f9615e6bbe5a5d40ea4496b7e84a3d9/llvm/docs/AIToolPolicy.md
---

**Stance: any tool, with a human who has read the result.** `AI_USAGE_POLICY.md` opens:

> Contributors can use whatever tools they would like to craft their contributions, but there must be a
> human in the loop.[^cr-policy]

and asks for the obvious consequences: *"Contributors must read and review all LLM-generated code or text
before they ask other project members to review it."* The text goes on: *"The contributor is always the
author and is fully accountable for their contributions."*[^cr-policy] Its list of covered contributions includes code, *"Issues or security vulnerabilities"* and *"Comments and
feedback on pull requests"*.[^cr-policy] See [human in the loop](../mechanisms/human-in-the-loop.md).

**There is no `CONTRIBUTING.md`.** The policy is reached from three places instead: the pull request
template,[^cr-pr-template] the README's contributing paragraph (*"If you are using AI, please review our AI
usage policy"*),[^cr-readme] and `SECURITY.md`.[^cr-security]

## It is LLVM's policy, shortened

The file's last line is a link headed *"LLVM AI Tool Use Policy"*, pointing at LLVM's discussion thread.
Nowhere does the file say the text was adapted from LLVM's. Compared sentence by sentence with the LLVM text in force when it
landed (revision `6695f1d97f`, 2026-03-05; markdown stripped, split at `.`, `!`, `?` and `:`), **13 of
CRoaring's 19 sentences appear verbatim in LLVM's**; the other six are headings run into the sentence after
them, a first sentence recast from *"LLVM's policy is that contributors…"* to *"Contributors can…"*, and a
disclosure section CRoaring wrote itself.[^cr-policy][^cr-llvm-policy] The LLVM text is unchanged in those
sentences today. See [policy by copying](../mechanisms/policy-by-copying.md).

**What the copy left out**, each checked by searching the CRoaring file for the phrase:

- **The labelling requirement.** LLVM expects contributors to *"be transparent and label contributions that
  contain substantial amounts of tool-generated content"* and suggests an `Assisted-by:` trailer.
  CRoaring says *"we encourage you to disclose its use and explain your process"*, and adds a sentence of its
  own that turns non-disclosure into a suspicion rather than a breach: *"If a submission appears to rely
  heavily on AI without disclosure, we may doubt that the human-in-the-loop requirement has been
  met."*[^cr-policy][^cr-llvm-policy] No trailer is mentioned.
- **The ban on autonomous agents.** LLVM's text says its policy bans agents that take action in the project's
  digital spaces without human approval. CRoaring never says it, and nothing in its file mentions autonomy.
- **The `good first issue` rule, the violations process, the exceptions and the examples.**
- **The golden rule and its source.** LLVM credits the framing to Nadia Eghbal in a block quotation.
  CRoaring keeps the word *extractive* and the sentence defining it, and drops the passage that says where
  the word came from; neither *golden* nor *Eghbal* appears.
- **Kept verbatim:** the copyright section, including *"Using AI tools to regenerate copyrighted material
  does not remove the copyright"*.

The result is a rule that says a human must be in the loop and gives a maintainer little to enforce it with:
no label to look for, no named sanction, no ban on the thing that would make the human absent.

## The same maintainer then wrote for the agents

The policy file was added on 2026-03-23, in a commit titled *"improving pull request template"*, by the
`lemire` account — the maintainer `SECURITY.md` names as the contact.[^cr-policy-history] On 2026-06-11 the
same account added `AGENTS.md` in three commits, the first titled *"a word for our agents."*, which also
edited `SECURITY.md`.[^cr-agents-history] Its single subject is a class of report:

> Many AI-generated bug reports claim that deserialization functions … "trigger bugs" or "cause crashes"
> when given malformed or untrusted input.
>
> **These reports are bogus.**[^cr-agents]

It explains the documented contract — the *safe* deserializers are memory-safe, but a result built from
untrusted bytes must pass `roaring_bitmap_internal_validate` before use — and ends with an instruction:

> When triaging such reports, point to the validation requirement in the function documentation and close as
> "not a bug / user error / documented behavior."[^cr-agents]

`SECURITY.md` says the same in the project's own voice: *"we are getting too many invalid bug reports causes
by AI"* (sic), calling it *"a drain on our maintainers and a disservice to the community."*[^cr-security]

**Who the file is for is not stated.** Read one way it briefs an agent that is *looking for bugs* and tells
it the finding is already refuted; read the other, it briefs an agent that is *triaging* them and tells it
how to close. The file serves either, and the commit message names neither. What is unusual is the
**direction**. Other agent files in this bundle brief the agent *contributing* or *reviewing* —
[Valkey](valkey.md)'s is the nearest, a brief for a review bot — while this one tries to **pre-empt a
category of AI output with a standing refutation**, in the one file an agent is certain to read. Other
records, [curl](curl.md) among them, deal with AI-generated reports in policy text; searching this bundle
for *bogus* and for agent-file lines that mention reports or triage found no other agent file that does it.
The policy file asks humans to be in the loop; the agent file assumes some reports will arrive without one.

## Practice: no AI credits

A partial clone of `master` on 2026-10-03 (`--shallow-since=2025-10-01`, 148 commits) finds **no commit
with a `Co-Authored-By`, `Assisted-by` or `Generated-by` trailer naming an AI tool.** The 27 trailers that
look like tools are dependabot, and the rest name people. The probe was checked with a planted string that
no commit contains; it returned zero.

**That is a lower bound, and a policy-consistent one.** The policy asks for no label, so a commit without a
trailer says nothing about whether a model was used. It is also a different position from LLVM's, which
asks for one.

## What a contributor must do

Use any tool, read all of its output before asking anyone to review it, be able to answer questions about it,
and start small if you are new. Disclosure is encouraged and not required, and no trailer is expected.
**Do not report a crash in a `*_deserialize_safe` function without having validated the result first:** the
project has said in two files that such reports are closed, and the agent file instructs agents to close them.

## Re-verification notes

**Neither the issue tracker nor the pull request history was read** — whether the policy has been applied to
a closed pull request, or the agent file's instruction carried out on a closed report, is not established.
**The licence of the copy was not examined** — whether adapting LLVM's text carried an attribution duty here
is the question [LLVM's own record](llvm.md) raises about its Fedora source. **LLVM's file has three commits in its history**, so *unchanged since copying* is a short claim; re-run the
sentence comparison if LLVM revises it. The link to LLVM's discussion thread was not fetched.

[^cr-policy]: [AI_USAGE_POLICY.md (RoaringBitmap/CRoaring, master)](https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/AI_USAGE_POLICY.md)
[^cr-agents]: [AGENTS.md (RoaringBitmap/CRoaring, master)](https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/AGENTS.md)
[^cr-security]: [SECURITY.md (RoaringBitmap/CRoaring, master)](https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/SECURITY.md)
[^cr-pr-template]: [Pull request template (.github/pull_request_template.md, RoaringBitmap/CRoaring, master)](https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/.github/pull_request_template.md)
[^cr-readme]: [README.md (RoaringBitmap/CRoaring, master)](https://raw.githubusercontent.com/RoaringBitmap/CRoaring/master/README.md)
[^cr-policy-history]: [Commit history of AI_USAGE_POLICY.md (RoaringBitmap/CRoaring, master)](https://github.com/RoaringBitmap/CRoaring/commits/master/AI_USAGE_POLICY.md)
[^cr-agents-history]: [Commit history of AGENTS.md (RoaringBitmap/CRoaring, master)](https://github.com/RoaringBitmap/CRoaring/commits/master/AGENTS.md)
[^cr-llvm-policy]: [AIToolPolicy.md (llvm/llvm-project at 6695f1d97f, the revision in force on 2026-03-23)](https://raw.githubusercontent.com/llvm/llvm-project/6695f1d97f9615e6bbe5a5d40ea4496b7e84a3d9/llvm/docs/AIToolPolicy.md)
