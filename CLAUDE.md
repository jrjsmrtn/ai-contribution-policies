# CLAUDE.md

Guidance for working in this repository.

## Project Context

- **Category**: Knowledge / documentation — no application code
- **Type**: OKF bundle — `knowledge/` is the bundle root; the repository is its container
- **Stack**: Markdown + YAML frontmatter. No code
- **License**: CC BY 4.0 for knowledge, CC0-1.0 for dotfiles — see `REUSE.toml`
- **Tier**: t1
- **Charter**: `supplychain-workspace` ADR-0011

## The unit is an organisation, not a concept

This is the **entity-keyed** bundle. One record per organisation, answering *what its policy on
AI-authored contributions says, who decided it, and where that is written down*. The sibling
`software-supply-chain-landscape` is concept-keyed (`copyleft-floor.md`, `spdx-license-expression.md`);
do not import its filing habits wholesale. Guidance in `okf-skills` was written for concept
bundles and may not transfer — where it does not, that is worth reporting back rather than
working around.

## Filing rule

By **what the organisation is**, never by what its policy currently says. Stance is the volatile
attribute this bundle exists to track; filing by stance means re-filing every record whose fact
changes. Identity is stable, policy is a field.

## Verification is the work

A record is worth nothing if nobody checked it. Every record carries `sources` pointing at the
organisation's *own* statement — not a summary, not a news article — plus `verified` and
`stale_after`.

**`stale_after` is six months here**, not the year the landscape uses. A policy is a decision a
body can revisit at any meeting; a specification is not.

**Never write a record from a secondary source or from an older survey.** The survey this bundle
replaces went eleven months without re-checking, which is the entire reason the bundle exists.
Re-verify against the primary page, and if it has moved, record where it moved to.

## Scope boundaries (ADR-0011)

- **Procedure** — how to check requirements before contributing — belongs to `analyze-project`.
- **Design guidance** — when a project should adopt a policy — belongs to the *AI Contribution
  Policy Pattern*.
- **Supply-chain mechanics** — licensing, provenance, disclosure generally — belong to the
  landscape bundle. Reference them; do not restate them.

## Gates

```bash
okf validate knowledge     # conformance — bundle root is knowledge/, not the repo root
okf lint knowledge         # recommended fields and style
reuse lint                 # licensing
```

Dates are ISO 8601 everywhere, including prose (`2026-08-04`, never `August 4, 2026`).

## Current Development Status

**Skeleton.** One verified record. The 27-entry survey is not imported; doing so would fill the
bundle with unchecked claims. Extraction and re-verification are one piece of work.
