---
brief_id: <yyyy-mm-advocacy-{program}>
issued_by: field-marketing-orchestrator
issued_to: customer-advocacy-references
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Program type, target advocate count, incentive structure, CSM
partner, business outcome.>

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md`
- <CRM list of healthy accounts, NPS data, prior case studies,
  reference-program inventory>

## Deliverable

`work/{brief_id}/v1.md`: advocate identification process, permission
flow (legal-reviewed), advocate ROI tracking, reference health-check
cadence, advocate-recognition program.

## Acceptance Criteria

- [ ] Identification process names CRM signals (NPS, usage, expansion).
- [ ] Permission flow includes legal-reviewed consent template.
- [ ] ROI tracking: which deals cited which references, attribution
      cadence.
- [ ] Reference-health-check cadence: prevent reference burnout (cap
      at N requests / quarter per advocate).
- [ ] Recognition program: at minimum 1 non-monetary recognition
      mechanism.
- [ ] CSM partnership: owner per advocate (CSM, not Marketing,
      stewards the relationship).

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Legal / privacy: advocate consent rules per region.
- <Budget for incentives.>

## Instructions

1. Read linked context first.
2. Use capability `AD` (advocate identification), `RC` (reference
   call program), `CS` (case study) as scope dictates.
3. Write `v1.md`; update `state.yaml`.
