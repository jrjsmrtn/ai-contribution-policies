---
type: Practice
title: How open source treats AI-authored contributions
description: The read-through map of project positions on AI-generated code — the stances that recur, what each demands of a contributor, and why a survey of them decays.
tags:
  - ai-contribution
  - policy
  - overview
status: draft
generated:
  by: claude/opus-5
  at: '2026-08-04T21:20:00Z'
stale_after: 2027-02-04
sources:
  - id: adr-0011
    title: ADR-0011 — Extract AI-Contribution Policies as a Sibling Bundle
    resource: https://example.invalid/adr-0011
---

> **Skeleton.** This page is the read-through map, and is deliberately unwritten. It is the
> destination of the quick-reference document named in ADR-0011, and should be written *after*
> the records exist — a map drawn before the territory is surveyed describes the surveyor.

## What this bundle is for

A contributor about to send AI-assisted work upstream needs one fact before starting: **what does
this project's policy say?** Discovering it afterwards is the failure the `analyze-project` skill
records — an absent policy found only once the code was written.

## Why it expires

Every claim here is about *another organisation's current position*, which changes without
telling anyone. That is the whole reason for the format: `sources` records where a claim came
from, `verified` records that somebody checked, and `stale_after` makes the decay visible instead
of silent.

## The stances that recur

*To be written from the records, not from memory.* The survey being migrated grouped projects
into bans, guidelines-in-progress, active integration, and no stated policy — that grouping is a
hypothesis to re-test against re-verified records, not a conclusion to import.
