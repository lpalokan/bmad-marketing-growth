---
brief_id: <yyyy-mm-{experiment-name}>
issued_by: growth-marketing-orchestrator
issued_to: experimentation-funnel-lead
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One-paragraph hypothesis statement and the decision the experiment
informs.>

## Context (links)

- `{output_folder}/company-context/kpis.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/tech-stack.md`
- <link to current funnel dashboard, prior tests in this area, the
  surface where the change ships>

## Deliverable

`work/{brief_id}/v1.md` containing: hypothesis, randomization unit,
variants, primary + guardrail metrics, sample-size calculation with
source, expected duration, rollback plan, read-out plan, the rollout
decision criteria.

## Acceptance Criteria

- [ ] Hypothesis is a single sentence and testable.
- [ ] Randomization unit explicit (visitor / account / user / cohort).
- [ ] Primary metric named and tied to a KPI in `kpis.md`.
- [ ] At least 2 guardrail metrics named.
- [ ] Sample-size calculation cites the baseline source.
- [ ] Expected duration computed: required N ÷ weekly traffic.
- [ ] Rollback plan describes how to revert in < 15 minutes.
- [ ] Read-out plan names cadence and the rollout decision criteria.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Experimentation platform: <from `tech-stack.md`>.
- <Engineering or design capacity constraints.>

## Instructions

1. Read linked files first.
2. Use capability `EX` (single experiment) or `FA` (funnel audit) from
   your SKILL.md.
3. Write `v1.md`; update `state.yaml`.
