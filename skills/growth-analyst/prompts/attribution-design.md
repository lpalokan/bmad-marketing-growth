# Attribution Model Design

<instructions>
Design (or refresh) the attribution approach. The implementation lives
elsewhere; this prompt produces the spec.
</instructions>

<process>
1. Confirm: business question the attribution must answer (channel
   allocation, individual deal credit, campaign incrementality).
2. Recommend one of:
   - Multi-touch attribution (MTA): when journey is fully tracked and
     opportunity-level credit matters.
   - Marketing Mix Modeling (MMM): when channels are many and offline
     channels matter; statistically rigorous but slow.
   - Lift / incrementality study: best for demand-creation channels.
   - Last-click: only when nothing else is operationally feasible.
3. Trade-offs: cost, time-to-signal, data requirements, sensitivity to
   tracking gaps.
4. Implementation hand-off: which agent (Mark Auto for instrumentation,
   Posy Paid for in-platform lift studies).
5. Reporting cadence: who reads, day-of-week, decision authority.
6. Write into `work/{id}/v{n}.md`.
</process>
