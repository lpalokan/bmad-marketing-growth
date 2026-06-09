# Tech Stack Refresh

<instructions>
Refresh `company-context/tech-stack.md`. This is the only file this
agent writes to `company-context/`.
</instructions>

<process>
1. Read current `tech-stack.md`. Summarise back to the user.
2. Ask what changed since last refresh: new vendor, deprecated tool,
   re-platform, integration added, scoring model rewritten.
3. Update sections: CDP, MAP, CRM, analytics, ad platforms, identity
   resolution, lead-routing rules, scoring model, known gaps.
4. Sources: user-provided only (or contract URLs / vendor pages with
   citations). Do not invent vendor versions.
5. Frontmatter: `owner: marketing-automation-engineer`,
   `last_updated: <today>`, `last_updated_by: marketing-automation-engineer`,
   `schema_version: 1`, `status: Stable`.
6. Also emit `work/{yyyy-mm-tech-stack-refresh}/v{n}.md` with the diff
   summary, for auditability.
</process>
