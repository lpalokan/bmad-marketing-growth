# Runbook

<instructions>
Produce an on-call runbook for a workflow.
</instructions>

<process>
1. Workflow name and link.
2. Top 3 failure modes, each with: symptom, detection (dashboard /
   alert), diagnostic steps, fix steps, rollback.
3. On-call contact rotation and escalation path.
4. SLA: time-to-detect, time-to-mitigate, time-to-resolve.
5. Post-incident: where to log the incident (sidecar
   `incidents-log.md`), template for the writeup.
6. Write into `v{n}.md`.
</process>
