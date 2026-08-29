---
type: Organization
title: NetworkManager
description: Permits AI assistance and requires no disclosure of it at all — no tag, no declaration. Prose is reserved to humans, the ability to discuss your own patch with a reviewer is the enforcement mechanism, and unreviewed machine-generated merge requests are closed. It also has no DCO, so certification runs through an LGPL relicensing commitment instead.
resource: https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/main/CONTRIBUTING.md
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - communication
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-29T03:25:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-29T03:25:00Z'
stale_after: 2027-02-28
sources:
  - id: nm-contributing
    title: 'CONTRIBUTING.md — Guidelines for Contributing (NetworkManager, main)'
    resource: https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/CONTRIBUTING.md
  - id: nm-policy-commit
    title: 'commit 565a3422 — CONTRIBUTING: add a policy for AI coding assistants'
    resource: https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/commit/565a342281d6cf32885783f87c008734a235f779
---

**Stance: permitted, with no disclosure requirement whatsoever.** NetworkManager added an *"AI coding
assistants"* section to `CONTRIBUTING.md` on **2026-08-07**.[^nm-policy-commit] It is nine sentences
long, asks for no tag, no trailer and no declaration, and is still one of the more demanding policies
in this bundle — because what it asks for is not a disclosure but a demonstration.

## The whole policy

> Authors are responsible for 100% of the code they submit. Do not send a patch you cannot explain,
> and do not send one you have not built and tested yourself.
>
> Write your own commit messages and Merge Request descriptions. Those explain why you are making the
> change, which is the part a tool cannot know.
>
> Respond to review comments yourself. If you cannot discuss your own patch with a reviewer, it will
> not be merged.
>
> Everything in the Legal section applies unchanged. You are the one certifying that the contribution
> can be released under LGPL-2.1-or-later. A tool cannot certify that for you.
>
> Large machine-generated Merge Requests that no human has reviewed line by line will be
> closed.[^nm-contributing]

## Demonstration, not detection or declaration

This bundle's [overview](../overview.md) separates policies that try to **detect** AI-generated work
from those that require you to **declare** it. NetworkManager does neither, and lands on a third
thing:

> Respond to review comments yourself. If you cannot discuss your own patch with a reviewer, it will
> not be merged.[^nm-contributing]

**The test is conducted in review, on the contributor, in public, and it is not fakeable by the
tool** — the reviewer does not need to determine how the patch was produced, only whether the person
sending it can defend it. That sidesteps the enforcement problem that [Rust](rust.md)'s draft
concedes and that [Git](git.md)'s detection-flavoured guidance runs into, without asking anyone to
self-report.

It is also, unusually, a rule whose sanction is stated: *"it will not be merged"*, and for volume,
*"Large machine-generated Merge Requests that no human has reviewed line by line will be closed."*
**A volume threshold with a stated consequence** is rarer here than the threshold alone.

## Prose is reserved to humans, with a reason

> Write your own commit messages and Merge Request descriptions. Those explain why you are making the
> change, which is the part a tool cannot know.[^nm-contributing]

The *reason* is what makes this worth copying. Elsewhere the prose restriction is asserted rather
than argued — [Debian](../distributions/debian.md)'s Proposal C would have required human-drafted
messages and its Proposal G put communication in scope, neither adopted;
[TeX Live](../distributions/tex-live.md) bars undelimited AI-written mail; [Zig](zig.md) goes furthest
and forbids even discussing chatbot use. NetworkManager grounds it in what a commit message is *for*:
the change is in the diff, the *why* is only in the author's head, so delegating the prose deletes
the one thing the prose exists to carry.

**The author's own framing is stronger than the adopted text**, which is worth noting rather than
smoothing over. The commit message says the policy states *"AI assistance is prohibited in
communication"*.[^nm-policy-commit] The text in `CONTRIBUTING.md` is written as an instruction —
*"Write your own"*, *"Respond … yourself"* — not as a prohibition with a named sanction, apart from
the merge consequence. A contributor reads the file, so the file is what binds; but the intent behind
it was a ban.

## No DCO at all — the certification runs through relicensing

Most records in this bundle turn on the Developer Certificate of Origin: the
[kernel](linux-kernel.md) bars agents from signing it, [QEMU](qemu.md) reads it as excluding
AI-generated content outright. NetworkManager removes the instrument from the board entirely:

> Do not use "Signed-off-by:" lines in commits for NetworkManager. It has no
> meaning.[^nm-contributing]

Certification instead attaches to a **licensing commitment**: all new contributions *"**MUST** be
made under terms of LGPL-2.1-or-later"*, including to files currently under GPL-2.0-or-later, so that
the project can relicense later.[^nm-contributing] The AI clause hooks directly to that — *"You are
the one certifying that the contribution can be released under LGPL-2.1-or-later. A tool cannot
certify that for you."*

**So the DCO is not load-bearing for an AI policy.** Three projects here reach three different
positions — bar the agent from signing, treat the certificate as unsatisfiable, or have no
certificate — and all three still land on the contributor carrying the legal risk. The instrument
varies; the placement of responsibility does not.

## What a contributor must do

Build it, test it, and be able to explain it. Write the commit message and merge request description
yourself. Handle review yourself — if you cannot discuss the patch, it will not merge. Do **not** add
`Signed-off-by:`; it means nothing here. Be sure your contribution can go out under
LGPL-2.1-or-later. There is nothing to disclose and no tag to add, which makes this easy to comply
with and impossible to comply with dishonestly for long.

## Re-verification notes

The policy is a section of `CONTRIBUTING.md` in the repository, so `git log -- CONTRIBUTING.md` on
`gitlab.freedesktop.org/NetworkManager/NetworkManager` dates it and is authoritative.

**Fetch the raw path, not the blob page.** GitLab renders file content client-side, so
`/-/blob/main/CONTRIBUTING.md` returns HTTP 200 with the file text **absent** from the response body;
`/-/raw/main/CONTRIBUTING.md` returns the file. The blob URL is the `resource:` here because it is
the right link for a human, but a re-verification must read the raw path or the API. During this
first pass the raw path also returned a GitLab *"404: Page not found"* body under HTTP 200 once,
transiently, before serving correctly — **check for the text you came for, never for the status
code.**

Watch for the section moving out of `CONTRIBUTING.md`: at nine sentences it is small enough to be
folded into a wiki or a separate policy file, and the freedesktop GNOME-adjacent projects are
actively writing these. Watch also for a disclosure requirement being added — its absence is the most
distinctive thing here, and the easiest thing to change.

[^nm-contributing]: [CONTRIBUTING.md — Guidelines for Contributing (NetworkManager, main)](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/CONTRIBUTING.md)
[^nm-policy-commit]: [commit 565a3422 — CONTRIBUTING: add a policy for AI coding assistants](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/commit/565a342281d6cf32885783f87c008734a235f779)
