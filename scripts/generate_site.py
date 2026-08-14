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

import json
import os
import re
import sys
from urllib.parse import quote

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from adf_transform import adf_to_html, generate_meta_description

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
CONFIG_FILE = os.path.join(ROOT, "sites.json")
DATA_DIR = os.path.join(ROOT, "data")
OUT_DIR = ROOT

_WIDGET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "get_help_widget.html")
with open(_WIDGET_PATH) as _f:
    GET_HELP_WIDGET_TEMPLATE = _f.read()


def confluence_style_path_segment(title):
    """Mirrors Confluence's own URL style: spaces become a literal '+',
    other characters unsafe in a URL path get percent-encoded."""
    with_plus = (title or "untitled").replace(" ", "+")
    return quote(with_plus, safe="+()")


def page_url(page_id, space_key, titles):
    """Root-absolute URL for a page: /space/{KEY}/{pageId}/{Title+With+Plus}/"""
    title_segment = confluence_style_path_segment(titles.get(page_id, "untitled"))
    return f"/space/{space_key}/{page_id}/{title_segment}/"


NAV_SHELL_TEMPLATE = """
<div class="brand"><span class="brand-mark">{brand_name}</span></div>
<div class="brand-tag">{tagline}</div>
<p class="pilot-note">{count} pages in this space, fetched live from Confluence via API.</p>
<nav>{nav_items}</nav>
"""


def build_nav_tree(parent_id, pages_by_parent, space_key, titles, active_id, valid_ids, depth=0, max_depth=4):
    child_ids = [c for c in pages_by_parent.get(parent_id, []) if c in valid_ids]
    if not child_ids or depth > max_depth:
        return ""
    items = []
    for cid in child_ids:
        cls = ' class="active"' if cid == active_id else ""
        sub = build_nav_tree(cid, pages_by_parent, space_key, titles, active_id, valid_ids, depth + 1, max_depth)
        items.append(f'<li><a href="{page_url(cid, space_key, titles)}"{cls}>{titles[cid]}</a>{sub}</li>')
    return f"<ul>{''.join(items)}</ul>"


def build_nav(pages_by_parent, space_key, titles, valid_ids, roots, active_id):
    top_items = []
    for rid in roots:
        cls = ' class="active"' if rid == active_id else ""
        sub = build_nav_tree(rid, pages_by_parent, space_key, titles, active_id, valid_ids)
        top_items.append(f'<li><a href="{page_url(rid, space_key, titles)}"{cls}>{titles[rid]}</a>{sub}</li>')
    return f"<ul>{''.join(top_items)}</ul>"


def page_shell(title, meta_description, nav_html, page_count, body_html, brand, widget_html, extra_head=""):
    safe_desc = (meta_description or "").replace('"', "&quot;")
    nav_shell = NAV_SHELL_TEMPLATE.format(
        brand_name=brand.get("name", "Docs"),
        tagline=brand.get("tagline", "Live docs, fetched from Confluence via API."),
        count=page_count,
        nav_items=nav_html,
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} | {brand.get("name", "Docs")}</title>
<meta name="description" content="{safe_desc}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="/styles.css">
{extra_head}
</head>
<body>
<div class="shell">
  <main class="content">
    <h1>{title}</h1>
    {body_html}
  </main>
  <aside class="sidebar">{nav_shell}</aside>
</div>
{widget_html}
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


def rewrite_internal_links(body_html, space_key, titles, valid_ids):
    soup = BeautifulSoup(body_html, "html.parser")
    for a in soup.find_all("a", href=True):
        m = re.search(r"/pages/(\d+)", a["href"])
        if m and m.group(1) in valid_ids:
            a["href"] = page_url(m.group(1), space_key, titles)
    return str(soup)


def load_includes(pages):
    includes = {}
    for p in pages:
        if p["title"] and p["title"].startswith("_") and p.get("adf"):
            includes[p["title"]] = adf_to_html(p["adf"])
    return includes


def render_children_list(parent_id, pages_by_parent, space_key, titles, valid_ids, depth=2):
    children = [c for c in pages_by_parent.get(parent_id, []) if c in valid_ids]
    if not children:
        return ""
    items = []
    for child_id in children:
        title = titles.get(child_id, "Untitled")
        sub = ""
        if depth > 1:
            sub = render_children_list(child_id, pages_by_parent, space_key, titles, valid_ids, depth=depth - 1)
        items.append(f'<li><a href="{page_url(child_id, space_key, titles)}">{title}</a>{sub}</li>')
    if not items:
        return ""
    return f"<ul class='children-list'>{''.join(items)}</ul>"


def build_space(data_path, out_dir, brand, jsm_project_key=None, jsm_request_type_id=None):
    """Builds one space's pages. Returns (space_key, roots, titles, built_list) —
    the caller needs space_key/roots/titles to build the top-level home page
    once it knows about every space, not just this one."""
    with open(data_path) as f:
        data = json.load(f)

    space_key = data.get("space_key", "SPACE")

    pages = [p for p in data["pages"] if p.get("adf") and not (p["title"] or "").startswith("_")]
    titles = {p["id"]: p["title"] for p in pages}
    valid_ids = set(titles.keys())
    includes = load_includes(data["pages"])

    media_map = {k: f"/{v}" for k, v in data.get("media", {}).items()}

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
        )
        if "<!--CHILDREN_MACRO-->" in body_html:
            children_html = render_children_list(p["id"], pages_by_parent, space_key, titles, valid_ids)
            body_html = body_html.replace("<!--CHILDREN_MACRO-->", children_html)
        body_html = rewrite_internal_links(body_html, space_key, titles, valid_ids)
        meta_desc = generate_meta_description(p["adf"])
        faq_schema = build_faq_schema(body_html)

        nav_html = build_nav(pages_by_parent, space_key, titles, valid_ids, roots, p["id"])

        html_out = page_shell(
            title=p["title"],
            meta_description=meta_desc,
            nav_html=nav_html,
            page_count=len(pages),
            body_html=body_html,
            brand=brand,
            widget_html=widget_html,
            extra_head=faq_schema,
        )

        url_path = page_url(p["id"], space_key, titles)
        out_path = os.path.join(out_dir, url_path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w") as f:
            f.write(html_out)
        built.append((url_path, p["title"], bool(faq_schema)))

    return space_key, roots, titles, built


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
<p>Redirecting to <a href="{target_url}">{title}</a>…</p>
</body>
</html>
"""
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(redirect_html)


def write_space_picker(out_dir, spaces_info, brand):
    """Home page listing every configured space, used once there's more than
    one — a single-space redirect no longer makes sense when there's a real
    choice to present."""
    items = []
    for space_key, roots, titles in spaces_info:
        home = page_url(roots[0], space_key, titles) if roots else f"/space/{space_key}/"
        items.append(f'<li><a href="{home}"><strong>{space_key}</strong></a></li>')
    body = f"<h1>{brand.get('name', 'Docs')}</h1><ul>{''.join(items)}</ul>"
    html_out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{brand.get("name", "Docs")}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<div class="shell"><main class="content">{body}</main></div>
</body>
</html>
"""
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html_out)


def build_from_config(config_path=CONFIG_FILE, data_dir=DATA_DIR, out_dir=OUT_DIR):
    with open(config_path) as f:
        config = json.load(f)

    brand = config.get("brand", {})
    spaces_cfg = config["spaces"]

    all_built = []
    spaces_info = []
    for space_cfg in spaces_cfg:
        space_key = space_cfg["space_key"]
        data_path = os.path.join(data_dir, space_key, "pages.json")
        if not os.path.exists(data_path):
            print(f"WARNING: {data_path} not found — has fetch_confluence.py run for this space yet? Skipping.")
            continue
        sk, roots, titles, built = build_space(
            data_path,
            out_dir,
            brand,
            jsm_project_key=space_cfg.get("jsm_project_key"),
            jsm_request_type_id=space_cfg.get("jsm_request_type_id"),
        )
        all_built.extend(built)
        spaces_info.append((sk, roots, titles))

    if len(spaces_info) == 1:
        sk, roots, titles = spaces_info[0]
        if roots:
            write_redirect(out_dir, page_url(roots[0], sk, titles), titles.get(roots[0], brand.get("name", "Docs")), brand)
    elif len(spaces_info) > 1:
        write_space_picker(out_dir, spaces_info, brand)

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
