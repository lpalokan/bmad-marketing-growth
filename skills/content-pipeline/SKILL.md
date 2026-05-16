---
name: content-pipeline
description: "End-to-end content creation workflow from brief to publication. Lead: content-architect."
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

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Ask the user for the inputs required by this workflow: content type (blog, guide, case study, landing page, email sequence), target topic/keyword, and target audience.

3. Load and execute the sibling `workflow.yaml` (colocated with this SKILL.md) phase by phase. Delegate to specialist agents as directed.

4. Save outputs to `{output_folder}/content-pipeline/`.
