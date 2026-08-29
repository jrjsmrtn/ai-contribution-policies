---
type: Organization
title: GNOME
description: Rejects AI-authored Shell extensions at review while permitting AI as a development tool, and is the only record here that names the artifacts it looks for — imaginary API usage and comments serving as LLM prompts. The rule governs the third-party extension channel; the project handbook carries no AI policy at all, and the modules disagree — of 321 surveyed, nine state a policy, ranging from a named-vendor ban to GTK's conditional permission.
resource: https://gjs.guide/extensions/review-guidelines/review-guidelines.html
tags:
  - ai-contribution
  - policy
  - project
  - restricted
status: stable
generated:
  by: claude/opus-5
  at: '2026-08-29T03:40:00Z'
verified:
  - by: claude/opus-5
    at: '2026-08-29T03:40:00Z'
stale_after: 2027-02-28
sources:
  - id: gnome-review-guidelines
    title: 'GNOME Shell Extensions — Review Guidelines (gjs-guide, main)'
    resource: https://gitlab.gnome.org/World/javascript/gjs-guide/-/raw/main/docs/extensions/review-guidelines/review-guidelines.md
  - id: gnome-ai-guideline-commit
    title: 'commit dd6429b2 — review-guidelines: add guideline prohibited AI-generated code'
    resource: https://gitlab.gnome.org/World/javascript/gjs-guide/-/commit/dd6429b20e3b
  - id: gnome-handbook
    title: GNOME Project Handbook
    resource: https://handbook.gnome.org/
  - id: gnome-libadwaita-contributing
    title: 'CONTRIBUTING.md — Use of Generative AI (libadwaita, main)'
    resource: https://gitlab.gnome.org/GNOME/libadwaita/-/raw/main/CONTRIBUTING.md
  - id: gnome-commander-contributing
    title: 'CONTRIBUTING.md — why we don''t want "AI" contributions (gnome-commander, main)'
    resource: https://gitlab.gnome.org/GNOME/gnome-commander/-/raw/main/CONTRIBUTING.md
---

**Stance: AI as a tool is permitted, an AI-authored extension is rejected — and what this governs is
a submission channel, not a codebase.** The rule was added to the GNOME Shell extension review
guidelines on **2025-11-30**.[^gnome-ai-guideline-commit]

> ### Extensions must not be AI-generated
>
> While it is **not** prohibited to use AI as a learning aid or a development tool (i.e. code
> completions), extension developers should be able to justify and explain the code they submit,
> within reason.
>
> Submissions with large amounts of unnecessary code, inconsistent code style, imaginary API usage,
> comments serving as LLM prompts, or other indications of AI-generated output will be
> rejected.[^gnome-review-guidelines]

## It names the artifacts, which no other detection rule here does

[Git](git.md) writes the bundle's other detection rule and looks for **prose**: things that sound
*"overly formal or bloated"*, that look like *"AI slop"*. That inherits detection's classic
false-positive problem, since a careful non-native speaker writes formal prose.

GNOME looks for **code artifacts** instead, and lists them:

| Indicator | What it actually catches |
|---|---|
| large amounts of unnecessary code | generation padding out a small change |
| inconsistent code style | text assembled from several sources |
| **imaginary API usage** | hallucinated methods that do not exist in GJS |
| **comments serving as LLM prompts** | the instructions left in the file |

**The last two cannot be produced by a competent human writing carefully**, which is what makes this
list better than a prose test. A hallucinated API call is not a stylistic judgement — it either
resolves against the platform or it does not. Prompt text surviving in comments is not something a
non-native speaker does. A project wanting a detection rule that does not tax the people
[GCC](gcc.md) carves out should copy this list rather than Git's.

## The same rule states its scope three times, at three strengths

Worth reading carefully before adopting it, because the operative sentence is the mildest of the
three:

- The **heading** is absolute: *"Extensions must not be AI-generated."*
- The **body** is a detection-and-explainability rule: AI is *"not prohibited … as a learning aid or
  a development tool"*, and rejection follows *"indications of AI-generated
  output"*.[^gnome-review-guidelines]
- The **commit message** scopes it by proportion: it prohibits *"extensions that are predominately
  AI-generated"*.[^gnome-ai-guideline-commit]

A submitter reads the heading and may conclude any AI use disqualifies them; a reviewer applies the
body. This is the same shape as [NetworkManager](networkmanager.md), whose commit message describes a
prohibition its adopted text writes as an instruction — **in both cases the stricter statement is the
one that is not operative**, and in both the gap would decide a borderline case.

## The ground is reviewer strain, again

> Add a review guideline prohibiting the submission of extensions that are predominately
> AI-generated, **to reduce the strain on volunteer reviewers**.[^gnome-ai-guideline-commit]

Not licensing, not copyright, not quality in the abstract — **review bandwidth**, which is the same
reason the Linux wireless maintainer gave for refusing compliant patches, and the same one the
kernel's `generated-content.rst` opens with. Three independent projects, one motive: *reviewer and
maintainer attention is the scarce resource, and generation is cheap on the other side.*

The fallback test is explainability — *"developers should be able to justify and explain the code
they submit, within reason"* — which is [NetworkManager](networkmanager.md)'s demonstration rule
applied at submission review rather than in conversation. **The qualifier *"within reason"* is doing
real work**, and no other policy here has it: it concedes that a maintainer cannot demand unbounded
justification, which is what makes the test usable by volunteers.

## What this record does not cover

**This is the rule for the third-party extension channel**, `extensions.gnome.org`, where volunteers
review submissions from outside the project. It is closer to an app-store review policy than to a
contribution policy, and its subject is a *submitted artifact* rather than a patch to GNOME's own
code.

**The GNOME Project Handbook carries no AI policy at all**, checked 2026-08-29 across **all 76 of
its pages**, reading each page's article body rather than its navigation. The absence holds on
precisely the pages where such a rule would sit:[^gnome-handbook]

| Page | What it covers | AI mentions |
|---|---|---|
| `development/change-submission` | *"how to submit code changes to projects … hosted on gitlab.gnome.org"* | none |
| `development/commit-messages` | commit conventions — where a trailer would be documented | none |
| `development/legal` | *"GNOME's legal guidelines and requirements for development projects"* | none |

Also none across the six `maintainers/` pages, the seven `issues/` pages, or anywhere else.

## The modules disagree, and nothing above them decides

The handbook's silence is not the end of the story. **All 321 non-archived projects in the `GNOME`
group were surveyed on 2026-08-29**: 45 carry a `CONTRIBUTING` file, and **nine of those state an AI
policy**. They fall into three incompatible positions.

**A shared ban, in seven modules** — `glycin`, `libadwaita`, `loupe`, `libshumate`, `gnome-maps`,
`gnome-calendar`, `libmanette`:

> This project does not allow contributions generated by large languages models (LLMs) and chatbots.
> This ban includes … tools like ChatGPT, Claude, Copilot, DeepSeek, and Devin
> AI.[^gnome-libadwaita-contributing]

**It is the first named-vendor ban in this bundle.** The grounds are quality and *"likely copyright
violations"*; the scope is unusually wide — *"code, documentation, issues, and artworks"* — with one
exception, *"purely translating texts for issues and comments to English"*, which is the same
accessibility instinct [GCC](gcc.md) writes as a carve-out. It also states a consequence nothing else
here does: *"we cannot supply support on anything referencing AI
output."*[^gnome-libadwaita-contributing]

**The shared text has already drifted.** `libadwaita` added Ollama to the banned list on 2025-07-11
and `libmanette` carries it too; the other five do not. **A policy propagated by copy-paste diverges
on exactly the detail a contributor needs** — whether their tool is named — and no mechanism
reconciles the copies.

**An argued ban, in `gnome-commander`**: *"only contributions that are 100% human-made"*, with a
section explaining why. Maintenance requires understanding the code, and *"an LLM can only fake
it"*; generated work is *"plausible looking and on the first glance maybe even working but still
wrong/suboptimal"*. Then a ground **no other record in this bundle states**:

> By making LLMs do the work for you you deny yourself an opportunity for growth. Open Source is
> shorthanded as it is, and people never improving their coding skills because they rely on LLMs
> instead is going to make the situation much worse (deskilling).[^gnome-commander-contributing]

It also rejects the assist-only compromise on evidence rather than principle — *"people using LLMs
for assistance grow increasingly reliant on them and stop questioning the
results"*.[^gnome-commander-contributing]

**A conditional permission, in [GTK](gtk.md)**, which has its own record. It permits AI use under six
requirements, requires disclosure in the merge request, and **forbids the `Assisted-by:` trailer the
Linux kernel requires** — on the same anti-vendor-advertising ground the kernel used to narrow it.

## What the survey establishes

**"GNOME's AI policy" does not exist as a single thing.** A contributor to `libadwaita` is banned
from using an LLM at all; a contributor to GTK may use one under conditions; a contributor to a module
with no `CONTRIBUTING` has no rule to follow. The handbook that covers change submission, commit
messages and legal requirements for the whole project is silent on all of it.

That is the finding worth carrying, and it generalises past GNOME: **for a federated project, the
umbrella's documentation may not be where the rule lives, and sibling modules may contradict each
other.** Checking the organisation is not the same as checking the repository you are sending to.

The extension channel fits this pattern rather than breaking it: GNOME gates a submission channel it
curates centrally while leaving its own modules to decide separately. **A project can police the
channel long before it says anything about its own codebase.**

## What a contributor must do

Use AI for completion and for learning; do not let it write the extension. Before submitting, read
your own diff for the four named tells — dead code, mixed style, calls to APIs that do not exist, and
prompt text left in comments. Be ready to explain what the code does and why, in reasonable measure.
There is no tag, no disclosure field and no declaration; the check happens at review, on the
artifact.

## Re-verification notes

The guidelines are Markdown in `World/javascript/gjs-guide` on `gitlab.gnome.org`
(`docs/extensions/review-guidelines/review-guidelines.md`), rendered at `gjs.guide`. **Read the raw
source, not the rendered page** — and note that the GitLab *blob* view renders client-side, so it
answers HTTP 200 with the file text absent, exactly as
[NetworkManager](networkmanager.md)'s does. `git log` on that path dates every rule.

**The handbook, by contrast, is static HTML and fully machine-retrievable** — a Sphinx site, every
page readable with a plain fetch. The first version of this record asserted the opposite, that it
*"renders client-side"*, and used that to excuse not checking. It was wrong: the absence above was
established with 76 ordinary HTTP requests. **An untested assumption about a source's retrievability
became a reason not to look**, which is the same failure as trusting a status code, one step earlier.

**The news lead that surfaced this was nine months out of date on the fact.** It ran 2026-08-03 about
GNOME establishing an RFC process, with AI-generated extensions as context; the guideline itself
landed 2025-11-30. **A report about a project is not evidence about when its rule changed** — the
commit history is, and checking it moved the date by three quarters of a year.

Watch for: a policy covering GNOME's own modules appearing in the handbook, which would make this
record the narrower half of a pair; and for the heading and body being reconciled, since the gap
between them is the kind of thing a contributor complaint tends to close.

[^gnome-review-guidelines]: [GNOME Shell Extensions — Review Guidelines (gjs-guide, main)](https://gitlab.gnome.org/World/javascript/gjs-guide/-/raw/main/docs/extensions/review-guidelines/review-guidelines.md)
[^gnome-ai-guideline-commit]: [commit dd6429b2 — review-guidelines: add guideline prohibited AI-generated code](https://gitlab.gnome.org/World/javascript/gjs-guide/-/commit/dd6429b20e3b)
[^gnome-handbook]: [GNOME Project Handbook](https://handbook.gnome.org/)
[^gnome-libadwaita-contributing]: [CONTRIBUTING.md — Use of Generative AI (libadwaita, main)](https://gitlab.gnome.org/GNOME/libadwaita/-/raw/main/CONTRIBUTING.md)
[^gnome-commander-contributing]: [CONTRIBUTING.md — why we don't want "AI" contributions (gnome-commander, main)](https://gitlab.gnome.org/GNOME/gnome-commander/-/raw/main/CONTRIBUTING.md)
