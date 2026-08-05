# Changelog

All notable changes to this bundle are documented here. `knowledge/log.md` is the content-level
view of the same history, date-grouped per OKF §9; this file is the repository-level view.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-08-05

First public release. Every record was read from the organisation's own text; nothing was imported
from the survey this replaces.

### Added

- Bundle skeleton per `supplychain-workspace` ADR-0011: structure, categories filed by
  organisation type, `log.md`.
- Records across `distributions/`, `foundations/` and `projects/` — see `okf list knowledge`.
  Selection is **curated, not exhaustive**: foundations first, then novel reasoning, then what the
  consuming tools encounter. 190+ organisations have published policies; enumeration is not the
  goal.
- `knowledge/overview.md` — the read-through map. Sorted by the **shape** of a policy (what the
  rule governs) rather than by its verdict, because verdict turned out to be the least predictive
  thing about a policy.
- Pre-publication files: `CONTRIBUTING.md` (including this bundle's own AI-contribution policy),
  `SECURITY.md`, `CODE_OF_CONDUCT.md`, root `LICENSE`.

### Notes

- **Two sources are unread and no records exist for them.** Fedora's council policy and GCC's wiki
  both sit behind proof-of-work challenges that return HTTP 200 with a challenge page rather than
  the document. Located, not verified; see `knowledge/log.md`.
- `supplychain-workspace` ADR-0011 was amended 2026-08-05: the field is 190+ organisations, not 27,
  so completeness is not the deliverable and "born red" is a steady state rather than a backlog.
