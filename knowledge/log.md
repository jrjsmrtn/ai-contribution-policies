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
* **Creation**: [Rust](projects/rust.md), [Python](projects/python.md),
  [Ansible](projects/ansible.md). Ansible's policy is the most conventionally drafted in the bundle
  — RFC 2119 keywords, a stated scope covering forum and Matrix as well as code, and a named
  reporting address. It also uses `Assisted-by:`, **the same field name as the kernel with a
  different value grammar**, so the tag is a convention rather than a format. Rust has nothing
  adopted (RFC 3950 closed; RFC 3959 and rust-forge#1040 open) but the open draft is the most
  developed text encountered, and the only one that concedes its own unenforceability: its goal is
  *"to remove plausible deniability"*, modelled on anti-money-laundering compliance.
* **Creation**: [Linux Kernel](projects/linux-kernel.md), [Git](projects/git.md),
  [Debian](distributions/debian.md), [FreeBSD](distributions/freebsd.md). Two are **state changes
  the survey could not have known**: the kernel's guidelines were merged in-tree as
  `Documentation/process/coding-assistants.rst` (2026-04), and Debian opened a General
  Resolution on LLM usage whose discussion period runs 2026-07-23 to 2026-08-08. Git turns out to
  carry an explicit AI section that both rejects AI-looking submissions *and* recommends careful AI
  use. FreeBSD documents a verified **absence** — Core reported drafting a policy in 2025; the
  Committer's Guide still has no mention of AI as of 2026-08-04.
* **Creation**: [NetBSD](distributions/netbsd.md) and [QEMU](projects/qemu.md), both verified
  against their own pages. Both are **narrower than the survey recorded**: NetBSD presumes LLM
  output tainted but permits it with *prior written approval by core*, and QEMU grounds its rule in
  DCO compliance and runs a documented exceptions process. "Complete ban" was wrong for both.
* **Blocked**: Fedora's council policy. The docs site *and* its pagure source repository both sit
  behind an Anubis proof-of-work challenge, returning HTTP 200 with a challenge page rather than
  the document. Source located, retrieval needs a human; no record written.
* **Creation**: [Gentoo](distributions/gentoo.md), verified against the Council's own wiki page
  rather than imported from the survey this bundle will replace. It is the first record and sets
  the shape: what the policy says, when the body decided it, and where that is written down.
