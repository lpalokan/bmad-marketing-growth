---
brief_id: <yyyy-qN-abm-instrumentation>
issued_by: field-marketing-orchestrator
issued_to: marketing-automation-engineer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

Close the instrumentation gaps surfaced by the ABM signals matrix.

## Context (links)

- `work/{program}/signals.md`
- `{output_folder}/company-context/tech-stack.md`

## Deliverable

`work/{program}/instrumentation.md`: per gap, MAP / CRM / analytics
spec to wire the signal to its action.

## Acceptance Criteria

- [ ] Each gap has a spec and an owner.
- [ ] Runbook for any new workflow.
- [ ] Rollback in < 5 minutes.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Stack: from tech-stack.md.

## Instructions

1. Use capability WF (workflow spec) from your SKILL.md.
