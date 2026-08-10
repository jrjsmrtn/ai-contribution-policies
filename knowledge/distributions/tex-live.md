---
type: Organization
title: TeX Live
description: Accepts AI-assisted contributions on a responsibility-first framing — a knowledgeable human must review every line — with disclosure required when AI copied third-party material and expected for substantial use.
resource: https://tug.org/texlive/aipolicy.html
tags:
  - ai-contribution
  - policy
  - distribution
  - disclosure
  - has-policy
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-10T20:00:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-10T20:00:00Z'
stale_after: 2027-02-10
sources:
  - id: tl-aipolicy
    title: Policy on AI-assisted contributions for TeX Live
    resource: https://tug.org/texlive/aipolicy.html
  - id: tl-agents
    title: AGENTS.md — TeX Live source tree
    resource: https://github.com/TeX-Live/texlive-source/blob/master/AGENTS.md
  - id: tl-pkgcontrib
    title: TeX Live package contributions
    resource: https://tug.org/texlive/pkgcontrib.html
---

**Stance: permitted, with human responsibility as the organising principle rather than a ban or a
disclosure ritual.**

TeX Live "accepts AI-assisted contributions, but human contributors remain fully responsible, both
technically and legally, for the changes they submit, whether AI-assisted or not."[^tl-aipolicy] The
operative consequence is a review obligation, not a labelling one: "a knowledgable human must review
every line of code/documentation and test the package's basic functionality before uploading or
reporting."[^tl-aipolicy]

# Three separable obligations

**Legal.** Free-software policies "apply equally to all contributions, regardless of whether they
were human-written or AI-written". If the AI "copied a nontrivial amount of content that is owned by
third parties", the contributor must ensure that content is available under a compatible free
software licence *and* attribute it to the original authors in the public
documentation.[^tl-aipolicy]

**Transparency.** Disclosure is mandatory in that copying case — "it is imperative to disclose the
use of AI, in the public documentation". Beyond it, disclosure of "the extent of any substantial use
of AI" is *good practice* rather than required, and routine autocompletion plus spelling, grammar
and similar linguistic corrections "need not be disclosed".[^tl-aipolicy]

**Communication.** A separate rule that most policies omit: do not use AI to generate message text
sent to the public mailing lists or privately to maintainers "unless the AI's responses are clearly
indicated and delimited from the rest of your email". Translation from a native language is
exempt.[^tl-aipolicy]

The technical elaboration lives in `AGENTS.md` at the root of the source tree, which repeats the
responsibility framing verbatim and adds "Use AI as a tool, not as an authority."[^tl-agents] The
policy is linked from the package-contribution page, so a package maintainer meets it on the normal
path.[^tl-pkgcontrib]

# The scope clause is the part worth quoting

"This policy is for TeX Live. Other parts of the TeX world, notably CTAN, as well as individual
package and program maintainers, have their own policies. Their policies must also be complied with;
TeX Live's policy does not override anyone else's."[^tl-aipolicy]

That sentence asserts CTAN has its own policy. No such policy is discoverable — see
[CTAN](ctan.md), where the absence is recorded with its search path. A contributor reading only this
page would reasonably conclude one exists and go looking for it.

# Why this one is unusually well-formed

Three properties are rare enough to name. It **separates legal exposure from disclosure etiquette**,
so the mandatory part is small and the advisory part is honest about being advisory. It **names its
exemptions** — autocompletion, spelling, grammar — rather than leaving contributors to guess whether
an editor suggestion counts. And it **covers communication as well as code**, which matters because
AI-written mailing-list traffic is a maintainer-time problem distinct from AI-written patches.

Its acknowledgements cite HarfBuzz, the Fedora AI-Assisted Contributions Policy and the Linux
Foundation Generative AI policy,[^tl-aipolicy] which makes it a downstream adopter rather than an
independent formulation.

[^tl-aipolicy]: Policy on AI-assisted contributions for TeX Live — https://tug.org/texlive/aipolicy.html
[^tl-agents]: AGENTS.md — TeX Live source tree — https://github.com/TeX-Live/texlive-source/blob/master/AGENTS.md
[^tl-pkgcontrib]: TeX Live package contributions — https://tug.org/texlive/pkgcontrib.html
