#!/usr/bin/env python3
"""
generate_site.py (v2) — builds the static site from data/pages.json, which
fetch_confluence.py produces from a live Confluence API call. This script
has no knowledge of any specific page's content — swap the space and rerun
the fetch, and this same code builds a different site.
"""

import json
import os
import re
import sys

from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from adf_transform import adf_to_html, generate_meta_description

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
DATA_FILE = os.path.join(ROOT, "data", "pages.json")
OUT_DIR = ROOT


def slugify(title):
    slug = (title or "untitled").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug or "untitled"


NAV_SHELL_TEMPLATE = """
<div class="brand"><span class="brand-mark">Foxly</span></div>
<div class="brand-tag">Docs — Live Pilot</div>
<p class="pilot-note">{count} pages, fetched live from Confluence via API.</p>
<nav>{nav_items}</nav>
"""


def build_nav_tree(parent_id, pages_by_parent, slugs, titles, active_id, valid_ids, depth=0, max_depth=4):
    """Build nested <ul> nav matching the real Confluence page hierarchy,
    instead of one flat list of every page. Stops nesting past max_depth as
    a safety valve — the real tree here only goes 2-3 levels deep anyway."""
    child_ids = [c for c in pages_by_parent.get(parent_id, []) if c in valid_ids]
    if not child_ids or depth > max_depth:
        return ""
    items = []
    for cid in child_ids:
        cls = ' class="active"' if cid == active_id else ""
        sub = build_nav_tree(cid, pages_by_parent, slugs, titles, active_id, valid_ids, depth + 1, max_depth)
        items.append(f'<li><a href="{slugs[cid]}.html"{cls}>{titles[cid]}</a>{sub}</li>')
    return f"<ul>{''.join(items)}</ul>"


def build_nav(pages_by_parent, slugs, titles, valid_ids, roots, active_id):
    top_items = []
    for rid in roots:
        cls = ' class="active"' if rid == active_id else ""
        sub = build_nav_tree(rid, pages_by_parent, slugs, titles, active_id, valid_ids)
        top_items.append(f'<li><a href="{slugs[rid]}.html"{cls}>{titles[rid]}</a>{sub}</li>')
    return f"<ul>{''.join(top_items)}</ul>"


def page_shell(title, meta_description, nav_html, page_count, body_html, extra_head=""):
    safe_desc = (meta_description or "").replace('"', "&quot;")
    nav_shell = NAV_SHELL_TEMPLATE.format(count=page_count, nav_items=nav_html)
    # Main content comes BEFORE the sidebar in the HTML source — a crawler or
    # someone reading View Source sees the actual article first, not 40+
    # lines of nav links. CSS `order` puts the sidebar back on the left
    # visually; nothing changes for a human looking at the rendered page.
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} | Foxly Docs</title>
<meta name="description" content="{safe_desc}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="styles.css">
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


def rewrite_internal_links(body_html, slugs):
    soup = BeautifulSoup(body_html, "html.parser")
    for a in soup.find_all("a", href=True):
        m = re.search(r"/pages/(\d+)", a["href"])
        if m and m.group(1) in slugs:
            a["href"] = f"{slugs[m.group(1)]}.html"
    return str(soup)


def load_includes(pages):
    """Pages whose title starts with '_' are treated as transclusion targets (e.g. _Footer)."""
    includes = {}
    for p in pages:
        if p["title"] and p["title"].startswith("_") and p.get("adf"):
            includes[p["title"]] = adf_to_html(p["adf"])
    return includes


def render_children_list(parent_id, pages_by_parent, slugs, titles, depth=2):
    """Real replacement for Confluence's 'children' macro, built from the actual
    page tree instead of leaving an 'unmapped macro' box — we have this data anyway."""
    children = pages_by_parent.get(parent_id, [])
    if not children:
        return ""
    items = []
    for child_id in children:
        slug = slugs.get(child_id)
        title = titles.get(child_id, "Untitled")
        if not slug:
            continue
        sub = ""
        if depth > 1:
            sub = render_children_list(child_id, pages_by_parent, slugs, titles, depth=depth - 1)
        items.append(f'<li><a href="{slug}.html">{title}</a>{sub}</li>')
    if not items:
        return ""
    return f"<ul class='children-list'>{''.join(items)}</ul>"


def build_all(data_path=DATA_FILE, out_dir=OUT_DIR):
    with open(data_path) as f:
        data = json.load(f)

    pages = [p for p in data["pages"] if p.get("adf") and not (p["title"] or "").startswith("_")]
    pages_by_id = {p["id"]: p for p in pages}
    slugs = {p["id"]: slugify(p["title"]) for p in pages}
    titles = {p["id"]: p["title"] for p in pages}
    includes = load_includes(data["pages"])

    pages_by_parent = {}
    for p in data["pages"]:
        parent = p.get("parent_id")
        if parent:
            pages_by_parent.setdefault(parent, []).append(p["id"])

    valid_ids = set(slugs.keys())
    # Roots = pages with no parent, or whose parent wasn't fetched (orphans
    # still need a way into the nav rather than becoming unreachable).
    roots = [
        p["id"] for p in data["pages"]
        if p["id"] in valid_ids and (p.get("parent_id") not in valid_ids)
    ]

    built = []
    for p in pages:
        body_html = adf_to_html(
            p["adf"],
            unresolved_includes=includes,
            link_titles=titles,
            media_map=data.get("media", {}),
        )
        if "<!--CHILDREN_MACRO-->" in body_html:
            children_html = render_children_list(p["id"], pages_by_parent, slugs, titles)
            body_html = body_html.replace("<!--CHILDREN_MACRO-->", children_html)
        body_html = rewrite_internal_links(body_html, slugs)
        meta_desc = generate_meta_description(p["adf"])
        faq_schema = build_faq_schema(body_html)

        nav_html = build_nav(pages_by_parent, slugs, titles, valid_ids, roots, p["id"])

        html_out = page_shell(
            title=p["title"],
            meta_description=meta_desc,
            nav_html=nav_html,
            page_count=len(pages),
            body_html=body_html,
            extra_head=faq_schema,
        )

        slug = slugs[p["id"]]
        out_path = os.path.join(out_dir, f"{slug}.html")
        with open(out_path, "w") as f:
            f.write(html_out)
        built.append((slug, p["title"], bool(faq_schema)))

    return built


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=DATA_FILE)
    parser.add_argument("--out", default=OUT_DIR)
    args = parser.parse_args()

    built = build_all(data_path=args.data, out_dir=args.out)
    print(f"Built {len(built)} pages from {args.data}:")
    for slug, title, has_schema in built:
        tag = " [+FAQPage schema]" if has_schema else ""
        print(f"  - {slug}.html  ({title}){tag}")
