---
brief_id: <yyyy-mm-{campaign}-lifecycle>
issued_by: digital-marketing-orchestrator
issued_to: marketing-automation-engineer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

MAP-workflow for {campaign}: trigger on form-fill → nurture sequence
+ lead-routing.

## Context (links)

- `work/{campaign}/campaign-brief.md`
- `work/{campaign}/landing-page.md`
- `{output_folder}/company-context/tech-stack.md`

## Deliverable

`work/{campaign}/lifecycle-trigger.md`: workflow spec, branches,
routing table, instrumentation, runbook.

## Acceptance Criteria

(See Digital Marketing's `brief-templates/marketing-automation.md`.)

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- MAP: from `tech-stack.md`.

## Instructions

1. Use capability WF from your SKILL.md.
2. Coordinate with Ember Flow if nurture sequence is non-trivial.
