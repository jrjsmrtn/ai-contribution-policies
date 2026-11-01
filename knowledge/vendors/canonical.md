---
type: Organization
title: Canonical
description: Requires a Harmony-based CLA and has no AI-contribution policy. Its contributor documentation and CLA are silent, while its VP of Engineering has said Ubuntu will ship code co-authored by AI, and the repository behind the contributor documentation now carries instructions for coding agents and an LLM-assisted review tool.
resource: https://ubuntu.com/project/docs/contributors/
tags:
  - ai-contribution
  - policy
  - vendor
  - no-policy
  - cla
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-05T07:50:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-05T07:50:00Z'
  - by: claude/opus-5-5
    at: '2026-11-01T14:30:00Z'
stale_after: 2027-05-01
sources:
  - id: ubuntu-contributors
    title: Contributing to Ubuntu Development — contributor documentation
    resource: https://ubuntu.com/project/docs/contributors/
  - id: canonical-cla
    title: Contributor Licence Agreement — Ubuntu and Canonical Legal
    resource: https://canonical.com/legal/contributors
  - id: seager-ai-post
    title: The future of AI in Ubuntu — Jon Seager, Ubuntu Discourse, 2026-04-27
    resource: https://discourse.ubuntu.com/t/the-future-of-ai-in-ubuntu/81130
  - id: seager-clarification
    title: The future of AI in Ubuntu, reply 41 (raw) — Jon Seager, Ubuntu Discourse, 2026-04-28
    resource: https://discourse.ubuntu.com/raw/81130/41
  - id: upd-tools-instructions
    title: '.github/instructions/tools-development.instructions.md (ubuntu/ubuntu-project-docs, main)'
    resource: https://raw.githubusercontent.com/ubuntu/ubuntu-project-docs/main/.github/instructions/tools-development.instructions.md
  - id: upd-auto-mir
    title: 'tools/auto-mir/README.md (ubuntu/ubuntu-project-docs, main)'
    resource: https://raw.githubusercontent.com/ubuntu/ubuntu-project-docs/main/tools/auto-mir/README.md
---

**Stance: no AI-contribution policy, and a CLA that has nothing to say about AI either.**

## The absence is verified, and the search path is wide

Ubuntu's contributor documentation contains **no mention** of AI, LLMs, generative tooling or coding
assistants.[^ubuntu-contributors] Since this record was first written the page has become part of a
larger Ubuntu project documentation site, built from the `ubuntu/ubuntu-project-docs` repository.
Searched on 2026-11-01, that whole repository mentions AI only in the documentation of one tool,
Auto-MIR (below), and in a build dependency.

This is a stronger absence than a single-file check. The documentation covers the whole contribution
path, including the sponsorship queue and the Patch Pilots, where an AI-assistance rule would most
naturally sit, and says nothing.

## The CLA is the binding instrument, and it is silent

Canonical **requires a Contributor Licence Agreement**, based on the Harmony framework. It licenses
rather than assigns:

> you're giving us a licence, but you still own the copyright — so you retain the right to modify
> your code and use it in other projects.[^canonical-cla]

There is **no AI-related term in it**.[^canonical-cla] So a contributor to a Canonical project signs
an agreement about copyright and patents that is entirely silent on whether the work may be
AI-assisted — the [CLA](https://github.com/jrjsmrtn/software-supply-chain-landscape/blob/main/knowledge/provenance/cla.md)
instrument does not carry that question, and Canonical has not added it elsewhere.

Worth noting for anyone comparing: a **CLA is a heavier instrument than a DCO** and Canonical uses
one, so the barrier to contributing is already higher than at most projects here — and it still
does not answer the AI question.

## The tension worth recording

Jon Seager, Canonical's VP of Engineering, set out the company's plans for AI in Ubuntu on the Ubuntu
Discourse on 2026-04-27. On the kind of contribution this bundle tracks, he wrote: *"Many of you will
have read reports of "slop" pull requests and contributions that have been flung at open source
projects with little care, consideration or thought. This has never been an acceptable way to
contribute, and is absolutely not what is being encouraged at Canonical."*[^seager-ai-post]

A day later, replying in the same thread:

> Regarding whether or not we should ship code that was co-authored by an AI - in reality we will be
> doing this. Even foundational projects in the ecosystem like the Kernel itself now have policies
> around how to govern this, and will accept tasteful, correct contributions that have been authored
> with AI.[^seager-clarification]

Those are statements about **product strategy and internal practice**, not a contribution policy —
and this record does not treat them as one. But the gap is real: Canonical plans to *produce*
AI-assisted code while publishing nothing about *receiving* it. A contributor cannot infer from a
roadmap what will be accepted in a merge proposal. The kernel policy he points to has itself changed
since: see [the Linux kernel](../projects/linux-kernel.md).

## The documentation repository already has rules for agents

The repository behind the contributor documentation carries three path-scoped GitHub Copilot
instruction files, the first added on 2026-03-12. The one for tool code tells the agent: *"Sign-off is
not configured here: create every commit with `git commit --no-gpg-sign` (It will be reviewed and
signed by a human reviewer later)."*[^upd-tools-instructions] The signature here is a GPG commit
signature, not a DCO sign-off, and the rule is addressed to the agent, not to a contributor.

The same repository has shipped **Auto-MIR** since 2026-09-07, a tool that uses an LLM to draft Main
Inclusion Review reports and reviews. It keeps the decision with a person: *"Auto-MIR does not post to
Launchpad and does not make the final ACK or NACK decision. A reviewer must verify, edit, and complete
every generated draft."*[^upd-auto-mir] So Canonical publishes rules for an LLM helping its own
reviewers and for agents editing its documentation, and still none for a contributor using one.

## The vendor pattern, third variant

Three vendors, three shapes: [SUSE](suse.md) binds its **employees** by policy (in one of two
published versions), [Red Hat](red-hat.md) publishes a **disposition** and defers to each community,
and Canonical publishes **neither** — while operating the heaviest inbound instrument of the three.

The common thread is that a vendor's rules govern its own staff, not contributors. Where the vendor
also runs a community — Fedora for Red Hat, openSUSE for SUSE, Ubuntu for Canonical — **the
community's policy is the one that binds a contributor**, and it is a separate document with a
separate adoption process.

## What a contributor must do

Sign the CLA — that part is not optional and is worth checking against your employer before you
start, since a CLA can be a hard stop. On AI assistance, **nothing is published**, so disclose
voluntarily and ask in the sponsorship queue or on the relevant Ubuntu Matrix channel. An absent
policy is not permission, and Canonical's stated intent to ship AI-assisted code says nothing about
what it will accept from outside.

## Re-verification notes

Three places, all needed:

1. **`ubuntu.com/project/docs/contributors/`** — where a contribution rule would live. Note this URL
   is the redirect target; `documentation.ubuntu.com/project/contributors/` 301s to it.
2. **`ubuntu/ubuntu-project-docs`** — the repository that page is built from. Search the whole
   repository, not the page: a rule could land in any guide, and the agent instructions and Auto-MIR
   live here too.
3. **`canonical.com/legal/contributors`** — the CLA. An AI clause added *there* would bind every
   contributor at once and is the higher-leverage change to watch.

Also watch the Discourse thread: a plan to ship AI-co-authored code makes a rule for receiving it the
obvious next document.

A Canonical policy is more likely to appear as a CLA amendment than as a documentation section,
because the CLA is the instrument contributors actually sign.

[^ubuntu-contributors]: [Contributing to Ubuntu Development — contributor documentation](https://ubuntu.com/project/docs/contributors/)
[^canonical-cla]: [Contributor Licence Agreement — Ubuntu and Canonical Legal](https://canonical.com/legal/contributors)
[^seager-ai-post]: [The future of AI in Ubuntu — Jon Seager, Ubuntu Discourse, 2026-04-27](https://discourse.ubuntu.com/t/the-future-of-ai-in-ubuntu/81130)
[^seager-clarification]: [The future of AI in Ubuntu, reply 41 (raw) — Jon Seager, Ubuntu Discourse, 2026-04-28](https://discourse.ubuntu.com/raw/81130/41)
[^upd-tools-instructions]: [.github/instructions/tools-development.instructions.md (ubuntu/ubuntu-project-docs, main)](https://raw.githubusercontent.com/ubuntu/ubuntu-project-docs/main/.github/instructions/tools-development.instructions.md)
[^upd-auto-mir]: [tools/auto-mir/README.md (ubuntu/ubuntu-project-docs, main)](https://raw.githubusercontent.com/ubuntu/ubuntu-project-docs/main/tools/auto-mir/README.md)
