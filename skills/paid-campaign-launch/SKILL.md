---
name: paid-campaign-launch
description: "Paid campaign launch workflow. Lead: Dani Demand (Digital). Coordinates paid-search + paid-demand + LP + tracking + lifecycle nurture into a single launch motion. Use when user says paid campaign launch, paid ramp, or coordinated paid + LP + lifecycle launch."
---

# Paid Campaign Launch Workflow

## Overview
End-to-end paid-campaign launch: from objective and audience through
asset production, tracking verification, launch, and weekly hygiene.
Lead is Digital (Dani Demand); delegates to paid-search,
paid-social-demand, web-cro, and marketing-automation-engineer.

## Phases
1. **Inputs** — objective, audience, budget, attribution.
2. **Build** — paid setup (search + demand), LP, tracking, lifecycle.
3. **QA** — tracking verification, brand-safety, budget pacing.
4. **Launch** — ramp + weekly hygiene cadence.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## On Activation

1. Load configuration per template.
2. Confirm company-context exists; route to bootstrap if not.
3. Execute the sibling `workflow.yaml` phase by phase.
4. Save outputs to `{output_folder}/work/{campaign-name}/`.
