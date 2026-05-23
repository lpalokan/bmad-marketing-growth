---
brief_id: <yyyy-mm-{campaign}-paid-demand>
issued_by: digital-marketing-orchestrator
issued_to: paid-social-demand-specialist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Demand creation vs lead capture; platforms; budget; dates.>

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/brand-voice.md`
- `{output_folder}/company-context/kpis.md`
- <link to creative assets, gated asset(s), landing pages, prior
  campaign reports>

## Deliverable

`work/{brief_id}/v1.md`: audience definition per platform, creative
concept per audience, frequency cap, brand-safety controls, attribution
model, reporting cadence, kill criteria.

## Acceptance Criteria

- [ ] Audiences mapped to named ICP segments from `icp.md`.
- [ ] Creative concept named per audience (no one-size-fits-all).
- [ ] Frequency cap stated per platform.
- [ ] Brand-safety controls listed (exclusion lists, inventory tiers).
- [ ] Attribution approach named: lift study / MMM / last-click /
      MTA — with rationale.
- [ ] Reporting cadence: dashboard URL + day-of-week + KPI per row.
- [ ] Kill criteria: when do we pause spend, signed off by Pixel.
- [ ] Google Demand Gen and YouTube Ads are explicit options (not just
      LinkedIn/Meta).

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Total monthly budget: <amount, user-provided>.
- Platforms in scope: <subset of LinkedIn / Meta / Google Demand Gen /
  YouTube Ads / others>.

## Instructions

1. Define audiences against `icp.md`. Do not invent firmographics.
2. Pair every audience with a creative concept and a landing page.
3. Write `v1.md`; update `state.yaml`.
