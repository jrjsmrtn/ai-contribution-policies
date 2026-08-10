---
type: Organization
title: CTAN
description: No formal AI-contribution policy, confirmed on the record by a CTAN team member — but an operating practice exists, in which authors disclose AI involvement and packages where AI produced poor work are rejected on review.
resource: https://tug.org/pipermail/tex-live/2026-May/052424.html
tags:
  - ai-contribution
  - policy
  - archive
  - no-policy
  - informal-practice
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-10T20:05:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-10T20:40:00Z'
stale_after: 2026-11-10
sources:
  - id: lotz-ctan
    title: Manfred Lotz (CTAN team) on the tex-live list, 2026-05-21
    resource: https://tug.org/pipermail/tex-live/2026-May/052424.html
  - id: berry-separate
    title: Karl Berry — TeX Live and CTAN are separate; write ctan@ctan.org, 2026-05-20
    resource: https://tug.org/pipermail/tex-live/2026-May/052423.html
  - id: ctan-upload-pkg
    title: CTAN — How can I upload a package?
    resource: https://ctan.org/help/upload-pkg
  - id: ctan-addendum
    title: Additional Information for CTAN Uploaders (upload addendum)
    resource: https://ctan.org/file/help/ctan/CTAN-upload-addendum
  - id: clawxiv
    title: clawxiv — the package cited as disclosing AI involvement well
    resource: https://www.ctan.org/pkg/clawxiv
---

**Stance: no formal policy, stated as such by the CTAN team — with an informal practice that is
already being applied to submissions.**

# On the record, from CTAN

Asked directly on the `tex-live` list whether CTAN had a policy on AI-generated packages, Manfred
Lotz replied **"from the CTAN team"** on 2026-05-21:[^lotz-ctan]

> For CTAN, also no official policy is in place. We are in discussion here.

He then gave a personal view carrying three operative points:[^lotz-ctan]

1. Agreement with TeX Live's position that a human takes full technical and legal responsibility.
2. **"A package author should mention if a package was created in collaboration with an AI"**,
   citing [`clawxiv`](https://www.ctan.org/pkg/clawxiv) as an example done well.[^clawxiv]
3. **"Currently, we reject a new package if the author of a new package used AI and created stupid
   stuff. Fortunately, in most cases this can relatively easy be recognized."**

His recommendation to the asker: "go ahead and mention openly that AI was involved."

Point 3 is the substantive finding. There is no written rule, but there **is** an enforced quality
bar applied at review time, and AI-assisted submissions are already being judged against it. The
absence of a policy does not mean the absence of a practice.

# CTAN and TeX Live are separate, and CTAN has no public discussion list

Karl Berry, answering the same question the day before: "TeX Live and CTAN are two different things,
with different people involved. For an answer about CTAN, you should write
ctan at ctan.org."[^berry-separate]

That routing matters, because **CTAN has no public mailing list**. Of the 63 public lists on
`lists.tug.org`, none is `ctan` or `ctan-ann`; `ctan.org/ctan-ann` is a web announcement feed, not a
discussion forum. So there is no CTAN archive to search — questions of this kind surface on
`tex-live`, as this one did, or go privately to `ctan@ctan.org`.

# The published documents remain silent

Checked 2026-08-10: the upload instructions,[^ctan-upload-pkg] the upload
addendum[^ctan-addendum] (26,125 characters of plain text; **zero** matches for AI, artificial
intelligence, LLM, generative, machine-generated or ChatGPT), the full help index, and the candidate
URLs `/aipolicy`, `/help/ai`, `/ai-policy`, `/help/aipolicy` (all HTTP 404). CTAN's published
conditions are licence-based: state the licence, be entitled to upload.

# What a submitter should do

Disclose AI involvement in the package documentation, and expect the work to be reviewed on merit.
That satisfies the practice Lotz describes without waiting for a document that does not yet exist.
"We are in discussion here" also dates this record: a formal policy may appear, which is why it
carries a three-month expiry rather than the usual six.

Compare [TeX Live](tex-live.md), which reached a written policy from the same conversation — the
question in this thread is what prompted it.

[^lotz-ctan]: Manfred Lotz (CTAN team), tex-live list, 2026-05-21 — https://tug.org/pipermail/tex-live/2026-May/052424.html
[^berry-separate]: Karl Berry, tex-live list, 2026-05-20 — https://tug.org/pipermail/tex-live/2026-May/052423.html
[^ctan-upload-pkg]: CTAN — How can I upload a package? — https://ctan.org/help/upload-pkg
[^ctan-addendum]: Additional Information for CTAN Uploaders — https://ctan.org/file/help/ctan/CTAN-upload-addendum
[^clawxiv]: clawxiv on CTAN — https://www.ctan.org/pkg/clawxiv
