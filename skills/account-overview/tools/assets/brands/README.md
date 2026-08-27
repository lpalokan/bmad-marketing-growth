# Brand packs

Empty on purpose. **This module ships no company's colours.**

A suite that other companies install should not render their work in someone
else's identity, so `briefing.css` carries a brand-neutral placeholder palette
and a pack is something you supply.

A pack is a small CSS file that redefines the seven brand tokens and nothing else:

```css
:root{
  --ink:#111111;      /* body text, and the story band background */
  --accent:#2450D8;   /* accent on light: labels, numbers, rules */
  --accent-dark:#7FB0FF;  /* accent on dark: inside the story band only */
  --rule:var(--accent);   /* the 5px rule across the top */
  --ring-a:var(--accent); /* rings behind the story band, gradient start */
  --ring-b:var(--accent); /* rings behind the story band, gradient end */
  --brand-font:'Inter',Arial,Calibri,system-ui,-apple-system,sans-serif;
}
```

Leave the structure tokens alone. `reference/design-spec.md` has the rules that
hold whoever the brand belongs to.

Use one by path:

```
BRIEFING_BRAND=/path/to/pack.css python ../../build_briefing_html.py <account-id>
```

Dropping a pack in this folder lets you use its bare name instead. Most companies
keep theirs with their own brand-compliance skill, which is the source of truth
if the two ever disagree. Digital Workforce, for example, ships a matched pair at
`dwf-brand-compliance/reference/brand/css/` — `briefing.css` for the card and
`dossier.css` for the long document, so both read as one family.
