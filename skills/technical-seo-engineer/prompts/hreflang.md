# Hreflang Implementation Plan

<instructions>
Plan an hreflang implementation for a multi-locale site.
</instructions>

<process>
1. Read brief. Identify: locales in scope, URL structure (subdomain /
   subdirectory / ccTLD), CMS support.
2. Hreflang matrix: every locale → every other locale (must be
   reciprocal). Include x-default.
3. Implementation: HTML head, HTTP header, or XML sitemap — choose
   based on site type and engineering capacity.
4. QA checklist: return code, reciprocal coverage, no chains of
   redirects, no conflicts with canonicals.
5. Common failure modes for this stack (cite source).
6. Write into `v{n}.md`.
</process>
