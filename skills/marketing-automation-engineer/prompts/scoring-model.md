# Scoring Model

<instructions>
Design (or refresh) the lead-scoring model.
</instructions>

<process>
1. Inputs: behavioral signals (page views, form fills, email opens —
   only if meaningful in B2B; many opens are bots), firmographic fit
   (from `icp.md`), recency.
2. Per signal, propose a weight with rationale. Cite source for any
   benchmark; the user's own historical conversion data preferred.
3. Threshold: define MQL cutoff. Show the expected MQL volume / week
   from current data (ask the user for current weekly form-fill
   numbers; do not invent).
4. Decay / negative scoring: rules for downscoring stale leads or
   unsubscribed prospects.
5. Observability: how the team will revise the model quarterly.
6. Write into `v{n}.md`. Recommend `growth-analyst` (Pixel) review
   the model design before implementation.
</process>
