---
name: seo-sprint
description: Focused SEO optimization sprint workflow from audit to actionable quick wins. Lead: seo-strategist.
---

# SEO Sprint Workflow

## Overview
Focused SEO optimization sprint workflow.
From audit to actionable quick wins in a structured approach. Typical duration: 2 weeks.

## Phases
1. **SEO Audit** — Comprehensive SEO health check
2. **Keyword Strategy** — Define target keyword strategy
3. **Content Gap Analysis** — Identify content opportunities
4. **Quick Wins Execution** — Implement high-impact, low-effort optimizations
5. **Sprint Review** — Review progress and plan next steps

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Ask the user for the inputs required by this workflow: website URL, niche/industry, top 3 business objectives, and current SEO tools in use.

3. Load and execute the sibling `workflow.yaml` (colocated with this SKILL.md) phase by phase. Delegate to specialist agents as directed.

4. Save outputs to `{output_folder}/seo-sprint/`.
