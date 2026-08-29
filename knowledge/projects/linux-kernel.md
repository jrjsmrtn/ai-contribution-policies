---
type: Organization
title: Linux Kernel
description: Permits AI-assisted contributions under two merged in-tree documents — a tool-generic one covering anything not written by a person in the Signed-off-by chain, and an AI-specific one that bars agents from signing off and requires an Assisted-by tag. The tag no longer names the model, because identifying it was judged free advertising for proprietary vendors.
resource: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/process/coding-assistants.rst
tags:
  - ai-contribution
  - policy
  - project
  - permitted
  - dco
  - attribution
  - disclosure
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-04T23:10:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-04T23:10:00Z'
  - by: claude/opus-5
    at: '2026-08-29T03:15:00Z'
stale_after: 2026-11-29
sources:
  - id: kernel-coding-assistants-src
    title: Documentation/process/coding-assistants.rst (torvalds/linux, mainline)
    resource: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/process/coding-assistants.rst
  - id: kernel-generated-content
    title: Documentation/process/generated-content.rst (torvalds/linux, mainline)
    resource: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/process/generated-content.rst
  - id: kernel-submitting-patches
    title: Documentation/process/submitting-patches.rst (torvalds/linux, mainline)
    resource: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/process/submitting-patches.rst
  - id: kernel-commit-simplify-attribution
    title: 'commit 816d9992 — coding-assistants: simplify attribution'
    resource: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id=816d9992d9ed434ec52cfbd63080d518e535a41b
  - id: kernel-commit-bug-procedure
    title: 'commit 3d7c44f7 — docs: coding-assistant: explain important steps when looking for bugs'
    resource: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id=3d7c44f73765d98665fb97a4fb89c002c88ba1b9
  - id: kernel-docs-rendered
    title: AI Coding Assistants — The Linux Kernel documentation (rendered, lags the tree)
    resource: https://docs.kernel.org/process/coding-assistants.html
  - id: kernel-wireless-syzbot
    title: 'sysbot AI patches and wireless — linux-wireless thread, 2026-08-06'
    resource: https://lore.kernel.org/linux-wireless/3b6c46b6d79f3a0e0ded2967db3cfd469314b05c.camel@sipsolutions.net/T/
---

**Stance: permitted, with mandatory disclosure and a human on the hook.** The kernel governs this in
**two merged in-tree documents**, and reading only the AI-specific one gets the rule wrong:

| Document | Scope | In tree since |
|---|---|---|
| `generated-content.rst` | **any tool**, AI or not — Coccinelle, `checkpatch.pl --fix`, chatbots, translation | 2026-01-20 |
| `coding-assistants.rst` | AI coding assistants specifically | 2026-01-06 |

The broader document is the one most policies elsewhere have no equivalent of. Its trigger is not
*"was AI involved?"* but whether *"a meaningful amount of content in a kernel contribution was not
written by a person in the Signed-off-by chain, but was instead created by a
tool."*[^kernel-generated-content] **That framing makes the AI question a special case of an older
one**, which is why the kernel could absorb generative AI without inventing a separate regime.

## The rule that has teeth

> AI agents MUST NOT add Signed-off-by tags. Only humans can legally certify the Developer
> Certificate of Origin (DCO).[^kernel-coding-assistants-src]

The human submitter is responsible for *"Reviewing all AI-generated code"*, *"Ensuring compliance
with licensing requirements"*, *"Adding their own Signed-off-by tag to certify the DCO"*, and
*"Taking full responsibility for the contribution."*[^kernel-coding-assistants-src]

Note what this does to the DCO argument. [QEMU](qemu.md) reads the same certificate and concludes
that AI-generated content cannot satisfy it. The kernel reaches the opposite conclusion from the
same premise by **relocating the certification** — the human certifies, having reviewed, and the
tool is credited without signing. Two projects, one instrument, opposite outcomes: the DCO does not
by itself determine a policy.

## The attribution tag, and why it stopped naming the model

    Assisted-by: LLM [TOOL1] [TOOL2]

The bracketed items *"are optional specialized analysis tools used (e.g., coccinelle, sparse,
smatch, clang-tidy)"*, and *"Basic development tools (git, gcc, make, editors) should not be
listed."* The example given is:[^kernel-coding-assistants-src]

    Assisted-by: LLM coccinelle sparse

**Until 2026-08-03 the tag named the agent and the model** — `Assisted-by: AGENT_NAME:MODEL_VERSION`,
with `Assisted-by: Claude:claude-3-opus coccinelle sparse` as the example. Commit `816d9992`,
*"coding-assistants: simplify attribution"*, replaced both with the bare literal `LLM`. The stated
ground is one no other organisation in this bundle reasons from:

> The requirement to identify specific models used in the Assisted-by tag **provides free
> advertising to proprietary software companies** while adding little or no useful information.
> Change the requirement to simply: `Assisted-by: LLM` to capture the fact that an LLM was used
> without tracking which one.[^kernel-commit-simplify-attribution]

**This is an axis, not a detail: attribution *granularity*.** Every other policy here decides
*whether* to disclose; the kernel has now decided *how precisely*, and resolved it against
specificity on anti-vendor-marketing grounds rather than privacy or practicality. A project copying
the tag should copy the reasoning or reject it deliberately — the two formats collect different
data, and the kernel gave up the model-level dataset on purpose.

**Disclosure is required, and that is stated in the main submission document** rather than only in
the AI-specific one. `submitting-patches.rst` carries a *"Using Assisted-by:"* section: *"If you
used any sort of advanced coding tool in the creation of your patch, you need to acknowledge that
use by adding an Assisted-by tag. Failure to do so may impede the acceptance of your
work."*[^kernel-submitting-patches] A contributor following the ordinary process meets the
requirement without ever opening the AI policy.

**Why a new token rather than `Co-developed-by:`.** The kernel's existing vocabulary makes the
obvious choice incoherent: `Co-developed-by:` denotes authorship, and every one *"must be
immediately followed by a Signed-off-by: of the associated co-author"*[^kernel-submitting-patches]
— a sign-off this policy forbids an agent from adding. `Assisted-by:` is the only shape consistent
with both rules. Guidance recommending `Co-developed-by:` for AI attribution, which circulated
widely before this policy landed, asks for a structurally invalid trailer block.

## Disclose the prompts, not just the fact

`generated-content.rst` asks for more than a trailer. Contributors *"should be transparent about the
origin of content in cover letters and changelogs"*, and the suggested detail
includes:[^kernel-generated-content]

> If code was largely generated from a single or short set of prompts, include those prompts. For
> longer sessions, include a summary of the prompts and the nature of resulting
> assistance.[^kernel-generated-content]

**No other record in this bundle asks for the prompts.** It also asks which tools were used, which
portions they affected, and how the result was tested — and for Coccinelle specifically, *"The input
to the tools you used, like the Coccinelle source script."*

**There is an explicit triviality carve-out**, and it is drawn by effect rather than by technology:
spelling and grammar fixes, *"Typing aids like identifier completion"*, *"Purely mechanical
transformations like variable renaming"* and reformatting are all out of scope — though *"you should
still always consider if it would help reviewing your contribution if the reviewer knows about the
tool that you used."*[^kernel-generated-content] Compare [GCC](gcc.md), which draws its line at
**legal significance** instead; both exempt the trivial, on different tests.

## Maintainer discretion is enumerated, not assumed

The document does not promise uniform treatment. *"As with all contributions, individual maintainers
have discretion to choose how they handle the contribution"*, and it lists what they may do —
including *"Reject it outright"*, review *"at a lower priority than human-generated content"*, ask
the contributor *"to elaborate on how the tool or model was trained"*, and *"Suggest a better prompt
instead of suggesting specific code changes."*[^kernel-generated-content]

Two consequences a contributor should read plainly. *"If tools permit you to generate a contribution
automatically, expect additional scrutiny in proportion to how much of it was generated."* And the
sanction: *"maintainers are entitled to reject your series without detailed review"* if you cannot
defend what you submitted.[^kernel-generated-content]

**This is why a subsystem may look stricter than the kernel.** A maintainer refusing AI-generated
patches outright is exercising a discretion the policy grants, not contradicting it — so *"the Linux
kernel permits this"* is true at project level and may be false for the tree you are actually
sending to.

## The discretion exercised: wireless, 2026-08-06

Three days before those steps were merged, the wireless maintainer used the discretion above in
public, and the exchange is the most useful thing in this record for anyone drafting a
policy.[^kernel-wireless-syzbot]

**syzbot had begun sending AI-generated fixes.** Johannes Berg's reply:

> I'm going to state, for the record, that I'm going to make judicious use of ability to ignore
> patches, and apply it to pretty much all syzbot-AI-generated patches unless a 3-second review says
> "obviously right".
>
> In particular, I will absolutely *not* "comment on the patches as usual" and argue with an LLM that
> can bullshit out code faster than another computer can even deliver it to me by
> email.[^kernel-wireless-syzbot]

**The patches were fully compliant with the policy above, and that is the point.** syzkaller's
Aleksandr Nogikh replied within the hour: *"Every AI-generated patch sent by syzbot has been
pre-reviewed and approved by a human engineer. The person who approved the patch is listed in the
From: and Signed-off-by: fields"*, and no LLM handles the follow-ups — *"so you have not been
interacting with an LLM."*[^kernel-wireless-syzbot] A human signed off, having reviewed, which is
exactly what `coding-assistants.rst` requires.

**Berg's objection is that compliance did not deliver what the rule exists for:**

> the experience still seems to be one of me effectively consuming pure LLM output, just via an
> intermediary.[^kernel-wireless-syzbot]

> This is why I'm refusing these patches, because clearly nobody actually even bothers to look at the
> semantics of the code before or during the patching.[^kernel-wireless-syzbot]

His complaint is not about provenance but about **what the intermediary failed to do**: an LLM asked
for a targeted fix produces a targeted fix, and *"the human in the loop should actually take a step
back from that and ask what the semantics of the code should be"*. The cost falls in the wrong place
— *"I really cannot make that judgement call myself for every single issue like that, if I could …
I could be doing all of this myself. Need the contributors to do that."* And it does not scale *"both
in terms of long-term maintenance (sprinkling checks all over the code disregarding the architecture)
and also in terms of review bandwidth"*.[^kernel-wireless-syzbot]

**syzkaller stopped, within three hours**: *"We'll stop sending AI-assisted patches to the wireless
subsystem."*[^kernel-wireless-syzbot] No policy was amended and no rule was broken. This is the
enumerated discretion working exactly as `generated-content.rst` describes it, which is why a
subsystem can be closed to a class of contribution the project as a whole permits.

**The finding worth carrying, though, is about disclosure — argued from the receiving end.** Berg
notes that refusing the labelled channel does not stop the patches arriving:

> now that I say this (and you disabled it) I guess I'll just see the patches pasted into an email
> manually instead, and I've lost the signal that I could use to just ignore them
> entirely.[^kernel-wireless-syzbot]

Everywhere else in this bundle disclosure is argued as an obligation on the contributor, for honesty
or for legal hygiene. Here it is **a filter the maintainer wants to keep**: a declared AI channel is
more useful to the person receiving it than an undeclared one, and the cost of driving it underground
falls on review. That is the strongest practical argument for a disclosure requirement recorded here,
and it comes from someone refusing the contributions.

He also names the human cost plainly, to the two contributors caught in it: *"I'm sorry you're
effectively the two first victims of this new process."*[^kernel-wireless-syzbot]

## A mandatory procedure for AI bug-hunting

Added 2026-08-04 by commit `3d7c44f7`, prompted by report quality: *"the quality of reports
(especially when they're believed to be security relevant) is still lacking a
lot."*[^kernel-commit-bug-procedure] When an AI assistant is used to find and fix bugs it **MUST**
follow nine steps, of which the load-bearing ones are:[^kernel-coding-assistants-src]

- Read the whole process documentation first — *"Do not rely on isolated parts found by keyword
  search."*
- Attempt a reproducer for any non-trivial bug; *"Stop here if it finally looks wrong."*
- Write the fix — *"This part is not optional"* — then build and verify it, dropping fixes that do
  not work.
- Add `Assisted-by:`, and **no** `Signed-off-by:`.
- State what could not be done: *"maintainers currently waste too much time analyzing unverified
  reports and untested fixes."*
- Classify against `threat-model.rst` and leave the result for human review — **the assistant
  *"must never send anything itself"*.**

That last rule is the kernel's counterpart to GCC's *"An LLM may not commit code to the project
repository"*: both constrain what an **agent with access** may do, as distinct from what generated
text must look like.

## What a contributor must do

Review what the tool produced, well enough to defend it — *"If you are unable to do so, then do not
submit the resulting changes."*[^kernel-generated-content] Add your own `Signed-off-by`. Add
`Assisted-by: LLM` in the current format, **not** the older `AGENT_NAME:MODEL_VERSION` shape. Say in
the changelog what the tool did and, where the code came from prompts, what they were. Never let an
agent add a `Signed-off-by`, and never let one send mail. Then check the subsystem: the maintainer
you are sending to may have set a higher bar, and is entitled to.

## Re-verification notes

**Checked 2026-08-29 against the source tree.** Four claims in the previous version were wrong by
then, all from changes landing within a day either side of the 2026-08-04 first read: the tag
format, the worked example, the file length (59 → 96 lines), and the absence of any mention of
`generated-content.rst`.

**The last of those was a miss, not drift.** `generated-content.rst` had been in tree since
2026-01-20 — seven months before this record was written — and linked from `coding-assistants.rst`
since 2026-07-22. Reading the AI-specific document and stopping there produced a record that was
accurate about half a policy.

**The previous version predicted its own failure and could not act on it.** Its closing note said to
*"Watch specifically for the tag format changing: the `AGENT_NAME:MODEL_VERSION` shape is unusual"* —
which is exactly what happened, on 2026-08-03, the day before that sentence was written. A correct
prediction is worth nothing without a re-read cadence short enough to catch it, which is why
`stale_after` is now **three months rather than six**: three substantive commits landed in this
policy during August alone.

**Source the tree, not the rendered docs.** `docs.kernel.org/process/coding-assistants.html` renders
a released kernel — **7.2.0** as of this check — and still showed the superseded
`AGENT_NAME:MODEL_VERSION` format and the `Claude:claude-3-opus` example after mainline had dropped
both.[^kernel-docs-rendered] It was this record's `resource:` and is now demoted to a citation for
the lag itself. `git.kernel.org` is authoritative; `raw.githubusercontent.com/torvalds/linux/master`
was verified byte-identical to it on 2026-08-29 and is an acceptable mirror. **A quotation taken
from the rendered site can be stale while looking perfectly sourced.**

**The lag has already propagated.** [MacPorts](macports.md) opened a pull request on 2026-08-04 —
one day after the format changed — proposing the `Assisted-by:` trailer *"in the format recommended
by the Linux kernel developers"*, citing
`docs.kernel.org/process/coding-assistants.html#attribution` and reproducing the **retired**
`AGENT_NAME:MODEL_VERSION` form. As of 2026-08-29 that PR is open and nobody in its thread has
noticed. **A stale rendered page is not merely a re-verification trap for this bundle; it is
exporting a superseded rule to other projects.**

**`lore.kernel.org` sits behind an Anubis proof-of-work challenge**, answering HTTP 200 with
*"Making sure you're not a bot!"* to `curl` on both the message and `/raw` paths. The message-id was
correct throughout; only the retrieval was blocked, and a real browser clears it. Confirm the URL
from the lore *search* results, which do answer, rather than assembling a message-id by hand.

The audit trail is `git log --follow Documentation/process/coding-assistants.rst` and the same for
`generated-content.rst`. Watch for the two documents diverging: the tool-generic one sets the
threshold and the AI-specific one sets the tag, so a change to either moves the rule.

[^kernel-coding-assistants-src]: [Documentation/process/coding-assistants.rst (torvalds/linux, mainline)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/process/coding-assistants.rst)
[^kernel-generated-content]: [Documentation/process/generated-content.rst (torvalds/linux, mainline)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/process/generated-content.rst)
[^kernel-submitting-patches]: [Documentation/process/submitting-patches.rst (torvalds/linux, mainline)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/Documentation/process/submitting-patches.rst)
[^kernel-commit-simplify-attribution]: [commit 816d9992 — coding-assistants: simplify attribution](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id=816d9992d9ed434ec52cfbd63080d518e535a41b)
[^kernel-commit-bug-procedure]: [commit 3d7c44f7 — docs: coding-assistant: explain important steps when looking for bugs](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/patch/?id=3d7c44f73765d98665fb97a4fb89c002c88ba1b9)
[^kernel-docs-rendered]: [AI Coding Assistants — The Linux Kernel documentation (rendered, lags the tree)](https://docs.kernel.org/process/coding-assistants.html)
[^kernel-wireless-syzbot]: [sysbot AI patches and wireless — linux-wireless thread, 2026-08-06](https://lore.kernel.org/linux-wireless/3b6c46b6d79f3a0e0ded2967db3cfd469314b05c.camel@sipsolutions.net/T/)
