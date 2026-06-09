# Read-out & Rollout Decision

<instructions>
Write the post-experiment read-out and apply the pre-registered
rollout criterion.
</instructions>

<process>
1. Read the experiment design (the matching `v{n}.md` from the
   brief). Identify the pre-registered rollout criterion.
2. Pull the results from the experimentation platform. State:
   primary metric delta + CI, guardrail metric deltas, segment
   splits (only where N supports).
3. Apply the rollout criterion verbatim. State the decision: ROLL
   OUT / DO NOT ROLL OUT / EXTEND.
4. If EXTEND, justify: did we starve for N, did a segment show
   promise.
5. Lessons: what should next experiment do differently.
6. Write into `v{n}.md` of a new `work/{id}-readout/` folder (the
   experiment folder is frozen on accept).
</process>
