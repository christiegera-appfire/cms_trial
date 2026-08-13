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


NAV_TREE_TEMPLATE = """
<div class="brand"><span class="brand-mark">Foxly</span></div>
<div class="brand-tag">Docs — Live Pilot</div>
<p class="pilot-note">{count} pages, fetched live from Confluence via API.</p>
<nav><ul>
    {nav_items}
</ul></nav>
"""


def build_nav(pages_by_id, slugs, active_id):
    items = []
    for pid, page in pages_by_id.items():
        cls = ' class="active"' if pid == active_id else ""
        items.append(f'<li><a href="{slugs[pid]}.html"{cls}>{page["title"]}</a></li>')
    return "\n    ".join(items)


def page_shell(title, meta_description, active_id, pages_by_id, slugs, body_html, extra_head=""):
    nav_html = NAV_TREE_TEMPLATE.format(
        count=len(pages_by_id),
        nav_items=build_nav(pages_by_id, slugs, active_id),
    )
    safe_desc = (meta_description or "").replace('"', "&quot;")
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
  <aside class="sidebar">{nav_html}</aside>
  <main class="content">
    <h1>{title}</h1>
    {body_html}
  </main>
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


def build_all(data_path=DATA_FILE, out_dir=OUT_DIR):
    with open(data_path) as f:
        data = json.load(f)

    pages = [p for p in data["pages"] if p.get("adf") and not (p["title"] or "").startswith("_")]
    pages_by_id = {p["id"]: p for p in pages}
    slugs = {p["id"]: slugify(p["title"]) for p in pages}
    includes = load_includes(data["pages"])

    built = []
    for p in pages:
        body_html = adf_to_html(p["adf"], unresolved_includes=includes)
        body_html = rewrite_internal_links(body_html, slugs)
        meta_desc = generate_meta_description(p["adf"])
        faq_schema = build_faq_schema(body_html)

        html_out = page_shell(
            title=p["title"],
            meta_description=meta_desc,
            active_id=p["id"],
            pages_by_id=pages_by_id,
            slugs=slugs,
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
