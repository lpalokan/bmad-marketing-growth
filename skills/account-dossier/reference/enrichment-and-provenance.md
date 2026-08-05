# Enrichment and provenance

Covers Clay MCP and any other enrichment source that supplies people, companies
or firmographics.

**Which tool to call is not decided here.** The agents own that:
`account-research-analyst` uses `find-and-enrich-company`,
`buying-committee-mapper` uses `find-and-enrich-contacts-at-company` and
`find-and-enrich-list-of-contacts`, `account-sourcing-strategist` sources
companies, and signal work may use `ask-question-about-accounts`. Each of those
skills already states that Clay is an enhancement rather than a requirement, with
`WebSearch` and `WebFetch` as the fallback.

This file decides something different: **how an enrichment-derived fact is
allowed to appear in front of an Account Executive.**

## Why this file exists

Two failures on real accounts:

- A buying committee shipped with fabrication risk that had to be caught and the
  whole deliverable rebuilt. It was only trusted after the names were verified
  against LinkedIn.
- A committee roster was carried forward from an enrichment pull one month old.
  When the leadership page was checked live, a title had already moved. The
  enrichment said "EVP, Chief Technology Officer" and the company's own page said
  something else entirely.

Enrichment is fast and broad. It is also a snapshot of a database rather than a
statement by the company.

## Rules

**1. Label the tool and the date, always.**
`(KNOW: Clay find-and-enrich-contacts-at-company, 2026-07-08)`
An unlabelled enrichment fact is not KNOW. It has no provenance at all.

**2. Corroborate a person before they reach the reader-facing table.**
Name, title and seat need a public second source. The company's own governance or
leadership page is best, LinkedIn is acceptable. Corroborated people go in the
committee table. Uncorroborated people go in a separately headed block that says
where they came from, when, and that they must be re-verified before use.

**3. The company's own page wins on titles.**
Where enrichment and the company disagree, publish the company's version and note
the disagreement. Titles decay faster than anything else in a dossier.

**4. Never source a business number from enrichment.**
Revenue bands and headcount from enrichment are estimates and ranges. Financials
come from the filing, the results release or the annual report. Use enrichment for
shape, never for a figure that will appear in an argument.

**5. Flag staleness.**
Enrichment older than about thirty days is stale. Say so in the dossier next to
the block it produced, and put re-verification on the pre-send checklist.

**6. Log the pull.**
Record the task or run identifier so a committee can be audited later. A roster
nobody can trace back to a pull is a roster nobody can defend.

**7. Write-backs need explicit approval.**
`add-company-data-points`, `add-contact-data-points` and `track-event` change the
user's own workspace. They are outward-facing actions. Never fire them silently
during a dossier build. Ask first, every time.

**8. Check credits before a large pull.**
`get-credits-available` first when a pull will be broad. Enrichment costs the user
money.

**9. Never let the dossier depend on enrichment being reachable.**
It may be absent in headless or scheduled runs. Every dossier must be completable
from public sources alone, with the committee thinner and the gaps named.

## Contact detail

Where enrichment returns email addresses or phone numbers, keep them out of the
dossier body. The dossier is a document that gets forwarded. Personal contact
detail belongs in the CRM.

## What to record in the sources block

Enrichment-derived material gets its own heading in section 8, "Inherited, needs
re-verification", naming the tool, the date, and which sections depend on it.
