---
name: growth-audit
description: Comprehensive growth metrics audit workflow that analyzes all marketing channels and provides actionable recommendations. Lead: growth-analyst.
---

# Growth Audit Workflow

## Overview
Comprehensive growth metrics audit workflow.
Analyzes all marketing channels and provides actionable recommendations.

## Phases
1. **Data Collection** — Gather data from all marketing channels
2. **Deep Analysis** — Analyze collected data for insights
3. **Problem Diagnosis** — Identify issues and opportunities
4. **Strategic Recommendations** — Develop actionable recommendations
5. **Audit Report** — Compile comprehensive audit report

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Ask the user for the inputs required by this workflow: audit time period (30/60/90 days), channels to analyze, and key questions to answer.

3. Load and execute the sibling `workflow.yaml` (colocated with this SKILL.md) phase by phase. Delegate to specialist agents as directed.

4. Save outputs to `{output_folder}/growth-audit/`.
