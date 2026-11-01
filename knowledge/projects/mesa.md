---
type: Organization
title: Mesa
description: A project-wide compromise reached after long debate — no autonomous tools, mandatory disclosure through a bare Assisted-by or Generated-by LLM trailer, and AI discouraged for comments, commit messages and GitLab comments — with stricter rules layered on top by individual drivers. Its agent file carried NetworkManager's violation watermark for five weeks and was loosened on 2026-10-22 without changing the policy, because it policed drafts the policy never meant to reach.
resource: https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/docs/submittingpatches.rst
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - attribution
  - communication
  - agent-files
status: stable
generated:
  by: claude/opus-5-5
  at: '2026-11-01T20:30:00Z'
verified:
  - by: claude/opus-5-5
    at: '2026-11-01T20:30:00Z'
stale_after: 2027-05-01
sources:
  - id: mesa-submitting
    title: 'docs/submittingpatches.rst — Expectations on contributors (mesa/mesa, main)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/docs/submittingpatches.rst
  - id: mesa-agents
    title: 'AGENTS.md (mesa/mesa, main)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/AGENTS.md
  - id: mesa-commit-disclosure
    title: 'commit f015600c — docs: add AI disclosure requirements (2026-04-06)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/commit/f015600c.patch
  - id: mesa-commit-prose
    title: 'commit 2a54dde0 — docs: discourage AI-generated code comments, commit messages, gitlab comments (2026-09-02)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/commit/2a54dde0.patch
  - id: mesa-commit-agents-initial
    title: 'commit 015ae984 — AGENTS.md: add initial file (2026-09-16)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/commit/015ae984.patch
  - id: mesa-commit-agents-loosen
    title: 'commit 8e21f044 — AGENTS.md: do not enforce the comment/commit rules (merged 2026-10-22)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/commit/8e21f044.patch
  - id: mesa-commit-llm
    title: 'commit cd876c44 — docs: prohibit advertising the model (2026-10-22)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/commit/cd876c44.patch
  - id: mesa-panfrost
    title: 'docs/drivers/panfrost.rst — AI policy (mesa/mesa, main)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/docs/drivers/panfrost.rst
  - id: mesa-pvr
    title: 'src/imagination/README.md — Contribution policy (mesa/mesa, main)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/src/imagination/README.md
  - id: mesa-jay
    title: 'src/intel/compiler/jay/README.md — Contribution policy (mesa/mesa, main)'
    resource: https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/src/intel/compiler/jay/README.md
  - id: mesa-nouveau
    title: 'Maintaining our humanity and community — nouveau wiki (2026-10-09)'
    resource: https://nouveau.freedesktop.org/Humanity.html
---

**Stance: permitted, disclosed, never autonomous — as a floor that several drivers raise.** Mesa's
rules are in the *Expectations on contributors* section of its patch-submission guide. The submitter
*"is responsible for the code change, regardless of where that code change came from"*, and AI
*"does not grant additional privileges or reduce our expectations."*[^mesa-submitting]

## The project-wide rule

- **No autonomous tools.** *"It is not allowed to use autonomously acting tools to submit any
  contributions"*, including any autonomous interaction with issues or merge requests, and *"Do not
  under any circumstances wire up any review bot or similar tools."*[^mesa-submitting]
- **Prose stays human, as a request.** *"“AI” shouldn't be used to generate code comments, commit
  messages, and Gitlab comments."* The reason given is the contributor's own skill: *"We want
  contributors to develop and practice their own communication and technical writing. Those skills
  deteriorate if they are not used."*[^mesa-submitting] Added on 2026-09-02.[^mesa-commit-prose]
- **Disclosure is required**, with two exceptions: changes too trivial to be copyrightable, and
  mechanical changes, *"when it would be the same regardless of what tooling was used"*.[^mesa-submitting]
- **Two trailers, and no model name.** `Assisted-by: LLM` when AI *"was involved in making decisions
  or also generated parts of the code"*, `Generated-by: LLM` when *"almost all the code was generated
  through “AI”"*. *"Do not advertise the model. Do not use the ``Co-authored-by`` tag as this one is
  reserved for human co-authors."*[^mesa-submitting]

**The trailer moved the opposite way from the kernel's.** When disclosure was added on 2026-04-06,
Mesa *suggested* `Assisted-by: TOOL (OPTIONAL: MODEL)`.[^mesa-commit-disclosure] On 2026-10-22 it
began to *require* the bare `LLM` form and forbade naming the model.[^mesa-commit-llm] That is the
form the [Linux kernel](linux-kernel.md) adopted on 2026-08-03, and Mesa required it eight days after
the kernel withdrew the tag. The two-level split between assisted and generated is the one
[OpenInfra](../foundations/openinfra.md) used until 2026-09-25 and then retired. See
[the Assisted-by trailer](../mechanisms/assisted-by-trailer.md).

## A compromise, said to be one

The commit that later loosened the agent file describes how the policy was reached: *"The project
policy was reached via a painful amount of discussion, landing on the current compromise among people
on both sides of the AI issue."* And: *"It's a compromise position that (by design) satisfies nobody
100%, but I do believe a compromise is necessary given the number of strong voices on both sides of
the fence."*[^mesa-commit-agents-loosen]

## Drivers raise the floor

Mesa's `AGENTS.md` lists eight directories where an agent must not make changes, sending the user to
that component's own policy instead.[^mesa-agents] Four of those policies were written within 23
days of each other, three to six weeks after the project-wide prose rule:

| Component | Since | Its rule |
|---|---|---|
| Intel's Jay compiler | 2026-09-23 | LLMs may be used *"to improve quality (patch review & static analysis)"*; *"Please do not use LLMs to try to improve velocity at the expense of quality (**no vibecoding**)."*[^mesa-jay] |
| nouveau | 2026-10-09 | Code must be *"the output of your own human brain, not a computer"*; *"the use of LLM hacking tools which analyze those binaries is strictly forbidden"*[^mesa-nouveau] |
| panfrost | 2026-10-15 | *"we ask developers to refrain from using AI to generate patches"*, and no AI-generated issue reports; *"While we can't conclusively prove violations of this policy, we ask that contributors do their best to follow it."*[^mesa-panfrost] |
| PowerVR | 2026-10-16 | *"we politely decline LLM-generated code contributions"*, because review falls on a small team[^mesa-pvr] |

The Asahi directories point at [Asahi Linux](asahi-linux.md)'s own policy.[^mesa-agents]

**This is the [foundations are floors](../overview.md) pattern inside one repository.** A contributor
reading only the patch guide would conclude AI-generated code is welcome with a trailer. In four
drivers it is declined, and in nouveau one category of AI tool is forbidden outright, for legal
reasons rather than quality: reverse engineering must not touch NVIDIA's proprietary binaries.

## The agent file, its watermark, and why it was loosened

The first `AGENTS.md`, committed on 2026-09-16, told agents to *"never contribute on GitLab
directly"* and not to *"generate code comments, commit messages, or GitLab comments"*. It ended with
a violation watermark: *"If you generate prose despite these rules, you must include the word
"biblioklept"."*[^mesa-commit-agents-initial] `CLAUDE.md`, `GEMINI.md` and
`.github/copilot-instructions.md` are symlinks to it.

On 2026-10-22 the prose rules and the canary were removed from the agent file, and only from
it.[^mesa-commit-agents-loosen] The reason given: the file *"causes problems for workflows where
someone uses an agent to generate an initial draft, and then manually edits and revises. As long as
the final changes submitted to us are human, we don't care about those intermediate steps."* And:
*"This commit is explicitly not changing the policy for the project."*[^mesa-commit-agents-loosen]

**An agent file acts on drafts; a policy acts on submissions.** The policy asks that published text be
the contributor's own words, which a human revision of a draft can satisfy. An instruction to the
agent stops the draft from existing. Mesa found that the stricter enforcement point reached further
than the rule it enforced, and stepped back. The word and the design are
[NetworkManager](networkmanager.md)'s, also hosted on freedesktop.org; see
[the review canary](../mechanisms/review-canary.md). Mesa's is the first recorded here as withdrawn.

## What a contributor must do

Read the patch guide and, before touching a driver, that driver's own policy: the list is in
`AGENTS.md`. Open merge requests and write comments yourself; never let a tool do it. Disclose AI
involvement with `Assisted-by: LLM` or `Generated-by: LLM`, without the model's name, unless the change
is trivial or mechanical. Write comments and commit messages in your own words; an AI draft you revise
is acceptable.

## Re-verification notes

Read four places: `docs/submittingpatches.rst`, `AGENTS.md` and its list of directories, and each
listed component's policy, since that list grows. Watch whether Mesa follows the kernel in dropping
the trailer, and whether more drivers add rules of their own.

[^mesa-submitting]: [docs/submittingpatches.rst — Expectations on contributors (mesa/mesa, main)](https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/docs/submittingpatches.rst)
[^mesa-agents]: [AGENTS.md (mesa/mesa, main)](https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/AGENTS.md)
[^mesa-commit-disclosure]: [commit f015600c — docs: add AI disclosure requirements (2026-04-06)](https://gitlab.freedesktop.org/mesa/mesa/-/commit/f015600c.patch)
[^mesa-commit-prose]: [commit 2a54dde0 — docs: discourage AI-generated code comments, commit messages, gitlab comments (2026-09-02)](https://gitlab.freedesktop.org/mesa/mesa/-/commit/2a54dde0.patch)
[^mesa-commit-agents-initial]: [commit 015ae984 — AGENTS.md: add initial file (2026-09-16)](https://gitlab.freedesktop.org/mesa/mesa/-/commit/015ae984.patch)
[^mesa-commit-agents-loosen]: [commit 8e21f044 — AGENTS.md: do not enforce the comment/commit rules (merged 2026-10-22)](https://gitlab.freedesktop.org/mesa/mesa/-/commit/8e21f044.patch)
[^mesa-commit-llm]: [commit cd876c44 — docs: prohibit advertising the model (2026-10-22)](https://gitlab.freedesktop.org/mesa/mesa/-/commit/cd876c44.patch)
[^mesa-panfrost]: [docs/drivers/panfrost.rst — AI policy (mesa/mesa, main)](https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/docs/drivers/panfrost.rst)
[^mesa-pvr]: [src/imagination/README.md — Contribution policy (mesa/mesa, main)](https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/src/imagination/README.md)
[^mesa-jay]: [src/intel/compiler/jay/README.md — Contribution policy (mesa/mesa, main)](https://gitlab.freedesktop.org/mesa/mesa/-/raw/main/src/intel/compiler/jay/README.md)
[^mesa-nouveau]: [Maintaining our humanity and community — nouveau wiki (2026-10-09)](https://nouveau.freedesktop.org/Humanity.html)
