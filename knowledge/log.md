# Bundle Update Log

Content changes to the knowledge bundle: records added, re-verified, corrected or expired.

**Date headings, per OKF §9**, which requires ISO 8601 `YYYY-MM-DD` and admits no other heading
form. The log's model is date-grouped, not release-grouped, so an entry cannot carry its release
in a heading. The release map below is how a `knowledge/` tree separated from this repository
still names its version: OKF has no in-band content-version field, and a git tag does not travel
with a copied directory.

**Releases**, newest first: **v0.2.0** 2026-08-05 · **v0.1.0** 2026-08-05.
[`../CHANGELOG.md`](../CHANGELOG.md) is the repository-level view of the same releases.

## 2026-08-05

* **Correction — "located, retrieval blocked" was wrong for both Fedora and GCC.** Those entries
  rested on HTTP 200 responses from Anubis-protected hosts. **Anubis serves a challenge page for any
  path, including ones that do not exist**, so a 200 never confirmed the pages were real. Both URLs
  were simply wrong: `gcc.gnu.org/wiki/AIpolicy` does not exist (the policy is at
  `gcc.gnu.org/ai-policy.html`), and neither did the Fedora council path recorded here. The earlier
  caution — *a status code proves the server answered, never that the content arrived* — was applied
  to **content** and not to **existence**, which is the same error one level up.
* **`vendors/` filled** — [SUSE](vendors/suse.md), [Red Hat](vendors/red-hat.md),
  [Canonical](vendors/canonical.md). The category was empty and now carries the finding that
  justifies it existing: **a vendor's policy governs its own staff, not your contribution.** SUSE
  says so outright (*"The policy applies to SUSE employees"*), Red Hat defers to *"standards and
  practices of each unique community"*, and Canonical publishes nothing. Where a vendor also runs a
  community — Fedora, openSUSE, Ubuntu — the community's policy is what binds a contributor, and
  reading the vendor's stance as its communities' policy gets both wrong.
* **SUSE contradicts itself across two published versions**, which is the sharpest caution in the
  bundle about trusting a single source. The **2024-04 PDF** states *"AI pair programming must not
  be used"*; the **live web policy contains no AI clause at all** — verified by counting occurrences,
  and confirmed complete because it carries the four sections that *bracket* the AI clause in the
  PDF. Which is current is not established. "SUSE bans AI pair programming" is widely repeated and
  traces to the PDF; it may no longer be true.
* **A claim declined.** Secondary sources describe Red Hat as having staff guidelines *"based on 3
  principles"*. **No such enumeration appears in either Red Hat post read**, so it is not recorded —
  the record names the claim, says where it looked, and leaves the gap open. The second post is
  industry guidance addressed to organisations generally, not Red Hat policy; reading it as policy is
  an easy category error to make from a search result.
* **Canonical's absence is a strong one**: no AI mention across eighteen sections of contributor
  documentation covering the whole contribution path, *including the sponsorship queue where such a
  rule would sit*. It also requires a **Harmony-based CLA** that licenses rather than assigns and is
  itself silent on AI — so contributors sign a heavier instrument than most projects ask for, and it
  still does not answer the question.
* **Re-verified [Debian](distributions/debian.md)** three days before its discussion period closes.
  Still *In Discussion* to 2026-08-08; **voting period not yet announced**. Three material changes
  since first recorded: Proposal **B** amended twice, **C** amended once, and **A** is now framed as
  an amendment to the **Social Contract**.
* That last one changes the ballot's arithmetic. The Social Contract is a **Foundation Document**
  (Constitution §4.1(5.2)) and superseding one requires a **3:1 majority** (§4.1(5.3)) — so the
  prohibition option must clear a supermajority its five rivals do not. **The vote page states no
  majority requirement**, so this is read from the Constitution and the record says so. A six-way
  list looks like an even contest and is not one.
* **`overview.md` updated for both new records**, and it needed a structural change rather than two
  more rows. **Six shapes became seven**: GCC's copyright-threshold rule is genuinely new — its line
  is the test that already decides whether a contribution needs an assignment, so *"is this
  AI-generated?"* is subordinate to *"is this legally significant?"*.
* **A fourth state was added alongside prohibited / permitted / undecided: a rule in force that
  cannot be read.** Fedora's policy is adopted and effective and its text is unpublished, which no
  existing category described.
* The axes section gained **"who the rule taxes"**, the least considered and most consequential of
  them. A blanket "no AI" rule falls hardest on contributors who need AI to work at all; every
  project that thought about translation permits it, and only GCC extends the reasoning to
  accessibility. *A policy that does not carve this out has excluded people without deciding to.*
* The DCO section now notes GCC accepts **either** an FSF assignment **or** a DCO, and its AI policy
  turns on neither — further evidence the instrument is not the unit of choice. Plus the one rule
  nobody else states: *"An LLM may not commit code to the project repository"*, a constraint on
  agents with write access rather than on generated text.
* The attribution table gained GCC as a **fourth** `Assisted-by:` adopter, and the
  `Co-developed-by:` trap that explains why a new token was coined instead of an existing one reused.
* **The gate caught a real defect in this edit**: `[^gcc-ai-policy]` was cited three times with no
  `sources` entry and no definition. A summary page is exactly where an uncited claim survives,
  because it reads as a conclusion drawn from records rather than as a claim of its own.
* **Creation**: [Fedora](distributions/fedora.md) — **a status record, not a content record.** The
  Council approved the AI-Assisted Contributions policy on 2025-10-22 by a minuted **+7, 0, 0** vote,
  effective immediately. Nine months on it is **not on the Council Policies page**, against an
  assigned action to put it there, and the agreed text exists only as a comment on Pagure ticket
  #542 — which was unreachable from two networks at the time of writing.
* The record therefore states that a policy exists and binds, and **deliberately does not state what
  it says**. Fedora did the governance well — open proposal, weeks of public discussion, revisions
  from feedback, a recorded unanimous vote — and failed at the last step, which is the one a
  contributor needs. A rule in force that cannot be read is not a rule anyone can follow.
* The Community Blog carries a full policy text and it is the **proposal**, superseded by *"the
  latest revision"* the Council actually approved. Quoting it would reproduce precisely the error
  this bundle exists to correct: a plausible, well-formatted, out-of-date text presented as an
  organisation's current position.
* `CONTRIBUTING.md` gains a narrowly-drawn exception for status records, because this one would
  otherwise contradict the stated rule. The rule is unchanged where it counts — no claim about what
  a policy *says* without reading the text.
* **Creation**: [GCC](projects/gcc.md), read in full from `ai-policy.html` (dated 2026-07-29). Its
  threshold is **legal significance** — the copyright test that already decides whether a
  contribution needs an assignment — and nothing else in this bundle draws its line there. That
  makes the policy an extension of existing legal machinery rather than a new regime.
* Three exceptions, each doing distinct work: legally insignificant LLM content is acceptable *if
  clearly marked*; **test cases are exempt even when legally significant** (the only such carve-out
  here, and coherent with the threshold logic); and imported code such as `libsanitizer` is out of
  scope, so GCC declines to impose its rule on upstreams it merely vendors.
* **The accessibility carve-out is the clause most worth copying.** Screen readers, text-to-speech,
  direct translation and spelling/grammar assistance are outside the policy entirely, provided the
  contributor verifies the output. A blanket "no AI" rule silently taxes contributors who rely on
  assistive technology, and non-native speakers through translation; GCC names both.
* It is also the only policy here whose **first section is about people** — contributors *"should be
  treated with respect and kindness"*, presumed to act in good faith, and **guided** rather than
  rejected if they have not yet followed the policy. That is an explicit hedge against the
  enforcement failure mode Rust's draft concedes: an unverifiable rule turns into suspicion.
* GCC is the **fourth** adopter of `Assisted-by:` with no shared specification, and joins the kernel
  in reserving `Signed-off-by:` to humans — going further with *"An LLM may not commit code to the
  project repository"*, a rule about agents with write access rather than about generated text.
* The policy is **CC0 1.0** — the only one here released for reuse, so a project wanting a
  copyright-threshold rule can adopt the text outright.
* `stale_after` is **2027-01-15** because the source named its own review date: *"At the latest the
  policy will be reviewed at the start of 2027."*

## 2026-08-04

* **Initialization**: Created the bundle per `supplychain-workspace` ADR-0011 — structure,
  categories filed by organisation type, and one verified exemplar record.
* **`overview.md` written.** It was held as a skeleton on the rule that a map drawn before the
  territory is surveyed describes the surveyor. Fifteen records now span every shape encountered, so
  it is drawable — and under the amended ADR-0011 it is no longer waiting on coverage, which is not
  the deliverable. The survey's four-group taxonomy (bans / guidelines-in-progress / active
  integration / no policy) is **not** what it was replaced with: that grouping sorted by *verdict*,
  and verdict turned out to be the least predictive thing about a policy. The map sorts by **shape**
  — what the rule governs — because that is what tells a contributor what to do.
* **One unsourced claim caught in the draft.** The tag table listed Fedora as using `Assisted-by:`.
  True according to secondary reporting, but Fedora has no record because its primary is unreachable,
  so the overview would have asserted as fact something the bundle deliberately declined to record.
  Removed. A summary page is exactly where an unsourced claim survives longest, because it reads as
  a conclusion drawn from the records rather than as a claim of its own.
* **Strengthened**: [Linux Kernel](projects/linux-kernel.md) gains a second primary,
  `submitting-patches.rst`, found while writing the landscape's commit-trailers concept. The
  `Assisted-by:` tag is **required, not encouraged**, and the requirement sits in the *main*
  submission document — *"Failure to do so may impede the acceptance of your work"* — so a
  contributor following the ordinary process meets it without opening the AI policy. The record
  previously cited only `coding-assistants.rst` and understated this.
* Also records **why the kernel invented a token** instead of reusing `Co-developed-by:`: that tag
  denotes authorship and each one *"must be immediately followed by a Signed-off-by: of the
  associated co-author"* — a sign-off the AI policy forbids an agent from adding. `Assisted-by:` is
  the only shape consistent with both rules. The retired 27-project survey recommended
  `Co-developed-by:` for AI attribution, which asks for a structurally invalid trailer block.
* **Creation**: [OpenInfra](foundations/openinfra.md), [curl](projects/curl.md),
  [Zig](projects/zig.md) — chosen for novel reasoning under the amended scope, and between them they
  bracket the whole spectrum. **OpenInfra settles the tag question**: it uses `Assisted-By:` for
  *predictive* tools and `Generated-By:` for *generative* ones, so the field names other projects
  disagree about are not competing spellings but names for two degrees of authorship. Its labels are
  also **mutable** — reviewers may remove one after substantial rework — which makes the tag a
  statement about the current artifact rather than about its history. Nothing else here works that
  way, and the two readings are incompatible. **curl** is the only policy shaped by inbound security
  reports: disclosure is a **MUST** for AI-found findings, and fabricated reports earn an immediate
  ban. **Zig** is the maximum, and its force comes from placement — the ban is a **Code of Conduct**
  clause, so a violation is misconduct rather than a bad patch.
* **A cross-record correction.** The ASF record said the tag field names were "an unsettled
  convention". OpenInfra shows they are not unsettled so much as *partial* — each project adopted
  the tag for one degree and left the other unnamed. The ASF record now points at OpenInfra rather
  than leaving the weaker claim standing.
* **GCC recorded** — see the 2026-08-05 entry. The URL logged here was wrong, not blocked.
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
