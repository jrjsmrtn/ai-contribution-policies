---
type: Practice
title: Prose reserved to humans
description: Fifteen records here permit AI in the code and restrict or forbid it in the writing around the code — commit messages, issue text, pull request descriptions, review replies, mailing lists. The split runs opposite to the intuition that code is the risky part, it is the one rule in this bundle that enforces itself without detection, and translation is the exception nearly every project that thought about it grants.
resource: https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/CONTRIBUTING.md
tags:
  - ai-contribution
  - mechanism
  - policy-design
  - communication
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-10T09:20:00Z'
verified:
  - by: claude/opus-5
    at: '2026-09-10T09:20:00Z'
stale_after: 2027-03-10
sources:
  - id: pr-nm
    title: 'CONTRIBUTING.md (NetworkManager, main)'
    resource: https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/CONTRIBUTING.md
  - id: pr-nerves
    title: 'CONTRIBUTING.md (nerves-project/nerves, main)'
    resource: https://raw.githubusercontent.com/nerves-project/nerves/main/CONTRIBUTING.md
  - id: pr-k8s
    title: 'contributors/guide/pull-requests.md — AI Guidance (kubernetes/community, master)'
    resource: https://raw.githubusercontent.com/kubernetes/community/master/contributors/guide/pull-requests.md
  - id: pr-gtk
    title: 'CONTRIBUTING.md (GNOME/gtk, main)'
    resource: https://gitlab.gnome.org/GNOME/gtk/-/raw/main/CONTRIBUTING.md
  - id: pr-git
    title: 'Documentation/SubmittingPatches — Use of Artificial Intelligence (git/git, master)'
    resource: https://raw.githubusercontent.com/git/git/master/Documentation/SubmittingPatches
  - id: pr-perl
    title: 'AI_POLICY.md (Perl/perl5, blead)'
    resource: https://raw.githubusercontent.com/Perl/perl5/blead/AI_POLICY.md
  - id: pr-texlive
    title: 'TeX Live AI policy'
    resource: https://tug.org/texlive/aipolicy.html
  - id: pr-dt
    title: 'AGENTS.md (DependencyTrack/dependency-track, main)'
    resource: https://raw.githubusercontent.com/DependencyTrack/dependency-track/main/AGENTS.md
  - id: pr-django
    title: 'docs/internals/contributing/writing-code/submitting-patches.txt (django/django, main)'
    resource: https://raw.githubusercontent.com/django/django/main/docs/internals/contributing/writing-code/submitting-patches.txt
  - id: pr-python
    title: 'Using Artificial Intelligence tools — Python Developer''s Guide'
    resource: https://devguide.python.org/getting-started/ai-tools/
---

**The most widely shared rule in this bundle is not about code.** Fifteen records permit or tolerate
AI assistance in the patch and then restrict it in the writing around the patch, and a sixteenth put
it to a vote and declined. That is the opposite
of what the risk arguments elsewhere would predict — the copyright, licensing and correctness
worries all attach to the code, and the prose is where none of them apply.

## Which surface each one reserves

| Record | Commit message | Issue / PR text | Review replies | Lists & forums |
|---|:--:|:--:|:--:|:--:|
| [NetworkManager](../projects/networkmanager.md) | ● | ● | ● | |
| [Nerves](../projects/nerves.md) | ● | ● | ● | |
| [Zig](../projects/zig.md) | ● | ● | ● | ● |
| [Perl](../projects/perl.md) | ● | ● | ● | ● |
| [Astral](../vendors/astral.md) | | ● | ● | |
| [ripgrep](../projects/ripgrep.md) | | ● | ● | |
| [Zed](../projects/zed.md) | | ● | ● | |
| [Kubernetes](../projects/kubernetes.md) | ● | | ● | |
| [LLVM](../projects/llvm.md) | | ● | ● | |
| [Git](../projects/git.md) | ● | ● | ● | |
| [TeX Live](../distributions/tex-live.md) | | | | ● |
| [Dependency-Track](../projects/dependency-track.md) | | ● | | |
| [GTK](../projects/gtk.md) | | | ● | |
| [Asahi Linux](../projects/asahi-linux.md) | ● | ● | ● | ● |
| [Elixir](../projects/elixir.md) | | | | ● |
| [Debian](../distributions/debian.md) | ○ | ○ | ○ | ○ |

● reserved · ○ proposed and not adopted — Debian's Proposal C would have required human-drafted
commit messages and Proposal G put communication in scope; the project adopted neither.

**Review replies are the near-universal cell**, and the four-surface rows are the outright
prohibitions. The interesting entries are the narrow ones: GTK reserves *only* review feedback, TeX
Live *only* mail, Dependency-Track *only* the act of opening a thread.

## Why prose and not code

**NetworkManager gives the only argument that explains the asymmetry:**

> Write your own commit messages and Merge Request descriptions. Those explain **why** you are making
> the change, which is the part a tool cannot know.[^pr-nm]

The change is in the diff; the reason is only in the author's head. Delegating the prose deletes the
one thing the prose exists to carry. **Everywhere else the restriction is asserted rather than
argued** — which matters, because a rule with a stated reason survives contact with an edge case and
a bare prohibition does not.

Two other motives appear. **Reviewer time**: Kubernetes bans *"Large AI generated PRs and AI
generated commit messages"*[^pr-k8s] in the same clause, treating generated prose as volume rather
than as fraud. And **conversation as the point of review**: GTK's *"Do NOT feed the review feedback
to an LLM/GenAI tool"*[^pr-gtk] and NetworkManager's *"Respond to review comments yourself"*[^pr-nm]
both protect an exchange between two people, not an artifact.

## It is the one rule that enforces itself

Detection is the unsolved problem across this bundle. **This rule does not need it.** A maintainer
who asks a question in review learns whether the contributor can answer, and the answer is produced
live, in public, by the person. Nothing has to be determined about how the patch was made.

That is why the same sentence appears as both a prose rule and an enforcement mechanism —
NetworkManager's *"If you cannot discuss your own patch with a reviewer, it will not be merged"* is
simultaneously the obligation and the test.

**Git is the exception that tries to detect, and shows why the others do not.** It rejects
submissions that *"sound overly formal or bloated"*[^pr-git] — a register test, applied to the prose
rather than to the person. It catches machine-written text and it also catches a careful non-native
speaker, and the project supplies no way to tell the two apart.

## Translation is the carve-out everyone converges on

**[Nerves](../projects/nerves.md) draws the line the others reach for:**

> Using AI to **translate or tighten your own writing is fine**. Using it to **write in your place**
> is not.[^pr-nerves]

**Assist versus substitute**, and it is what makes the rule defensible against the strongest
objection to it. [Perl](../projects/perl.md) exempts *"LLM use for translation of human-written
messages"*[^pr-perl]; [Python](../projects/python.md) explicitly permits *"Assistance with writing
comments, especially in a non-native language"*[^pr-python]; Elixir, FreeBSD and Rust's draft all
carve out translation; even [Zig](../projects/zig.md), which forbids everything else, tells
contributors to post in their own language instead.

**A prose ban with no translation exception taxes non-native speakers and nothing else** — the
projects that thought about it say so, and the ones that did not are the ones whose rule is a bare
assertion.

TeX Live takes a fourth position: not a ban but a **delimiter requirement**, permitting AI-written
mail *"unless the AI's responses are clearly indicated and delimited from the rest of your
email"*.[^pr-texlive] Attribution rather than prohibition, and the only instance of it here.

## Where it is a rule about agents rather than about writing

[Dependency-Track](../projects/dependency-track.md) reserves the same surface from the other end,
instructing the tool instead of the contributor: *"Never create an issue. Never create a
PR."*[^pr-dt] **It is the only record here that does**, and [Perl](../projects/perl.md) is the
mirror — the same rule, addressed to the human. [LLVM](../projects/llvm.md) also binds the
contributor for the agent's behaviour: write the PR description yourself, and do not let an agent
post anything without your approval, review comments included.

**The two framings are not equivalent.** A rule addressed to the contributor binds someone who can be
sanctioned; a rule addressed to the agent depends on the agent reading it — see
[agent-file pointers](agent-file-pointers.md) for what that convention rests on.

## Two things worth holding onto

**Django is the counter-example, and it is deliberate.** Its disclosure rule names *"drafting commit
messages"* as an example of a use to disclose[^pr-django] — permitted, provided you say so. A project
with an otherwise detailed AI policy, reached from a documented increase in *"inaccurate, misleading,
or fictitious content"*, still did not reserve the prose. **The convergence is not unanimity.**

**And the clause does not survive copying.** The attributed lineage runs Astral → ripgrep → Zed →
[systemd](../projects/systemd.md), and the first three all reserve issue text, PR descriptions and
review replies. systemd inherited the [review canary](review-canary.md) and bars AI from *credit* in
commit messages — but it does not reserve the writing. **A policy adapted from another policy loses
clauses silently**, and this is the clause that was dropped.

## What to watch

Whether the register test spreads — Git is alone in it, and it is the version of this rule that
punishes a person for how they write. Whether the delimiter approach picks up a second
implementation, since it is the only one that treats the problem as attribution rather than
authorship. And whether any project reserves prose *without* granting the translation exception now
that six have granted it; that combination is what the objection to this rule is actually about.

[^pr-nm]: [CONTRIBUTING.md (NetworkManager, main)](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/CONTRIBUTING.md)
[^pr-nerves]: [CONTRIBUTING.md (nerves-project/nerves, main)](https://raw.githubusercontent.com/nerves-project/nerves/main/CONTRIBUTING.md)
[^pr-k8s]: [contributors/guide/pull-requests.md — AI Guidance (kubernetes/community, master)](https://raw.githubusercontent.com/kubernetes/community/master/contributors/guide/pull-requests.md)
[^pr-gtk]: [CONTRIBUTING.md (GNOME/gtk, main)](https://gitlab.gnome.org/GNOME/gtk/-/raw/main/CONTRIBUTING.md)
[^pr-git]: [Documentation/SubmittingPatches — Use of Artificial Intelligence (git/git, master)](https://raw.githubusercontent.com/git/git/master/Documentation/SubmittingPatches)
[^pr-perl]: [AI_POLICY.md (Perl/perl5, blead)](https://raw.githubusercontent.com/Perl/perl5/blead/AI_POLICY.md)
[^pr-texlive]: [TeX Live AI policy](https://tug.org/texlive/aipolicy.html)
[^pr-dt]: [AGENTS.md (DependencyTrack/dependency-track, main)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/main/AGENTS.md)
[^pr-django]: [docs/internals/contributing/writing-code/submitting-patches.txt (django/django, main)](https://raw.githubusercontent.com/django/django/main/docs/internals/contributing/writing-code/submitting-patches.txt)
[^pr-python]: [Using Artificial Intelligence tools — Python Developer's Guide](https://devguide.python.org/getting-started/ai-tools/)
