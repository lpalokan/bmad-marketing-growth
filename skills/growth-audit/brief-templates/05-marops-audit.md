---
brief_id: <yyyy-qN-marops-audit>
issued_by: growth-analyst
issued_to: marketing-automation-engineer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

Audit the MarOps layer: workflow health, routing SLA adherence,
scoring model performance, instrumentation gaps.

## Context (links)

- MAP / CRM admin access.
- `{output_folder}/company-context/tech-stack.md`

## Deliverable

`work/{audit-id}/marops-audit.md`: per-workflow status, SLA
adherence rate, scoring-model performance, gap list.

## Acceptance Criteria

- [ ] Per workflow: status, failure modes, runbook freshness.
- [ ] Routing SLA adherence with current vs target.
- [ ] Scoring model: precision / recall against won deals.
- [ ] Instrumentation gaps prioritised for next quarter.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Stack: from tech-stack.md.

## Instructions

1. Use capabilities WF, RT, SC, RB from your SKILL.md.
