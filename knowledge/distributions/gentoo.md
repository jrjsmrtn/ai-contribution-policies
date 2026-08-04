---
type: Organization
title: Gentoo
description: Source-based Linux distribution whose Council voted an express ban on contributions created with the assistance of NLP AI tools, on copyright, ethical and quality grounds.
resource: https://wiki.gentoo.org/wiki/Project:Council/AI_policy
tags:
  - ai-contribution
  - policy
  - distribution
  - prohibited
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T21:20:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T21:20:00Z'
stale_after: 2027-02-04
sources:
  - id: gentoo-council-ai-policy
    title: "Project:Council/AI policy — Gentoo wiki"
    resource: https://wiki.gentoo.org/wiki/Project:Council/AI_policy
---

**Stance: prohibited.** The Gentoo Council voted on 2024-04-14 that it is *"expressly forbidden to
contribute to Gentoo any content that has been created with the assistance of Natural Language
Processing artificial intelligence tools."*[^gentoo-council-ai-policy]

## What it covers

The policy binds **Gentoo contributions and the official Gentoo projects**. It does not prohibit
adding packages that are themselves AI tooling — the restriction is on how contributed content is
produced, not on what the distribution ships.[^gentoo-council-ai-policy]

## The stated grounds

Three, named together: **copyright, ethical and quality concerns**. The motion is explicitly
revisitable *"should a case been made over such a tool that does not pose"* those
concerns[^gentoo-council-ai-policy] — so the ban is conditional on the state of the tooling rather
than on the idea of AI assistance, and a re-check should look for whether that case has been made.

## What a contributor must do

Do not send AI-assisted work. There is no disclosure route that makes it acceptable: unlike
policies that permit contribution subject to attribution, this one has no permitted path.

## Re-verification notes

The decision is a Council vote recorded on a wiki page, so the page's history is the audit trail —
check whether the motion has been revisited before trusting a cached answer. The `stale_after` here
is six months rather than a year: a conditional ban is more likely to move than a settled one.

[^gentoo-council-ai-policy]: [Project:Council/AI policy — Gentoo wiki](https://wiki.gentoo.org/wiki/Project:Council/AI_policy)
