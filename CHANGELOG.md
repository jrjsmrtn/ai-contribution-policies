# Changelog

All notable changes to this bundle are documented here. `knowledge/log.md` is the content-level
view of the same history, date-grouped per OKF §9; this file is the repository-level view.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
