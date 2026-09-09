# Changelog

All notable changes to this bundle are documented here. `knowledge/log.md` is the content-level
view of the same history, date-grouped per OKF §9; this file is the repository-level view.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.13.0] - 2026-09-09

### Added

- **[`projects/llvm.md`](knowledge/projects/llvm.md)** — the most theorised policy in the bundle,
  reached from a parked lead about an `AGENTS.md` debate that turned out to be the delivery argument
  for a policy in force since 2026-01-16. It **names the problem** — an *extractive contribution*,
  quoted from Nadia Eghbal and attributed — states a **golden rule**, and **diagnoses what changed**:
  a patch used to evidence a would-be contributor's interest, and generation destroyed that signal.
  Enforcement is countable: a paste-ready refusal, escalation, and an `extractive` label carrying
  **41** pull requests. Forbids AI on `good first issue`, inverting Elixir's label gating. Grants the
  bundle's only named exception. And **copies attributed text from Fedora's policy**, which this
  bundle records as in force but unpublished.

### Fixed

- **[`projects/osquery.md`](knowledge/projects/osquery.md)** — the record said no agent-instruction
  files existed in its 2,559 tree entries. It carries **`.cursor/rules/build-format.mdc` and
  `.cursorignore`**; the sweep probed for `.cursorrules`, the legacy single-file name, and missed the
  current directory convention. A systematic re-sweep across eleven conventions confirmed **osquery is
  the only affected record**. The conclusion is unchanged — both files are build guidance — and its
  basis is now correct.

### Changed

- **[`mechanisms/agent-file-pointers.md`](knowledge/mechanisms/agent-file-pointers.md)** — records
  that `.cursor/rules/` is a **directory**, so the symlink construction cannot reach it, and that
  `.cursorignore` is a different artifact class: every other file there adds context, that one
  subtracts it.
- **[`mechanisms/instruction-file-governance.md`](knowledge/mechanisms/instruction-file-governance.md)**
  — `.mdc` frontmatter carries `alwaysApply`, so a rule may be applied conditionally rather than every
  session. **That is the staging `AGENTS.md` lacks, as a format feature rather than a discipline**,
  and the admission rules are corrected to a fallback for the always-applied case.



## [0.12.0] - 2026-09-09

### Added

- **[`mechanisms/instruction-file-governance.md`](knowledge/mechanisms/instruction-file-governance.md)**
  — the fourth mechanism concept, and the last candidate ADR-0012 named. An instruction file is a
  **budget, not a document**, loaded whole every session. systemd admits a rule only after watching an
  agent fail on it; Zed sets three criteria, bars the agent from editing `.rules` during ordinary
  work, and scopes rules per crate. **No shared text** — arriving at the same principle separately is
  the finding. Records what neither solves: both bound what enters and neither describes removal.

- **[`mechanisms/agent-file-pointers.md`](knowledge/mechanisms/agent-file-pointers.md)** — the third
  mechanism concept. Agents look for instructions under different filenames and no specification says
  which; **every project here that solves it uses a git symlink**, and the one that duplicated the
  content instead maintains two files that have already diverged.

### Fixed

- **A claim asserted in six records was wrong.** Asahi Linux's, Dependency-Track's and systemd's
  `CLAUDE.md` were described as "nine-byte pointer files" and contrasted with the "symlinks" Elixir
  and NetworkManager chose. **All of them are symlinks** (mode `120000`, verified via the git tree
  API), so the distinction did not exist and *"a pointer can go stale and a symlink cannot"* was false
  about every example it was attached to. Corrected in all six.
- **The cause is recorded as a retrieval hazard.** `raw.githubusercontent.com` serves a symlink's
  target path as its content, so a symlink fetches as a small file containing a filename and is
  indistinguishable from a deliberate stub. **Check the mode, not the bytes.**



## [0.11.0] - 2026-09-09

### Added

- **[`mechanisms/assisted-by-trailer.md`](knowledge/mechanisms/assisted-by-trailer.md)** — the second
  mechanism concept. **`Assisted-by:` is not an AI tag**: the kernel defines it for "any sort of
  advanced coding tool" and lists a model beside `coccinelle` and `sparse`, so projects narrowed a
  general instrument to a specific question and most of the disagreement follows. Five mutually
  exclusive positions across nine projects and foundations; `Co-developed-by:`'s structural
  impossibility sourced from the kernel's own sign-off rule; and two failure modes no entity record
  states — the field is **unverifiable**, and it **attributes at the wrong granularity**.

### Changed

- **[`overview.md`](knowledge/overview.md)** — its trailer section shrank from 74 lines to 46, applying
  the ADR-0012 anti-duplication rule at creation rather than deferring it. The map keeps what carries
  beyond the field and the documented `docs.kernel.org` retrieval hazard; the detail moved to the
  concept.

### Fixed

- **A malformed heading in `knowledge/log.md`, shipped in v0.10.0.** The `## 2026-09-08` heading was
  concatenated onto the preceding line by a scripted insertion whose anchor began with a newline while
  the inserted text did not, so it rendered as inline prose and that day's entries were orphaned.
  **`okf validate` passed it** — OKF §9 constrains the form of log headings, so a heading that is not
  a heading is invisible to the check.
- **A gate now covers that class.** `check-bundle-log.py` joins the shared checkers and is wired into
  this bundle's pre-commit hook and the weekly sweep. It checks `glued-heading`, `bad-heading`,
  `impossible-date` and `order`; `--self-test` plants each fault, and the decisive test is the actual
  broken file recovered from the `v0.10.0` tag, which it reports at line 12. A `dup-date` rule was
  written and **removed when it failed four correct logs** — repeating a date is a deliberate
  tranche convention in this portfolio.



## [0.10.0] - 2026-09-09

### Added

- **[`vendors/astral.md`](knowledge/vendors/astral.md)** — the head of the four-hop lineage, and the
  cleanest inherited floor here: one `AI_POLICY.md` in `astral-sh/.github`, **no project overrides
  it**, verified across five repositories including `uv` and `ruff`. Argues its human-in-the-loop rule
  from the **criticality** of what it maintains, which nobody else does. Recorded with a checkable
  event and no inference: Astral is joining OpenAI while forbidding autonomous agents.

- **[`projects/ripgrep.md`](knowledge/projects/ripgrep.md)** — the middle hop of the only attributed
  policy lineage here, which is now four dated hops: `astral-sh/.github` (2026-03-13, an org-level
  default) → ripgrep (2026-05-26) → Zed (2026-08-21) → systemd (2026-09-03, canary only,
  unattributed). **ripgrep pins its citation to a commit and the pin was verified byte-identical to
  upstream**, where Zed cites a page. Its whole `CONTRIBUTING.md` is 213 bytes pointing at the policy.
  Two clauses nobody else has: responsibility named in **both** directions, and a **length bound** on
  quoted model output, following from a sanction of hiding rather than closing.

- **`knowledge/mechanisms/` and [`review-canary.md`](knowledge/mechanisms/review-canary.md)** — a new
  category for recurring mechanisms, and its first concept. A mechanism concept says how a thing
  works, who built it, how it spread and how it fails; an entity record says what one organisation
  chose. The canary now has **three implementations across three projects and two designs** — a
  review canary planted on every AI-touched change, and a violation watermark planted only on a
  breach — which no single entity record could own.
- **[`projects/zed.md`](knowledge/projects/zed.md)** — the canary's origin, and the only record whose
  policy cites its own source (*"adapted from ripgrep's AI policy"*). Welcomes LLM coding, refuses
  autonomous agents, reserves maintainer-facing prose to humans, and carries the most generous
  translation clause in the bundle.
- **[`projects/systemd.md`](knowledge/projects/systemd.md)** — treats AI as equivalent to `sed`, `awk`
  or `coccinelle`, requires all thinking to precede the tooling, bars authorship credit entirely, and
  sanctions the contributor rather than the patch. Copied Zed's canary instruction **without** its
  check.

### Changed

- **[`overview.md`](knowledge/overview.md)** — its claim that `vendors/` is "the one category where
  the policy does not bind the reader" was falsified by Astral, whose org-wide policy governs any
  contributor to `uv` or `ruff`. The section now names the exception and the rule that actually
  helps: not who published a policy, but **who it binds**.
- **[`projects/ripgrep.md`](knowledge/projects/ripgrep.md)** — Astral is no longer "not yet a record".


- **[`projects/networkmanager.md`](knowledge/projects/networkmanager.md)** — a published record had
  gone false. It said the project required no disclosure; since 2026-09-03 disclosure is a mandatory
  merge-request template field, alongside an `AGENTS.md`, a refusal list, an extended trailer ban and
  CI enforcement of a `biblioklept` watermark. The record's own re-verification note had named this
  as the likeliest change and it still went stale for five days.



## [0.9.0] - 2026-09-07

### Added

- **[`projects/perl.md`](knowledge/projects/perl.md)** — `AI_POLICY.md`, added 2026-07-30, the only
  policy here that draws its lines **by artifact type**: code may be accepted, documentation will
  not, prose is grounds for dismissal, reading the codebase is free, and agents are barred from every
  channel. **Documentation is governed more strictly than code**, inverting the usual premise. Adds a
  competence bound (*"code that you could not … have written yourself"*) and a **maintenance
  obligation** extending past the merge, plus a unique verified-security-analysis exception and a
  scope boundary drawn by module ownership rather than repository.
- **[`projects/elixir.md`](knowledge/projects/elixir.md)** — permitted with restraint, argued from
  redundancy rather than risk: *"Elixir maintainers already have access to AI … we often find the
  point of view of the human behind the agent more valuable."* Two mechanisms nothing else here has —
  agent work **gated by issue label**, and automated compiler/type-system changes required to be
  **paired with adversarial agents** whose approval is advisory. Gives the DCO a third answer: the
  agent may write, only the human may certify. Its `AGENTS.md` is a **git symlink** to
  `CONTRIBUTING.md`, so agent-facing and human-facing text cannot drift.

- **[`projects/osquery.md`](knowledge/projects/osquery.md)** — reversing the 2026-09-06 decision not
  to record it. osquery is a Series of LF Projects, LLC, so unlike the other silent projects here it
  sits under a foundation that has published on AI — and **what it inherits is weaker than it looks**:
  the charter binds contributors to the `lfprojects.org` policy list, which has no AI policy, while
  the LF's generative-AI text sits elsewhere, reads as *should*, and invites projects to write their
  own. It also keeps the overview's "checking only the foundation is a reliable way to be wrong"
  warning honest, as a large, funded, actively maintained counter-example. **The asymmetry no other
  record has**: two open issues propose tables inventorying AI agents and skills on an endpoint, so
  the project is being extended to report which agents run across a fleet while saying nothing about
  whether one may write its own code.

- **[`foundations/owasp.md`](knowledge/foundations/owasp.md)** — the fourth foundation record and the
  first that sets **no AI baseline**. OWASP mandates the DCO and requires contributions be a
  contributor's "original work", with any substitute agreement covering "the risks of plagiarized
  code" — a provenance floor written **2021-09-30** and never revisited. Those are the two concepts
  every provenance-based position in this bundle is built from, so the machinery is present and
  unused. The absence is established, not unfound: zero AI terms across all 60 files of
  `OWASP/www-policy`, positive control at 56, and the checker proven able to fail on a planted
  positive.

### Changed

- **[`projects/cdxgen.md`](knowledge/projects/cdxgen.md)** — its claim that "OWASP is not a
  foundation of the kind this bundle records under `foundations/`" was true when written and false
  once the record existed; rewritten to point at it.
- **[`overview.md`](knowledge/overview.md)** — the foundations section enumerated three foundations
  that "each set a permissive baseline". It now carries the fourth that sets none, and the qualifier
  that *foundations are floors* holds only where a foundation has poured one.



## [0.8.0] - 2026-09-07

### Fixed

- **Bundle-relative links were checked by nothing.** `.lefthook.yml` had retired
  `check-doc-links.py` for `knowledge/` on the stated grounds that `okf` resolves bundle links. It
  does not: measured in the landscape sibling on 2026-09-04, a planted missing target left `okf
  validate` and `okf lint` both reporting `valid: true` at exit 0. The checker is wired back in over
  `knowledge/` (249 links across 36 files, previously unchecked). Re-wiring it needed a fix in the
  shared checker, whose reference-style guard matched OKF footnote definitions (`[^id]:`) and so
  fired on every concept file.
- **The `okf` version is now an asserted floor of 0.4.0, not prose.** The hook said `v0.2.1`,
  `run-gates.sh` said `v0.3.0`, the installed tool was `0.4.0`, and nothing compared them.

### Changed

- **[`overview.md`](knowledge/overview.md)** — two additions carrying record-level findings up to the
  cross-cutting map. **"An eighth artifact, and it is not a shape"**: cdxgen's self-declaration
  governs nobody, so it is an artifact class rather than a shape, and the section states the trap —
  a reader asking whether a project accepts AI contributions finds a dated, machine-readable file
  that does not answer. **"The filename predicts nothing"**, added to the location section with a
  measurement: across four Ash agent files, zero carry permission, prohibition, disclosure or
  trailer language against 4 in the Kubernetes control, and the 181-byte `AGENTS.md` that forbids
  everything is two hundred times smaller than the 36 KB one that governs nothing. `verified` was
  deliberately not bumped — the new claims were checked today, the rest was not re-read.



- **[`projects/cdxgen.md`](knowledge/projects/cdxgen.md)** — corrected and extended with the agent
  artifact surface, which the first draft understated as one file. It is **24 paths**: 5 skills in
  `.agents/skills/`, 14 in the Claude Code plugin, 1 at the repository root describing cdxgen to
  consumers, plus three instruction files and the marketplace manifest. The finding is the
  **tiering** — `.agents/README.md` mirrors two skills into the plugin and withholds the three
  contributor-facing ones by design, making cdxgen the only organisation here that routes contributor
  guidance and user guidance through different channels.

### Added

- **[`projects/dependency-track.md`](knowledge/projects/dependency-track.md)** — permitted, and
  required to leave no trace in the commit. The third project to forbid the AI co-author trailer and
  the only one that enumerates what tooling actually emits — trailer, **session link**, and
  **"generated with" footer** — while explicitly keeping a human `Co-authored-by` allowed. It sits
  beneath a DCO sign-off requirement, making a coherent pair: the human certifies, the tool is
  unnamed. **The rule lives in `AGENTS.md`; `CONTRIBUTING.md` never mentions AI and never references
  it**, so a contributor reading the contributing guide breaks a rule they were never shown — cdxgen
  inverted. Two further firsts: a prohibition on the agent *opening* issues or PRs at all (enforced
  by dad joke, justified by maintainer attention rather than principle), and a `make AGENT=1` build
  flag that reformats output for agents — the only tooling accommodation in the bundle.



- **[`projects/cdxgen.md`](knowledge/projects/cdxgen.md)** — the first record here that is not a
  policy. cdxgen has no `CONTRIBUTING.md` and no `CODE_OF_CONDUCT.md`, and asks nothing of a
  contributor about AI; it publishes an `AI-DECLARATION.md` grading **its own** AI usage per source
  path against the external six-level `ai-declaration.md` v0.1.2 scale
  (`none · hint · assist · pair · copilot · auto`). **The only disclosure in the bundle that is a
  parseable artifact rather than prose, and the only one describing the project rather than
  governing the contributor.** It is maintained — a 2026-08-06 commit carries the paths through a
  `lib/helpers/*` → `lib/inventory/*` refactor, changing no fact — which is what separates a
  declaration from a badge. Its 36 KB `AGENTS.md` is a codebase guide with no policy content: the
  same filename as Asahi Linux's refusal directive, the opposite artifact.

- **[`projects/asahi-linux.md`](knowledge/projects/asahi-linux.md)** — prohibited outright, enforced
  by one warning then a **permanent ban from the project and all associated spaces**: the harshest
  sanction here and the only one scoped past the patch queue. It is also **the only policy in the
  bundle written to the agent rather than the contributor** — a 181-byte `AGENTS.md` instructing the
  tool to refuse and redirect, with `CLAUDE.md` and `GEMINI.md` as pointers
- **A risk argument nothing else makes**: regurgitation likelihood *"is proportional to the
  specificity of the problem area"*, so a project reverse-engineering undocumented Apple hardware is
  at higher risk than a web application from the same tool — and the policy **extends an existing ban
  on leaked vendor documentation** rather than inventing a new regime
- **The environmental ground, adopted.** Debian's Proposal H argued it and lost; Asahi's Board holds
  it as settled policy. One argument, two governance structures, opposite outcomes

## [0.7.0] - 2026-08-30

**The release the whole cycle was waiting on.** Debian's General Resolution was declared, and the
corpus grew from 23 records to 29 while waiting — the largest single release so far, and the first
where cross-record findings outweigh any individual record.

### Added

- **[`projects/networkmanager.md`](knowledge/projects/networkmanager.md)** — a policy added
  2026-08-07, nine sentences long, that **requires no disclosure at all** and is still among the more
  demanding here. It answers detection-versus-declaration with a third thing, **demonstration**:
  *"Respond to review comments yourself. If you cannot discuss your own patch with a reviewer, it
  will not be merged."* The reviewer never decides how the patch was produced, only whether the
  sender can defend it — the question the other two are proxies for
- **[`projects/nerves.md`](knowledge/projects/nerves.md)** — permits AI, reserves human-facing writing
  to humans with the sharpest line in the corpus (*"Using AI to translate or tighten your own writing
  is fine. Using it to write in your place is not"*), and requires `Assisted-by:` **naming the model**
  — the format the kernel retired eleven days earlier. Only record here governing agent-config files
  (`AGENTS.md`, `CLAUDE.md`), and a fifth DCO position: no `Signed-off-by` at all
- **[`projects/macports.md`](knowledge/projects/macports.md)** — a **proposal, not a rule**: PR #420 is
  open and contested. It matters because it **documents a hazard the bundle could previously only
  describe**: it adopts the trailer *"in the format recommended by the Linux kernel developers"*,
  **citing `docs.kernel.org`** — which still serves the retired format — in a PR opened **one day
  after** mainline changed it. A stale rendered page is exporting a superseded rule to other projects
- **One trailer, three mutually exclusive live rules**: kernel requires it without the model, Nerves
  requires it with the model, GTK forbids it. MacPorts' PR calls it *"the emerging de facto
  standard"*; **the corpus is now direct evidence that no such standard exists**
- **[`projects/gtk.md`](knowledge/projects/gtk.md)** — and the finding of the release. GTK **forbids
  the `Assisted-by:` trailer the Linux kernel requires**, citing the same reason: it is *"free
  advertising for AI companies"*. Identical premise, opposite instrument — the kernel deleted the
  vendor from the tag, GTK deleted the tag. **The trailer is therefore not portable**, and tooling
  must key on the destination project. GTK also binds *maintainers*, caps the **shape** of a change
  rather than its volume, bans **fabricated** benchmarks and reproducers, and forbids feeding review
  feedback to a tool
- **[`projects/gnome.md`](knowledge/projects/gnome.md)** — the AI rule in the GNOME Shell extension
  review guidelines, added 2025-11-30. **The only detection rule here that names its artifacts**:
  *"large amounts of unnecessary code, inconsistent code style, imaginary API usage, comments serving
  as LLM prompts"*. The last two cannot be produced by a careful human, so it is Git's detection rule
  with the false-positive surface removed. Its ground is **reviewer strain**, the third policy today
  to say so. Scope is the third-party extension channel, not GNOME's own modules — the record states
  that boundary and declines to claim an absence it did not establish
- **A fourth DCO destination: abolish the instrument.** NetworkManager — *"Do not use
  "Signed-off-by:" lines in commits … It has no meaning."* Certification attaches to a licensing
  commitment instead. With the kernel, QEMU and the Linux Foundation, the bundle now shows four
  positions on the DCO and one constant: the contributor carries the legal risk either way
- **A second kernel policy document**, `generated-content.rst`, in tree since 2026-01-20 and never
  cited. **Tool-generic** rather than AI-specific, it asks for **prompts** to be disclosed and
  **enumerates maintainer discretion** including outright rejection. Its absence was a miss at
  creation, not drift — it predated the record by seven months
- **The kernel's nine-step mandatory procedure for AI bug-hunting** (commit `3d7c44f7`), including
  that the assistant *"must never send anything itself"*
- **The wireless subsystem exchange of 2026-08-06**, in
  [`projects/linux-kernel.md`](knowledge/projects/linux-kernel.md) — the enumerated maintainer
  discretion exercised in public. syzbot's AI-generated patches were **fully compliant** (human
  `From:` and `Signed-off-by:`, pre-reviewed by a named engineer) and were refused anyway, because
  *"clearly nobody actually even bothers to look at the semantics of the code"*. **Formal compliance
  with an AI policy does not deliver what the policy exists for.** It resolved in three hours with
  syzkaller withdrawing, and no rule broken or amended
- **The strongest argument for disclosure here now comes from someone refusing the contributions**
  (also in [`overview.md`](knowledge/overview.md)): losing the labelled channel does not stop the
  patches, only the ability to triage them. From the receiving end disclosure is **a filter**, which
  answers the objection that such rules are unenforceable
- **[`distributions/debian.md`](knowledge/distributions/debian.md) records the 2025 AI General
  Resolution Debian withdrew** — *"Interpretation of DFSG on Artificial Intelligence (AI) Models"* —
  as an **excluded neighbour**, not as a record. It is model licensing, not contribution policy;
  naming it makes the scope boundary legible, since otherwise a reader cannot tell a subject this
  bundle excluded from one it missed. Both primaries were read, including the proposer's withdrawal
  message of 2025-05-08
- **A changelog-structure gate**, `check-changelog.py`, wired into `.lefthook.yml`. It catches
  duplicated sections within a release, duplicate or misordered versions, malformed headings, a
  misplaced `[Unreleased]`, and empty sections — the shape faults, which are checkable even though the
  prose is not. It exists because `[Unreleased]` duplicated itself in this very release and nothing
  saw it. **Its `empty-section` check was wrong on first run** and flagged a valid prose-only `Notes`
  section; it now counts content rather than bullets, which is why it was run against the real file
  before being trusted. Deliberately does **not** police the section vocabulary (this corpus uses
  `Notes` legitimately) or re-implement ISO date checking, which `check-dates.py` owns
- **[`projects/kubernetes.md`](knowledge/projects/kubernetes.md)** — policy dated to **2025-11-08**,
  making it one of the oldest here. It is the **second project to forbid the `Assisted-by:` trailer,
  for the opposite reason to GTK's**: accountability rather than vendor advertising — five positions
  now on one tag. And it holds the **only mechanical enforcement in the bundle**: the CNCF CLA check
  enabled for co-authors, which an AI cannot satisfy, so the prohibition enforces itself before a
  maintainer looks. Also notable for stating sanctions in advance, supplying disclosure wording, and
  giving a motive nothing else does — the policy exists partly to stop the argument recurring
- **[`projects/qemu.md`](knowledge/projects/qemu.md) re-verified and extended.** The prohibition
  **stands** (checked against `master` 2026-08-30), but a **relaxation patch has been pending since
  2026-05-28** that would permit AI in revert-cheap areas and add an **`AI-used-for:`** trailer — a
  fourth position on attribution, and one that reframes the question: `Assisted-by` *"doubles as a
  check that the author has read the policy"*, whereas `AI-used-for` is guidance for the reviewer.
  It also carries the corpus's sharpest statement of why review cost is the real constraint —
  *"a reviewer can no longer assume that the submitter has reasoned through every line"* — and its
  `stale_after` drops to 2026-11-30, because a live proposal to reverse a stance outruns a six-month
  cadence
- **An index-freshness gate**, `check-bundle-index.py`, wired into `.lefthook.yml`. `index.md` is
  **derived** — `okf index` generates it from concept frontmatter — and nothing compared the two,
  which is how three drifts survived every hook. It regenerates into a temporary copy and diffs, and
  was proved against planted faults in both directions it reports

### Changed

- **[`distributions/debian.md`](knowledge/distributions/debian.md): the result is official.** The
  Secretary's declaration, quorum arithmetic and a **425-vote tally sheet** were published 2026-08-30,
  ~36 hours after the ballot closed. **Option 5, "Responsible Use of Generative AI"** is the declared
  winner. The record had carried Devotee's automated tally for a day, labelled as unofficial; every
  figure matched **except quorum**, which was 47.244 unofficially and **48.4897** in the declaration.
  `stale_after` returns to six months

- **[`distributions/debian.md`](knowledge/distributions/debian.md) rewritten around the result.** The
  General Resolution closed 2026-08-28 and **Option 5, "Responsible Use of Generative AI"**
  (Proposal E) won outright — sole member of the Schwartz set, beating *None of the above* 281–126.
  Debian **permits** generative AI under the standards that already applied, with disclosure
  **encouraged but explicitly not required**
- **The record's own derived claim was confirmed by the tally.** On 2026-08-05 it read the
  Constitution and concluded Proposal A needed a **3:1** majority its rivals did not, when the vote
  page stated no requirement. The tally dropped that option at **0.560 < 3**. First time a claim this
  bundle *derived* rather than read has been checked against the primary and held
- **Recorded from the automated tally and labelled as such** — the Devotee publication states it is
  *"an automated, unofficial publication of vote results"*. `stale_after` is two weeks, and the next
  read is triggered by the Secretary's declaration rather than by a date
- **[`projects/linux-kernel.md`](knowledge/projects/linux-kernel.md) rewritten.** The `Assisted-by:`
  tag stopped naming the model on 2026-08-03 (commit `816d9992`): `AGENT_NAME:MODEL_VERSION` became
  the bare literal `LLM`, because identifying it *"provides free advertising to proprietary software
  companies"*. The **requirement is unchanged** — narrower than the reporting suggested — but it
  establishes a new axis, attribution *granularity*. Its `stale_after` drops from six months to three
- **[`overview.md`](knowledge/overview.md)**: Debian joins the **responsibility rule** row, as does
  NetworkManager, which also adds the demonstration case and a fourth DCO destination. A draft that
  filed Debian as an eighth shape, "the deliberate non-rule", was withdrawn before shipping — the
  adopted text is the same shape Python, curl and the kernel hold
- **`CLAUDE.md`'s status section**: the record count is now derived (`okf list knowledge`) rather than
  written out, and verification coverage is stated as a dated audit event, because a probe confirmed
  that removing a `verified:` block produces no `okf lint` finding
- **Category index regenerated** with `okf index`, correcting three drifts no gate was watching:
  Debian's row still said *"six competing proposals in discussion"*, and CTAN and TeX Live sat in a
  bullet list outside the table with CTAN's pre-correction description
- **A second GNOME sweep read `README` and `HACKING` across all 321 modules**, after the record
  flagged them unsurveyed. **Seventeen modules state an AI policy — nine in `CONTRIBUTING`, eight in
  `README`/`HACKING`, with zero overlap.** Reading only `CONTRIBUTING` misses almost half, which is a
  caution about survey method as much as about GNOME
- **The boilerplate ban's origin is now documented**: written for Loupe, announced on GNOME Discourse
  **2025-02-26** with an explicit call to adopt it *"for all official GNOME software"*, and credited
  in place by `console`, `dia` and `gitg`. **Policy diffusion across a federation, dated and
  observable — and it bypassed the handbook entirely**, which was never amended
- **`libxml2` rejects the boilerplate's translation exception** — *"No LLMs for comments on the bug
  tracker, including translation"* — offering native-language posting instead. The accessibility
  carve-out GCC calls the clause most worth copying is decided **both ways inside one federation**.
  `vte` frames its ban as licensing and broader: *"wholly or partly, by using AI in any form"*
- **[`projects/gnome.md`](knowledge/projects/gnome.md) rewritten around a survey of all 321 modules**
  in the GNOME group: 45 carry a `CONTRIBUTING`, **nine state an AI policy**, in three incompatible
  positions — a seven-module named-vendor ban (the first here), `gnome-commander`'s argued ban on
  **deskilling** grounds, and GTK's conditional permission. The shared ban text **has already
  drifted**: two copies name Ollama and five do not. The generalisable finding is that **for a
  federated project the umbrella's documentation may not be where the rule lives, and sibling modules
  may contradict each other**

### Fixed

- **[`projects/gnome.md`](knowledge/projects/gnome.md) asserted something false about its own
  sources.** It said GNOME's rules for its own modules were *"not established"* because the handbook
  *"renders client-side"*. The handbook is a **Sphinx site serving static HTML**, fully retrievable.
  **An untested assumption about a source became a reason not to look.** Replaced with a verified
  absence: **no AI policy anywhere in the GNOME Project Handbook**, across all 76 pages, including
  `development/change-submission`, `development/commit-messages` and `development/legal`. The absence
  is bounded — per-module `CONTRIBUTING` files were not surveyed — and the corrected fact is the more
  interesting one: GNOME gates the extension channel it curates while its own contributor
  documentation is silent
- **The kernel record's `resource:` served superseded text.** `docs.kernel.org` renders a released
  kernel (7.2.0) and still showed the old tag format after mainline dropped it. Sources now point at
  `git.kernel.org`; the rendered page is demoted to a citation for the lag itself. **A quotation from
  a rendered docs site can be stale while looking perfectly sourced**
- **The same stale format was asserted in three other files** — `overview.md`,
  `foundations/apache-software-foundation.md` and `projects/ansible.md` — because it had been copied
  into comparison tables. All corrected; the Ansible comparison is sharper than before, since the two
  projects share the field name and now encode opposite intentions with it
- **Where the Debian record said to look for the result was wrong.** It named the vote page; hours
  after the ballot closed that page had no outcome section, no tally sheet and no quorum log, while
  the result was already on the `debian-vote` list. **The list publishes first**
- **This section had duplicated itself.** `[Unreleased]` carried two `### Added` blocks, two
  `### Changed` blocks, and a `### Notes` entry stating `distributions/debian.md` was *"deliberately
  left expired"* — which the same day's later work made false. Consolidated. **No gate reads a
  changelog for sense**, which is the same failure mode as every other item in this release
- **Scratch output no longer trips `reuse lint`**: `.playwright-mcp/` (browser-tooling console logs
  and page snapshots) and `.tmuxp.yml` are ignored

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
