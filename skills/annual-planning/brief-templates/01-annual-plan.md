---
brief_id: <yyyy-annual-plan>
issued_by: marketing-orchestrator
issued_to: marketing-orchestrator
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

Build the year's marketing plan: domain bets, quarterly sequencing,
budget split, success metrics.

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/kpis.md`
- prior year's marketing report (ask user for path)

## Deliverable

`work/{yyyy}-annual-plan/v1.md`: annual plan covering per-quarter
dominant motions, per-domain resourcing, success metrics, and the
3 risks to flag to the board.

## Acceptance Criteria

- [ ] Each quarter names 1-2 dominant motions (not a wish list).
- [ ] Each motion ties to a KPI from `kpis.md`.
- [ ] Per-domain resourcing (budget + headcount) stated.
- [ ] Cross-domain dependencies mapped.
- [ ] 3 top risks named with mitigations.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Total marketing budget: <user-supplied>.
- Headcount cap: <user-supplied>.

## Instructions

1. Use capability `AP` (annual plan).
2. Surface to user before issuing per-domain briefs.
