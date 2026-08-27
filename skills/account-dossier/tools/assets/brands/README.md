# Brand packs

Empty on purpose. **This module ships no company's colours.**

A suite that other companies install should not render their work in someone
else's identity, so `dossier.css` carries a brand-neutral placeholder palette and
a pack is something you supply.

A pack redefines the seven brand tokens and nothing else:

```css
:root{
  --ink:#111111;            /* body text and the darkest fill */
  --accent:#2450D8;         /* links, rules, key seats */
  --accent-2:#7FB0FF;       /* the secondary accent, and provenance on dark */
  --deep:#16307F;           /* the deep fill behind white text */
  --grad-full:linear-gradient(90deg,#7FB0FF 0%,#2450D8 48%,#16307F 100%);
  --grad-bc:linear-gradient(90deg,#2450D8 0%,#7FB0FF 100%);
  --brand-font:'Inter',Arial,Calibri,system-ui,-apple-system,sans-serif;
}
```

Leave the structure tokens alone: the greys, the panel tints and white are not
brand.

`--grad-full` is read stop by stop, not rebuilt from `--accent` and `--deep`. A
brand's gradient can carry a hue that appears nowhere else, so write the stops
you actually want.

Use one by path:

```
DOSSIER_BRAND=/path/to/pack.css python ../../build_dossier_html.py <slug>
DOSSIER_BRAND=/path/to/pack.css python ../../build_committee_chart.py committee.json
```

Both tools read the same file, so the page and the diagram inside it stay one
design. Dropping a pack in this folder lets you use its bare name instead.

Most companies keep their packs with their own brand-compliance skill, which is
the source of truth if the two ever disagree. Digital Workforce, for example,
ships a matched pair at `dwf-brand-compliance/reference/brand/css/` —
`dossier.css` here and `briefing.css` for the account-overview one-slider.
