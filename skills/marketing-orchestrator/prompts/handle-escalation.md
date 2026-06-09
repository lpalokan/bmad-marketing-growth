# Handle Escalated Brief

<instructions>
A domain orchestrator has escalated a brief whose `revision > max_revisions`.
Decide the next step.
</instructions>

<process>
1. Read the `work/{escalated-brief-id}/` folder: `brief.md`,
   `state.yaml`, every `v{n}.md` and `v{n}-review.md`.
2. Identify the persistent failure mode: scope ambiguity, specialist
   skill gap, conflicting acceptance criteria, missing context.
3. Decide one of:
   - Supersede with a new brief (often the right answer — original
     brief had unclear acceptance criteria or wrong specialist).
   - Re-scope and re-issue to a different specialist.
   - Drop the work (the underlying business question changed).
   - Bring it back to the user for a strategic decision (the
     escalation reveals a business-level question the v2 protocol
     can't resolve).
4. Write a one-page escalation memo into the work folder:
   `escalation-resolution.md` with the decision, rationale, and next
   step. Update the brief's `state.yaml`.
5. If superseding, write the new brief and link it from the old
   `escalation-resolution.md`.
</process>
