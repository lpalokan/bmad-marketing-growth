---
name: social-campaign
description: Multi-platform social media campaign workflow from strategy to coordinated publication. Lead: social-media-strategist.
---

# Social Media Campaign Workflow

## Overview
Multi-platform social media campaign workflow.
From strategy to creation to coordinated publication across channels.

## Phases
1. **Campaign Strategy** — Define campaign goals, platforms, and approach
2. **Content Creation** — Create platform-specific content
3. **Campaign Publication** — Execute coordinated publication
4. **Campaign Analysis** — Measure and report on campaign performance

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Ask the user for the inputs required by this workflow: campaign objective (awareness, engagement, traffic, leads), target audience, key message/offer, and target platforms.

3. Load and execute the sibling `workflow.yaml` (colocated with this SKILL.md) phase by phase. Delegate to specialist agents as directed.

4. Save outputs to `{output_folder}/social-campaign/`.
