---
type: Practice
title: How open source treats AI-authored contributions
description: The read-through map — the six shapes a policy takes, the seven axes each one decides, and the cross-cutting findings that only appear when the primary texts are read side by side.
tags:
  - ai-contribution
  - policy
  - overview
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T01:15:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T01:15:00Z'
stale_after: 2026-11-05
sources:
  - id: git-submitting-patches-src
    title: Documentation/SubmittingPatches (git/git, master)
    resource: https://raw.githubusercontent.com/git/git/master/Documentation/SubmittingPatches
  - id: kernel-coding-assistants-src
    title: Documentation/process/coding-assistants.rst (torvalds/linux, master)
    resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst
  - id: qemu-code-provenance
    title: Code provenance — QEMU developer documentation
    resource: https://www.qemu.org/docs/master/devel/code-provenance.html
  - id: lf-generative-ai
    title: Policy Guidance Regarding Use of Generative AI Tools for Open Source Software Development
    resource: https://www.linuxfoundation.org/legal/generative-ai
  - id: asf-generative-tooling
    title: Generative Tooling Guidance — The Apache Software Foundation
    resource: https://www.apache.org/legal/generative-tooling.html
  - id: openinfra-ai-policy
    title: AI Generated Content Policy — OpenInfra Foundation
    resource: https://openinfra.org/legal/ai-policy
  - id: rust-forge-1040
    title: 'Add an LLM policy for `rust-lang/rust` (rust-lang/rust-forge#1040)'
    resource: https://github.com/rust-lang/rust-forge/pull/1040
  - id: zig-coc
    title: 'Code of Conduct — Zig Programming Language (section: Strict No LLM / No AI Policy)'
    resource: https://ziglang.org/code-of-conduct/
  - id: curl-contribute
    title: Contribute to curl — on AI use in curl
    resource: https://curl.se/dev/contribute.html
  - id: gcc-ai-policy
    title: GNU Compiler Collection - AI Policy
    resource: https://gcc.gnu.org/ai-policy.html
  - id: policy-index
    title: open-source-ai-contribution-policies (third-party index; lead list only)
    resource: https://github.com/melissawm/open-source-ai-contribution-policies
  - id: debian-gr-2026-002
    title: 'General Resolution: LLM usage in Debian (2026 vote_002)'
    resource: https://www.debian.org/vote/2026/vote_002
---

A contributor about to send AI-assisted work upstream needs one fact before starting: **what does
this project's policy say?** Finding out afterwards is the failure this bundle exists to prevent.

The short answer is that there is no consensus, and the disagreement is not the one people expect.
It is not ban-versus-allow. Projects that reach the same verdict frequently do so from incompatible
reasoning, and projects that share reasoning frequently reach opposite verdicts.

> **Read the project's own page.** This map is for orientation. Every record here exists because a
> summary of that project was wrong in a way that mattered — see *Why summaries fail*, below.

## Seven shapes

Almost every policy read so far is one of these. The shape predicts what a contributor must *do*
far better than the stance label does.

| Shape | What it governs | Example |
|---|---|---|
| **Absolute prohibition** | origin, including laundering routes | [Zig](projects/zig.md) |
| **Provenance prohibition** | inability to certify origin | [QEMU](projects/qemu.md), [NetBSD](distributions/netbsd.md), [Gentoo](distributions/gentoo.md) |
| **Detection rule** | how the submission *looks* | [Git](projects/git.md) |
| **Declaration rule** | whether you *said so* | [Rust](projects/rust.md) (draft), [OpenInfra](foundations/openinfra.md) |
| **Responsibility rule** | whether you can defend it | [Python](projects/python.md), [curl](projects/curl.md), [Linux kernel](projects/linux-kernel.md) |
| **Licence-compatibility rule** | rights in the output | [Linux Foundation](foundations/linux-foundation.md), [ASF](foundations/apache-software-foundation.md) |
| **Copyright-threshold rule** | whether the contribution is *legally significant* | [GCC](projects/gcc.md) |

GCC's is the newest shape and the most reusable. Its line is the **copyright threshold** — the same
test that already decides whether a contribution needs an assignment — so the policy extends existing
legal machinery instead of creating a new regime, and *"is this AI-generated?"* becomes subordinate
to *"is this legally significant?"*. It is also the only policy here released **CC0**, so the text can
be adopted outright.

Three are unshaped rather than shaped: [Debian](distributions/debian.md) is mid-vote,
[FreeBSD](distributions/freebsd.md) has a reported intention and no published rule, and
**[Fedora](distributions/fedora.md) has a policy in force whose text is not published anywhere
reachable** — approved by a minuted unanimous vote, effective immediately, and nine months later
absent from the Council Policies page. A rule nobody can read is a fourth state, distinct from
prohibited, permitted and undecided.

## Detection and declaration fail differently

This is the distinction most worth carrying away, because the two look similar and behave nothing
alike.

**Git writes a detection rule**: *"we will reject anything that looks AI generated, that sounds
overly formal or bloated, that looks like AI slop … or that senders don't understand or cannot
explain."*[^git-submitting-patches-src] It needs no disclosure and inherits detection's
false-positive problem — a careful non-native speaker writes prose that trips it.

**Rust's draft writes a declaration rule**, and says why: *"We are aware that many clauses in this
policy are unenforceable. Our goal is not to catch every violation … Instead, our goal is to remove
plausible deniability: to force a choice between following the policy and intentionally violating
it."*[^rust-forge-1040] It cites anti-money-laundering compliance as the model, and elsewhere:
*"It's not your job to play detective."*

curl shows the two are one observable seen from opposite ends. *"If someone can spot that the
contribution was made with the help of AI, you have more work to do."*[^curl-contribute] Git tells
maintainers what to reject; curl tells contributors what to fix.

## The DCO settles nothing

Four organisations reason from the **Developer Certificate of Origin** and reach four destinations:

- **QEMU → prohibition.** The copyright status of generated output *"is ill-defined with no
  generally accepted, settled legal foundation"*, so how contributors *"could comply with DCO terms
  (b) or (c) … is unclear."*[^qemu-code-provenance]
- **Git → volume-scoped caution.** Satisfying the DCO is unclear *"when submitting significant
  amount of content"* — the concern is scoped to bulk, not to any assistance.[^git-submitting-patches-src]
- **Linux kernel → relocated certification.** *"AI agents MUST NOT add Signed-off-by tags. Only
  humans can legally certify."*[^kernel-coding-assistants-src] The human certifies, having reviewed;
  the tool is credited without signing.
- **Linux Foundation → not invoked at all.** Its policy contains zero occurrences of `DCO`,
  `Developer Certificate of Origin` or `Signed-off-by`, and reaches permission via licence
  compatibility instead.[^lf-generative-ai]

So *"they require a DCO"* predicts nothing about a project's stance. Any summary organised around
that fact is organised around noise.

[GCC](projects/gcc.md) shows the instrument is not even the unit of choice: it accepts **either** an
FSF copyright assignment **or** a DCO sign-off, and its AI policy turns on neither — it turns on
whether the contribution crosses the copyright threshold those instruments exist to
manage.[^gcc-ai-policy] It does adopt the kernel's rule that only a human may sign off, and adds one
nobody else states: *"An LLM may not commit code to the project repository"* — a constraint on
**agents with write access**, not on generated text.[^gcc-ai-policy]

## Foundations are floors, not answers

The [Linux Foundation](foundations/linux-foundation.md), [ASF](foundations/apache-software-foundation.md)
and [OpenInfra](foundations/openinfra.md) each set a permissive baseline across many projects — and
each says projects may go further. *"Individual Linux Foundation projects may develop their own
project-specific guidance."*[^lf-generative-ai] The kernel's in-tree policy is exactly that, and it
is stricter.

**Checking only the foundation is a reliable way to be wrong about the project.** The more active a
project, the more likely it has written its own rule.

Where the two foundations differ is instructive. Both ask contributors to check the AI tool's terms;
only the ASF bounds the duty — *"Don't second guess vendor's terms of use (TOU) … you are not
expected to go outside of the TOU text for further clarifications."*[^asf-generative-tooling] The
ASF also makes the obligation satisfiable at all: nobody can audit training data, so the **tool's own
similarity reporting** is what discharges the third-party-material check.[^asf-generative-tooling]

## Disclosure tags name degrees, not preferences

Three field names are in use, and they are not competing spellings. OpenInfra uses **both** and
states the distinction: `Assisted-By:` for *predictive* tools (auto-complete), `Generated-By:` for
*generative* ones.[^openinfra-ai-policy]

| Field | Used by |
|---|---|
| `Assisted-by:` | [Linux kernel](projects/linux-kernel.md) (`AGENT_NAME:MODEL_VERSION [TOOLS]`), [Ansible](projects/ansible.md) (`[tool name/version]`), [GCC](projects/gcc.md) |
| `Generated-by:` | ASF |
| **both, distinguished** | OpenInfra |

**Do not reach for `Co-developed-by:`.** It was widely recommended for AI attribution before project
policies landed, and it is structurally invalid for a tool: it denotes *authorship*, so the kernel
requires each one be immediately followed by a `Signed-off-by:` from that co-author — which the same
project's policy forbids an AI agent from adding. The trailer demands a sign-off no tool may give,
and that constraint is why a distinct token was coined rather than an existing one reused.

Two consequences. **Value grammars differ even where the field matches** — a trailer formatted for
the kernel is not a valid Ansible one, so emit what the target project asks for. And OpenInfra's
labels are **mutable**: reviewers may remove one *"if substantial human reworking
occurs"*.[^openinfra-ai-policy] Everywhere else the tag records history and is permanent. Those are
incompatible readings of what a provenance tag *is*, and a project should pick one deliberately — a
mutable history-tag is just an inaccurate one.

## The seven axes

Six people drafting [Debian](distributions/debian.md)'s competing ballot options converged on the
same questions.[^debian-gr-2026-002] Adding what the other records surface, a policy has to decide:

1. **Prohibit, discourage, or regulate?**
2. **Disclosure — mandatory, encouraged, or silent?** And above what threshold: any use, or
   unmodified bulk?
3. **Prose and human conversation, or only code?** Debian's Proposal C requires messages to humans
   be *"drafted solely by humans"*; Ansible's scope covers its Forum and Matrix; Zig forbids even
   *"talking about use of chatbot/LLM services"*.[^zig-coc]
4. **Upstream, or only the project's own work?**
5. **May contributor data leave the project's infrastructure?**
6. **Is there a volume threshold?**
7. **Who carries the burden — submitter only, or reviewers too?** OpenInfra requires reviewers to
   apply *"heightened scrutiny"* to labelled changes.[^openinfra-ai-policy]

A policy silent on any of these has a gap someone will find. Two more decisions sit underneath:
**where the rule lives** (Zig's ban is a Code of Conduct clause, so a violation is misconduct rather
than a bad patch), and **who the rule taxes**.

That last one is the least considered and the most consequential. A blanket "no AI" rule falls
hardest on contributors who use AI to work at all. Every project that thought about **translation**
permits it so as not to tax non-native speakers — except Zig, which refuses and moves the translation
to the reader.[^zig-coc] Only [GCC](projects/gcc.md) extends the reasoning to **accessibility**,
putting screen readers, text-to-speech, direct translation and spelling assistance outside the policy
entirely, provided the contributor verifies the output.[^gcc-ai-policy] A policy that does not carve
this out has excluded people without deciding to.

## Why summaries fail

Every record in this bundle was checked against a prior summary. The summaries were wrong in a
consistent direction: **they dropped the qualifier that determines what a contributor should do.**

- Gentoo's ban is explicitly revisitable.
- NetBSD's is a rebuttable presumption with a named approver — *prior written approval by core*.
- QEMU's has a documented exceptions process.
- Git both rejects AI-looking work **and** says *"We strongly recommend using AI tools carefully and
  responsibly."*[^git-submitting-patches-src]
- Zig's translation refusal comes with an invitation to post in your own language.

All five were filed as "complete ban". The pattern is not carelessness; it is what compression does
to this subject. **The exceptions are the operative part** — whether a route exists, and who decides.

[Fedora](distributions/fedora.md) shows the failure can start earlier than any summary. Its policy
was adopted properly — open proposal, weeks of public discussion, revisions from feedback, a recorded
unanimous vote — and then never published where a contributor can read it. **A rule in force that
cannot be read is not a rule anyone can follow**, and every downstream summary of it, including a
careful one, is then unverifiable by construction.

## What this bundle does not do

It does not enumerate. A public index lists **190+ organisations** with published AI contribution
policies[^policy-index], and the 27-entry survey this replaced was already a slice. Coverage is not
the goal and completeness is not claimed: records are chosen for foundations first, then novel
reasoning, then what the consuming tools encounter. See ADR-0011 as amended.

That index is a **lead list only**. It is a third-party aggregation, some of its links are already
stale — it points at CPython's `generative-ai/` path, which now redirects — and no entry in it
counts as evidence here until its primary has been read.

It also does not treat all absences alike. FreeBSD has a record because its Core Team publicly
stated it was drafting a policy and named where it would land — a claim with a falsifiable location.
Projects merely probed clean are logged, not recorded.

## Why it expires

Every claim here is about another organisation's *current* position, which changes without telling
anyone. Two records in this bundle already document state the prior survey could not have known: the
kernel merged its policy, and Debian opened a vote. `sources` records where a claim came from,
`verified` records that somebody checked, and `stale_after` makes decay visible instead of silent.

**A caution that applies to re-verification specifically.** Some primary sources are not
machine-retrievable — Fedora's council policy and GCC's wiki both sit behind proof-of-work
challenges that return HTTP 200 with a challenge page. A status code proves the server answered,
never that the content arrived. Check for the text you came for.

[^git-submitting-patches-src]: [Documentation/SubmittingPatches (git/git, master)](https://raw.githubusercontent.com/git/git/master/Documentation/SubmittingPatches)
[^kernel-coding-assistants-src]: [Documentation/process/coding-assistants.rst (torvalds/linux, master)](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst)
[^qemu-code-provenance]: [Code provenance — QEMU developer documentation](https://www.qemu.org/docs/master/devel/code-provenance.html)
[^lf-generative-ai]: [Policy Guidance Regarding Use of Generative AI Tools for Open Source Software Development](https://www.linuxfoundation.org/legal/generative-ai)
[^asf-generative-tooling]: [Generative Tooling Guidance — The Apache Software Foundation](https://www.apache.org/legal/generative-tooling.html)
[^openinfra-ai-policy]: [AI Generated Content Policy — OpenInfra Foundation](https://openinfra.org/legal/ai-policy)
[^rust-forge-1040]: [Add an LLM policy for `rust-lang/rust` (rust-lang/rust-forge#1040)](https://github.com/rust-lang/rust-forge/pull/1040)
[^zig-coc]: [Code of Conduct — Zig Programming Language (section: Strict No LLM / No AI Policy)](https://ziglang.org/code-of-conduct/)
[^curl-contribute]: [Contribute to curl — on AI use in curl](https://curl.se/dev/contribute.html)
[^gcc-ai-policy]: [GNU Compiler Collection - AI Policy](https://gcc.gnu.org/ai-policy.html)
[^policy-index]: [open-source-ai-contribution-policies (third-party index; lead list only)](https://github.com/melissawm/open-source-ai-contribution-policies)
[^debian-gr-2026-002]: [General Resolution: LLM usage in Debian (2026 vote_002)](https://www.debian.org/vote/2026/vote_002)
