# Bundle Update Log

Content changes to the knowledge bundle: records added, re-verified, corrected or expired.

**Date headings, per OKF §9**, which requires ISO 8601 `YYYY-MM-DD` and admits no other heading
form. The log's model is date-grouped, not release-grouped, so an entry cannot carry its release
in a heading. The release map below is how a `knowledge/` tree separated from this repository
still names its version: OKF has no in-band content-version field, and a git tag does not travel
with a copied directory.

**Releases**, newest first: *(none yet — the bundle is a skeleton)*.
[`../CHANGELOG.md`](../CHANGELOG.md) is the repository-level view of the same releases.

## 2026-08-04

* **Initialization**: Created the bundle per `supplychain-workspace` ADR-0011 — structure,
  categories filed by organisation type, and one verified exemplar record.
* **Creation**: [Gentoo](distributions/gentoo.md), verified against the Council's own wiki page
  rather than imported from the survey this bundle will replace. It is the first record and sets
  the shape: what the policy says, when the body decided it, and where that is written down.
