---
type: Organization
title: LLVM
description: The most theorised policy here. It names the problem — an extractive contribution, borrowed with attribution from Nadia Eghbal — states a golden rule that a change must be worth more than the time it takes to review, and diagnoses why LLMs broke the old economics. It is enforced by a paste-ready template and an extractive label carrying 41 pull requests, forbids AI on good-first-issues, and grants the bundle's only named exception.
resource: https://llvm.org/docs/AIToolPolicy.html
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - restricted
  - disclosure
  - attribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-09T00:12:26Z'
verified:
  - by: claude/opus-5
    at: '2026-09-09T00:12:26Z'
stale_after: 2027-03-09
sources:
  - id: llvm-ai-policy
    title: 'LLVM AI Tool Use Policy (llvm/docs/AIToolPolicy.md, llvm/llvm-project, main)'
    resource: https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/docs/AIToolPolicy.md
  - id: llvm-agents-pr
    title: 'Add minimal AGENTS.md (llvm/llvm-project#220659, draft, opened 2026-09-02)'
    resource: https://github.com/llvm/llvm-project/pull/220659
  - id: llvm-extractive-label
    title: 'The `extractive` label (llvm/llvm-project)'
    resource: https://api.github.com/repos/llvm/llvm-project/labels/extractive
  - id: llvm-copilot-instructions
    title: '.github/instructions/llvm.instructions.md (llvm/llvm-project, main)'
    resource: https://raw.githubusercontent.com/llvm/llvm-project/main/.github/instructions/llvm.instructions.md
---

**Stance: permitted with a human in the loop, and argued more thoroughly than anything else here.**
The policy landed **2026-01-16** and has been amended once. Its opening is conventional:

> Contributors can use whatever tools they would like to craft their contributions, but there must be
> a **human in the loop**. … The contributor is always the author and is fully accountable. …
> Contributors should be sufficiently confident that the contribution is high enough quality that
> asking for a review is **a good use of scarce maintainer time**.[^llvm-ai-policy]

What follows is not.

## It names the problem, and borrows the name

> Sending the unreviewed output of an LLM to open source project maintainers **extracts** work from
> them in the form of design and code review, so we call this kind of contribution an **"extractive
> contribution"**.
>
> Our **golden rule** is that **a contribution should be worth more to the project than the time it
> takes to review it.**[^llvm-ai-policy]

The term is quoted from Nadia Eghbal's *Working in Public* and attributed in place — *"extractive
contributions are those where the marginal cost of reviewing and merging that contribution is greater
than the marginal benefit to the project's producers."*[^llvm-ai-policy]

**Six projects in this bundle describe review cost; this one gives it a name, a source and a
decision rule.** Naming it is what makes it usable: a maintainer can say *this is extractive* and be
understood, which a complaint about workload does not achieve.

## The historical diagnosis, which nothing else states

> Prior to the advent of LLMs, open source project maintainers would often review any and all changes
> sent to the project simply because **posting a change for review was a sign of interest from a
> potential long-term contributor**. While new tools enable more development, it **shifts effort from
> the implementor to the reviewer**.[^llvm-ai-policy]

**That is the sharpest account of the problem in this bundle.** The submission used to carry
information beyond its content — it was costly to produce, so it evidenced intent, and reviewing it
was an investment in a future contributor. Generation made patches cheap and destroyed the signal.
Everything else here treats review cost as a quantity that went up; this identifies *what was lost*,
which explains why the answer is a bar on value rather than a cap on volume.

The consequence is stated as a community argument, not an efficiency one: *"Passing maintainer
feedback to an LLM doesn't help anyone grow, and does not sustain our
community."*[^llvm-ai-policy]

## Enforcement that exists and can be counted

Three mechanisms, and unusually all three are observable:

**A paste-ready response.** The policy supplies the text a maintainer should use, so refusing costs
one paste rather than a drafted explanation: *"This PR doesn't appear to comply with our policy on
tool-generated content, and requires additional justification for why it is valuable enough to the
project for us to review it."*[^llvm-ai-policy]

**A label.** `extractive`, described in the repository as *"Used for PRs which are extractive
according to our developer policy"*, exists and carried **41 issues and pull requests** when checked
on 2026-09-09.[^llvm-extractive-label] Its stated purpose is triage — *"to help other reviewers
prioritize their review time"* — so the label routes attention rather than punishing.

**Escalation.** If a contributor does not make the change less extractive, maintainers *"escalate to
the relevant moderation or admin team for the space (GitHub, Discourse, Discord, etc) to lock the
conversation."*[^llvm-ai-policy]

**A count is rare here.** [Kubernetes](kubernetes.md)'s CLA check is the only other mechanical
enforcement and its effect cannot be seen from outside; this one is a number anyone can query.

## Two prohibitions, one of which inverts another project's rule

> An important implication of this policy is that it **bans agents that take action in our digital
> spaces without human approval**, such as the GitHub `@claude` agent. Similarly, **automated review
> tools that publish comments without human review are not allowed.** However, an opt-in review tool
> that keeps a human in the loop is acceptable.[^llvm-ai-policy]

That is a sharper line than the projects that deploy review bots — [Kubernetes](kubernetes.md),
[Dependency-Track](dependency-track.md) and [systemd](systemd.md) all run one — and LLVM's own
`.github/instructions/*.instructions.md` files are review guidance for exactly such a
tool.[^llvm-copilot-instructions] **The rule is not against AI review; it is against publication
without a human**, which those instructions do not violate.

> **Using AI tools to fix issues labelled as "good first issues" is forbidden.** These issues are
> generally not urgent, and are intended to be learning opportunities for new
> contributors.[^llvm-ai-policy]

**[Elixir](elixir.md) gates agent work by label in the opposite direction** — no agents on existing
issues *unless* marked `Contributions Welcome`. LLVM bars them from a specific label and permits
elsewhere. Two projects reached label-scoped rules independently with **inverted polarity**, and
between them they bracket the design: an allow-list and a deny-list over the same tracker
machinery.

## What the trailer is for, stated

> Our policy on labelling is **intended to facilitate reviews, and not to track which parts of LLVM
> are generated**. … use a commit message trailer like `Assisted-by: <name of code
> assistant>`.[^llvm-ai-policy]

[The Assisted-by trailer](../mechanisms/assisted-by-trailer.md) records that projects have asked one
field to do several different jobs. **This is the fourth stated purpose and the first to disclaim
provenance outright** — LLVM wants the tag to direct a reviewer's attention and explicitly does not
want a map of generated code. Contrast [QEMU](qemu.md), for which the tag *"doubles as a check that
the author has read the policy"*.

Note also that LLVM asks for the tool's **name**, the grammar the [kernel](linux-kernel.md) retired
and [Nerves](nerves.md) mandates.

## Copyright, extended rather than invented

> Our policy on AI tools is **similar to our copyright policy**: contributors are responsible for
> ensuring they have the right to contribute code under the terms of our licence. **Using AI tools to
> regenerate copyrighted material does not remove the copyright.**[^llvm-ai-policy]

The same move [GCC](gcc.md) and [Asahi Linux](asahi-linux.md) make — see
[extending existing machinery](../mechanisms/extending-existing-machinery.md).

## The only granted exception anywhere here

> We have **one exception** to this policy for the Bazel-fixer bot. The project council approved this
> RFC proposing to use a combination of `dwyu` and LLMs to maintain the Bazel build files. Any future
> exception will be considered individually on its own merits as to whether it is useful to the
> project or **extracts work from maintainers**.[^llvm-ai-policy]

Several policies here admit exceptions in principle; this is the only one that **names a granted one,
identifies the body that granted it, and links the decision**. It also shows the golden rule working
as a test rather than a slogan: the bot was approved because it *reduces* maintainer work.

## It copied from a policy this bundle cannot read

The References section attributes its sources, and one is remarkable:

> Some of the text above was **copied from the Fedora project policy proposal**, which is licensed
> under the Creative Commons Attribution 4.0 International License. **This link serves as
> attribution.**[^llvm-ai-policy]

[Fedora](../distributions/fedora.md) is recorded here as a policy **in force but unpublished** — approved
by a minuted unanimous vote and absent from the Council Policies page. **LLVM's document is therefore
a partial, attributed view of text this bundle could not otherwise reach**, and the licence is what
made that possible, as with [GCC](gcc.md)'s CC0 and [ripgrep](ripgrep.md)'s Unlicense.

It is also the only copying event here where the borrower names a source that is **itself
unreachable**, and the only one where attribution was *owed* rather than offered — see
[policy by copying](../mechanisms/policy-by-copying.md). The other references are Rust's draft policy
on burdensome pull requests and a post by Seth Larson.

## The delivery mechanism is still being argued

LLVM's `.gitignore` carries a block titled `# Coding assistants' stuff` that ignores **every**
agent-file convention: `.agents/`, `/CLAUDE.md`, `/instructions.md`, `.claude/`, `/GEMINI.md`,
`.gemini/`, `AGENTS.md`, `.codex/` and `.cursor`. **A stance expressed through `.gitignore`** — these
are personal tooling artifacts, not project files — and nothing else in this bundle takes it.

Draft pull request **#220659**, opened 2026-09-02 and unmerged, would reverse two lines of that and
add a two-line pointer:[^llvm-agents-pr]

```
AGENTS.md:  Review this project's @llvm/docs/AIToolPolicy.md and
            @llvm/docs/CodingStandards.md before contributing.
CLAUDE.md:  @AGENTS.md
```

**The `@` import is a fourth pointer construction**, alongside the symlinks and duplicated content in
[agent-file pointers](../mechanisms/agent-file-pointers.md) — a client-side include rather than a
filesystem link.

## What a contributor must do

Use tools, then **read and review everything before asking anyone else to.** Ask whether the change
is worth more than the time it takes to review — if it is large, complex or low-value, make it
smaller or more useful before posting. **Write the pull request description yourself** (translation
and copy-editing aside). **Label substantial tool-generated content**, in the description, the commit
message, or an `Assisted-by:` trailer naming the assistant. Do not point an agent at a **`good first
issue`**. Do not let an agent post anything without your approval — that includes review comments.
If you are new, start small.

## Re-verification notes

The policy is `llvm/docs/AIToolPolicy.md`, rendered at `llvm.org/docs/AIToolPolicy.html`. **Read the
repository copy**: `git log` shows exactly two commits, the 2026-01-16 addition and the 2026-03-05
Bazel exception, which is faster than diffing rendered pages.

**The `extractive` label count is the live number in this record** and the only figure here that moves
on its own. It was 41 on 2026-09-09; a re-verification should re-query rather than trust it, and the
trend matters more than the value.

Watch the `AGENTS.md` pull request. It is a **draft** and unmerged, and its outcome answers a question
no other record in this bundle poses: whether a project that deliberately git-ignores agent files
reverses that to meet the convention. Either result is informative, and the `.gitignore` block is the
thing to diff.

[^llvm-ai-policy]: [LLVM AI Tool Use Policy (llvm/docs/AIToolPolicy.md, llvm/llvm-project, main)](https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/docs/AIToolPolicy.md)
[^llvm-agents-pr]: [Add minimal AGENTS.md (llvm/llvm-project#220659, draft, opened 2026-09-02)](https://github.com/llvm/llvm-project/pull/220659)
[^llvm-extractive-label]: [The `extractive` label (llvm/llvm-project)](https://api.github.com/repos/llvm/llvm-project/labels/extractive)
[^llvm-copilot-instructions]: [.github/instructions/llvm.instructions.md (llvm/llvm-project, main)](https://raw.githubusercontent.com/llvm/llvm-project/main/.github/instructions/llvm.instructions.md)
