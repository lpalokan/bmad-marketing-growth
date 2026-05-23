---
brief_id: <yyyy-mm-{workflow}-automation>
issued_by: digital-marketing-orchestrator
issued_to: marketing-automation-engineer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<What outcome the automation drives — e.g. "Route inbound demo
requests to AE within 5 minutes, with handoff back to nurture if no
contact in 24 hours.">

## Context (links)

- `{output_folder}/company-context/tech-stack.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/kpis.md`
- <link to existing workflows in MAP, SLAs, scoring rules>

## Deliverable

`work/{brief_id}/v1.md`: trigger logic, branching diagram, lead-routing
table, scoring deltas, instrumentation hooks, rollback plan, on-call
runbook, test cases.

## Acceptance Criteria

- [ ] Trigger logic explicit; no implicit defaults.
- [ ] Routing table covers all segments named in `icp.md`.
- [ ] Scoring deltas mapped to behaviors with rationale.
- [ ] Instrumentation hooks emit one event per branch (so the workflow
      is observable in dashboards).
- [ ] Rollback plan describes how to disable in < 5 minutes.
- [ ] Runbook lists the top 3 failure modes and on-call response.
- [ ] Test cases cover: positive flow, negative flow, edge cases
      (duplicates, missing fields, opt-outs).
- [ ] Honors opt-out / consent rules per region (GDPR, CASL, etc.).

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- MAP: <HubSpot / Marketo / Pardot / etc. from `tech-stack.md`>.
- CRM: <Salesforce / HubSpot / etc.>.
- Compliance: <GDPR, CASL, regional opt-in rules>.

## Instructions

1. Plan, do not implement directly in the MAP — produce the spec for
   a human to execute. Mark "human action required" steps explicitly.
2. Write `v1.md`; update `state.yaml`.
