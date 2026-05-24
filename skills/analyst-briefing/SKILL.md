---
name: analyst-briefing
description: "Analyst briefing workflow (incl. Gartner MQ / Forrester Wave prep). Lead: Penny PR. Delegates to Ana Analyst."
---

# Analyst Briefing Workflow

## Overview
End-to-end analyst engagement: routine briefing OR MQ / Wave /
MarketScape submission prep. Lead is PR (Penny PR); delegates to Ana
Analyst.

## Phases
1. **Scope** — briefing vs submission.
2. **Prep** — deck mapped to evaluation criteria.
3. **Engage** — the call / the submission.
4. **Follow-up** — thank-you + post-publication response.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## On Activation

1. Load configuration per template.
2. Confirm company-context exists.
3. Execute the sibling `workflow.yaml`.
4. Save outputs to `{output_folder}/work/{yyyy-mm-{analyst-or-firm}}/`.
