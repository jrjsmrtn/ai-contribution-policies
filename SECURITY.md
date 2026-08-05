# Security

This repository contains **documentation only** — Markdown knowledge records, no executable code, no
dependencies, no build. There is no attack surface in the usual sense, and no supported-versions
table would mean anything.

What it *can* get wrong is a **claim**, and a wrong claim here has a real cost: someone reads that a
project permits AI-assisted contributions, contributes on that basis, and has the work rejected — or
reads that a project bans them and does not contribute at all. Both are failures of this bundle, and
both are worth reporting.

## Reporting an incorrect claim

Open an issue. Include:

- the record, and the specific claim,
- the **primary source** that contradicts it — the organisation's own page, not a summary,
- the date you read it.

Claims are corrected against primary sources only. A report without one is a useful prompt to
re-verify, but cannot itself change a record.

**Records carry an expiry.** A record past its `stale_after` is not a defect being hidden; it is the
mechanism working, and the corpus is swept weekly for exactly that. Reporting a stale record is
still welcome — the sweep says *when* to re-check, not *what changed*.

## Reporting a vulnerability

If you find something genuinely security-relevant — a malicious link in a record, a supply-chain
issue in the gate tooling this repository invokes — report it privately through
[GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
rather than opening a public issue.

The gate scripts themselves live in a separate repository and are not distributed with this bundle.
