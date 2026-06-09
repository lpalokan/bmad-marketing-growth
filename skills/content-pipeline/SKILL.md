---
name: content-pipeline
description: "End-to-end content creation workflow from brief to publication. Lead: content-architect. Use when user says content workflow, brief to publication, or end-to-end content production."
---

# Content Pipeline Workflow

## Overview
End-to-end content creation workflow from brief to publication.
Manages the full content lifecycle with quality gates.

## Phases
1. **Content Brief** — Define content requirements and specifications
2. **Content Creation** — Write and refine content
3. **Publication & Distribution** — Publish and promote content
4. **Performance Monitoring** — Track content performance

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Ask the user for the inputs required by this workflow: content type (blog, guide, case study, landing page, email sequence), target topic/keyword, and target audience.

3. Load and execute the sibling `workflow.yaml` (colocated with this SKILL.md) phase by phase. Delegate to specialist agents as directed.

4. Save outputs to `{output_folder}/content-pipeline/`.
