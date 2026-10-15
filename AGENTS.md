# Project handoff: Appfire docs static site

Static site generator that replaces the Refined-hosted support site for Appfire docs. Fetches Confluence content (ADF JSON) via API, renders server-side HTML for SEO, deploys on GitHub Pages.
Live: https://christiegera-appfire.github.io/cms_trial/ (noindex during trial). Repo moving to the Appfire GitHub org.

## Layout
- `scripts/fetch_confluence.py`: Confluence REST fetch. Writes `data/{SPACE}/pages.json`, downloads images to `assets/`. Retries 429 and 5xx via `request_with_retry`.
- `scripts/adf_transform.py`: ADF to HTML, macro handling, excerpt registries.
- `scripts/generate_site.py`: builds pages, nav tree, landing page, area pages, search index, `llms.txt`, per-page `index.md`.
- `scripts/*_widget.html`: JS snippets read at import time by generate_site.py.
- `sites.json`: 19 spaces, `path_prefix`, `noindex`, `external_links` (JXL is external only).
- `product-areas.json`: provisional product-area taxonomy (draft, needs sign-off).
- `tokens.css`, `styles.css`: Appfire design system. Dark default, light via `html[data-theme="light"]`.
- `product-icons/{SPACE_KEY}.svg|png`, `brand-assets/`, `fonts/`.
- `.github/workflows/rebuild.yml`: manual, every 6 hours, and `repository_dispatch` (webhook relay in `webhook-relay/` is built but not deployed). `clean_assets` input wipes `assets/` once.

## Secrets
`CONFLUENCE_EMAIL`, `CONFLUENCE_API_TOKEN` (Actions secrets, Basic auth). Plan: switch to an Atlassian service account with a scoped token (Bearer via `api.atlassian.com/ex/confluence/{cloudId}`), which needs a small change in fetch_confluence.py.

## Rules and gotchas learned the hard way
- `.nojekyll` must exist at repo root or Pages runs Jekyll and takes 15+ minutes.
- Any new widget file in `scripts/` must be committed, or the build crashes on import.
- Any new Python dependency must be added to the workflow's `pip install` line (currently requests, beautifulsoup4, markdownify).
- Python, widget, and JSON config changes need a rebuild. CSS, fonts, and icons do not.
- Pages artifact limit is 1 GB. `assets/` bloat caused a failure once (attachment titles with query strings were saved as filenames; fixed by stripping `?`).
- Hidden pages: title starts with `_` or `[Includes]`, or equals `Includes`. Excluded from nav, build, and counts.
- Page restrictions are checked at fetch time and fail closed. Space-level permissions are not checked.
- Sibling order uses Confluence `position`, with nulls last.
- Nav tree: grandchildren render only under the active page.
- Unmapped macros render a visible placeholder. The FAQ schema builder drops answers containing placeholders.
- Handled macros: panels, expand, layouts, Table Plus, MultiExcerpt, native excerpt/excerpt-include (same-space title lookup), Aura panel/button/tabs, Aura HTML (legacy redirect banners suppressed), Refined steps/expands. contentbylabel and anchor are suppressed. livesearch becomes a link to /search/.
- Language picker is a Google Translate proxy link (ja, de, fr, es, pt, zh-CN, pl). No native i18n.

## Direction (not started)
Considering moving authoring off Confluence to Docusaurus (Markdown/MDX in Git). Plan: a converter that turns ADF into MDX per space, maps macros to components, keeps current URL slugs, and emits a per-space conversion report (unmapped macros, broken images and links). Pilot one small space (POKERADO or RDD) to a noindex staging site, with writers testing. Confluence stays source of truth until cutover.

## Open items
- Anonymous access on appfire.atlassian.net is still on (SEO competition with the new site). Inbound links need updating before it is closed.
- Delete dead Vercel, Netlify, and "CMS Test" OAuth integrations.
- Strapi was evaluated and is not the likely path. Strapi's own docs run on Docusaurus.
- Never paste tokens into chat. Use env vars or Actions secrets.
