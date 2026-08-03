# Agent Recommendation (whole-suite routing)

<instructions>
Locate the user's request on the full org chart in `SKILL.md` ("The full
org chart") and recommend the single most specific owner: a workflow if
one matches the shape of the work, else a specialist, else a domain
orchestrator, else Max Growth or Sam Sell. Explain the routing in one or
two sentences and tell the user exactly how to invoke the recommendation
(the `/skill-name` and, where useful, the capability code to pick).
</instructions>

<process>
1. Classify the request:
   - **Named-account / outbound / prospecting** (win this account, target
     list, buying committee, outreach, replies) → sales wing. Whole-motion
     requests go to Sam Sell (`sales-prospecting-orchestrator`, capability
     RA); single-step requests go to the matching specialist.
   - **Marketing domain work** (positioning, content, paid, lifecycle,
     ABM programs, PR, partner…) → the matching domain orchestrator, or
     directly to a specialist when the request names one deliverable that
     clearly belongs to them.
   - **Repeatable multi-step motion** that matches a Tier-1/Tier-2
     workflow (launch, teardown, webinar, locale rollout…) → the workflow.
   - **Strategy, budget, prioritisation across marketing domains** → Max
     Growth (`marketing-orchestrator`).
   - **Cross-wing motion** (marketing air cover + sales ground game on
     the same targets) → keep it here: offer capability AH or GP.
   - **Setup** (missing company-context) → `company-context-bootstrap`;
     durable sales knowledge → `sales-context-bootstrap`.
2. If the request is ambiguous between two owners, ask ONE focused
   question rather than guessing.
3. State the recommendation: agent/workflow, persona name, why them, and
   what they will produce. Offer to brief them on the context gathered so
   far (the user re-invokes as the recommended skill).
</process>
