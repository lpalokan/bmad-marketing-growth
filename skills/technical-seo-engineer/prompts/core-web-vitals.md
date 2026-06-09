# Core Web Vitals

<instructions>
Diagnose CWV failures and propose fixes.
</instructions>

<process>
1. Ask user for: CrUX data (Search Console > Core Web Vitals), Lighthouse
   report URLs for the top 5 templates, and the framework / hosting
   stack from `tech-stack.md`.
2. Per metric (LCP, INP, CLS):
   - Current 75th percentile.
   - Common root cause for this stack (cite documentation).
   - Fix list with code-level pointers.
   - Expected impact (cite source).
3. Distinguish field data (CrUX) from lab data (Lighthouse) — they
   tell different stories.
4. Write into `v{n}.md`.
</process>
