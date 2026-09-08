---
type: Practice
title: The Assisted-by trailer
description: A git commit trailer that predates the AI question — the kernel defines it for any advanced coding tool, coccinelle and sparse included — which projects then reached for to record AI use. Four projects require it, five forbid it, three replaced it with a different field, and two of the bans give incompatible reasons. It is not portable between projects and is being displaced by disclosure in the pull request.
resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst
tags:
  - ai-contribution
  - mechanism
  - attribution
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-08T23:29:44Z'
verified:
  - by: claude/opus-5
    at: '2026-09-08T23:29:44Z'
stale_after: 2027-03-08
sources:
  - id: kernel-submitting-patches
    title: 'Documentation/process/submitting-patches.rst (torvalds/linux, master) — Using Assisted-by, and the Co-developed-by rule'
    resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst
  - id: kernel-coding-assistants
    title: 'Documentation/process/coding-assistants.rst (torvalds/linux, master)'
    resource: https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst
  - id: gtk-contributing-trailer
    title: 'CONTRIBUTING.md (GNOME/gtk, main)'
    resource: https://gitlab.gnome.org/GNOME/gtk/-/raw/main/CONTRIBUTING.md
  - id: k8s-guide-trailer
    title: 'contributors/guide/pull-requests.md — AI Guidance (kubernetes/community, master)'
    resource: https://raw.githubusercontent.com/kubernetes/community/master/contributors/guide/pull-requests.md
  - id: nerves-contributing-trailer
    title: 'CONTRIBUTING.md (nerves-project/nerves, main)'
    resource: https://raw.githubusercontent.com/nerves-project/nerves/main/CONTRIBUTING.md
  - id: openinfra-policy-trailer
    title: 'AI Generated Content Policy — OpenInfra Foundation'
    resource: https://openinfra.org/legal/ai-policy
  - id: asf-tooling-trailer
    title: 'Generative Tooling Guidance — The Apache Software Foundation'
    resource: https://www.apache.org/legal/generative-tooling.html
  - id: qemu-relax-trailer
    title: 'QEMU code provenance relaxation proposal (qemu-devel, 2026-05)'
    resource: https://lists.nongnu.org/archive/html/qemu-devel/2026-05/msg07614.html
---

**It is not an AI trailer.** That is the fact most readings of it get wrong, and it explains both why
projects reached for it and why it fits badly.

The Linux kernel defines `Assisted-by:` for **tools in general**:

> If you used **any sort of advanced coding tool** in the creation of your patch, you need to
> acknowledge that use by adding an Assisted-by tag. **Failure to do so may impede the acceptance of
> your work.**[^kernel-submitting-patches]

Its worked example lists a model beside two static analysers — `Assisted-by: LLM coccinelle sparse` —
and it explicitly excludes the ordinary ones: *"Basic development tools (git, gcc, make, editors)
should not be listed."*[^kernel-coding-assistants] **An LLM is a member of a category here, not the
category.** A project adopting the trailer for AI alone is narrowing a general instrument, and
several of the disagreements below follow from that.

## Four rules, and they are mutually exclusive

| Rule | Who | Form |
|---|---|---|
| **Required, model omitted** | [Linux kernel](../projects/linux-kernel.md) | `Assisted-by: LLM [TOOL1] [TOOL2]` |
| **Required, model named** | [Nerves](../projects/nerves.md), [Ansible](../projects/ansible.md) | `AGENT_NAME:MODEL_VERSION`, `[tool name/version]` |
| **Required** | [GCC](../projects/gcc.md) | `Assisted-by:` |
| **Forbidden** | [GTK](../projects/gtk.md), [Kubernetes](../projects/kubernetes.md), [Dependency-Track](../projects/dependency-track.md), [systemd](../projects/systemd.md), [NetworkManager](../projects/networkmanager.md) | — |
| **Replaced** | [ASF](../foundations/apache-software-foundation.md) `Generated-by:`; [OpenInfra](../foundations/openinfra.md) both, distinguished; [QEMU](../projects/qemu.md) proposed `AI-used-for:` | — |

[MacPorts](../projects/macports.md) has a proposal quoting a form the kernel had already retired; it
is not adopted.

**The same tag carries three incompatible requirements — required without the model, required with
the model, forbidden — and the first two moved apart within eleven days.** The kernel narrowed
`Assisted-by:` to the bare literal `LLM` on 2026-08-03 because naming models *"provides free
advertising to proprietary software companies"*; Nerves adopted `AGENT_NAME:MODEL_VERSION` on
2026-08-14, mandating the grammar the kernel had just abandoned.[^nerves-contributing-trailer] The
dates are checkable and **no influence is claimed in either direction.**

## Two bans, two reasons, and neither implies the other

[GTK](../projects/gtk.md) forbids the trailer because it is *"free advertising for AI
companies"*.[^gtk-contributing-trailer] [Kubernetes](../projects/kubernetes.md) forbids it because it
dilutes accountability — *"if something breaks, there needs to be a human who understands why and can
fix it."*[^k8s-guide-trailer]

**GTK's argument is the kernel's argument, and they reached opposite conclusions from it.** One
deleted the vendor from the tag; the other deleted the tag. A project persuaded by the advertising
objection has no reason to accept the accountability one, or the reverse — which is the clearest
demonstration in this bundle that **a shared premise does not determine a mechanism.**

## `Co-developed-by:` cannot carry a tool, structurally

It was widely reached for before policies landed, and it is invalid by construction:

> Since `Co-developed-by:` **denotes authorship**, every `Co-developed-by:` must be **immediately
> followed by a `Signed-off-by:` of the associated co-author**.[^kernel-submitting-patches]

The kernel's own AI guidance says *"Do not add a Signed-off-by tag"* for assistant-produced
work.[^kernel-coding-assistants] **So the trailer demands a certification the same project forbids the
agent to give.** That is not a policy choice that could go either way; it is why a distinct token had
to be coined rather than an existing one reused, and why the projects that ban AI co-authorship
([systemd](../projects/systemd.md), [NetworkManager](../projects/networkmanager.md),
[Dependency-Track](../projects/dependency-track.md)) name `Co-developed-by:` and `Co-authored-by:`
alongside `Assisted-by:`.

## The practical consequence: it is not portable

A contributor who learned the tag in one project breaks another's rule by applying it. **The kernel's
form is forbidden by GTK. Nerves' form is the one the kernel abandoned. GCC wants it; Kubernetes
closes pull requests that carry it.** There is no convention to follow, only per-project rules, and
tooling that emits these tags must key on the destination repository rather than on a default.

Two further incompatibilities sit under the same field name. **Value grammars differ** — a trailer
formatted for the kernel is not a valid Ansible one. And **OpenInfra's labels are mutable**: a
reviewer may remove one *"if substantial human reworking occurs"*.[^openinfra-policy-trailer]
Everywhere else the tag records history and is permanent. Those are incompatible readings of what a
provenance tag *is*, and a mutable history-tag is simply an inaccurate one.

## What is displacing it

The field is losing ground to **disclosure in the pull request**, which is what
[Kubernetes](../projects/kubernetes.md), [GTK](../projects/gtk.md) and
[NetworkManager](../projects/networkmanager.md) require instead — prose in the request rather than a
token in the commit. That is consistent with the bans: the commit stays clean and the request carries
the account.

Two alternatives kept the commit and changed the field. [ASF](../foundations/apache-software-foundation.md)
uses `Generated-by:`, reasoning from licence compatibility and third-party rights rather than from
attribution.[^asf-tooling-trailer] [OpenInfra](../foundations/openinfra.md) uses **both**, and states the
distinction: `Assisted-By:` for *predictive* tools such as auto-complete, `Generated-By:` for
*generative* ones.[^openinfra-policy-trailer] **That is the only place the vocabulary is split by what
the tool did rather than by whether one was used**, and it is the sharpest version of the field
available.

[QEMU](../projects/qemu.md)'s pending proposal reframes the job entirely with `AI-used-for:`,
recording **where** AI was used rather than that it was, and says why that differs: `Assisted-by`
*"doubles as a check that the author has read the policy."*[^qemu-relax-trailer] **So a project
choosing a trailer is choosing between proving compliance and directing a reviewer's attention** —
two different jobs one field has been asked to do, which is part of why none of this has settled.

## Why it works badly as a mechanism

**It is unverifiable.** Nothing checks that a trailer is present when it should be, or absent when it
should not be; the tag records a claim, and the only enforcement anywhere in this bundle is
[NetworkManager](../projects/networkmanager.md) grepping commit messages for trailers it forbids —
enforcement of the ban, never of the requirement.

**It attributes at the wrong granularity.** A commit-level tag says a tool touched the patch; it
cannot say which hunk, which is the question a reviewer actually has. QEMU's `AI-used-for:` is an
attempt at that and remains a proposal.

**And the disagreement is not converging.** Nine projects and foundations here hold five positions
between them, the two most recent adoptions moved apart rather than together, and the newest records
in this bundle mostly forbid the field rather than adopt it. **Treat `Assisted-by:` as a per-project
convention, not a standard**, and read the destination's rule before emitting one.

## What to watch

Whether the bans keep outnumbering the requirements among new policies — the trend across 2026 is
towards prohibition plus pull-request disclosure. Whether OpenInfra's predictive/generative split is
picked up anywhere else, since it is the only refinement of the field that adds information. And
whether QEMU's `AI-used-for:` lands, which would be the first token designed for the job rather than
borrowed for it.

[^kernel-submitting-patches]: [Documentation/process/submitting-patches.rst (torvalds/linux, master) — Using Assisted-by, and the Co-developed-by rule](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst)
[^kernel-coding-assistants]: [Documentation/process/coding-assistants.rst (torvalds/linux, master)](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst)
[^gtk-contributing-trailer]: [CONTRIBUTING.md (GNOME/gtk, main)](https://gitlab.gnome.org/GNOME/gtk/-/raw/main/CONTRIBUTING.md)
[^k8s-guide-trailer]: [contributors/guide/pull-requests.md — AI Guidance (kubernetes/community, master)](https://raw.githubusercontent.com/kubernetes/community/master/contributors/guide/pull-requests.md)
[^nerves-contributing-trailer]: [CONTRIBUTING.md (nerves-project/nerves, main)](https://raw.githubusercontent.com/nerves-project/nerves/main/CONTRIBUTING.md)
[^openinfra-policy-trailer]: [AI Generated Content Policy — OpenInfra Foundation](https://openinfra.org/legal/ai-policy)
[^asf-tooling-trailer]: [Generative Tooling Guidance — The Apache Software Foundation](https://www.apache.org/legal/generative-tooling.html)
[^qemu-relax-trailer]: [QEMU code provenance relaxation proposal (qemu-devel, 2026-05)](https://lists.nongnu.org/archive/html/qemu-devel/2026-05/msg07614.html)
