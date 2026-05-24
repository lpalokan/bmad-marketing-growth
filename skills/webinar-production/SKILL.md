---
name: webinar-production
description: "Webinar production workflow. Lead: Frank Field. Pre-event drip → day-of run-of-show → 24h follow-up motion → attribution."
---

# Webinar Production Workflow

## Overview
Focused workflow for producing a single webinar end-to-end. Lead is
Field (Frank Field); delegates to Ella Event for production.

## Phases
1. **Spec** — confirm webinar scope and pipeline target.
2. **Pre-event** — drip plan.
3. **Day-of** — run-of-show.
4. **Follow-up** — 24h motion.
5. **Retro** — measure + retro.

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
4. Save outputs to `{output_folder}/work/{yyyy-mm-webinar-X}/`.
