---
name: account-overview
description: "Account overview one-slider standard and build workflow. Lead: Sam Sell (New-Business Orchestrator). Produces a single 16:9 HTML card an Account Executive reads in 30 seconds before a call: the account's own objectives, what changed, and one storyline worth saying out loud. Internal only, never customer-facing. Uses the company's own tone-of-voice and brand-compliance skills where they exist. Use when user says account overview, account overview slide, seller briefing, one-slider, briefing card, or pre-call briefing. For the full 20 to 30 minute reading document, use account-dossier instead."
---

# Account Overview

## Overview
The standard for the account overview one-slider, plus the workflow that builds
one.

An account overview is a single card, 1280 by 720, that an **Account Executive**
reads in the thirty seconds before dialling in. It is internal. It carries no
product pitch, no feature list and no "why AI" framing, because the seller
already knows what we sell. It carries account intelligence and one storyline
sharp enough that the seller wants to say it out loud on the call.

## How this differs from `account-dossier`

Same account, same record, two deliverables with different jobs.

| | `account-dossier` (AD) | `account-overview` (AO) |
|---|---|---|
| Reading time | 20 to 30 minutes | 30 seconds |
| Form | Long document, eight sections | One card, fixed canvas |
| Job | Know the account, the people and the plan | Recall the one thing to say |
| Reader moment | Preparing the account | Waiting for the call to connect |
| Output | `dossier.md`, `dossier.html` | `briefing.md`, `overview.html` |

Both write into the same `account.md` record in the same account folder, and
both render into that folder too: `dossier.html` and `overview.html` side by
side. One account is one folder. Neither owns the other. Where the phrase
"account overview" appears inside a dossier it
names section 2 of that document, which is a different thing from this skill.
Route on the deliverable the user is asking for: a document is AD, a card is AO.

## What this skill owns

| File | Owns |
|---|---|
| `reference/story-spec.md` | The five-step narrative and the compelling-event rule |
| `reference/research-brief.md` | What to dig for, and what may never be asserted |
| `reference/fit-budget.md` | Per-slot caps for a 1280 by 720 canvas, and the cut order |
| `reference/design-spec.md` | Canvas, brand tokens, the two-colour rule, emphasis |
| `templates/briefing.md` | The source the renderer consumes |
| `tools/build_briefing_html.py` | The render |
| `tools/assets/briefing.css` | The stylesheet and the neutral placeholder palette |
| `tools/assets/brands/` | Brand packs, each redefining the seven brand tokens |
| `checklists/pre-publish.md` | The gate before an AE sees it |

## What this skill inherits

These are owned by `account-dossier` and are not restated here. Read them from
`../account-dossier/reference/`. Where a rule appears in both places, the
stricter one wins.

| File | Governs the one-slider's |
|---|---|
| `house-style.md` | Register, sentence rules, banned constructions, emphasis, numbers |
| `source-fidelity.md` | KNOW, ASSUME and GAP labelling, live verification |
| `enrichment-and-provenance.md` | Any Clay or enrichment-derived person or fact |
| `account-record.md` | The shared record and who writes which section |
| `research-method.md` | Fetch order and what must be verified in session |
| `third-parties.md` | When another company may be named |

`house-style.md` carries one rule this skill leans on hardest. **Bold does not
appear in body text.** The one-slider keeps that ban. Numbers still carry visual
weight, and they get it from the accent colour and a size step rather than from
bold. See `reference/design-spec.md`.

## Voice and brand, where the company has them

A card carries a company's identity, so where that company has written its voice
and its visual identity down as skills, use them. This module does not ship them
and does not name them, because they belong to whoever installs it.

- **A tone-of-voice skill** reviews the copy before it renders.
- **A brand-compliance skill** reviews the rendered card.
- **A brand pack** supplies the colours. See the brand section below.

How to find them: look for a skill whose name ends in `-tov` or
`-brand-compliance`, or whose description says it reviews content for a named
company's voice or visual identity. Digital Workforce, for example, ships
`dwf-tov` and `dwf-brand-compliance`. Where more than one could apply, ask which.

**None of these is required.** Where a company has none, the card still builds
and still ships: this skill's own `reference/design-spec.md` and
`../account-dossier/reference/house-style.md` carry the fallback, and the render
uses the brand-neutral placeholder palette. Say once which checks you could not
run, and carry on.

Where they do exist, running them is not optional. A card that skipped an
available voice or brand review is a draft, and the pre-publish gate says so.

## Principles
- The reader is a seller thirty seconds from a live call
- Everything on the card either changes what the seller says or comes off it
- One storyline, and it has a beginning, a change and a consequence
- A compelling event is dated, sourced and structurally connected, or absent
- An absent compelling event is stated plainly and never manufactured
- The account's environment is changing faster than its evidence model, and its
  controls are never called bad
- Every number on the card is in the record with a link behind it
- Two colours, and the neutrals are structure rather than a third hue
- The card is internal and is never sent to the account

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

Two extensions apply to a one-slider and only to a one-slider.

- **Never assert a technology detail that is not publicly confirmed.** Vendor
  names, core platforms and integration paths are the most common place a card
  gets a seller caught. An unconfirmed one goes in the out-of-scope box behind an
  `Unconfirmed, gap` flag, or it comes off the card.
- **Never name a live enforcement action.** Where regulatory pressure is real and
  sourced, convert it into general industry framing. Positive triggers such as
  growth, acquisitions and expansion may be named directly.

## Capabilities

| Code | Description | File |
|------|-------------|------|
| BO  | Build an account overview one-slider | `workflow.yaml` |
| RO  | Refresh an existing one-slider against a new event | `workflow.yaml`, phases 2 to 5 |
| SS  | Show the story spec and the compelling-event rule | `reference/story-spec.md` |
| FB  | Show the fit budget and the cut order | `reference/fit-budget.md` |
| DS  | Show the design spec and the brand tokens | `reference/design-spec.md` |
| QA  | Run the pre-publish checklist against a draft | `checklists/pre-publish.md` |
| HT  | Render a briefing to HTML | `tools/build_briefing_html.py` |

**HT needs Python 3.10+ and nothing else.** The renderer is standard library
only, deliberately, so a card can be rebuilt anywhere. Set `BRIEFING_ROOT` and
`BRIEFING_HTML` to override the input and output folders.

Styling is `tools/assets/briefing.css`, which ships a **brand-neutral placeholder
palette**. An install that has not chosen a brand renders in something obviously
generic rather than in someone else's identity. Set `BRIEFING_BRAND` to a brand
pack to change that:

```
BRIEFING_BRAND=/path/to/briefing.css python tools/build_briefing_html.py <account-id>
```

A pack is a small CSS file redefining seven brand tokens and nothing else. Point
`BRIEFING_BRAND` at its path. A bare name resolves against
`tools/assets/brands/`, which is empty in a fresh install: **this module ships no
company's colours.** A company that has a brand-compliance skill usually keeps
its pack there — Digital Workforce ships one at
`dwf-brand-compliance/reference/brand/css/briefing.css`.

Point `DOSSIER_BRAND` at the matching dossier pack from the same place, and a
card and a dossier for the same account read as one family. The renderer prints
the pack in use on every build. See `reference/design-spec.md`.

## Two ways in

**A dossier already exists.** This is the preferred path. Read `account.md`,
select down to the card, and re-verify only what has moved. No new research pass.
The compelling event must already be a dated why-now signal in the record.

**No dossier exists.** Run the trimmed research pass in
`reference/research-brief.md` and write every finding into the same `account.md`,
with the same KNOW, ASSUME and GAP labels the dossier uses. The work is not
thrown away. A later dossier build inherits it.

## On Activation

1. Load configuration (tolerant of missing files; for each value, the first file that provides it wins):
   - Try `{project-root}/_bmad/custom/config.user.toml`, then `{project-root}/_bmad/custom/config.toml` (pinned overrides -- always win when present).
   - Try `{project-root}/_bmad/marketing-growth/config.yaml` (BMAD 6.x module config; flat keys `user_name`, `communication_language`, `document_output_language`, `output_folder`).
   - Try `{project-root}/_bmad/config.user.toml`, then `{project-root}/_bmad/config.toml` (BMAD 6.x root config; `[core]` keys, e.g. `output_folder`, `document_output_language`).
   - Legacy fallback: try `{project-root}/_bmad/config.yaml` (`core.user_name`, `core.communication_language`, `core.document_output_language`, `marketing-growth.output_folder`), with `{project-root}/_bmad/config.user.yaml` overriding `core.user_name` and `core.communication_language`.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`.
   - Resolve `output_folder` **silently — never ask the user**. Normalize a relative value against `{project-root}`. Then use the first of these that already contains a `company-context/` folder: the configured value, `{project-root}/output`, `{project-root}/_bmad-output` (legacy name, retired in v2.4). If none does, glob the project for `**/company-context/index.md` and `**/company-context/icp.md` (excluding `.git/`, `node_modules/`, `_bmad/`, `**/work/**`) and use its parent when there is exactly one match. Still nothing: use `{project-root}/output`. `output/` is the canonical name; `_bmad-output/` is read-only compatibility — never create it.

2. Look for the company's voice and brand skills, and for a brand pack. None is
   required. Note which are present, say once which reviews you will therefore
   not be able to run, and continue either way. See **Voice and brand** below.

3. Load context **if available — never required, never blocks.**

   `{output_folder}/company-context/` is an OKF v0.1 bundle. A one-slider reads
   less of it than a dossier does, because most of the card is the account's own
   material. Read these, and note what is absent:

   - `index.md` first, to discover what the bundle actually carries.
   - `positioning.md` and `brand-voice.md`, for the one sentence that connects
     the account's situation to what we do.
   - `offerings.md` and **every file in `offerings/`**, to name the entry point
     rather than the default entry ask.
   - `case-studies/` where a proof point would otherwise be `[PROOF NEEDED]`.
   - `personas/` and `buying-committee-model.md`, for the buyer threads in the
     footer.
   - `icp-fit-model.md` where it carries offering-line routing.

   - This bundle is read-context that **supports** the brief you are given;
     it does not widen your mandate. When working a brief, read the
     concepts its *Context (links)* names and deliver exactly its
     Acceptance Criteria — finding more in the bundle is not licence to do
     more (see `docs/protocol.md`).
   - Missing files are fine. Note what is absent and continue. Do **not** stop or
     tell the user to run a bootstrap. If a load-bearing fact is missing from
     both the context and the brief, ask one focused question (Source Fidelity)
     or proceed with what is provided.

4. Check `{output_folder}/work/dossiers/{account-id}/` for an existing
   `account.md`. Say which of the two ways in applies before starting.

5. Greet `{user_name}` by name in `{communication_language}`. State that this
   skill builds the one-slider and that the long document is `account-dossier`.
   Present the Capabilities table.

6. When the user selects a capability code from the Capabilities table, read the
   matching file and follow its instructions literally. For **BO** and **RO**,
   execute the sibling `workflow.yaml`. Save outputs to
   `{output_folder}/work/dossiers/{account-id}/`.

7. **STOP and WAIT for user input.** Accept code, number, or fuzzy match.

**CRITICAL:** Only write to `{output_folder}/work/` (deliverables, per protocol.md). Read everywhere under `{output_folder}/company-context/`; never write there — this skill owns no shared-context concept. Never overwrite an existing briefing: write a dated file alongside it and record `supersedes:` in the frontmatter. The card is internal and is never sent to the account. Stay in character until dismissed.
