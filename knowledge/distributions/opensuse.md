---
type: Organization
title: openSUSE
description: Has no adopted AI-contribution policy. Its board waited for SUSE's corporate policy, drafted guidelines modelled on Fedora's in 2025-11, minuted the need to vote on them, and lost momentum when the board changed; a community thread reopened the question in 2026-08 without a conclusion. The openSUSE Forums meanwhile enforce a published rule for posts, and the Open Build Service has its own.
resource: https://en.opensuse.org/Portal:AI
tags:
  - ai-contribution
  - policy
  - distribution
  - undecided
  - no-policy
  - disclosure
status: stable
generated:
  by: claude/opus-5-5
  at: '2026-11-01T18:00:00Z'
verified:
  - by: claude/opus-5-5
    at: '2026-11-01T18:00:00Z'
stale_after: 2027-02-01
sources:
  - id: os-portal-ai
    title: Portal:AI — openSUSE wiki (recreated 2026-08-11)
    resource: https://en.opensuse.org/Portal:AI
  - id: os-board-2025-10-27
    title: openSUSE Board meeting minutes, 2025-10-27 — openSUSE AI Code Assist Policy
    resource: https://en.opensuse.org/Archive:Board_meeting_2025-10-27
  - id: os-board-2025-11-24
    title: openSUSE Board meeting minutes, 2025-11-24 — AI guidelines
    resource: https://en.opensuse.org/Archive:Board_meeting_2025-11-24
  - id: os-board-2025-12-08
    title: openSUSE Board meeting minutes, 2025-12-08 — AI Policy
    resource: https://en.opensuse.org/Archive:Board_meeting_2025-12-08
  - id: os-board-2026-02-02
    title: openSUSE Board meeting minutes, 2026-02-02 — Proposed AI Policy
    resource: https://en.opensuse.org/Archive:Board_meeting_2026-02-02
  - id: os-board-2026-08-17
    title: openSUSE Board meeting minutes, 2026-08-17 — AI Policy
    resource: https://en.opensuse.org/Archive:Board_meeting_2026-08-17
  - id: os-draft-guidelines
    title: openSUSE Project Generative AI Guidance — draft for community discussion (etherpad, plain-text export)
    resource: https://etherpad.opensuse.org/p/paiguidelines/export/txt
  - id: os-ml-thread
    title: Discuss openSUSE AI Policy — project@lists.opensuse.org, 2026-08-11 to 2026-09-15
    resource: https://lists.opensuse.org/archives/list/project@lists.opensuse.org/thread/WDWQ3354UXTZPWQ7LFTBPERHKCNTF7KB/
  - id: os-forums-faq
    title: FAQ — AI-Generated Content (openSUSE Forums)
    resource: https://forums.opensuse.org/faq
---

**Stance: undecided at project level, with a draft that stalled — and a rule already enforced on the
forums.** The project's own AI portal says it plainly: *"The openSUSE project has not yet adopted a
final policy or guidelines on AI use."*[^os-portal-ai]

## The board waited, drafted, and did not vote

The board first held back so as not to contradict SUSE, the project's main sponsor. On 2025-10-27 it
recorded that *"To avoid conflicts we decided to wait on SUSE to publish its corporate policy. That
policy has now been updated."*, pointed at Fedora's newly approved policy, and minuted three draft
principles, among them *"You push it, you are responsible (not some tool, AI or
otherwise)."*[^os-board-2025-10-27] What SUSE's update says is covered in the [SUSE](../vendors/suse.md)
record.

The minutes then trace a draft that never reached a vote:

| Meeting | Minuted |
|---|---|
| 2025-11-24 | *"Had a look at Fedora's guidelines and feel these are aligned."* A draft is under review on an etherpad[^os-board-2025-11-24] |
| 2025-12-08 | *"Need to formalize document, vote, and post"*[^os-board-2025-12-08] |
| 2026-02-02 | *"Submit for Public RFC after next board meeting (2026-02-16)."*[^os-board-2026-02-02] |
| 2026-08-17 | *"Conversation still developing on Mailing List"*[^os-board-2026-08-17] |

The public discussion on the project list was started on 2026-08-11, not by the board but by a
contributor writing in a personal capacity, *"because nobody else has done it yet"*.[^os-ml-thread] In the same thread the author of the draft explained that it might have lost
momentum during the board's change of members and chair.[^os-ml-thread] The thread ran to
2026-09-15 and ended without a proposal or a vote; its participants range from a full ban on generated
code and prose to accepting AI as a tool under the contributor's responsibility.

## What the draft says

The draft is titled *"openSUSE Project Generative AI Guidance"* and marked *"Draft for community
discussion"*.[^os-draft-guidelines] It is an etherpad, editable by anyone with the link, so what
follows is what it said on 2026-11-01, not a text anyone has agreed to:

- **Scope is the whole project**, packaging to marketing, and *"Everyone, SUSE employees and other
  contributors, shall find an even playing field."*
- **Accountability**, as in Fedora's policy, plus a constraint Fedora does not have: contributors
  must *"only use tools that DO NOT place restrictions on how their output can be used"*.
- **Threshold disclosure**, as at Fedora: *"If a significant part of a contribution is produced by an
  AI tool without substantial modification, you must disclose that."* The suggested trailers name
  models.
- **A rule about where not to disclose**: public wiki pages and documentation should not name the
  tool, *"in order to avoid the perception that openSUSE is endorsing these offerings"*. GTK reaches
  the same worry from the other end and forbids the trailer altogether.
- **Limits on AI in review and governance**: it may not be *"the sole or final decision-maker"*, and
  may not be used for *"Decisions involving trust or human behavior"* or Code of Conduct compliance.
  Fedora's policy has a similar clause.[^os-draft-guidelines]

**It concedes a limit no other draft here states**: because openSUSE ships what upstreams produce,
*"any consumer of openSUSE project has to expect some parts of it being an output of an AI, even if
not explicitly tagged."*[^os-draft-guidelines] A distribution's disclosure rule can only cover its
own layer.

## Rules already in force below the project level

**The openSUSE Forums publish one.** *"Automated or unreviewed AI-generated replies are not
allowed."* A post with significant AI help must *"include the prompt and an annotation indicating
which engine you used (e.g., Assisted-by: [Engine Name])"*, and *"Staff may hide or remove undisclosed
or unvetted AI content."*[^os-forums-faq] Apart from the [Linux kernel](../projects/linux-kernel.md)'s cover-letter guidance, it is the only rule here that asks for the prompt.

**The [Open Build Service](../projects/open-build-service.md) has its own**, adopted on 2026-05-29,
for contributions to the build service's code.

So a contributor meets three different positions depending on where they contribute: a binding rule on
the forums, a binding rule in OBS, and none for packaging or the distribution itself.

## What a contributor must do

For openSUSE packages and the distribution: nothing is required. Taking responsibility for what you
submit and disclosing substantial unmodified AI output is what both the draft and Fedora's adopted
policy ask, and the safe course while the draft is open. On the forums, follow the FAQ rule. For the
Open Build Service, follow its `CONTRIBUTING.md`.

## Re-verification notes

1. **`Portal:AI`** on the openSUSE wiki, recreated on 2026-08-11 as the place the policy will be
   linked from.[^os-portal-ai]
2. **Board minutes after 2026-08-17**, under `Archive:Board_meeting_*`. The wiki's MediaWiki API
   (`api.php?action=parse&prop=wikitext`) returns their source to a plain request.
3. **The project mailing list.** Its archive sits behind a proof-of-work check that refuses plain
   requests; a browser gets through, but repeated requests can fail the check.
4. **The etherpad.** A changed draft is a sign of activity, not of adoption.

Expiry is three months, not six, because the board said it means to vote.

[^os-portal-ai]: [Portal:AI — openSUSE wiki (recreated 2026-08-11)](https://en.opensuse.org/Portal:AI)
[^os-board-2025-10-27]: [openSUSE Board meeting minutes, 2025-10-27 — openSUSE AI Code Assist Policy](https://en.opensuse.org/Archive:Board_meeting_2025-10-27)
[^os-board-2025-11-24]: [openSUSE Board meeting minutes, 2025-11-24 — AI guidelines](https://en.opensuse.org/Archive:Board_meeting_2025-11-24)
[^os-board-2025-12-08]: [openSUSE Board meeting minutes, 2025-12-08 — AI Policy](https://en.opensuse.org/Archive:Board_meeting_2025-12-08)
[^os-board-2026-02-02]: [openSUSE Board meeting minutes, 2026-02-02 — Proposed AI Policy](https://en.opensuse.org/Archive:Board_meeting_2026-02-02)
[^os-board-2026-08-17]: [openSUSE Board meeting minutes, 2026-08-17 — AI Policy](https://en.opensuse.org/Archive:Board_meeting_2026-08-17)
[^os-draft-guidelines]: [openSUSE Project Generative AI Guidance — draft for community discussion (etherpad, plain-text export)](https://etherpad.opensuse.org/p/paiguidelines/export/txt)
[^os-ml-thread]: [Discuss openSUSE AI Policy — project@lists.opensuse.org, 2026-08-11 to 2026-09-15](https://lists.opensuse.org/archives/list/project@lists.opensuse.org/thread/WDWQ3354UXTZPWQ7LFTBPERHKCNTF7KB/)
[^os-forums-faq]: [FAQ — AI-Generated Content (openSUSE Forums)](https://forums.opensuse.org/faq)
