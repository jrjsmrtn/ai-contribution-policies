# Bundle Update Log

Content changes to the knowledge bundle: records added, re-verified, corrected or expired.

**Date headings, per OKF §9**, which requires ISO 8601 `YYYY-MM-DD` and admits no other heading
form. The log's model is date-grouped, not release-grouped, so an entry cannot carry its release
in a heading. The release map below is how a `knowledge/` tree separated from this repository
still names its version: OKF has no in-band content-version field, and a git tag does not travel
with a copied directory.

**Releases**, newest first: **v0.6.0** 2026-08-14 (debian re-verified) · **v0.5.0** 2026-08-13 (tooling only) · **v0.4.0** 2026-08-13 · **v0.3.0** 2026-08-05 · **v0.2.0** 2026-08-05 · **v0.1.0** 2026-08-05.
[`../CHANGELOG.md`](../CHANGELOG.md) is the repository-level view of the same releases. <!-- audience-ok: an explicit repository-level pointer; a copied tree loses it by design -->

## 2026-08-30

* **`projects/qemu.md` re-verified and extended: the prohibition stands, but it is under active
  challenge.** Found by mining Phoronix further back than the first sweep. The record's stance was
  checked against `master` and **holds** — *"Current QEMU project policy is to DECLINE any
  contributions which are believed to include or derive from AI generated content."*
* **A relaxation patch has been pending since 2026-05-28** — Paolo Bonzini, *"[PATCH] docs/devel:
  relax policy on AI-generated contributions"*. `code-provenance.rst` last changed 2026-05-22, before
  the patch, so it has not landed after three months. Recorded as a pending proposal, not a stance
  change.
* **It concedes the legal question rather than answering it**: *"The copyright and license status of
  LLM output remains unsettled, so that question is still open. What has shifted is the balance of
  risk."* Two grounds — no serious legal trouble observed elsewhere, and Red Hat's own risk
  assessment — with the qualification that matters: *"a community of individual developers does not
  have the legal backing of a company."* **A Red Hat engineer citing Red Hat and then saying it does
  not transfer is the vendor/community boundary argued from the inside.**
* **A third axis for "where is AI acceptable".** QEMU would scope by **blast radius** — *"easy to
  revert and unlikely to spread: tests, documentation, mechanical changes, and small bug fixes"*,
  with core code off-limits. GCC scopes by legal significance, GTK by the shape of the change. Same
  question, three incompatible cuts.
* **The sharpest statement in this bundle of why review cost is the problem**, and the only one that
  names the mechanism rather than the symptom: *"AI lowers the cost of producing a patch but does
  nothing to lower the cost of understanding and reviewing one; if anything it raises it, since **a
  reviewer can no longer assume that the submitter has reasoned through every line**."* Six projects
  now give reviewer bandwidth as their ground. This one explains why volume caps and
  "be-able-to-explain-it" clauses keep arriving together — both restore the prior the reviewer lost.
* **A fourth trailer, and it reframes what a trailer is for.** `AI-used-for:` would record *where* AI
  was used, and the patch says why that differs: `Assisted-by` *"doubles as a check that the author
  has read the policy"*. **Compliance signal versus reviewer guidance** — two jobs the same field has
  been asked to do, which is part of why no convention has settled. Four positions now: kernel
  (`LLM`), Nerves (`AGENT:MODEL`), GTK (forbidden), QEMU (`AI-used-for`, proposed).
* **`stale_after` shortened 2027-02-04 → 2026-11-30.** A live proposal to reverse a stance is exactly
  the condition a six-month expiry handles badly; had this not been re-checked opportunistically, a
  merge would have gone unnoticed for five months. **The record was right and nearly stale for the
  wrong reason** — its claim was accurate, its cadence was not.
* **The Phoronix listing misdates articles, and the sweep nearly inherited it.** The archive page
  attributed this story to 2026-06-10 and the Debian result to 2026-03-30; the real dates are
  2026-05-28 and 2026-08-29. The date is assigned from the nearest preceding date marker, which
  sidebar blocks break. **Every date here came from the article or the git history, not the listing.**

## 2026-08-29

* **Creation: [Nerves](projects/nerves.md) and [MacPorts](projects/macports.md), and together they
  turn a hypothetical hazard into a documented one.** Nerves was found in a newsletter; MacPorts came
  from a pull request the maintainer pointed at after this bundle had wrongly concluded MacPorts had
  nothing.
* **A rendered documentation site is exporting a superseded rule to other projects.**
  `docs.kernel.org` renders a released kernel and still serves the retired
  `Assisted-by: AGENT_NAME:MODEL_VERSION`. **MacPorts PR #420 proposes exactly that format,
  explicitly *"in the format recommended by the Linux kernel developers"*, citing that page — in a PR
  opened 2026-08-04, one day after mainline changed it.** The PR is still open and nobody in its
  thread has noticed. This was recorded this morning as a re-verification trap for this bundle; it is
  now evidence about the ecosystem. **The mechanism is evidenced; intent is not claimed.**
* **Nerves adopted the same retired format on 2026-08-14 and cites no authority at all**, so the same
  inference cannot be drawn about it — the two cases look alike and only one is evidenced. The
  distinction is kept deliberately rather than collapsed into a tidier story.
* **One trailer, three mutually exclusive rules, all live**: the kernel requires it *without* the
  model, Nerves requires it *with* the model, [GTK](projects/gtk.md) forbids it. MacPorts' PR body
  calls the trailer *"what appears to be the emerging de facto standard"* — **the corpus is now
  direct evidence that no such standard exists**, which is the most useful thing this bundle has said
  about attribution.
* **A MacPorts reviewer reached the kernel's conclusion independently**, without knowing the kernel
  had reached it: the trailer *"looks a bit hacked together, eg. mentioning Claude twice, and I don't
  see what the format of `MODEL_VERSION` is supposed to be"*. That is a precise reading of the retired
  example `Claude:claude-3-opus`, where agent and model name one vendor — **some evidence the format
  was the problem, not its documentation.**
* **Two positions appear that no adopted policy here holds.** Move disclosure from the commit trailer
  to the PR review checklist — which is GTK's arrangement, arrived at separately. And drop disclosure
  as uninformative: *"we can mostly just assume that everything is AI assisted. The important part …
  is that a human is responsible."*
* **Nerves draws the sharpest line on communication in the bundle**: *"Using AI to translate or
  tighten your own writing is fine. Using it to write in your place is not."* Several projects
  restrict AI in communication; none splits *assist* from *substitute* this cleanly, and the split is
  what answers the non-native-speaker objection.
* **Nerves is the only record here governing agent-instruction files** — *"Don't add AI tool
  configuration such as `AGENTS.md` or `CLAUDE.md` without asking first"* — and the only one asking a
  contributor to *"Comment on an open issue before pointing a coding agent at it"*, which prevents
  duplicated agent effort rather than reviewing it after the fact.
* **Review bandwidth is now the most common stated motive in this bundle**, ahead of licensing,
  copyright and output quality: GNOME, the Linux wireless maintainer, the kernel's
  `generated-content.rst`, Nerves (*"Friction is kind of the point"*) and now MacPorts (*"creating
  work for human beings"*) — **five independent projects.**
* **A source that cannot be fetched is labelled as such.** The Nerves rationale comes from an emailed
  newsletter with no per-issue public archive; every claim about what the policy *says* is taken from
  the public `CONTRIBUTING.md`, and the record states the limitation in place.
* **The project's own announcement overstates its rollout, checkably.** It says a copy sits *"in every
  official nerves repo"*; three of four sampled carry it and `nerves_system_br` has no `CONTRIBUTING.md`
  at all.
* **MacPorts is recorded as a proposal, not a rule**, with a warning that nothing in it is in force —
  the treatment [Rust](projects/rust.md)'s draft gets. Its `stale_after` is three months because an
  open PR's state is the thing most likely to change.


* **Second GNOME sweep: the policy count nearly doubled, and the first sweep's blind spot was the
  filename.** `README` and `HACKING` were read across all 321 modules — 342 such files — after the
  record itself flagged them as unsurveyed. **Seventeen modules now state an AI policy: nine in
  `CONTRIBUTING`, eight in `README`/`HACKING`, and the two sets do not overlap at all.**
* **Not one module puts the policy in both places.** Reading only `CONTRIBUTING` — the file a
  contributor is told to read — misses almost half. *Where a federation keeps its rules is not
  standardised, so a single-filename survey systematically under-reports*, which is a caution about
  method rather than about GNOME.
* **The boilerplate's origin is documented and dated.** Written for **Loupe** and announced on GNOME
  Discourse **2025-02-26** by `sophieherold`: *"I just merged an addition to Loupe's contribution
  guidelines that bans the use of AI generated content … I'm in favor of adopting a similar policy for
  all official GNOME software."* `console`, `dia` and `gitg` carry *"Adopted from Loupe"* in place,
  and `gitg` links back to that thread.
* **This is policy diffusion across a federation, observable, dated — and it bypassed the centre.**
  One maintainer wrote a text, proposed it fleet-wide on a forum, and a dozen modules copied it. The
  handbook was never amended and still says nothing. **The mechanism that spread the rule was social,
  not institutional.**
* **The drift is now explained rather than merely observed.** The original Loupe text does not name
  Ollama; `libadwaita` added it 2025-07-11 and five later copies carry it. The copies diverge on
  exactly the detail a contributor needs — whether their tool is named.
* **Two modules reject the boilerplate's own carve-out, on the axis this bundle treats as the most
  consequential.** The shared text exempts *"purely translating texts for issues and comments to
  English"*. `libxml2` refuses it — *"No LLMs for comments on the bug tracker, **including
  translation**"* — and substitutes a human accommodation: *"You are welcome to post in your native
  language and rely on others."* **The accessibility carve-out GCC treats as the clause most worth
  copying is being decided both ways inside one federation.**
* **`vte` frames the ban as licensing rather than quality**, and broader than the boilerplate: *"You
  may not contribute any code that was written, whether wholly or partly, by using AI in any form."*
  The boilerplate bans generated contributions; this bans AI's involvement in authorship at all.
* **The shortest policy in the bundle is here** — `showtime`, entire: *"We do not accept AI-generated
  contributions."* And `dia` cross-references from `HACKING.md` under *"So-called 'AI'"*: *"All
  hallucinations in Dia are purely organic in origin."*
* **Detection was two-part and proved on three fixtures first.** An AI term alone is worthless in a
  README, so a hit required an AI term **and** policy language within three lines. Proved to fire on a
  real ban, and to stay silent both on an innocent *"targets AI workloads"* README and on policy
  language with no AI in it. **All nine candidates turned out to be genuine** — no false positives to
  discard, which the CONTRIBUTING sweep's looser filter could not have promised.


* **Creation: [GTK](projects/gtk.md), and [GNOME](projects/gnome.md) rewritten around a survey of all
  321 modules in the group.** 45 carry a `CONTRIBUTING`; **nine state an AI policy**, in three
  incompatible positions. The survey was run because the previous version of the GNOME record had
  called per-module files unsurveyed.
* **GTK forbids the trailer the Linux kernel requires, and both argue it the same way.** GTK: *"Do
  not include trailers like "Co-authored-by:" or "Assisted-by:" in commit messages, since they serve
  as free advertising for AI companies."* The kernel narrowed the same trailer to the bare literal
  `LLM` because naming models *"provides free advertising to proprietary software companies"*.
  **Identical premise, opposite instrument** — one deleted the vendor from the tag, the other deleted
  the tag. GTK's wording landed 2026-04-03, the kernel's 2026-08-03; the dates are recorded because
  they are checkable and **no influence is claimed in either direction**.
* **The practical consequence outranks the curiosity: the trailer is not portable.** A contributor
  who learned `Assisted-by:` in the kernel breaks GTK's policy by applying it. Tooling that emits
  these tags must key on the destination project.
* **GTK also binds maintainers**, which almost nothing else here does — *"Review LLM/GenAI-assisted
  contributions more strictly"*, *"Reject comments and feedback that appear to be LLM/GenAI output"*.
  The kernel **enumerates** maintainer discretion; GTK **instructs**. Under one wording a strict
  maintainer is exercising a choice; under the other a lenient one is departing from policy.
* **Two GTK rules have no counterpart in the bundle.** It caps the *shape* of a change rather than its
  volume — no *"broad rewrites, large refactorings, or style changes"* — which targets the failure the
  wireless maintainer named as sprinkling checks across the code. And it bans **fabricated evidence**:
  *"Do NOT fabricate benchmarks, bug reports, test results, code samples, or reproducers"* — the
  artifacts a reviewer uses to check the code, rather than the code.
* **It closes the review loop from the contributor's side**: *"Do NOT feed the review feedback to an
  LLM/GenAI tool."* That is the counterpart to the wireless maintainer's refusal to argue with one —
  the same failure seen from opposite chairs, and GTK is the only policy here that closes it by rule.
* **The seven-module ban is the first named-vendor prohibition here** — ChatGPT, Claude, Copilot,
  DeepSeek, Devin AI — covering *"code, documentation, issues, and artworks"*, with a translation
  exception and a support-refusal clause: *"we cannot supply support on anything referencing AI
  output."*
* **The shared text has already drifted.** `libadwaita` added Ollama on 2025-07-11 and `libmanette`
  carries it; the other five copies do not. **A policy propagated by copy-paste diverges on exactly
  the detail a contributor needs** — whether their tool is named — and nothing reconciles the copies.
* **`gnome-commander` supplies a ground no other record states: deskilling.** *"people never improving
  their coding skills because they rely on LLMs instead is going to make the situation much worse"* —
  and it rejects the assist-only compromise on evidence rather than principle.
* **The generalisable finding: for a federated project, the umbrella's documentation may not be where
  the rule lives, and sibling modules may contradict each other.** GNOME's handbook is silent on AI
  while its modules ban it, permit it conditionally, or say nothing. **Checking the organisation is
  not checking the repository you are sending to.**


* **Correction to [GNOME](projects/gnome.md), hours after it shipped: the handbook is not
  client-side and the absence is now verified.** The record said GNOME's rules for its own modules
  *"were not established"* because the handbook *"renders client-side, so it resists the retrieval
  method used here"*. **That was false.** `handbook.gnome.org` is a Sphinx site serving static HTML,
  and every page reads with a plain fetch.
* **An untested assumption about a source's retrievability became a reason not to look** — which is
  the same failure as trusting a status code, one step earlier and worse, because it produced a
  recorded non-claim rather than a wrong claim. The check that settled it was 76 ordinary HTTP
  requests.
* **The absence is now recorded properly: no AI policy anywhere in the GNOME Project Handbook**,
  across all 76 pages, reading each page's article body rather than its navigation. It holds on
  exactly the pages where such a rule would sit — `development/change-submission`,
  `development/commit-messages` and `development/legal` — and across the six `maintainers/` and seven
  `issues/` pages.
* **The absence is bounded and says so.** Individual GNOME modules keep their own `CONTRIBUTING`
  files and those were not surveyed, so the defensible claim is *no project-level policy in the
  handbook*, not *no policy anywhere in GNOME*.
* **The corrected fact is more interesting than the one it replaces.** GNOME polices a submission
  channel it curates — third-party extensions — while its own contributor documentation says nothing
  about AI at all. **A project can gate the channel long before it says anything about its own
  codebase**, and reading only the extension rule would suggest the opposite.


* **Creation: [GNOME](projects/gnome.md)** — the AI rule in the Shell extension review guidelines,
  added **2025-11-30**. Read from the Markdown source in `World/javascript/gjs-guide`, with the commit
  history for the date and the rationale.
* **It is the only detection rule here that names the artifacts it looks for**, and that is what makes
  it better than the one it resembles. Git tests **prose** — *"overly formal or bloated"*, *"AI
  slop"* — and inherits the false positive against careful non-native speakers. GNOME tests **code**:
  *"large amounts of unnecessary code, inconsistent code style, imaginary API usage, comments serving
  as LLM prompts"*. **The last two cannot be produced by a competent human writing carefully** — a
  hallucinated API call either resolves against the platform or it does not, and prompt text left in a
  comment is not a stylistic tell. Same mechanism as Git's rule with the false-positive surface
  removed.
* **The same rule states its scope three times at three strengths**, and the operative one is the
  mildest: the heading says *"Extensions must not be AI-generated"*, the body permits AI as *"a
  learning aid or a development tool"* and rejects on *"indications"*, and the commit message scopes
  it to extensions that are *"predominately AI-generated"*. Recorded rather than smoothed, because a
  submitter reads the heading and a reviewer applies the body. **Same shape as NetworkManager**, whose
  commit describes a prohibition its text writes as an instruction — in both, the stricter statement
  is the one that is not operative.
* **The ground is reviewer strain, for the third time today**: *"to reduce the strain on volunteer
  reviewers."* Not licensing, not copyright, not quality in the abstract. GNOME, the Linux wireless
  maintainer and the kernel's `generated-content.rst` all open on the same motive — **maintainer
  attention is the scarce resource and generation is cheap on the other side.**
* *"Within reason"* qualifies the explainability fallback, and nothing else here has that qualifier.
  It concedes a reviewer cannot demand unbounded justification, which is what makes the test usable by
  volunteers.
* **The scope is narrower than the organisation name suggests, and the record says so.** This governs
  `extensions.gnome.org`, a third-party submission channel — closer to an app-store review policy than
  to a contribution policy. **GNOME's rules for its own modules were not established**, and the record
  declines to claim they are absent: the handbook renders client-side and resists this retrieval
  method, and *"no policy was found"* is not *"there is no policy"*.
* **The news lead was nine months out of date on the fact.** It ran 2026-08-03 about GNOME
  establishing an RFC process, with AI-generated extensions as context; the guideline itself landed
  2025-11-30. **A report about a project is not evidence about when its rule changed** — checking the
  commit history moved the date by three quarters of a year, and the lead would have dated the record
  wrong.


* **`projects/linux-kernel.md` gains the wireless subsystem exchange of 2026-08-06** — the enumerated
  maintainer discretion recorded earlier the same day, exercised in public three days before the
  bug-finding procedure was merged. Read from the `linux-wireless` thread, not from the reporting.
* **The patches complied with the kernel's policy, and that is the finding.** syzbot's AI-generated
  fixes carried a human's `From:` and `Signed-off-by:`, pre-reviewed and approved by a named engineer
  — precisely what `coding-assistants.rst` requires. The maintainer refused them anyway: *"the
  experience still seems to be one of me effectively consuming pure LLM output, just via an
  intermediary"*, and *"clearly nobody actually even bothers to look at the semantics of the code
  before or during the patching."* **Formal compliance with an AI policy does not deliver what the
  policy exists for**, and no other record here shows that gap directly.
* **The objection is about where the cost falls, not about provenance.** An LLM asked for a targeted
  fix produces one; the human in the loop *"should actually take a step back … and ask what the
  semantics of the code should be"*. Otherwise the judgement lands on the maintainer, who cannot
  supply it per-issue: *"if I could … I could be doing all of this myself. Need the contributors to do
  that."*
* **It resolved in under three hours and amended nothing.** syzkaller: *"We'll stop sending AI-assisted
  patches to the wireless subsystem."* No rule was broken and no policy changed — a subsystem is
  simply closed to a class of contribution the project permits, which is what enumerated discretion
  means in practice.
* **The strongest argument for disclosure in this bundle now comes from someone refusing the
  contributions**, and it is recorded in `overview.md` as well. Losing the labelled channel does not
  stop the patches: *"I'll just see the patches pasted into an email manually instead, and I've lost
  the signal that I could use to just ignore them entirely."* Everywhere else disclosure is an
  obligation on the contributor; **from the receiving end it is a filter**, which answers the standard
  objection that a disclosure rule is unenforceable — its value is the label honest submitters attach,
  not the liars it catches.
* **`lore.kernel.org` is Anubis-protected**, answering HTTP 200 with *"Making sure you're not a bot!"*
  to `curl` on both the message and `/raw` paths. The message-id was correct throughout and only
  retrieval was blocked; a browser clears the challenge. Recorded in the record's re-verification
  notes, with the working method: **take the URL from the lore search results, which do answer, rather
  than assembling a message-id by hand.**


* **Creation: [NetworkManager](projects/networkmanager.md)** — a policy added 2026-08-07 that is nine
  sentences long, **requires no disclosure of any kind**, and is still among the more demanding here.
  Read from `CONTRIBUTING.md` in the repository; found via a news sweep, recorded from the primary.
* **It answers the detection-versus-declaration problem with a third thing: demonstration.**
  *"Respond to review comments yourself. If you cannot discuss your own patch with a reviewer, it will
  not be merged."* The reviewer never has to decide how the patch was produced, only whether the
  person sending it can defend it — **which is the question detection and declaration are both
  proxies for.** It has the enforcement property Rust's draft says it cannot get, without asking
  anyone to self-report, and it cannot produce Git's false positive against a careful non-native
  speaker. Its cost is that it fires only at review time, which is why the same policy closes large
  unreviewed machine-generated merge requests before review begins.
* **The prose restriction is argued rather than asserted**, which is what makes it worth copying:
  *"Write your own commit messages and Merge Request descriptions. Those explain why you are making
  the change, which is the part a tool cannot know."* Debian's Proposals C and G, TeX Live and Zig all
  restrict communication; none of them says why in one line.
* **The commit message is stronger than the adopted text, and both are recorded.** The commit says the
  policy states *"AI assistance is prohibited in communication"*; `CONTRIBUTING.md` is written as an
  instruction rather than a prohibition. The file is what binds a contributor, so the file is quoted —
  but the gap between intent and text is the kind of thing that decides a borderline review.
* **A fourth DCO destination: abolish the instrument.** *"Do not use "Signed-off-by:" lines in commits
  for NetworkManager. It has no meaning."* Certification attaches to a **licensing commitment**
  instead — every contribution must be releasable under LGPL-2.1-or-later, and *"A tool cannot certify
  that for you."* The bundle now has bar-the-agent (kernel), unsatisfiable (QEMU), not-invoked (Linux
  Foundation) and abolished (here) — **the instrument varies and the placement of responsibility does
  not**, which is the finding.
* `overview.md` updated in three places: the shapes table, the detection/declaration section, and the
  DCO list.
* **Two retrieval traps hit in one record, both worth carrying.** GitLab renders file content
  client-side, so the `/-/blob/` URL returns HTTP 200 with the file text **absent** from the body; and
  the `/-/raw/` path once returned a GitLab *"404: Page not found"* body under HTTP 200, transiently,
  before serving correctly. Recording it as *"located, retrieval blocked"* on that first response
  would have been wrong. **Check for the text you came for, never for the status code** — the rule
  this bundle already states for Anubis hosts, now with a second, unrelated instance.


* **`projects/linux-kernel.md` rewritten: the kernel's attribution tag stopped naming the model, and
  the record had missed half the policy.** Found by chasing a news lead to the source tree; nothing
  from the lead is recorded, and every claim below comes from `git.kernel.org` or a commit diff.
* **The tag changed on 2026-08-03** — commit `816d9992`, *"coding-assistants: simplify attribution"*.
  `Assisted-by: AGENT_NAME:MODEL_VERSION` became the bare literal `Assisted-by: LLM`. The
  **requirement did not go away**; the model identification did, which is a narrower change than the
  reporting around it suggested.
* **The ground is an axis nothing else in this bundle argues from.** Identifying the model *"provides
  free advertising to proprietary software companies while adding little or no useful information"*.
  Every other policy decides *whether* to disclose; the kernel has now decided **how precisely**, and
  resolved it against specificity on anti-marketing grounds rather than privacy or practicality.
* **A second policy document was never cited, and that was a miss rather than drift.**
  `generated-content.rst` has been in tree since **2026-01-20** — seven months before this record was
  written — and linked from the AI document since 2026-07-22. It is **tool-generic**, triggering on
  content *"not written by a person in the Signed-off-by chain"* whether a chatbot, Coccinelle or
  `checkpatch.pl --fix` produced it. Reading the AI-specific file and stopping produced a record that
  was accurate about half a policy.
* **Two findings come only from that document.** It asks contributors to **disclose the prompts**,
  not merely the fact of tool use — nothing else here does. And it **enumerates maintainer
  discretion**, explicitly permitting *"Reject it outright"* and review *"at a lower priority than
  human-generated content"*, which means a subsystem stricter than the kernel is exercising a granted
  power rather than contradicting policy.
* **A mandatory nine-step procedure for AI bug-hunting** was added 2026-08-04 (`3d7c44f7`), including
  that the assistant *"must never send anything itself"* — the kernel's counterpart to GCC's rule
  that an LLM may not commit.
* **The rendered documentation site is the stale source, and it was this record's `resource:`.**
  `docs.kernel.org` builds a released kernel — 7.2.0 at this check — and still served the superseded
  format and example after mainline dropped both. It is demoted to a citation for the lag itself;
  `git.kernel.org` is now the primary, with the GitHub mirror verified byte-identical to it today.
  **A quotation taken from a rendered docs site can be stale while looking perfectly sourced.**
* **The previous version predicted this failure and could not act on it.** Its closing note said to
  *"Watch specifically for the tag format changing"* — which had already happened the day before that
  sentence was written. A correct prediction is worth nothing without a cadence short enough to catch
  it, so `stale_after` drops from six months to **three**: three substantive commits landed in this
  policy during August alone.
* **One upstream change falsified the same claim in three places.** The old tag format had been
  copied into comparison tables in `overview.md`, `foundations/apache-software-foundation.md` and
  `projects/ansible.md`. All three are corrected. **A fact restated across records has as many places
  to rot as it has copies** — the cross-reference was fixed, but no `verified:` entry was added to
  those three, because their own primaries were not re-read today.
* The Ansible comparison got sharper rather than merely corrected: the two projects share the field
  name and now encode **opposite intentions** with it — Ansible asks which tool, the kernel has
  decided it does not want to know.


* **Debian decided, and `distributions/debian.md` is rewritten around the result.** The General
  Resolution closed 2026-08-28 23:59:59 UTC and **Option 5, "Responsible Use of Generative AI"**
  (Proposal **E**) won outright — sole member of the Schwartz set, beating *None of the above*
  281–126. Debian now **permits** generative AI under the standards that already applied.
* **The record's own derived claim was confirmed by the tally.** On 2026-08-05 this record read the
  Constitution and concluded that Proposal A, amending the Social Contract, needed a **3:1**
  majority its rivals did not — at a time when the vote page stated no requirement at all. The tally
  dropped Option 1 at **0.560 (144/257) < 3**. A derived claim later matching the primary is the
  strongest evidence a record can give that its reasoning was sound, and it is why the derivation was
  written down instead of being left as background.
* **Recorded from the automated tally, and labelled as such.** The result was published by
  `devotee@vote.debian.org`, which states of itself that it is *"an automated, unofficial publication
  of vote results"* and that official results follow from the Secretary. `stale_after` is **two
  weeks**, not the bundle's six months, and the next read is triggered by the Secretary's
  declaration rather than by the date.
* **The adopted text was read in full, not summarised from the press.** Its operative move is that it
  **adds no new rule**: same standards regardless of tools, responsibility undiminished, review before
  submission, and a closing affirmation that AI is *"neither exempt from nor subject to special rules
  beyond the standards already expected"*. Disclosure is **encouraged and explicitly not required** —
  the opposite of the kernel's required trailer. Two firmer obligations sit underneath: no non-public
  project material to third-party AI services, and no automated action at scale without prior
  consensus and an accountable human.
* **Both misspellings in the disclosure sentence are reproduced verbatim** — *"enourage"*,
  *"assitance"* — because that is the operative wording of the adopted position.
* **Where this record said to look was wrong, and is corrected.** It said the vote page *"carries the
  result once the ballot closes"*. Hours after closing the page had no outcome section, no tally sheet
  and no quorum log, while the result was already on the `debian-vote` list. **The list publishes
  first.** The preferential-outcome caution also lapsed: the Schwartz set resolved to one option, so
  there is no ranked result to interpret.
* **`overview.md` corrected, and a taxonomy claim withdrawn before it shipped.** The first draft filed
  Debian as an *eighth shape*, "the deliberate non-rule". Checked against the shapes table, that is
  wrong: same standards, undiminished responsibility and review-before-submission is a
  **responsibility rule**, the shape Python, curl and the kernel already hold. Debian joins that row.
  What is genuinely new is **how it was reached** — every other responsibility rule here was written
  by maintainers, Debian's was selected by project-wide preferential ballot over eight alternatives.
* **The category index had drifted three ways, and nothing was watching it.** Running `okf index`
  showed Debian's row still describing *"six competing proposals in discussion"* — never regenerated
  after the v0.6.0 re-verification — and CTAN and TeX Live sitting in a **bullet list** rather than
  the table, with CTAN's pre-correction description still in place. Regeneration is not wired into
  any gate, so an index can contradict the records it indexes and every check stays green.
* **Found via Phoronix, resolved against the primary.** A news feed carried the result first; nothing
  from it is recorded here. The tally and the adopted text were read from `debian-vote` and the vote
  page.
* **Recorded the 2025 AI General Resolution that Debian withdrew, as an excluded neighbour rather
  than as a record.** `vote_002` of 2025, *"Interpretation of DFSG on Artificial Intelligence (AI)
  Models"*, asked whether a model released under a DFSG-compatible licence but **without its training
  data or program** may ship in `main`. That is model licensing, not contribution policy, so it earns
  no record here — but a reader who finds it and no mention of it cannot tell an excluded subject
  from a missed one. **A scope boundary is only legible if the near misses are named.**
* **It was withdrawn on 2025-05-08 by its own proposer, on readiness rather than merits** — *"we as
  a community is underprepared to vote on this"* — and conditionally, expecting cancellation unless
  a rival proposal found sponsors at the last minute.
* **The transferable finding is about process.** One stated reason for withdrawing was that the
  ballot had only one option: *"The lack of other options can make the result less convincing."*
  Fifteen months later the LLM ballot carried **eight**. The defect named in 2025 is exactly what
  the 2026 ballot does not have, so its eight-way split reads as a repaired condition rather than
  as disarray — a caution against reading a crowded ballot as a project failing to agree.
* **No `verified:` entry was added and `stale_after` was not moved** *(superseded hours later, same
  day, by the result entry above)*. When this was written the tally did not exist; two sources had
  been read and the record's claims about the 2026 ballot had not been re-checked, so stamping it
  verified would have asserted a pass that did not happen. Left standing rather than rewritten,
  because the sequence is the point: the record was correctly held expired right up to the moment
  the primary appeared.

## 2026-08-14

* **`distributions/debian.md` re-verified, and four claims had gone stale in nine days.** The
  General Resolution moved from *In Discussion* to *Voting*; the discussion period was **extended to
  2026-08-13**, a week past the date this record carried; the ballot is open **2026-08-15 to
  2026-08-28**; and **two further proposals were added, G and H — eight, not six.**
* **A caveat could be dropped rather than corrected.** The record derived Proposal A's 3:1
  requirement from the Constitution and said explicitly that the vote page stated no requirement.
  The page now states it in as many words. The derivation was right and is now sourced, which is the
  good outcome of writing down *where* a claim came from.
* **The shape of the disagreement changed, not just its size.** G puts human communication in scope
  alongside C, so that is now the position of two independent proposals rather than one. H argues
  from **environmental cost** — a ground no other option in this ballot, and no other organisation in
  this bundle, reasons from. A seventh axis was added to the list a policy must decide.
* **A count was replaced with a shape.** The disclosure argument had rested on "five of six ballot
  options"; it now describes which options ask for disclosure and why the two prohibitions make it
  moot, so the reasoning survives the ballot growing again.
* **All eight quotations were re-confirmed**, not only the three added. Five had been carried
  forward from the 2026-08-05 check — sourced-looking claims resting on an earlier session.
* `stale_after` moved **2026-09-15 → 2026-08-29**, the day after the ballot closes, so the record
  demands a re-read when the result exists rather than two weeks later.

## 2026-08-10

* **Added `distributions/tex-live` and `distributions/ctan`** — the TeX ecosystem, prompted by a
  concrete need: `mmd2tex` is an AI-assisted package heading for a CTAN upload, and its release
  runbook gates that step on knowing the position.

* **TeX Live has a well-formed policy**; it separates legal exposure from disclosure etiquette,
  names its exemptions (autocompletion, spelling, grammar), and uniquely covers *communication* —
  no AI-generated mailing-list or maintainer email unless clearly delimited.

* **CTAN publishes none**, verified across the upload instructions, the 26,125-character upload
  addendum, the full help index and four candidate URLs. Recorded as a verified absence rather
  than left unwritten.

* **The two records were left in tension, and the tension resolved the same day.** TeX Live's scope
  clause asserts CTAN "ha[s] their own policies"; no such policy was discoverable, so the CTAN
  record listed three readings that fit the evidence and picked none — absence of a page is evidence
  about publication, not about the existence of a position.

  **The CTAN team answered on the record.** Manfred Lotz, writing "from the CTAN team" on the
  tex-live list on 2026-05-21: *"For CTAN, also no official policy is in place. We are in discussion
  here."* That selects reading (1) — the scope clause disclaims scope rather than describing a
  policy that exists — and converts an unsourced absence into a **sourced** one, which is a
  different kind of claim: a mailing-list answer from the team is positive evidence, where four
  fruitless URL checks were only evidence about publication.

  *"We are in discussion here"* also dates the record. A formal policy may appear, which is why the
  concept says so rather than presenting the absence as settled.

  **This entry was itself corrected on 2026-08-13**, while cutting v0.4.0. The concept was rewritten
  when the answer arrived and the log was not, so this file went on saying the question was open for
  three days after it closed. Nothing could have caught it: `okf validate`, `okf lint`, `okf-gate`
  and the audience and type gates were all clean throughout, because every one of them checks
  structure and none of them reads for sense. `CLAUDE.md` says exactly that — *"the gates verify
  structure, not sense"* — and this is what it looks like in practice.

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

* **Initialization**: Created the bundle per `supplychain-workspace` ADR-0011 <!-- audience-ok: dated historical entry; rewriting it to conceal the charter would falsify the record --> — structure,
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
