# Scoring Model Design

<instructions>
Design the inputs / weights / thresholds for the scoring model.
Implementation goes to Mark Auto.
</instructions>

<process>
1. Inputs:
   - Behavioral signals (page views, form fills, content downloads —
     filter bot traffic; email opens are often noise in B2B).
   - Firmographic fit (segment match from `icp.md`).
   - Recency.
2. Weights per signal: propose with rationale. Cite source if a benchmark
   used; the user's own conversion data preferred.
3. Threshold: where does a lead become an MQL? Show expected MQL
   volume per week given current funnel data.
4. Decay: rules for downscoring stale leads.
5. Observability: what dashboard reports model performance, what
   triggers model revision.
6. Hand-off: `marketing-automation-engineer` implements in the MAP.
7. Write into `work/{id}/v{n}.md`.
</process>
