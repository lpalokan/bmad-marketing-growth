---
brief_id: <slug-source-accounts>
issued_by: sales-prospecting-orchestrator
issued_to: account-sourcing-strategist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What target-account list must exist and why now — e.g.
"Produce a sourced, tiered list of ~50 target accounts in {segment} for the Q3
outbound motion.">

## Context (links)

- `{output_folder}/company-context/icp.md` (if present)
- `{output_folder}/company-context/icp-fit-model.md` (if present — the tiering rubric)
- `{output_folder}/company-context/signal-library.md` (if present)
- <add: seed criteria, TAM list, exclusions, current-customer suppression list>

## Deliverable

Write `{output_folder}/work/{brief_id}/v1.md` containing:
- The sourced accounts with firmographic anchors (name, domain, industry, size, geo).
- An A/B/C tier per account with the one-line reason.
- The signals/why-now that put A-tier accounts on top.
- Source for each account (Clay enrichment, list, or user-provided).

## Acceptance Criteria

- [ ] Every account matches the ICP segment(s) named in the brief.
- [ ] Each account has an A/B/C tier with a one-line justification.
- [ ] Tiering follows `icp-fit-model.md` if present, else a stated rubric.
- [ ] Fit and timing are shown as separate inputs to the tier, not merged.
- [ ] Excluded/suppressed accounts are honored (no current customers).
- [ ] Every account carries a data source; no invented firmographics.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. target count, geos, industries in/out of scope, Clay credit budget>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Source candidates (Clay `find-and-enrich-company`, provided lists, web).
3. Tier each account on fit and timing separately, per the fit model.
4. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
