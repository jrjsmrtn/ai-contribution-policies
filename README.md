# ai-contribution-policies

How open-source organisations treat **AI-authored contributions**, as an OKF bundle. Knowledge
only — the gates that check it and the decisions that shaped it live in the meta-project this
sits in.

> **Status: skeleton.** One verified record. The 27-entry survey named in ADR-0011 has *not* been
> imported, deliberately: those entries were last reviewed 2025-09-04 and importing them would
> fill the bundle with claims nobody has checked in eleven months. Extraction and re-verification
> are one piece of work.

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
