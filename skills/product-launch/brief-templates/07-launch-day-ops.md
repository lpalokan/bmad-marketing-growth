---
brief_id: <yyyy-mm-{launch}-day-ops>
issued_by: product-marketing-orchestrator
issued_to: product-marketing-orchestrator
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

Launch-day run-of-show: 15-minute time-blocks T-day-1 through T+1.

## Context (links)

- All approved down-stream briefs (`work/{launch-name}/*`).

## Deliverable

`work/{launch-name}/launch-day-runbook.md`: 15-minute time-blocks
with owner, action, contingency per block.

## Acceptance Criteria

- [ ] Every time-block has owner + action + contingency.
- [ ] All domain owners (PR / Digital / Field / Content) sign off
      on their blocks.
- [ ] Comms tree for issues: who tells whom in what window.
- [ ] Kill / rollback criteria stated.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- T-day timezone: <e.g. PT for press embargo lift>.

## Instructions

1. Surface to all domain orchestrators.
2. Lock 48 hours before T-day.
