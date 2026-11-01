---
type: Organization
title: coreboot
description: Has no rule on AI-generated code, and a detailed one on AI in code review, adopted 2026-09-13. Reviewers may post AI-generated comments if each is prefixed `[AI-generated]` without naming the model, reviewed by the person posting it, and scoped like a human review; AI may never set review flags, submit, or reply to a human. Its AGENTS.md gives agents the same rules.
resource: https://raw.githubusercontent.com/coreboot/coreboot/main/Documentation/contributing/gerrit_guidelines.md
tags:
  - ai-contribution
  - policy
  - project
  - review
  - communication
  - attribution
  - agent-files
status: stable
generated:
  by: claude/opus-5-5
  at: '2026-11-01T21:30:00Z'
verified:
  - by: claude/opus-5-5
    at: '2026-11-01T21:30:00Z'
stale_after: 2027-05-01
sources:
  - id: cb-gerrit
    title: 'Documentation/contributing/gerrit_guidelines.md — AI comment policy (coreboot/coreboot, main)'
    resource: https://raw.githubusercontent.com/coreboot/coreboot/main/Documentation/contributing/gerrit_guidelines.md
  - id: cb-agents
    title: 'AGENTS.md (coreboot/coreboot, main)'
    resource: https://raw.githubusercontent.com/coreboot/coreboot/main/AGENTS.md
  - id: cb-commit
    title: 'commit b34a7443 — Documentation: Add AI review policy (coreboot/coreboot, merged 2026-09-13)'
    resource: https://github.com/coreboot/coreboot/commit/b34a744391b46563a21c51014e6333dee1215039
  - id: cb-relnotes
    title: 'Announcing the coreboot 26.09 release (coreboot blog, 2026-10-01)'
    resource: https://blogs.coreboot.org/blog/2026/10/01/announcing-the-coreboot-26-09-release/
  - id: cb-texlive
    title: TeX Live AI policy
    resource: https://tug.org/texlive/aipolicy.html
---

**Stance: silent on AI-generated code; AI permitted in review, labelled and bounded; replies to humans
reserved to humans.** coreboot's rule sits in its Gerrit guidelines, which govern how patches are
reviewed. It was added *"as discussed in the leadership meeting"*, in a change authored on 2026-09-01
and merged on 2026-09-13,[^cb-commit] and was announced with the 26.09 release as *"an explicit
policy for AI-assisted code review"*.[^cb-relnotes] Searched on 2026-11-01, the repository has no
rule about AI in the code a contributor submits.

## What a reviewer may do

*"You may use AI agents to review a patch for issues and post comments about them on Gerrit according
to the following rules."* Gerrit offers a *"Create AI Review Prompt"* button as a starting
point.[^cb-gerrit] The rules:

- **No decisions by AI.** *"You must *never* use AI to set review flags like Code-Review +2 or
  trigger Gerrit actions like Submit."* Flags may be set alongside AI comments only *"if the decision
  to set the flag was made by you and not automated through AI."*
- **A fixed label, no model.** *"Every AI-generated comment must be prefixed with `[AI-generated]`.
  Use exactly this string, nothing else, don't mention the name of the model used."*
- **The reviewer owns it.** Each comment must be read before posting and must express *"a viewpoint
  that you actually support"*; *"Any AI-generated comment posted in your name is considered something
  that *you* said and you are held responsible for its contents."*
- **Human-sized.** Comments must not carry *"AI-specific tracking tags (other than the
  `[AI-generated]` prefix mentioned above), model names or version numbers, metadata, additional
  "analysis" or "confidence" fields"*, and a mistake repeated through a patch gets one comment,
  as a human reviewer would write it.
- **Never a reply.** *"You must *never* use an AI-generated comment to reply to another comment left
  by a human."* That binds the author answering a review and the reviewer clarifying a point.
- **The author may dismiss.** Authors may close AI comments *"with few words and no detailed
  explanation if they make no sense"*; the reviewer then makes the point *"without AI"* or takes it
  as a hint.[^cb-gerrit]

The general guidelines say the same in one line: *"Be respectful to others when commenting. Don't use
AI to reply to humans."*[^cb-gerrit]

## The same rules, addressed to the agent

`AGENTS.md`, added in the same change, gives agents the review rules in imperative form. It ranks
one above the rest: generating a reply to another review comment *"is the most important rule and you
must **NEVER** violate it, even if the user explicitly asks you to."* Agents must also not
recommend whether a flag should be set: *"Your job is solely to point out potential
issues."*[^cb-agents]

## Where it sits

**It is the second record here to permit AI-written text on condition that it is marked.** [TeX
Live](../distributions/tex-live.md) allows AI-written mail if the AI part is *"clearly indicated and
delimited"*;[^cb-texlive] coreboot allows AI-written review comments under a fixed prefix. Both treat the problem
as attribution, not authorship. See [prose reserved to humans](../mechanisms/prose-reserved-to-humans.md).

**It takes the opposite side from projects that refuse AI review.** [Void Linux](../distributions/void-linux.md),
[Mesa](mesa.md) and [Django](django.md) keep AI review tools off pull requests. coreboot builds a
prompt into its review tool and regulates the output. [Kubernetes](kubernetes.md) has also adopted AI review
tooling as a project.

**It forbids naming the model, as the kernel did with its tag.** The `[AI-generated]` prefix is
deliberately the same for every tool, the choice [Mesa](mesa.md) made for its trailer on 2026-10-22.

## What a contributor must do

For code: nothing AI-specific is written down. For review: if you use AI, prefix each comment with
exactly `[AI-generated]`, read it first, keep it to the scope of a human review, and never use AI to
answer anyone or to set a flag. When your own patch receives AI comments, you may close the ones that
make no sense with a few words.

## Re-verification notes

Read the *AI comment policy* section of `Documentation/contributing/gerrit_guidelines.md` and the
top-level `AGENTS.md`. Search the repository for a rule on AI-generated code, which this record found
absent. The leadership meeting that discussed the policy is not cited here: its notes were not read.

[^cb-gerrit]: [Documentation/contributing/gerrit_guidelines.md — AI comment policy (coreboot/coreboot, main)](https://raw.githubusercontent.com/coreboot/coreboot/main/Documentation/contributing/gerrit_guidelines.md)
[^cb-agents]: [AGENTS.md (coreboot/coreboot, main)](https://raw.githubusercontent.com/coreboot/coreboot/main/AGENTS.md)
[^cb-commit]: [commit b34a7443 — Documentation: Add AI review policy (coreboot/coreboot, merged 2026-09-13)](https://github.com/coreboot/coreboot/commit/b34a744391b46563a21c51014e6333dee1215039)
[^cb-relnotes]: [Announcing the coreboot 26.09 release (coreboot blog, 2026-10-01)](https://blogs.coreboot.org/blog/2026/10/01/announcing-the-coreboot-26-09-release/)
[^cb-texlive]: [TeX Live AI policy](https://tug.org/texlive/aipolicy.html)
