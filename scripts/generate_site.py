#!/usr/bin/env python3
"""
generate_site.py (v4) — builds the static site from one or more spaces'
data/{space_key}/pages.json files, driven by sites.json.

v4 change: generalized from a single hardcoded space to config-driven
multi-space support. Space keys are globally unique across a Confluence
instance, so multiple spaces coexist cleanly under one flat
/space/{KEY}/{pageId}/{Title}/ tree with no path-prefix or collision
concerns — "multi-space" is really just "run the existing per-space
pipeline once per configured space, into the same output directory."

Each space can route its "Get Help" widget to its own JSM project, since
different spaces may belong to different products/teams with different
service desks.
"""

import html
import json
import os
import re
import shutil
import sys
from urllib.parse import quote

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from adf_transform import adf_to_html, generate_meta_description, build_multiexcerpt_registry

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
CONFIG_FILE = os.path.join(ROOT, "sites.json")
DATA_DIR = os.path.join(ROOT, "data")
OUT_DIR = ROOT

_WIDGET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "get_help_widget.html")
with open(_WIDGET_PATH) as _f:
    GET_HELP_WIDGET_TEMPLATE = _f.read()

_ADV_TABLES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "advanced_tables_widget.html")
with open(_ADV_TABLES_PATH) as _f:
    ADVANCED_TABLES_SCRIPT = _f.read()


def confluence_style_path_segment(title):
    """Mirrors Confluence's own URL style: spaces become a literal '+',
    other characters unsafe in a URL path get percent-encoded."""
    with_plus = (title or "untitled").replace(" ", "+")
    return quote(with_plus, safe="+()")


def page_url(page_id, space_key, titles, path_prefix=""):
    """URL for a page: {path_prefix}/space/{KEY}/{pageId}/{Title+With+Plus}/

    path_prefix is empty for root-domain hosting (Netlify's cmstrial.netlify.app,
    or a real custom domain like support.appfire.com). It's needed for GitHub
    Pages on a normal project repo, which serves under a subpath
    (https://username.github.io/repo-name/) rather than at the domain root —
    without this, every link on the site would be missing that subpath and
    resolve to the wrong place.
    """
    title_segment = confluence_style_path_segment(titles.get(page_id, "untitled"))
    return f"{path_prefix}/space/{space_key}/{page_id}/{title_segment}/"


NAV_SHELL_TEMPLATE = """
<div class="brand"><span class="brand-mark">{brand_name}</span></div>
<div class="brand-tag">{tagline}</div>
<p class="pilot-note">{count} pages in this space, fetched live from Confluence via API.</p>
<nav>{nav_items}</nav>
"""


def build_nav_tree(parent_id, pages_by_parent, space_key, titles, active_id, valid_ids, path_prefix="", depth=0, max_depth=4):
    child_ids = [c for c in pages_by_parent.get(parent_id, []) if c in valid_ids]
    if not child_ids or depth > max_depth:
        return ""
    items = []
    for cid in child_ids:
        cls = ' class="active"' if cid == active_id else ""
        sub = build_nav_tree(cid, pages_by_parent, space_key, titles, active_id, valid_ids, path_prefix, depth + 1, max_depth)
        items.append(f'<li><a href="{page_url(cid, space_key, titles, path_prefix)}"{cls}>{html.escape(titles[cid], quote=False)}</a>{sub}</li>')
    return f"<ul>{''.join(items)}</ul>"


def build_nav(pages_by_parent, space_key, titles, valid_ids, roots, active_id, path_prefix=""):
    top_items = []
    for rid in roots:
        cls = ' class="active"' if rid == active_id else ""
        sub = build_nav_tree(rid, pages_by_parent, space_key, titles, active_id, valid_ids, path_prefix)
        top_items.append(f'<li><a href="{page_url(rid, space_key, titles, path_prefix)}"{cls}>{html.escape(titles[rid], quote=False)}</a>{sub}</li>')
    return f"<ul>{''.join(top_items)}</ul>"


def page_shell(title, meta_description, nav_html, page_count, body_html, brand, widget_html, canonical_url, path_prefix="", noindex=False, extra_head=""):
    safe_title = html.escape(title or "", quote=False)
    safe_brand_name = html.escape(brand.get("name", "Docs"), quote=False)
    safe_desc = html.escape(meta_description or "", quote=True)
    nav_shell = NAV_SHELL_TEMPLATE.format(
        brand_name=safe_brand_name,
        tagline=html.escape(brand.get("tagline", "Live docs, fetched from Confluence via API."), quote=False),
        count=page_count,
        nav_items=nav_html,
    )
    if noindex:
        # Explicit "don't index this" beats silence. A missing sitemap or
        # canonical tag doesn't stop Google from crawling a publicly
        # reachable site — it just means there's no signal either way. This
        # is the actual mechanism that guarantees a trial deployment stays
        # out of search results regardless of how it's discovered.
        robots_tag = '<meta name="robots" content="noindex, nofollow">'
        canonical_tag = ""  # moot once noindex is set — nothing to consolidate toward
    else:
        robots_tag = ""
        canonical_tag = f'<link rel="canonical" href="{canonical_url}">' if canonical_url else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{safe_title} | {safe_brand_name}</title>
<meta name="description" content="{safe_desc}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{path_prefix}/styles.css">
{robots_tag}
{canonical_tag}
{extra_head}
</head>
<body>
<div class="shell">
  <main class="content">
    <h1>{safe_title}</h1>
    {body_html}
  </main>
  <aside class="sidebar">{nav_shell}</aside>
</div>
{widget_html}
{ADVANCED_TABLES_SCRIPT}
</body>
</html>
"""


def build_faq_schema(body_html):
    soup = BeautifulSoup(body_html, "html.parser")
    details = soup.find_all("details")
    if not details:
        return ""
    entities = []
    for d in details:
        summary = d.find("summary")
        if not summary:
            continue
        question = summary.get_text(strip=True)
        d_copy = BeautifulSoup(str(d), "html.parser")
        d_copy.find("summary").decompose()
        answer_text = d_copy.get_text(" ", strip=True)
        entities.append({
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {"@type": "Answer", "text": answer_text},
        })
    if not entities:
        return ""
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'


def rewrite_internal_links(body_html, space_key, titles, valid_ids, path_prefix=""):
    soup = BeautifulSoup(body_html, "html.parser")
    for a in soup.find_all("a", href=True):
        m = re.search(r"/pages/(\d+)", a["href"])
        if m and m.group(1) in valid_ids:
            a["href"] = page_url(m.group(1), space_key, titles, path_prefix)
    return str(soup)


def load_includes(pages):
    includes = {}
    for p in pages:
        if p["title"] and p["title"].startswith("_") and p.get("adf"):
            includes[p["title"]] = adf_to_html(p["adf"])
    return includes


def render_children_list(parent_id, pages_by_parent, space_key, titles, valid_ids, path_prefix="", depth=2):
    children = [c for c in pages_by_parent.get(parent_id, []) if c in valid_ids]
    if not children:
        return ""
    items = []
    for child_id in children:
        title = titles.get(child_id, "Untitled")
        sub = ""
        if depth > 1:
            sub = render_children_list(child_id, pages_by_parent, space_key, titles, valid_ids, path_prefix, depth=depth - 1)
        items.append(f'<li><a href="{page_url(child_id, space_key, titles, path_prefix)}">{html.escape(title, quote=False)}</a>{sub}</li>')
    if not items:
        return ""
    return f"<ul class='children-list'>{''.join(items)}</ul>"


def build_space(data_path, out_dir, brand, base_url="", path_prefix="", jsm_project_key=None, jsm_request_type_id=None, noindex=False, multiexcerpt_registry=None):
    """Builds one space's pages. Returns (space_key, roots, titles, built_list) —
    the caller needs space_key/roots/titles to build the top-level home page
    once it knows about every space, not just this one.

    path_prefix matters for GitHub Pages project repos (served under
    /repo-name/, not domain root) — see page_url()'s docstring. It's used
    for every link WRITTEN INTO the HTML (nav, images, stylesheet,
    canonical), but never for where files actually live on disk: GitHub
    adds that prefix automatically at serving time based on the repo name,
    so baking it into the output directory structure would be wrong.
    """
    with open(data_path) as f:
        data = json.load(f)

    space_key = data.get("space_key", "SPACE")
    space_name = data.get("space_name", space_key)

    pages = [p for p in data["pages"] if p.get("adf") and not (p["title"] or "").startswith("_")]
    titles = {p["id"]: p["title"] for p in pages}
    valid_ids = set(titles.keys())
    includes = load_includes(data["pages"])

    media_map = {k: f"{path_prefix}/{v}" for k, v in data.get("media", {}).items()}

    pages_by_parent = {}
    for p in data["pages"]:
        parent = p.get("parent_id")
        if parent:
            pages_by_parent.setdefault(parent, []).append(p["id"])

    roots = [
        p["id"] for p in data["pages"]
        if p["id"] in valid_ids and (p.get("parent_id") not in valid_ids)
    ]

    widget_html = GET_HELP_WIDGET_TEMPLATE.replace("__JSM_PROJECT_KEY__", jsm_project_key or "")

    built = []
    for p in pages:
        body_html = adf_to_html(
            p["adf"],
            unresolved_includes=includes,
            link_titles=titles,
            media_map=media_map,
            multiexcerpt_registry=multiexcerpt_registry,
        )
        if "<!--CHILDREN_MACRO-->" in body_html:
            children_html = render_children_list(p["id"], pages_by_parent, space_key, titles, valid_ids, path_prefix)
            body_html = body_html.replace("<!--CHILDREN_MACRO-->", children_html)
        body_html = rewrite_internal_links(body_html, space_key, titles, valid_ids, path_prefix)
        meta_desc = generate_meta_description(p["adf"])
        faq_schema = build_faq_schema(body_html)

        nav_html = build_nav(pages_by_parent, space_key, titles, valid_ids, roots, p["id"], path_prefix)
        # url_path is the CLEAN path — used for the on-disk output location,
        # since GitHub Pages adds the /repo-name/ prefix automatically at
        # serving time and baking it into the file layout would double it up.
        url_path = page_url(p["id"], space_key, titles)
        # href_path is what actually gets written into the HTML as this
        # page's own canonical URL — it needs the prefix, since that's the
        # real, publicly reachable address.
        href_path = page_url(p["id"], space_key, titles, path_prefix)
        canonical_url = f"{base_url.rstrip('/')}{href_path}" if base_url else ""

        html_out = page_shell(
            title=p["title"],
            meta_description=meta_desc,
            nav_html=nav_html,
            page_count=len(pages),
            body_html=body_html,
            brand=brand,
            widget_html=widget_html,
            canonical_url=canonical_url,
            path_prefix=path_prefix,
            noindex=noindex,
            extra_head=faq_schema,
        )

        out_path = os.path.join(out_dir, url_path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w") as f:
            f.write(html_out)
        built.append((href_path, p["title"], bool(faq_schema)))

    return space_key, space_name, roots, titles, len(pages), built


def write_redirect(out_dir, target_url, title, brand):
    redirect_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={target_url}">
<link rel="canonical" href="{target_url}">
<title>{brand.get("name", "Docs")}</title>
</head>
<body>
<p>Redirecting to <a href="{target_url}">{html.escape(title, quote=False)}</a>…</p>
</body>
</html>
"""
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(redirect_html)


def write_space_picker(out_dir, spaces_info, brand, path_prefix=""):
    """Real landing page listing every configured space as a card, used once
    there's more than one — a single-space redirect no longer makes sense
    once there's an actual choice to present. This is the page that makes
    "platform" visible rather than implied."""
    cards = []
    for space_key, space_name, roots, titles, page_count in spaces_info:
        home = page_url(roots[0], space_key, titles, path_prefix) if roots else f"{path_prefix}/space/{space_key}/"
        cards.append(f"""
<a class="space-card" href="{home}">
  <div class="space-card-key">{space_key}</div>
  <h2>{html.escape(space_name, quote=False)}</h2>
  <p>{page_count} pages</p>
</a>""")
    body = f"""
<h1>{brand.get('name', 'Docs')}</h1>
<p class="space-picker-intro">{brand.get('tagline', '')}</p>
<div class="space-grid">{''.join(cards)}</div>
"""
    html_out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{brand.get("name", "Docs")}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{path_prefix}/styles.css">
</head>
<body>
<div class="shell shell-full"><main class="content content-full">{body}</main></div>
</body>
</html>
"""
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html_out)


def write_sitemap(out_dir, base_url, all_built):
    """Real sitemap.xml listing every page — helps Google discover and
    prioritize the new site efficiently, which matters more once the old
    Confluence-hosted copy stops being crawlable and this becomes the only
    source Google has to work from."""
    if not base_url:
        print("WARNING: no base_url configured — skipping sitemap.xml (canonical tags were also skipped).")
        return
    urls = "".join(
        f"<url><loc>{base_url.rstrip('/')}{url_path}</loc></url>"
        for url_path, _title, _has_schema in all_built
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urls}"
        "</urlset>"
    )
    with open(os.path.join(out_dir, "sitemap.xml"), "w") as f:
        f.write(sitemap)


def write_robots_txt(out_dir, base_url, path_prefix="", noindex=False):
    if noindex:
        # Trial mode: block everything. No point pointing crawlers at a
        # sitemap for content you don't want indexed — that's a mixed
        # signal, so no Sitemap: line here either.
        lines = ["User-agent: *", "Disallow: /"]
    else:
        # This is the site we WANT indexed, unlike the old Confluence-hosted
        # copy, which needs Anonymous Access turned off on the Confluence
        # side (not something this script can control) to stop being
        # crawlable at all.
        lines = ["User-agent: *", "Allow: /"]
        if base_url:
            lines.append(f"Sitemap: {base_url.rstrip('/')}{path_prefix}/sitemap.xml")
    with open(os.path.join(out_dir, "robots.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")


def clean_output_dir(out_dir):
    """Removes generated output from previous builds before writing new
    output. Without this, old artifacts never get cleaned up — every
    pipeline version's output just accumulates in the repo forever, since
    generate_site.py only ever writes new files, never deletes stale ones.

    This specifically targets:
      - the entire space/ tree (everything this pipeline generates lives there)
      - any *.html file sitting directly at the output root that ISN'T
        index.html — those are leftovers from the earlier flat-file naming
        scheme (overview.html, foxly-faq.html, etc.) that this version of
        the pipeline never writes and has no other way of knowing to remove.

    Deliberately does NOT touch scripts/, netlify/, data/, sites.json,
    styles.css, .github/, or anything else outside what this script owns.
    """
    space_dir = os.path.join(out_dir, "space")
    if os.path.isdir(space_dir):
        shutil.rmtree(space_dir)

    if os.path.isdir(out_dir):
        for name in os.listdir(out_dir):
            if name.endswith(".html") and name != "index.html":
                path = os.path.join(out_dir, name)
                if os.path.isfile(path):
                    os.remove(path)


def build_from_config(config_path=CONFIG_FILE, data_dir=DATA_DIR, out_dir=OUT_DIR):
    with open(config_path) as f:
        config = json.load(f)

    clean_output_dir(out_dir)

    brand = config.get("brand", {})
    base_url = config.get("base_url", "")
    path_prefix = config.get("path_prefix", "").rstrip("/")
    noindex = config.get("noindex", False)
    if noindex:
        print("noindex mode is ON — every page gets a noindex meta tag, robots.txt disallows everything, no sitemap.xml is written.")
    if path_prefix:
        print(f"path_prefix is set to '{path_prefix}' — every link/asset path will include this (GitHub Pages project-repo subpath mode).")
    spaces_cfg = config["spaces"]

    # Load every space's raw pages up front (before any rendering) so a
    # multiexcerpt-include can resolve a source excerpt regardless of which
    # space or page order it's defined in relative to where it's used.
    all_raw_pages = []
    space_data_paths = {}
    for space_cfg in spaces_cfg:
        space_key = space_cfg["space_key"]
        data_path = os.path.join(data_dir, space_key, "pages.json")
        if not os.path.exists(data_path):
            print(f"WARNING: {data_path} not found — has fetch_confluence.py run for this space yet? Skipping.")
            continue
        space_data_paths[space_key] = data_path
        with open(data_path) as f:
            space_data = json.load(f)
        all_raw_pages.extend(space_data.get("pages", []))

    multiexcerpt_registry = build_multiexcerpt_registry(all_raw_pages)

    all_built = []
    spaces_info = []
    for space_cfg in spaces_cfg:
        space_key = space_cfg["space_key"]
        data_path = space_data_paths.get(space_key)
        if not data_path:
            continue
        sk, space_name, roots, titles, page_count, built = build_space(
            data_path,
            out_dir,
            brand,
            base_url=base_url,
            path_prefix=path_prefix,
            jsm_project_key=space_cfg.get("jsm_project_key"),
            jsm_request_type_id=space_cfg.get("jsm_request_type_id"),
            noindex=noindex,
            multiexcerpt_registry=multiexcerpt_registry,
        )
        all_built.extend(built)
        spaces_info.append((sk, space_name, roots, titles, page_count))

    if len(spaces_info) == 1:
        sk, space_name, roots, titles, page_count = spaces_info[0]
        if roots:
            write_redirect(
                out_dir,
                page_url(roots[0], sk, titles, path_prefix),
                titles.get(roots[0], brand.get("name", "Docs")),
                brand,
            )
    elif len(spaces_info) > 1:
        write_space_picker(out_dir, spaces_info, brand, path_prefix)

    # all_built's paths already include path_prefix (built by build_space),
    # so base_url here must stay a BARE origin (no subpath) — combining
    # base_url + href_path gives the correct full public URL without
    # double-counting the prefix.
    if not noindex:
        write_sitemap(out_dir, base_url, all_built)
    write_robots_txt(out_dir, base_url, path_prefix, noindex=noindex)

    return all_built


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=CONFIG_FILE)
    parser.add_argument("--data-dir", default=DATA_DIR)
    parser.add_argument("--out", default=OUT_DIR)
    args = parser.parse_args()

    built = build_from_config(config_path=args.config, data_dir=args.data_dir, out_dir=args.out)
    print(f"Built {len(built)} pages total from {args.config}:")
    for url_path, title, has_schema in built:
        tag = " [+FAQPage schema]" if has_schema else ""
        print(f"  - {url_path}  ({title}){tag}")
