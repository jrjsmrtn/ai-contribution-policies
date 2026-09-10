---
type: Practice
title: Certifying origin
description: Eleven records reach a position on AI by reasoning about a certification instrument, and one unchanged 2004 text — the Developer Certificate of Origin — is read as unsatisfiable, satisfiable only by a human, satisfiable below a volume threshold, irrelevant, and worth abolishing. The disagreement is not about AI but about what clause (b) and (c) always meant. Whatever the instrument, every destination puts the legal risk on the contributor.
resource: https://developercertificate.org/
tags:
  - ai-contribution
  - mechanism
  - policy-design
  - dco
  - licensing
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-10T15:10:00Z'
verified:
  - by: claude/opus-5
    at: '2026-09-10T15:10:00Z'
stale_after: 2027-03-10
sources:
  - id: co-dco
    title: 'Developer Certificate of Origin, Version 1.1'
    resource: https://developercertificate.org/
  - id: co-qemu
    title: 'Code provenance — QEMU developer documentation (master)'
    resource: https://www.qemu.org/docs/master/devel/code-provenance.html
  - id: co-kernel
    title: 'Documentation/process/coding-assistants.rst (torvalds/linux, mainline)'
    resource: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/process/coding-assistants.rst
  - id: co-git
    title: 'Documentation/SubmittingPatches — Use of Artificial Intelligence (git/git, master)'
    resource: https://raw.githubusercontent.com/git/git/master/Documentation/SubmittingPatches
  - id: co-lf
    title: 'Generative AI policy — The Linux Foundation'
    resource: https://www.linuxfoundation.org/legal/generative-ai
  - id: co-nm
    title: 'CONTRIBUTING.md (NetworkManager, main)'
    resource: https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/CONTRIBUTING.md
  - id: co-nerves
    title: 'CONTRIBUTING.md (nerves-project/nerves, main)'
    resource: https://raw.githubusercontent.com/nerves-project/nerves/main/CONTRIBUTING.md
  - id: co-k8s
    title: 'Open source maintainership in the age of AI (kubernetes.dev, 2026-06-26)'
    resource: https://www.kubernetes.dev/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/
  - id: co-owasp
    title: 'Project Policy — OWASP Foundation (operational/projects.md, www-policy)'
    resource: https://raw.githubusercontent.com/OWASP/www-policy/master/operational/projects.md
---

**One text, six destinations.** The Developer Certificate of Origin is Version 1.1 and has not
changed; eleven records here reach a position on AI by reasoning about it or about a substitute, and
they do not agree on what it requires, whether it can be met, or whether it is worth keeping.

**Any summary that explains a stance by *"they require a DCO"* is explaining nothing.**

## Where the instrument leads

| Record | Instrument | Reading | Destination |
|---|---|---|---|
| [QEMU](../projects/qemu.md) | DCO | compliance with terms **(b) or (c)** *"is unclear"*[^co-qemu] | **prohibition** |
| [Linux kernel](../projects/linux-kernel.md) | DCO | satisfiable, **but only by a human**[^co-kernel] | agents may not sign; the submitter does |
| [Elixir](../projects/elixir.md) | DCO | the kernel's sentence, adopted | the same |
| [Git](../projects/git.md) | DCO | unclear for a *"significant amount of"* generated content[^co-git] | **volume-scoped** caution |
| [Linux Foundation](../foundations/linux-foundation.md) | — | the DCO is **never mentioned**[^co-lf] | permission, from licence compatibility |
| [NetworkManager](../projects/networkmanager.md) | none | *"Signed-off-by … has no meaning"*[^co-nm] | certification moved to a **relicensing commitment** |
| [Nerves](../projects/nerves.md) | none | *"Do not add Signed-off-by tags"*[^co-nerves] | an `Assisted-by` trailer instead |
| [Kubernetes](../projects/kubernetes.md) | CLA | an AI **cannot** sign one[^co-k8s] | the inability becomes the **enforcement gate** |
| [OWASP](../foundations/owasp.md) | DCO, mandated | *"original work"*, *"risks of plagiarized code"*[^co-owasp] | **never extended** to AI |
| [FreeBSD](../distributions/freebsd.md) | none | the same licence-provenance argument | reached **without** a DCO |
| [GCC](../projects/gcc.md) | copyright assignment | a **threshold**, not a certification | *"legally significant"* output declined |

## The disagreement is about clause (b), not about AI

The DCO's three substantive clauses each assume a chain of human hands:[^co-dco]

- **(a)** *"created in whole or in part by me and I have the right to submit it"*
- **(b)** *"based upon previous work that, to the best of my knowledge, is covered under an
  appropriate open source license"*
- **(c)** *"provided directly to me by some other person who certified (a), (b) or (c)"*

**QEMU reasons from (b) and (c) and concludes they cannot be met**, because for generative tools
*"the copyright and license status of the output is ill-defined with no generally accepted, settled
legal foundation"*, and the project *"is not willing or able to accept the legal risks of
non-compliance."*[^co-qemu]

**The kernel reaches the opposite conclusion from the same document and names no clause at all.** It
states only that *"Only humans can legally certify the Developer Certificate of Origin"*[^co-kernel]
and requires the submitter to add their own sign-off — which works if the contribution is *"created
in whole or in part by me"* under (a), with the model as an instrument. **Neither project argues
against the other, because neither addresses the clause the other is reading.**

That is the whole disagreement. **It is not a question about AI; it is a question about what (b)
meant for any input of uncertain provenance**, which no project had to answer while every input
arrived from a person. Generative tools did not create the ambiguity, they made it unavoidable.

Git occupies the middle by scoping rather than deciding: the DCO *"requires contributors to certify
that they know the origin of their contributions … It's not yet clear that this can be legally
satisfied when submitting **significant amount of** content that has been generated by AI
tools."*[^co-git] **The qualifier is doing the work** — assistance does not trigger the concern,
volume does.

## Two projects removed the instrument

**NetworkManager abolished it.** *"Do not use 'Signed-off-by:' lines in commits for NetworkManager. It
has no meaning."*[^co-nm] Certification attaches instead to a licensing commitment — all new
contributions *"MUST be made under terms of LGPL-2.1-or-later"* — and the AI clause hooks directly to
that: *"You are the one certifying that the contribution can be released under LGPL-2.1-or-later. A
tool cannot certify that for you."*[^co-nm]

**Nerves dropped the sign-off and kept a trailer.** *"Do not add `Signed-off-by` tags. Nerves does not
use them"*[^co-nerves] — while requiring an `Assisted-by` trailer naming the model. Attribution
without certification, which is the inverse of what the kernel does with the same two tags; see
[the Assisted-by trailer](assisted-by-trailer.md).

## Kubernetes inverted QEMU's premise

QEMU's argument is that an AI cannot satisfy the certification, and it concludes with a ban.
**Kubernetes starts from the identical fact and builds a gate.** *"AI agents are not able to solve
these contributor license agreements so one enforcement the project made is to **enable the CLA check
for co-authors**."*[^co-k8s]

Listing an AI as co-author now fails an automated check. Nothing has to be detected and no maintainer
has to adjudicate — and it is the only enforcement in this bundle that runs before a human looks. The
same premise, one project's reason to refuse and another's mechanism to catch.

## The instrument is not load-bearing

**Every destination in the table above places the legal risk on the contributor**, whatever
instrument it uses or discards. FreeBSD reaches the licence-provenance conclusion with no DCO at all;
NetworkManager reaches it through relicensing; the Linux Foundation reaches permission through
licence compatibility while hosting projects that reason from the DCO to prohibition.

**Which means the certification instrument predicts nothing about the stance.** Two projects requiring
the same DCO land on prohibition and permission; two projects with no DCO land on the same
responsibility rule as one that has it. What varies is the argument; what does not vary is who
carries the risk.

OWASP is the case that makes this visible from the other side: it **mandates** the DCO, requires
contributions be a contributor's *"original work"*, requires any substitute agreement to cover *"the
risks of plagiarized code"*[^co-owasp] — and has never pointed any of it at AI. **Having the
instrument is not having a position**; see [extending existing machinery](extending-existing-machinery.md).

## An AI now checks the certificate

[Valkey](../projects/valkey.md) has no AI policy at all and briefs a review bot to *"Flag missing
`Signed-off-by`"* in every commit. **Nothing is inconsistent** — confirming a line is present is not
certifying anything — but it is the first instance here of AI touching the DCO, and it arrives from
the one direction none of the arguments above anticipated: not whether a machine may certify, but a
machine checking that a human did.

## What to watch

Whether any project cites a **clause number**. QEMU is the only one that does, and the argument
cannot be joined until a second project says which clause it is reading. Whether the CLA co-author
check spreads, since it is the only mechanical enforcement here. Whether the DCO itself is ever
revised — it is at Version 1.1 and every position above is an interpretation of text written before
the question existed. And whether a project that abolished the sign-off ever explains what it lost,
since NetworkManager and Nerves both dropped it without argument.

[^co-dco]: [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/)
[^co-qemu]: [Code provenance — QEMU developer documentation (master)](https://www.qemu.org/docs/master/devel/code-provenance.html)
[^co-kernel]: [Documentation/process/coding-assistants.rst (torvalds/linux, mainline)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/process/coding-assistants.rst)
[^co-git]: [Documentation/SubmittingPatches — Use of Artificial Intelligence (git/git, master)](https://raw.githubusercontent.com/git/git/master/Documentation/SubmittingPatches)
[^co-lf]: [Generative AI policy — The Linux Foundation](https://www.linuxfoundation.org/legal/generative-ai)
[^co-nm]: [CONTRIBUTING.md (NetworkManager, main)](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/main/CONTRIBUTING.md)
[^co-nerves]: [CONTRIBUTING.md (nerves-project/nerves, main)](https://raw.githubusercontent.com/nerves-project/nerves/main/CONTRIBUTING.md)
[^co-k8s]: [Open source maintainership in the age of AI (kubernetes.dev, 2026-06-26)](https://www.kubernetes.dev/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/)
[^co-owasp]: [Project Policy — OWASP Foundation (operational/projects.md, www-policy)](https://raw.githubusercontent.com/OWASP/www-policy/master/operational/projects.md)
