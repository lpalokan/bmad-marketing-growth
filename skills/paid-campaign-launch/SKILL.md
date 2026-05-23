---
name: paid-campaign-launch
description: "Paid campaign launch workflow. Lead: Dani Demand (Digital). Coordinates paid-search + paid-demand + LP + tracking + lifecycle nurture into a single launch motion."
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

## On Activation

1. Load configuration per template.
2. Confirm company-context exists; route to bootstrap if not.
3. Execute the sibling `workflow.yaml` phase by phase.
4. Save outputs to `{output_folder}/work/{campaign-name}/`.
