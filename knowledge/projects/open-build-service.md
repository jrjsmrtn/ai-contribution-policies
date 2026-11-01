---
type: Organization
title: Open Build Service
description: openSUSE's build service permits AI-assisted contributions, requires disclosure of any generative AI use and closes pull requests whose authors cannot explain them or answer reviewers without AI. Its 2026-05-29 rule credits its wording to Kubernetes, Fedora and the kernel's rendered documentation, and still recommends the kernel's model-named trailer, which the kernel simplified on 2026-08-03 and withdrew on 2026-10-14.
resource: https://raw.githubusercontent.com/openSUSE/open-build-service/master/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - attribution
  - communication
status: stable
generated:
  by: claude/opus-5-5
  at: '2026-11-01T18:30:00Z'
verified:
  - by: claude/opus-5-5
    at: '2026-11-01T18:30:00Z'
stale_after: 2027-05-01
sources:
  - id: obs-contributing
    title: 'CONTRIBUTING.md — AI Guidance (openSUSE/open-build-service, master)'
    resource: https://raw.githubusercontent.com/openSUSE/open-build-service/master/CONTRIBUTING.md
  - id: obs-pr-19758
    title: 'openSUSE/open-build-service PR #19758 — Adapt contribution guides to fight AI slop (merged 2026-05-29)'
    resource: https://github.com/openSUSE/open-build-service/pull/19758
  - id: obs-agents-md
    title: 'AGENTS.md (openSUSE/open-build-service, master)'
    resource: https://raw.githubusercontent.com/openSUSE/open-build-service/master/AGENTS.md
  - id: obs-k8s-guidance
    title: 'contributors/guide/pull-requests.md — AI Guidance (kubernetes/community, master)'
    resource: https://raw.githubusercontent.com/kubernetes/community/master/contributors/guide/pull-requests.md
  - id: obs-fedora-policy
    title: AI-Assisted Contributions Policy — Fedora Council
    resource: https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/
---

**Stance: permitted, with mandatory disclosure and the contributor answering for the change in
person.** The Open Build Service (OBS) is openSUSE's package build and distribution system. Its
`CONTRIBUTING.md` gained an *AI Guidance* section on 2026-05-29: *"Using AI tools to help write your
contribution is acceptable, as long as you follow the principles described below."*[^obs-contributing]
This governs the build service's own code; the [openSUSE](../distributions/opensuse.md) project as a
whole has no adopted policy.

## What it asks

- **Accountability.** *"As the author, you are *accountable* for the code you submit. Contributing to
  Open Build Service means vouching for the quality, license compliance, and utility of your
  contribution."*
- **Review your own output first.** *"Do not leave the first review of AI generated changes to the
  reviewers."* A pull request whose author *"cannot explain why a change was made"* is closed.
- **Answer reviewers yourself.** *"When responding to review comments, you must do so without relying
  on AI tools."* Not engaging directly also closes the pull request.
- **Disclose any use.** *"You **MUST** disclose if you have used generative AI tools in preparing
  portions of your contribution."* The recommended method is the trailer
  `Assisted-by: AGENT_NAME:MODEL_VERSION`.[^obs-contributing]

The disclosure rule has **no threshold**. Fedora, whose accountability wording OBS borrowed, asks for
disclosure only when a significant part is taken from a tool unchanged.[^obs-fedora-policy]

## A policy assembled from three, keeping a clause the source forbids

The pull request that added the section says where its words came from: *"Wording is ~~stolen~~
inspired from"* the Kubernetes AI guidance, Fedora's policy, and the attribution section of
`docs.kernel.org`.[^obs-pr-19758] Each borrowing can be found in the result. The accountability
sentence is Fedora's.[^obs-fedora-policy] The opening and the three review sentences are Kubernetes's:
*"Using AI tools to help write your PR is acceptable"*, *"Do not leave the first review of AI
generated changes to the reviewers"*, the closing of a pull request whose author *"cannot explain why
a change was made"*, and *"Reviewers want to engage directly with you"*.[^obs-k8s-guidance] So is the
disclosure rule with no threshold. The trailer is the kernel's.

**The combination is one Kubernetes rules out.** Kubernetes puts its disclosure in the pull-request
description, and in the same section says *"using the `assisted-by`, `co-developed` or similar commit
trailer is not allowed."*[^obs-k8s-guidance] OBS took the Kubernetes disclosure rule and delivered it
through the trailer Kubernetes forbids. See
[policy by copying](../mechanisms/policy-by-copying.md) for the bundle's other cases of a policy
inheriting some clauses of a source and not others.

## The trailer format it recommends is the kernel's old one

When OBS adopted it, `AGENT_NAME:MODEL_VERSION` was the kernel's current form. The kernel replaced it
with a plain `Assisted-by: LLM` on 2026-08-03 and removed the tag altogether on 2026-10-14; see
[the Assisted-by trailer](../mechanisms/assisted-by-trailer.md). OBS's text was not updated: a commit
on 2026-10-28 edited the same file without touching the section.

**Its agent file was written after the kernel changed, and still names the model.** `AGENTS.md`,
added on 2026-09-18, tells agents that *"all AI-assisted commits must disclose generative AI usage
using the `Assisted-by:` trailer"* and gives `Assisted-by: opencode:gemini-3.6-flash` as the
example.[^obs-agents-md] The rule is being followed: on 2026-11-01 GitHub's commit search returned
46 commits in the repository carrying `Assisted-by`, nearly all in the tool-and-model form, across
at least six spellings of the tool name (`opencode`, `OpenCode`, `claude-code`, `claude_code`,
`Claude Code`, `Anthropic`). Unlike [Homebrew](homebrew.md), OBS wants the vendor named.

This is the same propagation [MacPorts](macports.md) shows, a rendered kernel page copied into
another project's rule, with one difference: here the format was current on the day it was copied,
and went stale afterwards.

## What a contributor must do

Review and test your own AI-assisted change before opening a pull request, and be ready to explain
every change. Answer review comments yourself. Disclose any generative AI use, with an `Assisted-by:`
trailer naming the agent and model as the guide shows. That form is what OBS asks for, even though
the kernel it came from no longer uses it.

## Re-verification notes

Check the *AI Guidance* section of `CONTRIBUTING.md` and the disclosure section of `AGENTS.md`
together: the first is the rule, the second is what agents are told. Watch whether either drops the
model-named form now that its source has dropped the tag, and whether the openSUSE project adopts a
policy that OBS would then sit under.

[^obs-contributing]: [CONTRIBUTING.md — AI Guidance (openSUSE/open-build-service, master)](https://raw.githubusercontent.com/openSUSE/open-build-service/master/CONTRIBUTING.md)
[^obs-pr-19758]: [openSUSE/open-build-service PR #19758 — Adapt contribution guides to fight AI slop (merged 2026-05-29)](https://github.com/openSUSE/open-build-service/pull/19758)
[^obs-agents-md]: [AGENTS.md (openSUSE/open-build-service, master)](https://raw.githubusercontent.com/openSUSE/open-build-service/master/AGENTS.md)
[^obs-k8s-guidance]: [contributors/guide/pull-requests.md — AI Guidance (kubernetes/community, master)](https://raw.githubusercontent.com/kubernetes/community/master/contributors/guide/pull-requests.md)
[^obs-fedora-policy]: [AI-Assisted Contributions Policy — Fedora Council](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/)
