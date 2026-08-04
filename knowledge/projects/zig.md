---
type: Organization
title: Zig
description: Bans LLM use absolutely — including paraphrasing, editing, translation, brainstorming and bug-finding — as a Code of Conduct clause rather than a contribution guideline.
resource: https://ziglang.org/code-of-conduct/
tags:
  - ai-contribution
  - policy
  - project
  - prohibited
  - code-of-conduct
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T00:55:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T00:55:00Z'
stale_after: 2027-02-04
sources:
  - id: zig-coc
    title: 'Code of Conduct — Zig Programming Language (section: Strict No LLM / No AI Policy)'
    resource: https://ziglang.org/code-of-conduct/
---

**Stance: prohibited, without exception, and enforced as conduct.** Zig's *"Strict No LLM / No AI
Policy"* is the maximal position in this bundle. Verbatim, in full:[^zig-coc]

> - No LLM-generated content, whether it be code or prose.
> - No paraphrasing LLM-generated content.
> - No LLMs for editing, including fixing spelling or grammatical errors.
> - No LLMs for translation. English is encouraged, but not required. You are welcome to post in
>   your native language and rely on others to have their own translation tools of choice to
>   interpret your words.
> - No LLMs for brainstorming and then sharing the results of that brainstorming, even if you create
>   the prose. If you use a chatbot to give you advice on a comment on the issue tracker, that
>   comment is unwelcome.
> - No LLMs for finding bugs.
> - No talking about use of chatbot/LLM services.

## The placement is the mechanism

This is **in the Code of Conduct**, not in a contributing guide.[^zig-coc] That choice does more
work than any clause in it.

A contributing guideline governs artifacts and is enforced by rejecting them. A Code of Conduct
governs **participants** and is enforced by moderating them. Putting the rule here means a violation
is not a bad patch to be closed — it is misconduct, with whatever response the project applies to
misconduct. [Rust](rust.md)'s draft reaches for the same lever narrowly, making *lying about* LLM
use a CoC violation while the rest stays moderation policy. Zig applies it to the whole rule.

## It closes the laundering routes

Most policies here prohibit *submitting* generated content, which leaves the obvious workaround:
generate, then rewrite in your own words. Zig closes it explicitly — no paraphrasing, and no sharing
the results of LLM brainstorming *"even if you create the prose."*[^zig-coc]

That is the honest consequence of an origin-based rule. If what makes generated content
objectionable is where it came from, then rewriting it changes nothing, and a policy that stops at
"don't paste" has conceded the point. Zig is the only project here to follow the premise all the
way down.

## Two clauses that go further than any other

**No LLMs for finding bugs.** [curl](curl.md) permits exactly this with mandatory disclosure;
[Rust](rust.md)'s draft permits it if you verify the bug personally. Zig forbids it — so the ban
covers use that never produces a single line of contributed text.

**No talking about use of chatbot/LLM services.** This regulates *conversation about the tools*,
not their use. Nothing else in this bundle attempts that. It is unenforceable in the way
[Rust](rust.md)'s draft openly concedes about its own clauses, but it is not aimed at enforcement —
it is a statement about what the venue is for.

## Translation is refused, and the cost is moved rather than ignored

The translation clause is the one place the policy explains itself, and the qualifier matters:
*"English is encouraged, but not required. You are welcome to post in your native language and rely
on others to have their own translation tools of choice to interpret your
words."*[^zig-coc]

Every other project that thought about this — [Python](python.md), [curl](curl.md),
[FreeBSD](../distributions/freebsd.md), Rust's draft — permits machine translation precisely so as
not to tax non-native speakers. Zig refuses, and instead **moves the translation to the reader**.
A survey line reading "bans translation" would make this look like an oversight. It is a designed
trade.

## What a contributor must do

Do not use an LLM for any part of a Zig contribution — not writing, not editing, not spellchecking,
not translating, not bug-hunting — and do not rewrite its output into your own words. Post in your
own language if English is hard; that is explicitly welcome. Do not discuss chatbot use in project
venues.

## Re-verification notes

Check that the section is still **in the Code of Conduct**. If it migrates to a contributing guide,
the rule may read the same while its enforcement changes completely, and that is the substantive
change a text-diff would understate. Quote the list in full when re-verifying — its force comes from
the enumeration, and any summary of it loses the paraphrasing and brainstorming clauses first.

[^zig-coc]: [Code of Conduct — Zig Programming Language (section: Strict No LLM / No AI Policy)](https://ziglang.org/code-of-conduct/)
