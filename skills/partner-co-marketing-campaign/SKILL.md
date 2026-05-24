---
name: partner-co-marketing-campaign
description: "Partner co-marketing campaign workflow. Lead: Charlie Channel. End-to-end joint campaign with a strategic partner."
---

# Partner Co-Marketing Campaign Workflow

## Overview
A 6-8 week motion for a joint co-marketing campaign with a strategic
partner. Lead is Charlie Channel; delegates to Polly Partner.

## Phases
1. **Joint planning** — confirm both companies' goals and approvals.
2. **Build** — joint narrative + channel mix + assets.
3. **Launch** — coordinated launch.
4. **Retro** — joint read-out.

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
4. Save outputs to `{output_folder}/work/{yyyy-mm-partner-{name}-campaign}/`.
