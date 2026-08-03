# Score Fit (fit ✕ timing) + Action Tier

<instructions>
Score how appealing the offerings are for one prospect and whether now is the
moment to move — keeping FIT and TIMING as two separate scores, never collapsed
into one. Show the working, source every input, and emit an explicit action tier.
Output is `v{n}.md` (in the protocol) or
`{output_folder}/work/{account-id}/fit-scorecard.md` (standalone).
</instructions>

<process>
1. Read the inputs: `account-profile.md` (Remy's profile — firmographics,
   technographics, org shape, initiatives), `offerings.md` (what we're matching
   to), the signal scan / `signal-library.md` triggers, and the scoring model
   `icp-fit-model.md`. If the model is absent, note it and score against a
   transparent default rubric — do not block.

2. **Score FIT** — "should we sell here at all?" On the model's weighted rubric
   across three categories, each factor scored against the model's scale and each
   carrying the input it came from:
   - **Firmographic** — industry, size band, revenue/geo fit vs the ICP.
   - **Technographic** — stack signals: greenfield / complementary / displacement.
   - **Persona** — is the buying function present and shaped the way we sell into?
   Show the sub-scores and the weighted fit total. Fit uses durable facts, not
   this-quarter events.

3. **Score TIMING** — "is now the moment?" — separately, on triggers and intent:
   recency and strength of funding, hires, headcount moves, migrations, regulatory
   deadlines, job posts, intent spikes. A strong fit with cold timing is NOT the
   same as a weak fit with hot timing — report both numbers, never a blend.

4. **Map pains → product alignment.** For each material pain in the profile, score
   pain severity (1-5) × product alignment (1-5) and list the offering that
   addresses it. This is the qualitative bridge behind the fit number.

5. **Compute overall Priority = Fit × Signal-strength × Strategic-value.** State
   each term, its source, and the arithmetic — no hidden math. Strategic-value is
   defined in `icp-fit-model.md`; if absent, state the definition you used.

6. **Emit an ACTION TIER**, mapped from the model's cutoffs:
   **prioritize now / into sequences / nurture / deprioritize.** If the tier is
   **deprioritize**, say so plainly — do not soften a cold account into a warm
   sentence.

7. Write the scorecard: separate Fit and Timing sections with visible sub-scores,
   the pain↔alignment map, the priority arithmetic, the action tier, and a
   **Sources** line per input. Mark missing inputs `[UNKNOWN — needs input]`
   rather than guessing a factor.

8. Write the file as `fit-scorecard.md` (`v{n}.md` under the brief); in the
   protocol, set `state.yaml` `status: in-review` and notify the orchestrator.
</process>
