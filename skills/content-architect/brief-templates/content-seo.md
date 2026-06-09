---
brief_id: <yyyy-mm-{topic}-content-seo>
issued_by: content-architect
issued_to: content-seo-strategist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Scope: keyword research / content-gap analysis / topic cluster.
Target topic / category. What the work feeds downstream.>

## Context (links)

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/brand-voice.md`
- <link to current content inventory, prior keyword research, Search
  Console URL, current rankings spreadsheet>

## Deliverable

`work/{brief_id}/v1.md`: keyword research table, search-intent
classification, SERP analysis summary, target-page-type per cluster,
content-gap matrix, priority recommendation with rationale.

## Acceptance Criteria

- [ ] Each keyword tagged with search intent (informational /
      navigational / commercial / transactional).
- [ ] SERP analysis covers top 10 results per primary keyword (title,
      content type, word count, distinct angle).
- [ ] Each keyword mapped to a target page type (blog / pillar /
      glossary / product / category).
- [ ] Content-gap matrix names competitors covered vs ours.
- [ ] Priority recommendation cites volume + difficulty + business
      relevance.
- [ ] No invented search volumes — cited or marked `[volume: needs
      source]`.
- [ ] Hand-off note: which articles / pillars this enables in the
      content calendar.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <Tools available: Search Console, Ahrefs / Semrush / etc.>
- <Out of scope: technical SEO (refer to Tek Crawl).>

## Instructions

1. Read linked context first.
2. Use the appropriate capability from your SKILL.md (`KR`, `CG`, `TC`).
3. Write `v1.md`; update `state.yaml`.
