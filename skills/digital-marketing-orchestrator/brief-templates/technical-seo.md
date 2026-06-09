---
brief_id: <yyyy-mm-{site}-tech-seo>
issued_by: digital-marketing-orchestrator
issued_to: technical-seo-engineer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Site / subdirectory in scope; audit trigger; success criteria.>

## Context (links)

- `{output_folder}/company-context/tech-stack.md`
- `{output_folder}/company-context/positioning.md`
- <Search Console URL, current sitemap, prior audits, CWV report,
  hreflang implementation if any>

## Deliverable

`work/{brief_id}/v1.md`: audit findings table, fix-priority matrix
(impact × effort), implementation tickets, post-fix verification plan.

## Acceptance Criteria

- [ ] Audit covers: indexation, sitemap health, robots.txt, schema
      markup, Core Web Vitals (LCP / INP / CLS), hreflang (if multi-
      locale), canonicals, internal linking, JS rendering.
- [ ] Each finding has: severity, impacted URLs (sample), evidence
      link (Search Console, Lighthouse, third-party tool with cited
      source), recommended fix.
- [ ] Fix-priority matrix uses impact (high/med/low) × effort
      (high/med/low). Top 5 quick wins called out.
- [ ] Implementation tickets are repo-ready (title, description,
      acceptance criteria, owner).
- [ ] Post-fix verification plan names the metric, the tool, and the
      cadence.
- [ ] No fix is recommended without an evidence link.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Stack: <CMS, hosting, CDN, frontend framework from `tech-stack.md`>.
- <Engineering capacity constraints, freeze windows.>

## Instructions

1. Audit before recommending. No fix without evidence.
2. Distinguish "site bug" from "Google bug" — name external Google
   updates if relevant (cite source).
3. Write `v1.md`; update `state.yaml`.
