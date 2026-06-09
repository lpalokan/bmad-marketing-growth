# ICP Refresh

<instructions>
Refresh (or initialise) `company-context/icp.md`. This is the canonical
ICP that every other marketing agent reads on activation.
</instructions>

<process>
1. Read the current `icp.md` (if it exists). Summarise it back to the
   user in three lines: "Today's ICP says: …. Last updated …. Status: …".
2. Ask the user what changed since the last refresh: new won/lost deals,
   pricing change, ICP expansion or contraction, new geo, new segment.
3. For each primary segment, confirm or update: industry, company-size
   band, geo, ARR band, buyer persona (title + team), JTBD, top three
   pains, triggers, anti-personas. Do not invent firmographics — ask.
4. Cite sources for any numeric claim (deal counts, pipeline coverage,
   etc.). If the user can't cite, mark the figure `Source: pending`.
5. Draft the new `icp.md` body and walk the user through it section by
   section. Iterate until they approve.
6. Write the file with frontmatter: `owner: product-marketing-orchestrator`,
   `last_updated: <today>`, `last_updated_by: product-marketing-orchestrator`,
   `schema_version: 1`, `status: Stable`. Confirm the path.
</process>
