# Docusaurus pilot

Converts one fetched Confluence space into a Docusaurus site so writers can test it before any decision.

## Run it (Node 20+, Python 3)

```bash
cd docusaurus-pilot
python convert.py --data ../data/POKERADO/pages.json --assets ../assets --out .
npm install
npm start
```

Open http://localhost:3000. Read `CONVERSION_REPORT.md` first.

## Notes
- `convert.py` deletes and regenerates `docs/` every run. Do not hand-edit `docs/` during the test period; fix the converter or fix the page in Confluence and rerun.
- Confluence stays the source of truth. "Edit this page" links open the Confluence page.
- URLs keep the current scheme: `/space/{KEY}/{pageId}/{Title}`. The space home page is `/`.
- Broken links and anchors print as warnings during `npm run build`. Send them back with the report.
- Test other spaces by changing the `--data` path.

## What is not done yet
Search, Appfire theming (fonts, logo, product-area landing page), a `<Steps>` component (steps are plain numbered lists), Table Plus sorting, excerpt and MultiExcerpt macros, tabs polish, language picker.
