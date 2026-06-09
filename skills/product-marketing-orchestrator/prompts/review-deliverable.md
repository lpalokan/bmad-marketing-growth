# Review Deliverable

<instructions>
Review a specialist's `v{n}.md` against its `brief.md`. Produce
`v{n}-review.md` strictly per `docs/protocol.md`.
</instructions>

<process>
1. Ask the user for the `work/{deliverable-id}/` folder if not given.
2. Read `brief.md` and the latest `v{n}.md`. Read `state.yaml` to
   confirm current revision.
3. Score the deliverable against the brief's Acceptance Criteria
   checklist, item by item, ✓ or ✗ with a one-sentence justification.
   Do not introduce criteria that aren't in the brief.
4. Determine verdict:
   - All ✓ → APPROVED.
   - Any ✗ and `revision < max_revisions` → NEEDS_REVISION with a
     numbered Required Changes list (each item maps to a failing ✗).
   - Any ✗ and `revision >= max_revisions` → ESCALATED. Surface to Max
     or the user.
5. Write `v{n}-review.md` with the schema from `docs/protocol.md`.
6. Update `state.yaml`: increment `revision` only on APPROVED or
   NEEDS_REVISION (not ESCALATED). On APPROVED, set `frozen: true`,
   `accepted_at`, `accepted_version`.
7. Confirm next step with the user: revise (specialist), supersede
   (new brief), escalate (Max).
</process>
