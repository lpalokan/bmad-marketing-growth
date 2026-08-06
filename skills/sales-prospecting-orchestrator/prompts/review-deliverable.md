# Review Deliverable

<instructions>
Review a specialist's `v{n}.md` against its `brief.md`. Produce `v{n}-review.md`
strictly per `docs/protocol.md`. You own the verdict; the specialist never
self-approves.
</instructions>

<process>
1. Ask the user for the `work/{deliverable-id}/` folder if not given.
2. Read `brief.md` and the latest `v{n}.md`. Read `state.yaml` to confirm the
   current revision.
3. Score the deliverable against the brief's Acceptance Criteria checklist, item
   by item, ✓ or ✗ with a one-sentence justification. Do not introduce criteria
   that aren't in the brief.
   - **Research deliverables** (account profile, field scan, relationship layer,
     signal scan) carry the exit-check items in their Acceptance Criteria — score
     them as written: facts sorted Know/Assume/Don't-know; leaders/penalties/prices
     verified live this session; no peer case-study detail attributed to the target;
     the top Don't-know named as a meeting objective; ≥1 confirmed pain candidate.
     A missing or inherited-from-memory leader/penalty/price is an automatic ✗.
4. Determine the verdict:
   - All ✓ → APPROVED.
   - Any ✗ and `revision < max_revisions` → NEEDS_REVISION with a numbered
     Required Changes list (each item maps to a failing ✗).
   - Any ✗ and `revision >= max_revisions` → ESCALATED (switch to capability ES).
5. Write `v{n}-review.md` with the schema from `docs/protocol.md`.
6. Update `state.yaml`: increment `revision` on APPROVED or NEEDS_REVISION (not
   ESCALATED). On APPROVED set `frozen: true`, `accepted_at`, `accepted_version`,
   `status: accepted`.
7. Confirm the next step with the user: revise (specialist), supersede (new
   brief), or escalate.
</process>
