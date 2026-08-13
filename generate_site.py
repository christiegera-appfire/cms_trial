#!/usr/bin/env python3
"""
generate_site.py — the actual pipeline.

Loop over pages -> call transform_body() on the raw API HTML -> write output.
No page's content is ever hand-typed here. Swap raw_pages.PAGES for a live
call to Atlassian:getConfluencePage (looped over getPagesInConfluenceSpace's
results) and this script is the real thing, not a demo of it.
"""

import os
import re
import json
from bs4 import BeautifulSoup

from transform import transform_body, generate_meta_description
from raw_pages import PAGES, INCLUDES

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def slugify(title):
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug


# Build id -> slug map once, so internal links / nav can reference pages consistently.
SLUGS = {pid: slugify(page["title"]) for pid, page in PAGES.items()}

NAV_TREE_TEMPLATE = """
<div class="brand">
  <span class="brand-mark">Foxly</span>
</div>
<div class="brand-tag">Docs — Static Pilot</div>
<p class="pilot-note">{built_count} of 52 pages built for this proof of concept. Rendered live from the transformer, not hand-copied.</p>
<nav>
  <ul>
    {nav_items}
  </ul>
</nav>
"""


def build_nav(active_id):
    items = []
    for pid, page in PAGES.items():
        slug = SLUGS[pid]
        cls = ' class="active"' if pid == active_id else ""
        items.append(f'<li><a href="{slug}.html"{cls}>{page["title"]}</a></li>')
    items.append('<div class="more-note">+ 49 more FOX pages not built in this pilot</div>')
    return "\n    ".join(items)


def page_shell(title, meta_description, active_id, body_html, extra_head=""):
    nav_html = NAV_TREE_TEMPLATE.format(
        built_count=len(PAGES),
        nav_items=build_nav(active_id),
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} | Foxly Docs</title>
<meta name="description" content="{meta_description}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="styles.css">
{extra_head}
</head>
<body>
<div class="shell">
  <aside class="sidebar">
    {nav_html}
  </aside>
  <main class="content">
    <h1>{title}</h1>
    {body_html}
  </main>
</div>
</body>
</html>
"""


def build_faq_schema(body_html):
    """If a page is made entirely of <details>/<summary> blocks, emit FAQPage JSON-LD automatically."""
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


def rewrite_internal_links(body_html):
    """Rewrite links pointing at Confluence page IDs to the static site's own slugs, where we have them."""
    soup = BeautifulSoup(body_html, "html.parser")
    for a in soup.find_all("a", href=True):
        m = re.search(r"/pages/(\d+)", a["href"])
        if m and m.group(1) in SLUGS:
            a["href"] = f"{SLUGS[m.group(1)]}.html"
    return str(soup)


def build_all():
    built = []
    for pid, page in PAGES.items():
        transformed = transform_body(page["body"], unresolved_includes=INCLUDES)
        transformed = rewrite_internal_links(transformed)
        meta_desc = generate_meta_description(transformed)
        faq_schema = build_faq_schema(transformed)

        html = page_shell(
            title=page["title"],
            meta_description=meta_desc,
            active_id=pid,
            body_html=transformed,
            extra_head=faq_schema,
        )

        slug = SLUGS[pid]
        out_path = os.path.join(OUT_DIR, f"{slug}.html")
        with open(out_path, "w") as f:
            f.write(html)
        built.append((slug, page["title"], bool(faq_schema)))

    return built


if __name__ == "__main__":
    built = build_all()
    print(f"Built {len(built)} pages via the generic transformer:")
    for slug, title, has_schema in built:
        tag = " [+FAQPage schema auto-detected]" if has_schema else ""
        print(f"  - {slug}.html  ({title}){tag}")
