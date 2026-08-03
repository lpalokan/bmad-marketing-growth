# Request a Pierce Pitch Storyline Review

<instructions>
Hand the account storyline to **Pierce Pitch** (`sales-presentation-advisor`,
part of this suite) for a storyline review. Pierce reviews the storyline
against his three-act structure and headline craft; Stella folds his findings
into the next version. Never block on Pierce being absent: in the unlikely case
his skill files are missing, review against Stella's own acceptance criteria
instead and say so plainly.
</instructions>

<process>
1. Confirm the storyline exists (capability DS produced
   `work/{account-id}/account-storyline.md` or `v{n}.md`). It is the draft under
   review.

2. Confirm Pierce's skill files are present — `skills/sales-presentation-advisor/SKILL.md`
   and his review template
   `skills/sales-presentation-advisor/brief-templates/presentation-review.md`.
   Both ship with this suite, so this normally succeeds.

3. **If Pierce's files are present:**
   - Write the handoff brief using Pierce's own template
     (`brief-templates/presentation-review.md`), with `mode: review`.
   - Objective: state the audience (the account's buying committee), the desired
     decision (accept a meeting / engage on the insight), and that this is a
     `review` of a submitted storyline.
   - Context (links): the required `positioning.md`, `icp.md`, `brand-voice.md`,
     plus this account's storyline as the submitted draft
     (`work/{brief_id}/draft.md` — copy the storyline into it, or link the
     `account-storyline.md`).
   - Hand off and wait for Pierce's `v1-review.md`.
   - When it returns, fold his findings into a new storyline version (DS →
     `v{n+1}.md`), noting which changes came from the review.

4. **If Pierce's files are missing:**
   - Do not block and do not fabricate a review. Say so: "Pierce Pitch
     (`sales-presentation-advisor`) isn't available — reviewing against Stella's
     own acceptance criteria instead."
   - Self-review the storyline against: one clear value hypothesis; a Challenger
     teachable insight grounded in the account's real situation; 3–5 pillars each
     with headline + value + proof; proof uses a named comparable + a specific
     sourced metric; complete-sentence active-voice headlines; voice matches
     `brand-voice.md` if present; pillars map to the committee's roles.
   - Record the findings inline and revise via DS.

5. In the protocol, keep the orchestrator as the verdict owner — a Pierce review
   is input to Stella's next version, not an approval. Update `state.yaml`
   accordingly.
</process>
