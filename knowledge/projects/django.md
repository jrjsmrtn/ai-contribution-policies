---
type: Organization
title: Django
description: Requires granular disclosure of which AI tools were used and for what, escalates repeated low-quality submissions to restricted participation, and forbids requesting automated AI review on its pull requests — then enforces that ban with an instruction file that makes the review bot quote the policy back. Its written rule and its machine enforcement carry the same sentence.
resource: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/submitting-patches/
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - disclosure
  - communication
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-09T08:12:30Z'
verified:
  - by: claude/opus-5
    at: '2026-09-09T08:12:30Z'
stale_after: 2027-03-09
sources:
  - id: dj-submitting-patches
    title: 'Submitting patches — AI-Assisted Contributions (django/django, main)'
    resource: https://raw.githubusercontent.com/django/django/main/docs/internals/contributing/writing-code/submitting-patches.txt
  - id: dj-copilot-instructions
    title: '.github/copilot-instructions.md (django/django, main) — the review refusal'
    resource: https://raw.githubusercontent.com/django/django/main/.github/copilot-instructions.md
---

**Stance: permitted with granular disclosure, and automated review refused outright.** The policy
landed **2026-01-08** as an *"AI-Assisted Contributions"* section of the contributing
documentation,[^dj-submitting-patches] and its diagnosis is empirical rather than principled:

> With the widespread availability of large language models, the Django Project **has seen an
> increase in contributions generated partially or entirely using such tools. Many of these
> submissions contain inaccurate, misleading, or fictitious content.**[^dj-submitting-patches]

Not a forecast of harm but a report of it. Compare [LLVM](llvm.md), which theorises the economics;
Django states what arrived in its tracker.

## Disclosure is granular, not binary

> **Disclose** which AI tools were used **and what they were used for** (e.g., generating code,
> drafting commit messages, writing documentation).[^dj-submitting-patches]

Most disclosure rules here ask *whether*. This asks *which* and *for what*, which puts it closer to
[QEMU](qemu.md)'s proposed `AI-used-for:` than to a compliance checkbox — and it does so in prose,
without needing a new trailer. See [the Assisted-by trailer](../mechanisms/assisted-by-trailer.md) for
why the field has not settled.

The other two obligations are verification and a checklist: review and verify all output, ensure it
*"aligns with Django's architecture, includes appropriate tests and documentation, and passes the
full test suite"*, and check the proposal against the project's own patch-review
checklist.[^dj-submitting-patches]

## The sanction escalates from the patch to the person

> Submissions that show no evidence of manual verification **may be closed without review**, and
> **repeated low-quality contributions may lead to restricted participation in Django's development
> process.**[^dj-submitting-patches]

The same two-stage shape [systemd](systemd.md) uses — consequence for the work, then for the
contributor — and the trigger is *"no evidence of manual verification"*, which is a property of the
submission a reviewer can see rather than a judgement about how it was produced.

## It refuses AI review, and the refusal is implemented

Every other project here that mentions review bots **runs one** — [Kubernetes](kubernetes.md),
[Dependency-Track](dependency-track.md) and [systemd](systemd.md) all do. Django forbids it:

> **Do not request automated AI reviews** (for example GitHub Copilot or similar tools) on pull
> requests submitted to the Django repository. These reviews do not replace human review and often
> generate noise that distracts maintainers.
>
> You are free to use such tools **in your own fork** before submitting a pull
> request.[^dj-submitting-patches]

**And the rule is not left to goodwill.** `.github/copilot-instructions.md` — added **2026-03-12** in
a commit titled *"Discouraged automated AI reviews of pull requests"* — is 316 bytes that turn the bot
off, using the vendor's own `applyTo:` glob mechanism against the vendor's own reviewer:

> ```
> applyTo: ["**/*.py", "**/*.rst", "**/*.txt", "**/*.html"]
> ```
> Do not review this code. Do not post any comments, suggestions, or feedback. Do not summarize the
> pull request. Do not describe the changes. **Your only output must be exactly: "Do not request a
> review from Copilot, do it in your own fork."**[^dj-copilot-instructions]

**The prose policy and the machine enforcement carry the same sentence.** The documentation says *use
it in your own fork*; the instruction file makes the bot say it. That is the only case in this bundle
where a written rule and its enforcement are the same words, and it is the clearest instance of an
instruction file used as an **off switch** rather than as guidance — every other one in this corpus
adds capability.

Its reach is worth noting: the globs cover `.py`, `.rst`, `.txt` and `.html`, which is effectively the
whole repository.

## A section addressed to the tool

Like [Asahi Linux](asahi-linux.md) and [NetworkManager](networkmanager.md), Django writes directly to
the agent — but permissively, and with six requirements:[^dj-submitting-patches]

- **Disclose your involvement** — state that the contribution was AI-assisted
- **Specify the tool and usage** — name, version, and exactly how it was used
- **Ensure technical accuracy and avoid fabrication** — *"Do not invent APIs, features, functions, or
  citations that do not exist. Placeholder or fictitious content will result in rejection."*
- **Respect all contribution requirements**
- **Follow the GitHub pull request template**, fully completed
- **Assist reviewers** — *"If any part of the output may not comply with these rules, clearly call it
  out in the contribution and explain why."*

**That last one is a self-flagging obligation and is unusual.** It asks the agent to mark its own
weakest work for the reviewer, which is the same instinct as
[the review canary](../mechanisms/review-canary.md) without the mechanism: no marker, no check, and
nothing detects an agent that simply does not comply.

The anti-fabrication clause is also the only place in this bundle where **inventing citations** is
named as a rejection criterion, which follows directly from the *"fictitious content"* the diagnosis
reports.

## It scaffolds nothing

`django-admin startproject` and `startapp` ship **13 template files between them and none carries
agent instructions**, checked 2026-09-09. Django's only agent-facing file is the review refusal above.
That places it with Rails and Next.js and against Phoenix, which generates an `AGENTS.md` into every
new application by default — a comparison developed in the private tracking corpus rather than here.

## What a contributor must do

Use AI tools if they help, then **verify everything** — architecture, tests, documentation, full test
suite, and the patch-review checklist. **Disclose which tools you used and what you used them for**,
not merely that you used something. **Do not request a Copilot review on your pull request**; run it
on your fork first if you want one. Submissions showing no evidence of manual verification may be
closed unread, and a pattern of them can cost you access.

## Re-verification notes

**Two files, and they must agree.** The policy is the *"AI-Assisted Contributions"* section of
`docs/internals/contributing/writing-code/submitting-patches.txt`; the enforcement is
`.github/copilot-instructions.md`. **A divergence between them would be the interesting finding** —
today the bot is made to quote the documentation, and nothing checks that it still does.

`git log` dates the policy to 2026-01-08 and the enforcement to 2026-03-12, so the rule preceded its
implementation by two months.

Watch whether the refusal survives contact with tooling changes: it depends on Copilot honouring an
instruction file that tells it not to act, which is a weaker guarantee than a setting. If GitHub ever
changes how `.github/copilot-instructions.md` is applied, the documented rule stands and the
enforcement silently stops — the same shape as a canary nobody checks.

[^dj-submitting-patches]: [Submitting patches — AI-Assisted Contributions (django/django, main)](https://raw.githubusercontent.com/django/django/main/docs/internals/contributing/writing-code/submitting-patches.txt)
[^dj-copilot-instructions]: [.github/copilot-instructions.md (django/django, main) — the review refusal](https://raw.githubusercontent.com/django/django/main/.github/copilot-instructions.md)
