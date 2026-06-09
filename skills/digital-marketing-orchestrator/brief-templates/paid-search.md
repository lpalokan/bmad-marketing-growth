---
brief_id: <yyyy-mm-{campaign}-paid-search>
issued_by: digital-marketing-orchestrator
issued_to: paid-search-specialist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Campaign objective, budget, dates, geo.>

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/kpis.md`
- `{output_folder}/company-context/tech-stack.md`
- <link to landing page(s), current Google Ads account, prior campaign
  reports>

## Deliverable

`work/{brief_id}/v1.md`: keyword tiering, negatives list, ad-group
structure, ad variants (RSAs / PMax assets), landing-page UTMs,
bid strategy, daily/weekly reporting cadence, conversion-tracking
verification.

## Acceptance Criteria

- [ ] Keyword tiering covers brand / category / competitor / long-tail.
- [ ] At least 30 negatives in the starter list.
- [ ] 3+ ad variants per ad group with distinct angles.
- [ ] Each landing page UTM follows the tech-stack.md UTM convention.
- [ ] Bid strategy named with rationale tied to objective.
- [ ] Conversion-tracking verification (server-side or pixel)
      explicit; QA steps listed.
- [ ] Reporting cadence: dashboard URL + day-of-week.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Total monthly budget: <amount, user-provided>.
- Brand-safety / brand-bidding rules: <as per legal/PMM>.

## Instructions

1. Cap at the user's confirmed budget. Do not invent.
2. Pull bid benchmarks only from the user's own historical data; do
   not use industry averages without a cited source.
3. Write `v1.md`; update `state.yaml`.
