# Lead Routing & SLA

<instructions>
Design the lead-routing rules and the SLA per segment.
</instructions>

<process>
1. Read `icp.md` (segments) and current sales coverage (ask user — do
   not invent territories).
2. Build the routing table:
   - Segment (industry × size × geo).
   - Owner (AE name / pod / round-robin / territory).
   - SLA (time to first touch).
   - Escalation if SLA missed.
   - Disqualification path (when a lead routes back to nurture instead
     of AE).
3. Edge cases: re-engaged dormant accounts, partner-sourced leads,
   account-level routing (ABM overrides individual-lead routing).
4. Reporting: dashboard URL for SLA adherence.
5. Write into `v{n}.md`.
</process>
