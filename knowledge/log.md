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
* **Creation**: [Apache Software Foundation](foundations/apache-software-foundation.md). Its
  conditions are near-identical to the Linux Foundation's, but it **bounds the contributor's duty**:
  *"Don't second guess vendor's terms of use … you are not expected to go outside of the TOU text
  for further clarifications."* It also makes the tool's own similarity reporting the evidence that
  discharges the third-party-material check — an obligation otherwise unsatisfiable, since nobody
  can audit training data. Its disclosure token is `Generated-by:`, a **third spelling**.
* **Scope finding — the landscape is far larger than 27.** A public index
  (`melissawm/open-source-ai-contribution-policies`) lists **190+ organisations** with published AI
  contribution policies, including LLVM, OpenJDK, Django, Kubernetes, curl, GCC, SciPy, NumPy,
  PyTorch, Zig, Drupal, Firefox and Wikipedia. **Enumeration is no longer a reachable goal**, and
  the migrated survey's 27 entries were a slice of a much bigger field even when written. This
  bundle should be *curated and deep* — records that read the primary text and extract the
  transferable rule — and should point at that index for breadth rather than race it. Treat the
  index as a **lead list only**: it is a third-party aggregation, several of its links are already
  stale (it points at CPython's `generative-ai/` path, which now redirects), and nothing in it is
  evidence until the primary is read.
* **Fedora, fourth route, still blocked — but its state has changed.** Secondary reporting is
  consistent that the Council **approved** the policy (2025-10), that it requires disclosure *when a
  significant part is taken from a tool without changes*, that it uses `Assisted-by`, that AI *"must
  not be the sole or final arbiter"* in review, that scope extends past code to documentation,
  design assets and social posts, and that large-scale initiatives are excluded and handled
  individually. **None of that is recorded as a record**, because every route to the primary text
  returns an Anubis challenge: `docs.fedoraproject.org` (curl and WebFetch), pagure raw, and the
  GitLab mirror (403). Noted here so the next pass starts from "approved, needs a browser" rather
  than re-deriving it. If the disclosure threshold survives verification it is **near-identical to
  Ansible's** — both Red Hat-adjacent, which is worth checking for common drafting.
* **Creation**: [Linux Foundation](foundations/linux-foundation.md) — the first `foundations/`
  record, and the most upstream document in the bundle. It permits AI-generated contributions to LF
  projects as a **baseline projects may override**, and reasons entirely from licence compatibility
  and third-party rights. It **does not invoke the DCO**: zero occurrences of `DCO`,
  `Developer Certificate of Origin` or `Signed-off-by`, checked by counting on the fetched page
  rather than by reading it.
* **Negative sweep, not written up as records.** Phoenix, Ash, MacPorts, Proxmox and Pulp were
  probed for AI terms in their own contribution docs; none showed a contribution policy. These are
  **deliberately not records yet** — the evidence is one or two file fetches each, which is weaker
  than [FreeBSD](distributions/freebsd.md)'s absence, where Core publicly stated it was drafting a
  policy and named where it would land. Files checked: `phoenixframework/phoenix` `CONTRIBUTING.md`
  and `README.md`; `ash-project/ash` `README.md`; the MacPorts guide source; the Proxmox developer
  documentation wiki; the Pulp project developer docs. A future pass should start from these and
  widen, not repeat them.
* **A probe false positive worth remembering.** The Ash `README.md` matched the AI pattern — on
  `AshAI`, a *product feature* (Structured Outputs, MCP, Vectorization). A keyword sweep for
  contribution policy will hit projects that *build* AI tooling, and the hit rate is highest exactly
  where the subject matter overlaps. Confirm what a match is before recording it as a stance.
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
