# A/B Test Design

<instructions>
Design an A/B test with an honest sample-size calculation.
</instructions>

<process>
1. Ask for the baseline conversion rate of the primary metric (current
   value, source). Do not invent.
2. Compute sample size needed per variant for the user's stated
   minimum detectable effect at 80% power, 95% confidence. Show the
   calculation and call out the assumption.
3. Estimate test duration: required N ÷ current weekly traffic.
4. Define: primary metric, 2+ guardrail metrics, segmentation
   reporting, stopping rules (peeking discipline).
5. Rollback plan: how the variant gets turned off in <15 minutes.
6. Write into `v{n}.md`.
</process>
