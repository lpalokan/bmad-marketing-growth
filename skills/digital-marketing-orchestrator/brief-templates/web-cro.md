---
brief_id: <yyyy-mm-{page}-cro-test>
issued_by: digital-marketing-orchestrator
issued_to: web-cro-specialist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What page, what hypothesis, what the test will tell us.>

## Context (links)

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/brand-voice.md`
- `{output_folder}/company-context/kpis.md`
- <link to current page, current analytics, prior tests on this page>

## Deliverable

`work/{brief_id}/v1.md` containing: hypothesis, variants spec (control
+ challenger(s)), sample-size calculation with source, primary metric,
guardrail metrics, measurement plan, rollback plan, accessibility check
list, implementation tickets.

## Acceptance Criteria

- [ ] Hypothesis is single-sentence and testable.
- [ ] Sample-size calculation cites the baseline conversion rate
      source.
- [ ] Primary metric is named and tied to a KPI in `kpis.md`.
- [ ] At least 2 guardrail metrics named.
- [ ] Rollback plan describes how to revert within 15 minutes.
- [ ] WCAG 2.2 AA spot-check done; any failures flagged.
- [ ] No copy in variants conflicts with `brand-voice.md` don't list.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Stack: <CMS / experimentation tool from `tech-stack.md`>.
- <Brand or legal review requirements.>

## Instructions

1. Read every linked file before drafting.
2. Use capability `HV` (hypothesis + variants) from your SKILL.md.
3. Write `v1.md` and update `state.yaml`.
