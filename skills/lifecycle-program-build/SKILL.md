---
name: lifecycle-program-build
description: "Lifecycle program build workflow. Lead: Greta Growth. Designs and ships a multi-channel lifecycle program (activation / nurture / expansion / win-back)."
---

# Lifecycle Program Build Workflow

## Overview
End-to-end build of a lifecycle / activation program. Lead is Growth
(Greta Growth); delegates to Ember Flow.

## Phases
1. **Spec** — confirm program objective and channels.
2. **Design** — Ember Flow specs the sequence.
3. **Implement** — Mark Auto wires the MAP workflow.
4. **Read-out** — Pixel-validated measurement.

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
4. Save outputs to `{output_folder}/work/{yyyy-mm-lifecycle-{name}}/`.
