# Conversion Tracking QA

<instructions>
Verify conversion tracking before any spend ramps.
</instructions>

<process>
1. Read `tech-stack.md`. Identify tag manager, server-side / client-
   side setup, CRM integration.
2. Checklist:
   - Each conversion action has a defined trigger (URL, event, value).
   - Cross-domain tracking honored (if applicable).
   - Server-side tagging operational (if used).
   - Offline conversion import wired to CRM (if used).
   - Enhanced conversions / consent mode configured per region.
   - Test conversion fires end-to-end (manual QA URL + steps).
3. Output: pass/fail per item with evidence link.
4. Write into `v{n}.md`.
</process>
