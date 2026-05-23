---
brief_id: <yyyy-mm-{program}-lifecycle>
issued_by: growth-marketing-orchestrator
issued_to: lifecycle-activation
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Program objective: activation / nurture / expansion / win-back.
Target segment. Why now.>

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/brand-voice.md`
- `{output_folder}/company-context/kpis.md`
- `{output_folder}/company-context/tech-stack.md`
- <link to current sequences, current activation metrics, gated
  asset(s), past A/B test results>

## Deliverable

`work/{brief_id}/v1.md` containing:

- Cross-channel sequence map (timeline view, channel per step).
- Message-level copy per step (subject line + body for emails;
  notification copy for push; in-app surface + copy).
- Segmentation rules (entry, exclusion).
- Exit criteria per branch (no infinite loops).
- Suppression rules (frequency cap, opt-outs, consent).
- Measurement plan (primary metric, baseline source, read cadence).

## Acceptance Criteria

- [ ] Cross-channel by design — at least 2 channels unless explicitly
      single-channel in Constraints.
- [ ] Every email subject line has 3 variants for A/B testing.
- [ ] Each step has explicit exit criteria.
- [ ] Suppression rules respect global opt-outs and regional rules
      (GDPR / CASL).
- [ ] Measurement plan names primary metric + 2 guardrail metrics +
      baseline source.
- [ ] All copy passes `brand-voice.md` don't list.
- [ ] No copy invents a customer outcome / number without source.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Channels in scope: <subset>.
- Sequence length cap: <N steps>.
- <Compliance constraints, regional sending windows.>

## Instructions

1. Read every linked context file first.
2. Use capability `LFC` or `NS` from your SKILL.md as appropriate.
3. Write `v1.md`; update `state.yaml`.
