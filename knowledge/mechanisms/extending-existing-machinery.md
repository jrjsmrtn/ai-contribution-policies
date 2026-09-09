---
type: Practice
title: Extending existing machinery
description: The cheapest route to an AI policy is to point a rule the project already ran at the new question — a copyright threshold, a ban on leaked material, a tracker label, a tooling norm. Seven records here take it, one has the machinery and has not used it, and one concluded its existing bar already sufficed. It works because it inherits an answer to "who decides", and it fails where nothing suitable exists.
resource: https://gcc.gnu.org/ai-policy.html
tags:
  - ai-contribution
  - mechanism
  - policy-design
status: stable
generated:
  by: claude/opus-5
  at: '2026-09-09T10:54:00Z'
verified:
  - by: claude/opus-5
    at: '2026-09-09T10:54:00Z'
stale_after: 2027-03-09
sources:
  - id: ext-gcc
    title: 'GCC AI policy'
    resource: https://gcc.gnu.org/ai-policy.html
  - id: ext-asahi
    title: 'Generative AI Policy — Asahi Linux'
    resource: https://asahilinux.org/slop/
  - id: ext-llvm
    title: 'LLVM AI Tool Use Policy (llvm/docs/AIToolPolicy.md, main)'
    resource: https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/docs/AIToolPolicy.md
  - id: ext-systemd
    title: 'docs/CONTRIBUTING.md — Policy on the use of LLMs and AI tooling (systemd/systemd, main)'
    resource: https://raw.githubusercontent.com/systemd/systemd/main/docs/CONTRIBUTING.md
  - id: ext-owasp
    title: 'Project Policy — OWASP Foundation (operational/projects.md, www-policy)'
    resource: https://raw.githubusercontent.com/OWASP/www-policy/master/operational/projects.md
---

**Writing an AI policy from scratch means answering "who decides?" from scratch.** Extending a rule
the project already ran does not — the thresholds, the escalation path and the people with standing
to apply them come with it. Seven records here take that route, and what they extend is remarkably
varied.

## What each one pointed at the new question

| Project | Existing machinery | How it was extended |
|---|---|---|
| [GCC](../projects/gcc.md) | the **copyright threshold** deciding whether a patch needs an assignment | *"legally significant"* LLM contributions are declined; below the line nothing changes[^ext-gcc] |
| [Asahi Linux](../projects/asahi-linux.md) | an existing ban on **illegally acquired or leaked** vendor documentation | *"This also applies to regurgitated slop."*[^ext-asahi] |
| [LLVM](../projects/llvm.md) | its **copyright policy** | *"Our policy on AI tools is similar to our copyright policy"* — regenerating copyrighted material does not remove the copyright[^ext-llvm] |
| [systemd](../projects/systemd.md) | the norms already governing **`sed`, `awk`, `coccinelle`** | *"AI tools are treated the same as traditional tooling"*[^ext-systemd] |
| [Elixir](../projects/elixir.md) | **issue labels** in the tracker | no coding agents on existing issues unless marked *Contributions Welcome* |
| [Debian](../distributions/debian.md) | the **standards already expected of contributors** | generative AI is *"neither exempt from nor subject to special rules beyond"* them |
| [OWASP](../foundations/owasp.md) | a mandated **DCO** requiring *"original work"* and covering *"the risks of plagiarized code"* | **not extended** — see below[^ext-owasp] |

**GCC's is the clearest instance and the most reusable.** Its line is a test the project already
applied to every contribution, so *"is this AI-generated?"* becomes subordinate to *"is this legally
significant?"* — and a contributor who already knows the assignment rules already knows which of
their patches are in scope. Nothing had to be taught.

## Why it works

**It inherits an answer to the hardest question.** Every AI policy eventually meets *who judges, and
on what evidence*. A new regime has to invent that; an extension already has it, along with a body
that has used it before and contributors who recognise it.

**It narrows what has to be detected.** GCC does not need to determine how a patch was produced, only
whether it crosses a threshold it was already measuring. Asahi does not need to identify model
output, only material it was already refusing. **Detection was the enforcement problem across this
bundle, and extending sidesteps rather than solves it.**

**And it is cheap to state.** Asahi's extension is one sentence. systemd's is one clause. Neither
required a new document, a new field, or a new sanction.

## Where it does not reach

**Debian is the limit case: it extended nothing, deliberately.** Having put eight options to a
project-wide vote, it adopted the one creating no new obligation. That is the same instinct carried to
its conclusion — if the existing bar suffices, the extension is the empty one — and it is only
available to a project confident its bar already holds.

**OWASP is the counter-example, and the sharpest evidence that the move is a choice.** Its projects
policy mandates the DCO, requires contributions be a contributor's *"original work"*, and requires any
substitute agreement to cover *"the risks of plagiarized code"*.[^ext-owasp] Original work and
plagiarism risk are precisely the concepts every extension above is built from. **The machinery is
present, mandatory, and has not been pointed anywhere** — the clause dates to 2021 and predates the
question. Whether that is restraint or inattention is not stated anywhere and is not inferred here.

**It requires something suitable to exist.** A young project with no copyright assignment process, no
prior ban, and no tracker conventions has nothing to extend, which is part of why the newer records
in this bundle build new regimes instead. The route is cheapest for projects that are already old.

## What it does not solve

**An extension inherits the gaps of what it extends.** GCC's threshold says nothing about
contributions below it, which is most of them. Asahi's ban addresses provenance and not correctness.
systemd's framing settles authorship and leaves review cost untouched — which is why systemd needed a
separate sanction and a canary on top.

**And it can mislead by familiarity.** A contributor who knows the old rule may assume they know the
new one. Debian's outcome is the case to hold onto: **a project that argued the question to a
project-wide vote and concluded its existing standards sufficed is not in the same position as one
that never asked**, even though the visible result — no AI-specific rule — is identical.

## What to watch

Whether OWASP ever extends the clause it already has, which would convert guidance into obligation
across every project it covers at once. Whether any project extends something other than a legal or
tooling norm — Elixir's use of tracker labels is the only non-legal instance here, and the most
easily copied. And whether the newer, younger projects that built new regimes later fold them back
into existing machinery as they acquire some.

[^ext-gcc]: [GCC AI policy](https://gcc.gnu.org/ai-policy.html)
[^ext-asahi]: [Generative AI Policy — Asahi Linux](https://asahilinux.org/slop/)
[^ext-llvm]: [LLVM AI Tool Use Policy (llvm/docs/AIToolPolicy.md, main)](https://raw.githubusercontent.com/llvm/llvm-project/main/llvm/docs/AIToolPolicy.md)
[^ext-systemd]: [docs/CONTRIBUTING.md — Policy on the use of LLMs and AI tooling (systemd/systemd, main)](https://raw.githubusercontent.com/systemd/systemd/main/docs/CONTRIBUTING.md)
[^ext-owasp]: [Project Policy — OWASP Foundation (operational/projects.md, www-policy)](https://raw.githubusercontent.com/OWASP/www-policy/master/operational/projects.md)
