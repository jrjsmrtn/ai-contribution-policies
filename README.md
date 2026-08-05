# ai-contribution-policies

How open-source organisations treat **AI-authored contributions**, as an OKF bundle. Knowledge
only — the gates that check it and the decisions that shaped it live in the meta-project this
sits in.

> **Curated, not exhaustive — and that is deliberate.** 190+ organisations have published AI
> contribution policies. Enumerating them is not the goal and completeness is not claimed. Records
> are chosen for **foundations first** (they set defaults for many projects at once), then
> **novel reasoning**, then **what the consuming tools actually encounter**.
>
> Nothing here was imported from a prior survey. Every record was read from the organisation's own
> page, because the survey this replaces was consistently wrong in one direction — it dropped the
> qualifier that decides what a contributor should do. Five projects it filed as "complete ban"
> each turn out to carry a route: a revisitable decision, a named approver, a documented exceptions
> process. **The exceptions are the operative part.**

Run `okf list knowledge` for what is actually in here. This file deliberately quotes no count —
a hand-written total is the kind of claim that goes stale silently, which is the failure the
bundle exists to prevent.

## What is in here

One record per organisation, answering the question a contributor has **before** starting work:
*what does this project's policy say about AI-assisted contributions, and where is that written
down?* Every record carries its `sources`, who verified it and when, and a `stale_after` date.

Filed by **what the organisation is** — distribution, foundation, project, vendor — never by what
its policy currently says. Stance is the volatile attribute this bundle exists to track; filing by
stance would mean re-filing a record every time the fact it records changes.

## What is not in here

- **Procedure** — how to check a project's requirements before contributing. That is the
  `analyze-project` skill.
- **Design guidance** — when and why a project should adopt a policy of its own. That is the
  *AI Contribution Policy Pattern* in the pattern language.
- **Supply-chain mechanics** — licensing, provenance and disclosure generally. Those are the
  `software-supply-chain-landscape` bundle's, referenced rather than restated.

## Reading it

`knowledge/` is the bundle root. Start at [`knowledge/index.md`](knowledge/index.md); the
read-through map is [`knowledge/overview.md`](knowledge/overview.md), and
[`knowledge/log.md`](knowledge/log.md) records what changed when.

```bash
okf validate knowledge     # conformance
okf lint knowledge         # recommended fields and style
okf search knowledge --tag prohibited
```

## Licence

CC BY 4.0 for the knowledge, CC0-1.0 for dotfiles — see `REUSE.toml`. Attribution is what the
upstream sources ask for, and what the `sources` field does structurally.
