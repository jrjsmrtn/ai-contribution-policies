# Contributing

Corrections are the most valuable contribution here. Every record is a claim about an organisation's
*current* position, and those change without telling anyone — if a record is out of date or wrong,
saying so is more useful than adding a new one.

## The one rule: read the primary source

**A record is not accepted until someone has read the organisation's own text.** Not a summary, not
a news article, not an aggregator entry, not another bundle. This is the whole point: the survey
that preceded this bundle was assembled from secondary readings and was consistently wrong in one
direction — it dropped the qualifier that determines what a contributor should actually do.

If the primary source cannot be retrieved, **say so and stop**. Several policies sit behind
proof-of-work bot challenges that return HTTP 200 with a challenge page rather than the document; a
status code proves the server answered, never that the content arrived. A record saying *"located,
not verified, here is exactly where to look"* is worth more than one repeating a claim nobody
checked.

## What a record must have

Records are OKF concepts. Each needs:

- **`sources`** — every source the record cites, each with an `id`, `title` and `resource`.
- **Footnotes joining body to sources** — every `[^id]` reference must have a definition, every
  definition must be referenced, and every `sources` entry must have a footnote. The gates check all
  four directions, because a footnote defined but never cited renders as nothing, so a source that
  *looks* cited is not.
- **`verified`** — who read it and when.
- **`stale_after`** — when it must be re-checked. Six months by default; shorter when the subject is
  moving (a live vote, an open pull request).
- **Re-verification notes** — where to look next time, and what specifically to watch. If the policy
  is versioned in git, say so; that history is a better audit trail than any rendered page.

Quote the source directly and generously. Paraphrase is what this bundle is correcting.

## Filing

By **what the organisation is** — `distributions/`, `foundations/`, `projects/`, `vendors/` — never
by what its policy currently says. Stance is the volatile attribute the bundle exists to track;
filing by stance means re-filing every time the recorded fact changes.

## Absences

"No policy" is a legitimate record, but only as a **dated claim with a search path**. An empty entry
can mean *no policy*, *policy not found*, or *nobody looked* — three different things to a
contributor, and only the first is a fact. Name the files and pages you checked. If the evidence is
one or two fetches, log it rather than writing a record: not all absences carry the same weight.

## Scope

This bundle holds **what organisations' policies say**. It does not hold procedure for checking them
(that is the `analyze-project` skill), design guidance on adopting one, or supply-chain mechanics
generally — those are referenced, not restated.

## Gates

```bash
okf validate knowledge && okf lint knowledge
```

Conformance, attribution in both directions, ISO 8601 dates, links, `reuse lint` and secret scanning
run on every commit, and again weekly — expiry is a function of the date, not of the diff, so a
commit-triggered check alone would never notice a record going stale.

## Use of AI in contributions to this bundle

It would be odd for a bundle about AI-contribution policies not to have one.

**AI assistance is permitted.** It is not permitted to substitute for reading the source.

- **You must have read the primary text yourself.** A record summarising what a model reported about
  a page is precisely the failure mode this bundle documents, one layer removed.
- **Quotations must be verified against the source**, not reproduced from a model's output. Check
  the exact wording; a plausible near-quotation is worse than none, because it is citable.
- **Disclose it** with an `Assisted-by:` trailer naming the tool and model.
- **You are responsible for the contribution** regardless of what produced it, and you must be able
  to explain and defend every claim in it under review.

That places this bundle, on its own map, as a **responsibility rule** with mandatory disclosure —
and the reasoning is the same one Rust's draft gives: the goal is not to detect anything, it is to
make not saying so a deliberate act.
