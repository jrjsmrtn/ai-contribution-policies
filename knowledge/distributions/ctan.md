---
type: Organization
title: CTAN
description: No discoverable AI-contribution policy, despite TeX Live's policy asserting that CTAN has one — the upload conditions are silent across every documented location.
resource: https://ctan.org/help/upload-pkg
tags:
  - ai-contribution
  - policy
  - archive
  - no-policy
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-10T20:05:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-10T20:05:00Z'
stale_after: 2026-11-10
sources:
  - id: ctan-upload-pkg
    title: CTAN — How can I upload a package?
    resource: https://ctan.org/help/upload-pkg
  - id: ctan-addendum
    title: Additional Information for CTAN Uploaders (upload addendum)
    resource: https://ctan.org/file/help/ctan/CTAN-upload-addendum
  - id: ctan-help
    title: CTAN help index
    resource: https://ctan.org/help
  - id: tl-aipolicy
    title: Policy on AI-assisted contributions for TeX Live — scope clause
    resource: https://tug.org/texlive/aipolicy.html
---

**Stance: none published, as of 2026-08-10 — and the absence is in tension with a claim made
elsewhere in the TeX world.**

# The absence is verified, and the search path is wide

Checked on 2026-08-10:

| Location | Result |
|---|---|
| Upload instructions[^ctan-upload-pkg] | no mention of AI, authorship attestation or originality |
| **Upload addendum**[^ctan-addendum] — the fullest conditions document, 26,125 characters of plain text | **zero** matches for AI, artificial intelligence, LLM, generative, machine-generated, ChatGPT |
| Help index[^ctan-help] — every help entry enumerated | no policy, guidelines or conduct entry on the subject |
| `/aipolicy`, `/help/ai`, `/ai-policy`, `/help/aipolicy` | all HTTP 404 |
| Upload form | no declaration or checkbox beyond licence and entitlement to upload |

The addendum is the document where such a condition would live: it carries the naming rules, the
licensing expectations and the "more aspects we ask you keep in mind when preparing your upload".
The one authorship-adjacent requirement anywhere is the README licence statement.[^ctan-upload-pkg]

# The tension worth recording

TeX Live's policy states that "Other parts of the TeX world, notably CTAN, as well as individual
package and program maintainers, have their own policies. Their policies must also be complied with;
TeX Live's policy does not override anyone else's."[^tl-aipolicy]

That asserts a CTAN policy exists. None is discoverable at any documented location. Three readings
fit the evidence and this record does not choose between them:

1. the sentence is aspirational or anticipatory, written to disclaim scope rather than to describe a
   published document;
2. a CTAN position exists but is unpublished — held by the team and applied case by case;
3. "policies" means CTAN's general conditions (licensing, entitlement to upload), which do apply to
   AI-assisted work without naming it.

**Resolving this needs a direct answer from the CTAN team**, not more searching. Absence of a page
is evidence about publication, not about the existence of a position.

# What applies in the meantime

CTAN's stated conditions are licence-based: an uploader must state the licence and must be entitled
to upload.[^ctan-upload-pkg] Those bind AI-assisted work exactly as they bind any other — an
AI-assisted package whose provenance is clean and whose licence is stated meets the published bar.
The unresolved part is whether CTAN wants **disclosure**, and in what form, for the catalogue.

Contrast [TeX Live](tex-live.md), which publishes a detailed policy and reaches the same practical
place by a different route: permitted, human responsible, disclose when third-party material was
copied.

[^ctan-upload-pkg]: CTAN — How can I upload a package? — https://ctan.org/help/upload-pkg
[^ctan-addendum]: Additional Information for CTAN Uploaders — https://ctan.org/file/help/ctan/CTAN-upload-addendum
[^ctan-help]: CTAN help index — https://ctan.org/help
[^tl-aipolicy]: Policy on AI-assisted contributions for TeX Live — https://tug.org/texlive/aipolicy.html
