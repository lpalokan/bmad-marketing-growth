---
name: localization-rollout
description: "Localization rollout workflow. Lead: Brio Brand. End-to-end locale launch with Lily Locale, in-market reviewers, and hreflang hand-off to Tek Crawl. Use when user says locale launch, localization rollout, or new-locale go-to-market."
---

# Localization Rollout Workflow

## Overview
A multi-week motion to launch the product / website / sales motion in
one or more new locales. Lead is Brand (Brio Brand); delegates to
Lily Locale for execution; coordinates with Tek Crawl for hreflang.

## Phases
1. **Plan** — confirm locales, vendors, in-market reviewers.
2. **Build** — voice adaptation, glossary, TM, asset translation.
3. **QA** — three layers (linguistic, in-market, technical).
4. **Launch** — go-live + hreflang.
5. **Stabilise** — first 30-day quality watch.

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
4. Save outputs to `{output_folder}/work/{yyyy-mm-locale-{code}-rollout}/`.
