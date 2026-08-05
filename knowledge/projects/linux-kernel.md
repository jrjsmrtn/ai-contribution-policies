---
type: Organization
title: Linux Kernel
description: Permits AI-assisted contributions under a merged in-tree policy that bars AI agents from signing off, requires an Assisted-by tag, and leaves the human submitter fully responsible.
resource: https://docs.kernel.org/process/coding-assistants.html
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - dco
  - attribution
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T23:10:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T23:10:00Z'
stale_after: 2027-02-04
sources:
  - id: kernel-coding-assistants
    title: AI Coding Assistants — The Linux Kernel documentation
    resource: https://docs.kernel.org/process/coding-assistants.html
  - id: kernel-coding-assistants-src
    title: Documentation/process/coding-assistants.rst (torvalds/linux, master)
    resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst
  - id: kernel-submitting-patches
    title: Documentation/process/submitting-patches.rst (torvalds/linux, master)
    resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst
---

**Stance: permitted, with mandatory attribution and a human on the hook.** The kernel has a merged,
in-tree policy — `Documentation/process/coding-assistants.rst`, 59 lines — that *"provides guidance
for AI tools and developers using AI assistance when contributing to the Linux
kernel."*[^kernel-coding-assistants-src]

This is a **change of state, not of degree**: surveys written before 2026-04 recorded the kernel
as *developing* guidelines. It has them, in the tree, where `git log` can date them — and published
as part of the kernel's own process documentation.[^kernel-coding-assistants]

## The rule that has teeth

> AI agents MUST NOT add Signed-off-by tags. Only humans can legally certify the Developer
> Certificate of Origin (DCO).[^kernel-coding-assistants-src]

The human submitter is responsible for *"Reviewing all AI-generated code"*, *"Ensuring compliance
with licensing requirements"*, *"Adding their own Signed-off-by tag to certify the DCO"*, and
*"Taking full responsibility for the contribution."*[^kernel-coding-assistants-src]

Note what this does to the DCO argument. [QEMU](qemu.md) reads the same certificate and concludes
that AI-generated content cannot satisfy it. The kernel reaches the opposite conclusion from the
same premise by **relocating the certification** — the human certifies, having reviewed, and the
tool is credited without signing. Two projects, one instrument, opposite outcomes: the DCO does not
by itself determine a policy.

## The attribution tag

    Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]

`AGENT_NAME` is the tool or framework, `MODEL_VERSION` the specific model, and the bracketed items
*"are optional specialized analysis tools used (e.g., coccinelle, sparse, smatch, clang-tidy)."*
*"Basic development tools (git, gcc, make, editors) should not be listed."* The example given
is:[^kernel-coding-assistants-src]

    Assisted-by: Claude:claude-3-opus coccinelle sparse

The stated purpose is not credit but measurement — attribution *"helps track the evolving role of AI
in the development process."*[^kernel-coding-assistants-src] A project adopting this tag is
building a dataset about itself.

**It is required, not encouraged, and that is stated in the main submission document** rather than
only in the AI-specific one. `submitting-patches.rst` carries a *"Using Assisted-by:"* section:
*"If you used any sort of advanced coding tool in the creation of your patch, you need to
acknowledge that use by adding an Assisted-by tag. Failure to do so may impede the acceptance of
your work."*[^kernel-submitting-patches] A contributor following the ordinary process meets the
requirement without ever opening the AI policy.

**Why a new token rather than `Co-developed-by:`.** The kernel's existing vocabulary makes the
obvious choice incoherent: `Co-developed-by:` denotes authorship, and every one *"must be
immediately followed by a Signed-off-by: of the associated co-author"*[^kernel-submitting-patches]
— a sign-off this policy forbids an agent from adding. `Assisted-by:` is the only shape consistent
with both rules. Guidance recommending `Co-developed-by:` for AI attribution, which circulated
widely before this policy landed, asks for a structurally invalid trailer block.

## Everything else is the ordinary process

Contributions must follow `development-process.rst`, `coding-style.rst` and
`submitting-patches.rst`; be *"compatible with GPL-2.0-only"*; and *"Use appropriate SPDX license
identifiers."*[^kernel-coding-assistants-src] There is no separate review track, no volume cap and
no listed exception — the policy adds a prohibition, a tag and a responsibility statement to the
existing process rather than creating a parallel one.

## What a contributor must do

Review what the tool produced, well enough to defend it. Add your own `Signed-off-by`. Add
`Assisted-by:` in the documented format. Do not let an agent add a `Signed-off-by` under any
circumstance — that is the one hard prohibition in the document.

## Re-verification notes

The file is in-tree, so `git log --follow Documentation/process/coding-assistants.rst` is the audit
trail and is authoritative over any rendered page. Watch specifically for the tag format changing:
the `AGENT_NAME:MODEL_VERSION` shape is unusual, and a mechanically-applied tag that no longer
matches the spec is worse than none.

[^kernel-coding-assistants]: [AI Coding Assistants — The Linux Kernel documentation](https://docs.kernel.org/process/coding-assistants.html)
[^kernel-coding-assistants-src]: [Documentation/process/coding-assistants.rst (torvalds/linux, master)](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst)
[^kernel-submitting-patches]: [Documentation/process/submitting-patches.rst (torvalds/linux, master)](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst)
