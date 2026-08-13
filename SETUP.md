# Setting up the live Confluence fetch

This replaces the frozen `raw_pages.py` demo with a real pipeline: a
scheduled GitHub Action fetches the FOX space from Confluence, rebuilds
the static site, and pushes the result — which redeploys automatically
since Pages is already set to serve from `main`.

## 1. Create an API token

Go to https://id.atlassian.com/manage-profile/security/api-tokens and
create a new token (e.g. named "foxly-docs-pilot"). Copy it immediately —
you won't be able to see it again.

## 2. Add two repo secrets

In the repo: **Settings → Secrets and variables → Actions → New repository secret**

| Name | Value |
|---|---|
| `CONFLUENCE_EMAIL` | `christie.gera@appfire.com` |
| `CONFLUENCE_API_TOKEN` | the token from step 1 |

Never put the token directly in any file in the repo — secrets are the
only place it should live.

## 3. Remove the old demo files

These were the hand-copied/frozen-fixture versions from before the live
fetch existed — delete them so there's no confusion about which pipeline
is actually running:

- `build.py` (v1, hand-copied content)
- `transform.py` (v1, worked off Atlassian MCP's HTML format)
- `raw_pages.py` (v1, frozen snapshot)
- `generate_site.py` **at the repo root** (v1 — the real one now lives in `scripts/`)

Keep: `styles.css`, `.gitignore`, `.github/workflows/rebuild.yml`, and
everything under `scripts/` and `tests/`.

## 4. Run it

Go to the **Actions** tab → "Rebuild Foxly docs from Confluence" →
**Run workflow**. Watch the log — if the token or email is wrong, it'll
fail loudly at the fetch step rather than silently produce an empty site.

If it succeeds, check the repo: the `.html` files at the root should be
freshly committed by `foxly-docs-bot`, and a new `data/pages.json` will
show the raw fetched content (useful for debugging what Confluence
actually sent back).

After that, it reruns automatically every 6 hours (see the `cron` line
in `rebuild.yml` — change it to whatever cadence makes sense once you
trust it).

## 5. What to expect the first time

This is genuinely the first time this code has touched a real Confluence
API response — everything up to now was tested against a hand-built
fixture (`tests/fixture_pages.json`) that approximates the real shape.
Realistic first-run issues:

- **Macro types we haven't mapped.** The transformer renders unknown
  macros as a visible `[Unmapped macro: ...]` box instead of eating them —
  check the built pages for these and tell me what shows up, and I'll add
  a mapping rule.
- **Pagination or field-name mismatches.** Confluence's REST API has
  changed field names across versions before; if the fetch script errors
  out parsing the response, paste me the error and the response shape
  and I'll adjust `fetch_confluence.py`.
- **Rate limiting on 52 pages.** Shouldn't be an issue at this scale, but
  the script already backs off on HTTP 429 if it happens.

None of these are signs the approach is wrong — they're exactly the kind
of thing a first real run against production data surfaces, the same way
your Get Started audit surfaced the macro-dropping bug in the markdown
extraction approach.
