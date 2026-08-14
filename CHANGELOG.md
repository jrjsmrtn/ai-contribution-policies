# Changelog

All notable changes to this bundle are documented here. `knowledge/log.md` is the content-level
view of the same history, date-grouped per OKF §9; this file is the repository-level view.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.6.0] - 2026-08-14

**The first release driven by an expiry rather than by new material.** `distributions/debian.md`
carried a deliberately short `stale_after` because its subject is a vote in progress. It came due,
and four of its claims had gone stale in nine days.

### Changed

- **[`distributions/debian.md`](knowledge/distributions/debian.md) re-verified against the vote
  page.** The General Resolution moved from *In Discussion* to **Voting**; the discussion period was
  **extended to 2026-08-13**, a week past the date this record carried; the ballot is open
  **2026-08-15 to 2026-08-28**; and **two further proposals were added — G and H, making eight, not
  six**. Their operative text was read, not inferred from their titles
- **The disagreement changed shape, not only size.** **G** puts human communication in scope
  alongside **C**, so that is the position of two independent proposals rather than one project's
  outlier. **H** argues from **environmental cost** — a ground no other option in this ballot, and no
  other organisation in this bundle, reasons from
- **A seventh axis** was added to the list a policy must decide: *on what grounds?* A project could
  adopt H's position while agreeing entirely about quality, which none of the first six axes
  distinguishes
- **A count became a shape.** The disclosure argument rested on *"five of six ballot options"* — a
  figure the ballot growing to eight would have falsified. It now names which options ask for
  disclosure and why the two prohibitions make it moot, so the reasoning survives the next amendment
- `stale_after` **2026-09-15 → 2026-08-29**, the day after the ballot closes, so the record demands
  a re-read when the result exists rather than a fortnight later

### Removed

- **A caveat, rather than a correction.** The record derived Proposal A's 3:1 supermajority from the
  Constitution and stated plainly that the vote page gave no majority requirement. The page now
  states it — *"Proposal A needs a 3:1 majority, the other proposals need a simple majority"* — so
  the derivation was right and is now sourced. **Recording where a claim came from is what let this
  retire cleanly instead of reading as a contradiction**

### Notes

**All eight quotations in the record were re-confirmed against the page, not only the three added.**
Five had been carried forward from the 2026-08-05 check. A quotation nobody has re-read presents as
sourced while resting on an earlier session, and the gap was closed rather than written up as a
known limitation — one further fetch was cheaper than the caveat.

**Nothing else in the bundle was touched.** The remaining twenty-two concepts are 82 days or more
from expiry; working the list in date order is the point of the triage step, not a shortcut.

## [0.5.0] - 2026-08-13

**Tooling only — no concept changed.** Within `knowledge/` the only difference from v0.4.0 is the
one line of `log.md`'s release map. Verified: `git diff v0.4.0..HEAD -- knowledge/` was empty before
this release commit.

### Changed

- **The shared bundle checkers moved up one level**, to the outer meta-project, joining the link and
  ADR-index checkers as the single copy every workspace calls. Nothing about what they check
  changed; a second workspace needed them, and copying would have created the drift the promotion
  rule exists to prevent. This repository's hook now distinguishes what its own workspace owns from
  what every workspace shares
- **The audience checker now reads `README` and `CHANGELOG`**, not only `knowledge/`. A repository's
  most published-facing file had been audited by nothing. It flagged this `CHANGELOG` on its first
  run — every finding a dated release entry or a quotation, all legitimate, each now carrying a
  marker with its reason. History is not rewritten to satisfy a gate

## [0.4.0] - 2026-08-13

**A new category, and an absence that got an answer.** `distributions/` opens with the TeX
ecosystem, driven by a concrete need rather than survey completeness: `mmd2tex` is an AI-assisted
package heading for a CTAN upload, and its release runbook gates that step on knowing the position.

### Added

- **[TeX Live](knowledge/distributions/tex-live.md)** — a well-formed policy, unusual in three ways.
  It **separates legal exposure from disclosure etiquette**, so the mandatory part stays small and
  the advisory part is honest about being advisory; it **names its exemptions** (autocompletion,
  spelling, grammar) instead of leaving contributors to guess; and it uniquely covers
  **communication** — no AI-generated mailing-list or maintainer email unless clearly delimited
- **[CTAN](knowledge/distributions/ctan.md)** — recorded first as a **verified absence**, checked
  across the upload instructions, the 26,125-character upload addendum, the full help index and four
  candidate URLs. An absence written down is worth more than a gap left unwritten, but it is a claim
  about *publication*, not about whether a position exists
- **`.okf-types`** — this bundle's type vocabulary, in the file the gate reads.
  `check-bundle-types.py` checks it in both directions, since `okf` requires the `type` field (§4.1)
  but accepts any value
- **A documentation-link gate** over this repository's own `README`, `CLAUDE.md` and `CHANGELOG`,
  run **here against this repository's history** — the dead-filename set is repo-scoped, and names
  that died in the meta-project when this corpus was extracted are alive and correct here. Clean on
  first run

### Changed

- **The CTAN absence is now sourced.** Manfred Lotz, writing *"from the CTAN team"* on the tex-live
  list, 2026-05-21: *"For CTAN, also no official policy is in place. We are in discussion here."*
  That settles the tension TeX Live's scope clause created — it disclaims scope rather than
  describing a policy that exists — and upgrades the record from an unsourced absence to a sourced
  one, which is a different kind of claim. *"We are in discussion here"* dates it: a formal policy
  may appear
- **The footnote gate is `okf-gate`**, an installed command rather than a script reached through the
  meta-project. Three rules rather than two — measuring against `okf` v0.3.0 surfaced
  `okf/sources/footnote-unmatched`, a footnote label with no matching `sources[].id`, which had gone
  unenforced

### Fixed

- **`knowledge/log.md` said the CTAN question was still open**, three days after it closed. The
  concept was rewritten when the answer arrived and the log was not. Every gate was clean throughout
  — `okf validate`, `okf lint`, `okf-gate`, and the audience and type checks — because all of them
  verify structure and none reads for sense. Found while cutting this release, by reading

## [0.3.0] - 2026-08-05

**All four categories are now populated.** `vendors/` was an empty promise; filling it produced the
finding that justifies the category existing at all.

### Added

- **[SUSE](knowledge/vendors/suse.md)**, **[Red Hat](knowledge/vendors/red-hat.md)** and
  **[Canonical](knowledge/vendors/canonical.md)** — and with them the rule that **a vendor's policy
  governs its own staff, not your contribution**. That inverts every other category here: a
  distribution, project or foundation policy tells *you* what you may submit; a vendor policy tells
  its employees what *they* may do
  - Where a vendor also runs a community — Fedora, openSUSE, Ubuntu — **the community's policy is
    what binds a contributor**, and it is a separate document with a separate adoption process
  - **SUSE contradicts itself across two published versions.** The `2024-04` PDF states *"AI pair
    programming must not be used"*; the live web policy contains **no AI clause at all**. Verified by
    counting occurrences, and confirmed complete because the page carries the four sections that
    *bracket* the AI clause in the PDF. Which is current is not established — "SUSE bans AI pair
    programming" is widely repeated, traces to the PDF, and may no longer be true
  - **Red Hat publishes a disposition, not a policy**, deferring explicitly to each community's own
    rules. A widely-repeated claim that it has staff guidelines *"based on 3 principles"* is **named
    and declined** — no such enumeration appears in either post read
  - **Canonical's absence is verified across eighteen sections** of contributor documentation,
    including the sponsorship queue where such a rule would sit. It requires a Harmony-based **CLA**
    that licenses rather than assigns and is itself silent on AI

### Changed

- **[`overview.md`](knowledge/overview.md)** gains a vendors section stating the
  staff-not-contributor rule, and SUSE as the bundle's sharpest caution against trusting a single
  published source
- **[Debian](knowledge/distributions/debian.md) re-verified** three days before its discussion period
  closes. Still *In Discussion* to 2026-08-08, voting period unannounced. Proposal **B** amended
  twice, **C** once, and **A** is now framed as an amendment to the **Social Contract** — a
  Foundation Document, which the Constitution requires a **3:1 majority** to supersede. **A must
  clear a supermajority its five rivals do not**, and the vote page states no majority requirement,
  so this is read from the Constitution and cited as such

## [0.2.0] - 2026-08-05

The two sources v0.1.0 shipped as unread are both recorded. **Neither was blocked; both URLs were
wrong.**

### Added

- **[GCC](knowledge/projects/gcc.md)** — its threshold is **legal significance**, the copyright test
  that already decides whether a contribution needs an assignment, and nothing else in the bundle
  draws its line there. Three exceptions each do distinct work: legally insignificant LLM content is
  acceptable *if clearly marked*; **test cases are exempt even when legally significant**; and
  imported code such as `libsanitizer` is out of scope
  - Its **accessibility carve-out** is the clause most worth copying — screen readers, text-to-speech,
    translation and spelling assistance sit outside the policy entirely, provided the contributor
    verifies the output. A blanket "no AI" rule silently taxes contributors who rely on assistive
    technology, and non-native speakers through translation
  - The only policy here whose **first section is about people**: contributors presumed to act in
    good faith and **guided** rather than rejected. An explicit hedge against the failure mode Rust's
    draft concedes — an unverifiable rule turning into suspicion
  - Fourth adopter of `Assisted-by:` with no shared specification; reserves `Signed-off-by:` to
    humans and adds *"An LLM may not commit code to the project repository"* — a rule about **agents
    with write access**, not about generated text. The policy itself is **CC0 1.0**, the only one
    here released for reuse
- **[Fedora](knowledge/distributions/fedora.md)** — a **status record, not a content record**.
  Approved 2025-10-22 by a minuted **+7, 0, 0** Council vote, effective immediately; nine months on
  it is **not on the Council Policies page**, and the agreed text exists only as a comment on a
  Pagure ticket that was unreachable from two networks
  - The record states that a policy exists and binds, and **deliberately does not state what it
    says**. A rule in force that cannot be read is not a rule anyone can follow
  - The Community Blog carries a full policy text and it is the **proposal**, superseded by the
    revision actually approved. It is listed as a superseded draft rather than quoted

### Changed

- **[`overview.md`](knowledge/overview.md) restructured, not merely extended.** **Six shapes became
  seven** — GCC's *copyright-threshold rule* is genuinely new — and Fedora forced a **fourth state**
  alongside prohibited, permitted and undecided: **a rule in force that cannot be read**
  - The axes gained **"who the rule taxes"**: a blanket no-AI rule falls hardest on contributors who
    use AI to work at all. Every project that considered translation permits it; only GCC extends the
    reasoning to accessibility. *A policy that does not carve this out has excluded people without
    deciding to*
  - The DCO section records that GCC accepts **either** an FSF assignment **or** a DCO and its AI
    policy turns on neither — further evidence the instrument is not the unit of choice
- **[Linux kernel](knowledge/projects/linux-kernel.md) strengthened with a second primary.**
  `submitting-patches.rst` makes `Assisted-by:` **required, not encouraged** — *"Failure to do so may
  impede the acceptance of your work"* — in the *main* submission document, so a contributor
  following the ordinary process meets it. It also records **why** the kernel coined a token:
  `Co-developed-by:` denotes authorship and obliges a following `Signed-off-by:` from that co-author,
  which the AI policy forbids an agent from adding
- **`CONTRIBUTING.md` gains a narrowly-drawn exception for status records**, which the Fedora record
  would otherwise contradict. A status record makes different claims and needs different sources,
  **not weaker ones** — the rule is unchanged where it counts: no claim about what a policy says
  without reading the text

### Fixed

- **A wrong claim about why two sources were unread.** v0.1.0 logged Fedora and GCC as *"located,
  retrieval blocked"* on the strength of HTTP 200 responses from Anubis-protected hosts. **Anubis
  serves a challenge page for any path, including ones that do not exist**, so those 200s confirmed
  neither retrieval nor existence — `gcc.gnu.org/wiki/AIpolicy` never existed, and neither did the
  recorded Fedora council path. The caution already in `CLAUDE.md` — *a status code proves the server
  answered, never that the content arrived* — had been applied to **content** and not to
  **existence**
- The release map in `knowledge/log.md` still read *"none yet — the bundle is a skeleton"* after
  v0.1.0 was cut

## [0.1.0] - 2026-08-05

First public release. Every record was read from the organisation's own text; nothing was imported
from the survey this replaces.

### Added

- Bundle skeleton per `supplychain-workspace` ADR-0011: structure, categories filed by <!-- audience-ok: dated release entry citing the ADR that chartered this bundle -->
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
- `supplychain-workspace` ADR-0011 was amended 2026-08-05: the field is 190+ organisations, not 27, <!-- audience-ok: dated release entry recording an amendment to that ADR -->
  so completeness is not the deliverable and "born red" is a steady state rather than a backlog.
