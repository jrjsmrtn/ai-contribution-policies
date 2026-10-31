---
type: Organization
title: Python (CPython)
description: Permits AI tools in contributions, resting on contributor responsibility and the ability to explain the change in one's own words; disclosure is appreciated but not required. Since 2026-10 two labels and a bot apply the guidance, one asking for an explanation and leaving the issue or pull request open, the other closing it, and triagers are told not to apply either only because AI was used or disclosed.
resource: https://devguide.python.org/getting-started/ai-tools/
tags:
  - ai-contribution
  - policy
  - project
  - permitted
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T23:45:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T23:45:00Z'
  - by: claude/opus-5-5
    at: '2026-10-31T12:00:00Z'
stale_after: 2027-04-30
sources:
  - id: python-devguide-ai-tools
    title: 'Guidelines for using AI tools — Python Developer''s Guide'
    resource: https://devguide.python.org/getting-started/ai-tools/
  - id: python-triage-team
    title: 'Python triage team — Applying the AI policy labels, Python Developer''s Guide'
    resource: https://devguide.python.org/triage/triage-team/
  - id: python-devguide-1947
    title: 'python/devguide PR 1947 — Update Docs about AI policy enforcement (merged 2026-10-28)'
    resource: https://github.com/python/devguide/pull/1947
  - id: python-generative-ai-old
    title: 'getting-started/generative-ai.rst, the page replaced on 2026-05-21 (python/devguide, commit 42d2e0f2)'
    resource: https://raw.githubusercontent.com/python/devguide/42d2e0f2f971c467a98ee09f0773538928f8e72d/getting-started/generative-ai.rst
---

**Stance: permitted, with responsibility as the whole mechanism.** The Python Developer's Guide carries
guidelines on AI tools whose operative sentence is:

> The person submitting an issue or PR is responsible for its content, regardless of whether AI
> tools were used in its creation.[^python-devguide-ai-tools]

The survey being replaced filed Python under "developing guidelines". It has published ones, and
they have been revised several times.

## Disclosure is appreciated, not required

This is the distinguishing choice. *"Disclosure of the use of AI tools in the PR description is
appreciated, while not required. Be prepared to explain how the tool was used and what changes it
made."* The test underneath is explanation: *"We expect PR authors and those filing issues to be able
to explain their proposed changes in their own words."*[^python-devguide-ai-tools]

Compare the alternatives now visible across this bundle: [Ansible](ansible.md) says disclosure
SHOULD happen above a significance threshold; the [Linux kernel](linux-kernel.md) requires a
structured tag; [Rust](rust.md)'s policy makes it mandatory for a whole tier and treats lying as a
Code of Conduct violation. Python declines all three and keeps only the **explain-it test**, which
is the same test [Git](git.md) reaches by a different route.

## What is explicitly acceptable

*"Assistance with writing comments, especially in a non-native language"*, *"Gaining understanding
of existing code"*, and *"Supplementing contributor knowledge for code, tests, and
documentation"*.[^python-devguide-ai-tools]

The non-native-language allowance recurs across this bundle; a policy that forbids generated prose
outright taxes non-native speakers and nothing else — see
[prose reserved to humans](../mechanisms/prose-reserved-to-humans.md).

## The one hard prohibition

> It is not acceptable to alter or bypass existing tests, or remove desired functionality, in order
> to make a failing test pass.[^python-devguide-ai-tools]

This is not an AI rule at all: it is a rule about a **failure mode AI makes cheap**. An agent
optimising for a green test suite will do exactly this, and the prohibition names the outcome rather
than the tool, so it holds however the change was produced.

## Closing is tool-neutral; the labels are not

*"Maintainers may close issues and PRs that are not useful or productive, without explanation,
regardless of whether AI tools were used or not."* A contributor who keeps opening unproductive ones
*"may be blocked from contributing to the project"*.[^python-devguide-ai-tools]

**Since 2026-10-28 the guide also says how the AI guidelines are applied.** *"Using AI tools is not a
reason on its own for an issue or PR to be labeled or closed."* A maintainer who thinks the guidelines
were not followed applies one of two labels, and a bot posts a comment linking the
guidelines:[^python-devguide-ai-tools]

- `AI-needs-explanation`: *"the issue or PR stays open. Reply in your own words: explain what the
  change does or what the issue is about, and describe how you checked that it is correct."*
- `AI-guidelines-not-met`: *"the issue or PR is closed."*

The triage team's guidance adds the rule that protects disclosure: *"Don’t apply them only because AI
tools were used, or because the author disclosed using them."* Triagers start with
`AI-needs-explanation`, and move to closing when the author does not answer or answers with more
generated text.[^python-triage-team] **Disclosing AI use cannot by itself get a contribution labelled**,
which is what keeps an optional disclosure from being a trap. The pull request that added this section
also added a line to the triage checklist pointing at the labels.[^python-devguide-1947]

## What a contributor must do

Review it. Be able to explain it in your own words, including how you checked it. Do not make a
failing test pass by changing the test. Disclosure is optional; if a maintainer adds
`AI-needs-explanation`, reply yourself, not through the tool.

## Re-verification notes

**The URL moved**: `getting-started/generative-ai/` redirects to `getting-started/ai-tools/`. The
devguide is a git repository (`python/devguide`), so `git log -- getting-started/ai-tools.rst` is the
audit trail; read `triage/triage-team.rst` with it, since the enforcement lives there.

**Corrections made on 2026-10-31.** This record quoted three passages that the page did not contain
when the record was written on 2026-08-04. One, that maintainers may close issues and PRs
*"including those that are fully generated by AI"*, is from the page replaced on
2026-05-21.[^python-generative-ai-old] The other two, a requirement to explain *the tool's usage and
modifications* and a scope of *all forms of contributions in the python GitHub org*, appear in no
version of the page and are withdrawn, with the scope claim that rested on one of them.

[^python-devguide-ai-tools]: [Guidelines for using AI tools — Python Developer's Guide](https://devguide.python.org/getting-started/ai-tools/)
[^python-triage-team]: [Python triage team — Applying the AI policy labels, Python Developer's Guide](https://devguide.python.org/triage/triage-team/)
[^python-devguide-1947]: [python/devguide PR 1947 — Update Docs about AI policy enforcement (merged 2026-10-28)](https://github.com/python/devguide/pull/1947)
[^python-generative-ai-old]: [getting-started/generative-ai.rst, the page replaced on 2026-05-21 (python/devguide, commit 42d2e0f2)](https://raw.githubusercontent.com/python/devguide/42d2e0f2f971c467a98ee09f0773538928f8e72d/getting-started/generative-ai.rst)
