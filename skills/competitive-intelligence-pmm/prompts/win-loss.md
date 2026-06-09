# Win/Loss Pattern Analysis

<instructions>
Find patterns across a set of won and lost deals. User must supply
deal-level data — never invent counts.
</instructions>

<process>
1. Ask the user for: a dataset (CSV / table / list) of won and lost
   deals with the competitor of interest, including deal size,
   segment, reason coded, and reason free-text if available.
2. If the user can't supply, refuse and ask them to pull from CRM
   first. Do not estimate.
3. Cluster reason-codes; pattern by segment, deal size, region.
4. Output: top 5 win patterns, top 5 loss patterns, each with a
   specific recommendation routed to either Sales (improve pitch),
   Product (close gap), or Marketing (change positioning / asset).
5. Confidence level per pattern based on N (deal count). Flag any
   pattern with N < 5 as `low confidence`.
6. Write `v{n}.md`.
</process>
