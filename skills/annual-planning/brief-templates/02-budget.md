---
brief_id: <yyyy-annual-budget>
issued_by: marketing-orchestrator
issued_to: marketing-orchestrator
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

Allocate the year's marketing budget across the 8 domains, mapped to
the dominant motions.

## Context (links)

- `{output_folder}/work/{yyyy}-annual-plan/v1.md` (approved annual plan)
- `{output_folder}/company-context/kpis.md`

## Deliverable

`work/{yyyy}-annual-budget/v1.md`: budget table by domain × quarter,
with per-line tie to a motion from the annual plan.

## Acceptance Criteria

- [ ] Total ≤ user-confirmed total budget.
- [ ] Per-domain rows sum correctly per quarter.
- [ ] Every line ties to a motion (no orphan spend).
- [ ] Pixel-validated attribution allocation (measurement spend).

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Approved annual plan is law; this brief executes it.

## Instructions

1. Use capability `BA` (budget allocation).
2. Surface to user; require sign-off before per-domain briefs.
