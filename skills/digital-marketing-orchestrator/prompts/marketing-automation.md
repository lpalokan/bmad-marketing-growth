# Marketing Automation Build

<instructions>
Commission a marketing-automation build: MAP workflows, lead routing,
scoring rules. Delegates to marketing-automation-engineer.
</instructions>

<process>
1. Read `tech-stack.md`. Identify the relevant MAP / CRM / CDP and any
   integration constraints.
2. Confirm with the user: business outcome (e.g., "route inbound demo
   requests to AE within 5 minutes"), trigger, segment, exit criteria,
   SLA.
3. Issue brief using `brief-templates/marketing-automation.md`.
   Acceptance criteria: trigger logic, branching rules, lead-routing
   table, scoring deltas, instrumentation hooks (so changes are
   observable), rollback plan, runbook for on-call.
4. Review per `docs/protocol.md`.
</process>
