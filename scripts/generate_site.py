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
import traceback
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

_AURA_TABS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aura_tabs_widget.html")
with open(_AURA_TABS_PATH) as _f:
    AURA_TABS_SCRIPT = _f.read()

_COPY_CODE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "copy_code_widget.html")
with open(_COPY_CODE_PATH) as _f:
    COPY_CODE_SCRIPT = _f.read()

_SEARCH_SHORTCUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "search_shortcut_widget.html")
with open(_SEARCH_SHORTCUT_PATH) as _f:
    SEARCH_SHORTCUT_TEMPLATE = _f.read()

_PRODUCT_DIR_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates", "product_directory_template.html")
with open(_PRODUCT_DIR_TEMPLATE_PATH) as _f:
    PRODUCT_DIRECTORY_TEMPLATE = _f.read()


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


TOP_NAV_TEMPLATE = """
<header class="top-nav">
  <div class="top-nav-inner">
    <a class="top-nav-brand" href="{path_prefix}/">{brand_name}</a>
    <nav class="top-nav-links">
      <a href="{path_prefix}/product-directory/">Product directory</a>
      <a href="{path_prefix}/search/">Search <kbd>⌘K</kbd></a>
    </nav>
  </div>
</header>
"""


NAV_SHELL_TEMPLATE = """
<div class="brand"><span class="brand-mark">{brand_name}</span></div>
<div class="brand-tag">{tagline}</div>
<p class="pilot-note">{count} pages in this space, fetched live from Confluence via API.</p>
<nav>{nav_items}</nav>
"""


def build_ancestors(active_id, parent_of):
    """Walks upward from the active page through parent_id links, returning
    the set of every ancestor's ID (not including active_id itself). Used
    to decide which nav branches should be force-expanded by default —
    only the path to the current page, not every branch in the space."""
    ancestors = set()
    current = active_id
    seen = set()  # guards against a malformed/cyclic parent_id chain
    while current in parent_of and current not in seen:
        seen.add(current)
        current = parent_of[current]
        if current:
            ancestors.add(current)
    return ancestors


def build_nav_tree(parent_id, pages_by_parent, space_key, titles, active_id, valid_ids, ancestors, path_prefix="", depth=0, max_depth=6):
    child_ids = [c for c in pages_by_parent.get(parent_id, []) if c in valid_ids]
    if not child_ids or depth > max_depth:
        return ""
    items = []
    for cid in child_ids:
        cls = ' class="active"' if cid == active_id else ""
        sub = build_nav_tree(cid, pages_by_parent, space_key, titles, active_id, valid_ids, ancestors, path_prefix, depth + 1, max_depth)
        label = f'<a href="{page_url(cid, space_key, titles, path_prefix)}"{cls}>{html.escape(titles[cid], quote=False)}</a>'
        if sub:
            # A branch with children becomes a native <details> disclosure —
            # zero JS needed, and it degrades gracefully if JS is ever off.
            # Only open by default if this branch is on the path to the
            # active page; every other branch starts collapsed, which is
            # what actually makes a 1,000+ page space usable instead of
            # rendering every single page's nav link on every page load.
            open_attr = " open" if (cid in ancestors or cid == active_id) else ""
            items.append(f"<li><details{open_attr}><summary>{label}</summary>{sub}</details></li>")
        else:
            items.append(f"<li>{label}</li>")
    return f"<ul>{''.join(items)}</ul>"


def build_nav(pages_by_parent, space_key, titles, valid_ids, roots, active_id, path_prefix="", ancestors=None):
    ancestors = ancestors or set()
    top_items = []
    for rid in roots:
        cls = ' class="active"' if rid == active_id else ""
        sub = build_nav_tree(rid, pages_by_parent, space_key, titles, active_id, valid_ids, ancestors, path_prefix)
        label = f'<a href="{page_url(rid, space_key, titles, path_prefix)}"{cls}>{html.escape(titles[rid], quote=False)}</a>'
        if sub:
            open_attr = " open" if (rid in ancestors or rid == active_id) else ""
            top_items.append(f"<li><details{open_attr}><summary>{label}</summary>{sub}</details></li>")
        else:
            top_items.append(f"<li>{label}</li>")
    return f"<ul>{''.join(top_items)}</ul>"


def render_top_nav(brand, path_prefix=""):
    return TOP_NAV_TEMPLATE.format(
        brand_name=html.escape(brand.get("name", "Docs"), quote=False),
        path_prefix=path_prefix,
    )


def render_page_toc_panel(headings):
    """Real, always-present 'On this page' panel built from the page's
    actual headings — unlike the inline {toc} macro (which only appears
    if the Confluence author happened to insert one), this shows up on
    every page that has any headings at all, matching the real site's
    persistent right-rail TOC."""
    if not headings:
        return ""
    items = "".join(
        f'<li class="toc-level-{h["level"]}"><a href="#{h["id"]}">{html.escape(h["text"], quote=False)}</a></li>'
        for h in headings
    )
    return f'<div class="page-toc"><div class="page-toc-title">On this page</div><ul>{items}</ul></div>'


def render_breadcrumb(active_id, parent_of, titles, space_key, space_name, space_home_url, path_prefix=""):
    """Root-to-current breadcrumb trail (Space > Ancestor > ... > Current
    Page), reusing the same parent_of walk-up used for the collapsible
    nav's ancestor detection — just presented linearly instead of as a
    tree. A gap flagged early in this project, now cheap to build since
    the underlying ancestor-chain logic already exists."""
    chain = []
    current = active_id
    seen = set()
    while current and current not in seen:
        seen.add(current)
        chain.append(current)
        current = parent_of.get(current)
    chain.reverse()  # walk-up gives leaf-to-root; breadcrumb needs root-to-leaf

    parts = []
    if space_home_url:
        parts.append(f'<a href="{space_home_url}">{html.escape(space_name, quote=False)}</a>')
    else:
        parts.append(html.escape(space_name, quote=False))

    for i, pid in enumerate(chain):
        title = html.escape(titles.get(pid, "Untitled"), quote=False)
        if i == len(chain) - 1:
            parts.append(f'<span aria-current="page">{title}</span>')  # current page — not a link
        else:
            parts.append(f'<a href="{page_url(pid, space_key, titles, path_prefix)}">{title}</a>')

    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + ' <span class="breadcrumb-sep">/</span> '.join(parts) + '</nav>'


def estimate_reading_time(body_html):
    """Standard 200 words/minute estimate, computed from the page's actual
    rendered text — free, since we already strip HTML for the search
    snippet elsewhere; this just does the same extraction for a different
    purpose."""
    text = BeautifulSoup(body_html, "html.parser").get_text(" ", strip=True)
    word_count = len(text.split())
    minutes = max(1, round(word_count / 200))
    return f"{minutes} min read"


def page_shell(title, meta_description, nav_html, page_count, body_html, brand, widget_html, canonical_url, path_prefix="", noindex=False, extra_head="", toc_html="", breadcrumb_html="", reading_time="", confluence_edit_url=""):
    safe_title = html.escape(title or "", quote=False)
    safe_brand_name = html.escape(brand.get("name", "Docs"), quote=False)
    safe_desc = html.escape(meta_description or "", quote=True)
    nav_shell = NAV_SHELL_TEMPLATE.format(
        brand_name=safe_brand_name,
        tagline=html.escape(brand.get("tagline", "Live docs, fetched from Confluence via API."), quote=False),
        count=page_count,
        nav_items=nav_html,
        path_prefix=path_prefix,
    )
    top_nav = render_top_nav(brand, path_prefix)
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
<div id="top-nav-mount">{top_nav}</div>
<div class="shell">
  <main class="content">
    <div class="page-actions-row">
      {breadcrumb_html}
      {'<a class="open-in-confluence" href="' + confluence_edit_url + '" target="_blank" rel="noopener">Open in Confluence</a>' if confluence_edit_url else ''}
    </div>
    <h1>{safe_title}</h1>
    <div class="page-meta">{reading_time}</div>
    {body_html}
  </main>
  <aside class="sidebar">{nav_shell}</aside>
  <aside class="page-toc-rail">{toc_html}</aside>
</div>
{widget_html}
{ADVANCED_TABLES_SCRIPT}
{AURA_TABS_SCRIPT}
{COPY_CODE_SCRIPT}
{SEARCH_SHORTCUT_TEMPLATE.replace("__SEARCH_URL__", path_prefix + "/search/")}
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
            html_str, _headings = adf_to_html(p["adf"])
            includes[p["title"]] = html_str
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


def build_space(data_path, out_dir, brand, base_url="", path_prefix="", support_portal_url=None, noindex=False, multiexcerpt_registry=None, confluence_site=""):
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
    parent_of = {}
    for p in data["pages"]:
        parent = p.get("parent_id")
        if parent:
            pages_by_parent.setdefault(parent, []).append(p["id"])
            parent_of[p["id"]] = parent

    roots = [
        p["id"] for p in data["pages"]
        if p["id"] in valid_ids and (p.get("parent_id") not in valid_ids)
    ]

    widget_html = GET_HELP_WIDGET_TEMPLATE.replace(
        "__SUPPORT_PORTAL_URL__",
        html.escape(support_portal_url or "https://support.appfire.com/page/support", quote=True),
    )

    built = []
    for p in pages:
        # url_path is the CLEAN path — used for the on-disk output location,
        # since GitHub Pages adds the /repo-name/ prefix automatically at
        # serving time and baking it into the file layout would double it up.
        url_path = page_url(p["id"], space_key, titles)
        # href_path is what actually gets written into the HTML as this
        # page's own canonical URL — it needs the prefix, since that's the
        # real, publicly reachable address.
        href_path = page_url(p["id"], space_key, titles, path_prefix)
        out_path = os.path.join(out_dir, url_path.strip("/"), "index.html")

        try:
            body_html, page_headings = adf_to_html(
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

            ancestors = build_ancestors(p["id"], parent_of)
            nav_html = build_nav(pages_by_parent, space_key, titles, valid_ids, roots, p["id"], path_prefix, ancestors)
            canonical_url = f"{base_url.rstrip('/')}{href_path}" if base_url else ""
            space_home_url = page_url(roots[0], space_key, titles, path_prefix) if roots else ""
            breadcrumb_html = render_breadcrumb(p["id"], parent_of, titles, space_key, space_name, space_home_url, path_prefix)
            confluence_edit_url = f"https://{confluence_site}/wiki/spaces/{space_key}/pages/{p['id']}" if confluence_site else ""

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
                toc_html=render_page_toc_panel(page_headings),
                breadcrumb_html=breadcrumb_html,
                reading_time=estimate_reading_time(body_html),
                confluence_edit_url=confluence_edit_url,
            )
            has_schema = bool(faq_schema)
            snippet = BeautifulSoup(body_html, "html.parser").get_text(" ", strip=True)[:200]
        except Exception as e:
            # A single page's rendering bug used to crash the ENTIRE
            # multi-space build — confirmed the hard way when one Aura
            # Button on one page in one of 18 spaces took down the whole
            # site after a long, otherwise-successful fetch. That's no
            # longer acceptable: this page becomes a clearly-labeled error
            # page instead, and every other page — this space's and every
            # other space's — still builds normally.
            print(
                f"ERROR: page '{p.get('title', '?')}' (id={p.get('id', '?')}) in space "
                f"{space_key} failed to render — writing an error placeholder instead of "
                f"crashing the whole build.\n{traceback.format_exc()}",
                file=sys.stderr,
            )
            safe_title = html.escape(p.get("title", "Untitled"), quote=False)
            html_out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{safe_title} | {html.escape(brand.get("name", "Docs"), quote=False)}</title>
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="{path_prefix}/styles.css">
</head>
<body>
<div class="shell">
  <main class="content">
    <h1>{safe_title}</h1>
    <div class="img-placeholder">[This page failed to build — {html.escape(str(e), quote=False)}. Everything else on the site built normally; this one page needs a fix.]</div>
  </main>
</div>
</body>
</html>
"""
            has_schema = False
            snippet = "This page failed to build."
            page_headings = []

        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w") as f:
            f.write(html_out)
        built.append((href_path, p["title"], has_schema, space_key, space_name, snippet))

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


_MONTH_NAMES = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
}


def find_recent_release_notes(all_built, limit=12):
    """Detects release-notes-style pages by title pattern across every
    space, parses a real (month, year) out of the title text itself where
    possible (e.g. "Release notes April 2025"), and returns the most
    recent ones sorted chronologically — without needing any new fetch
    data, since the date is already sitting in the title as text. Falls
    back to placing undated matches at the end rather than guessing."""
    pattern = re.compile(r"\b(" + "|".join(_MONTH_NAMES.keys()) + r")\s+(\d{4})\b", re.IGNORECASE)
    candidates = []
    for url_path, title, _has_schema, space_key, space_name, _snippet in all_built:
        if "release notes" not in title.lower():
            continue
        match = pattern.search(title)
        if match:
            month_num = _MONTH_NAMES[match.group(1).lower()]
            year_num = int(match.group(2))
            sort_key = (year_num, month_num)
        else:
            sort_key = (0, 0)  # undated matches sort to the end, not guessed at
        candidates.append((sort_key, title, url_path, space_key, space_name))

    candidates.sort(key=lambda c: c[0], reverse=True)
    return candidates[:limit]


def render_whats_new_section(all_built, path_prefix=""):
    entries = find_recent_release_notes(all_built)
    if not entries:
        return ""
    items = "".join(
        f'<a class="whats-new-item" href="{url_path}">'
        f'<span class="whats-new-space">{html.escape(space_name, quote=False)}</span>'
        f'<span class="whats-new-title">{html.escape(title, quote=False)}</span>'
        f"</a>"
        for _sort_key, title, url_path, space_key, space_name in entries
    )
    return f'<section class="whats-new"><h2>What\'s New Across Appfire Products</h2><div class="whats-new-list">{items}</div></section>'


def write_space_picker(out_dir, spaces_info, brand, path_prefix="", base_url="", noindex=False, all_built=None):
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
    top_nav = render_top_nav(brand, path_prefix)
    whats_new_html = render_whats_new_section(all_built or [], path_prefix)
    body = f"""
<section class="hero">
  <h1>{brand.get('name', 'Docs')}</h1>
  <p class="hero-subtitle">{brand.get('tagline', '')}</p>
  <form class="hero-search" action="{path_prefix}/search/" method="get">
    <input type="search" name="q" placeholder="Search Appfire products...">
    <button type="submit">Search</button>
  </form>
</section>
<div class="picker-body">
{whats_new_html}
<a class="product-directory-cta" href="{path_prefix}/product-directory/">Browse the full Appfire app directory →</a>
<div class="space-grid">{''.join(cards)}</div>
</div>
"""
    # Same noindex/canonical handling as every other page on the site — this
    # was missing here specifically, a real gap given this page lists every
    # real product name and would otherwise be the one page NOT protected
    # during the trial phase while everything else correctly was.
    if noindex:
        extra_head = '<meta name="robots" content="noindex, nofollow">'
    elif base_url:
        extra_head = f'<link rel="canonical" href="{base_url.rstrip("/")}{path_prefix}/">'
    else:
        extra_head = ""

    html_out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{brand.get("name", "Docs")}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{path_prefix}/styles.css">
{extra_head}
</head>
<body>
{top_nav}
<div class="shell shell-full"><main class="content content-full">{body}</main></div>
</body>
</html>
"""
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html_out)


def write_product_directory(out_dir, spaces_info, brand, path_prefix="", base_url="", noindex=False):
    """Writes the app directory page (originally a standalone Refined-hosted
    page) at /product-directory/. The one real enhancement over the
    original: apps whose space has actually been migrated to this pipeline
    route to their real new URL here instead of the old
    support.appfire.com — computed fresh at build time from real data, so
    it stays accurate automatically as more spaces get added rather than
    needing this file hand-edited each time."""
    local_spaces = {}
    for space_key, space_name, roots, titles, page_count in spaces_info:
        if roots:
            local_spaces[space_key] = page_url(roots[0], space_key, titles, path_prefix)

    html_out = PRODUCT_DIRECTORY_TEMPLATE.replace(
        "__LOCAL_SPACES_JSON__", json.dumps(local_spaces)
    )
    html_out = html_out.replace("<body>", f"<body>\n{render_top_nav(brand, path_prefix)}", 1)

    if noindex:
        html_out = html_out.replace(
            "<head>",
            '<head>\n<meta name="robots" content="noindex, nofollow">',
            1,
        )
    elif base_url:
        canonical = f"{base_url.rstrip('/')}{path_prefix}/product-directory/"
        html_out = html_out.replace(
            "<head>",
            f'<head>\n<link rel="canonical" href="{canonical}">',
            1,
        )

    out_path = os.path.join(out_dir, "product-directory", "index.html")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(html_out)


def write_search_index(out_dir, all_built):
    """A lightweight JSON index of every real page — title, url, space,
    snippet — searched entirely client-side in the browser. This is real,
    working search, not a copy of Refined's: that page's actual
    functionality depends on Refined's own proprietary AI backend and an
    authenticated Confluence session, neither of which exists outside
    Refined's own infrastructure. This is a genuinely different, simpler
    mechanism (client-side substring matching), styled to look similar."""
    index = [
        {"title": title, "url": url_path, "space_key": space_key, "space_name": space_name, "snippet": snippet}
        for url_path, title, _has_schema, space_key, space_name, snippet in all_built
    ]
    with open(os.path.join(out_dir, "search-index.json"), "w") as f:
        json.dump(index, f)


def write_search_page(out_dir, brand, path_prefix=""):
    """Real, working search — client-side, built from search-index.json.
    Styled to resemble the real site's search page (platform-style filter
    checkboxes, "Showing X of Y results", highlighted match terms, result
    cards with a space badge) without depending on anything Refined-specific."""
    top_nav = render_top_nav(brand, path_prefix)
    html_out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Search | {html.escape(brand.get("name", "Docs"), quote=False)}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{path_prefix}/styles.css">
</head>
<body>
{top_nav}
<div class="shell shell-full">
<main class="content content-full">
<h1>Search {html.escape(brand.get("name", "Docs"), quote=False)}</h1>
<form id="search-form" class="search-bar">
  <input type="search" id="search-input" placeholder="Search by title or content...">
</form>
<div class="search-layout">
  <aside class="search-filters">
    <div class="search-filters-title">SPACE</div>
    <div id="space-filter-list"></div>
  </aside>
  <div class="search-results-area">
    <p id="search-count" class="search-count"></p>
    <div id="search-results"></div>
  </div>
</div>
</main>
</div>
<script>
(function () {{
  var INDEX_URL = "{path_prefix}/search-index.json";
  var input = document.getElementById("search-input");
  var resultsEl = document.getElementById("search-results");
  var countEl = document.getElementById("search-count");
  var spaceFilterList = document.getElementById("space-filter-list");
  var allPages = [];
  var activeSpaces = {{}};

  function highlight(text, term) {{
    if (!term) return escapeHtml(text);
    var idx = text.toLowerCase().indexOf(term.toLowerCase());
    if (idx === -1) return escapeHtml(text);
    return escapeHtml(text.slice(0, idx)) + "<mark>" + escapeHtml(text.slice(idx, idx + term.length)) + "</mark>" + escapeHtml(text.slice(idx + term.length));
  }}
  function escapeHtml(s) {{
    var div = document.createElement("div");
    div.textContent = s;
    return div.innerHTML;
  }}

  function render() {{
    var term = input.value.trim();
    var anySpaceFilterActive = Object.keys(activeSpaces).some(function (k) {{ return activeSpaces[k]; }});
    var matches = allPages.filter(function (p) {{
      var matchesTerm = !term || p.title.toLowerCase().indexOf(term.toLowerCase()) !== -1 || p.snippet.toLowerCase().indexOf(term.toLowerCase()) !== -1;
      var matchesSpace = !anySpaceFilterActive || activeSpaces[p.space_key];
      return matchesTerm && matchesSpace;
    }});
    countEl.textContent = "Showing " + Math.min(matches.length, 50) + " of " + matches.length + " results";
    resultsEl.innerHTML = matches.slice(0, 50).map(function (p) {{
      return '<a class="search-result-card" href="' + p.url + '">' +
        '<h3>' + highlight(p.title, term) + '</h3>' +
        '<p>' + highlight(p.snippet, term) + '</p>' +
        '<span class="search-result-badge">' + escapeHtml(p.space_name) + '</span>' +
        '</a>';
    }}).join("");
  }}

  function buildSpaceFilters() {{
    var spaces = {{}};
    allPages.forEach(function (p) {{ spaces[p.space_key] = p.space_name; }});
    spaceFilterList.innerHTML = Object.keys(spaces).sort().map(function (key) {{
      return '<label class="search-filter-checkbox"><input type="checkbox" data-space="' + key + '"> ' + escapeHtml(spaces[key]) + '</label>';
    }}).join("");
    spaceFilterList.querySelectorAll("input[type=checkbox]").forEach(function (cb) {{
      cb.addEventListener("change", function () {{
        activeSpaces[cb.dataset.space] = cb.checked;
        render();
      }});
    }});
  }}

  fetch(INDEX_URL)
    .then(function (r) {{ return r.json(); }})
    .then(function (data) {{
      allPages = data;
      buildSpaceFilters();
      var params = new URLSearchParams(window.location.search);
      var q = params.get("q");
      if (q) input.value = q;
      render();
    }});

  input.addEventListener("input", render);
  document.getElementById("search-form").addEventListener("submit", function (e) {{ e.preventDefault(); }});
}})();
</script>
</body>
</html>
"""
    out_path = os.path.join(out_dir, "search", "index.html")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
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
        for url_path, _title, _has_schema, _space_key, _space_name, _snippet in all_built
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
    confluence_site = config.get("confluence_site", "")
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
            support_portal_url=space_cfg.get("support_portal_url"),
            noindex=noindex,
            multiexcerpt_registry=multiexcerpt_registry,
            confluence_site=confluence_site,
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
        write_space_picker(out_dir, spaces_info, brand, path_prefix, base_url, noindex, all_built)

    write_product_directory(out_dir, spaces_info, brand, path_prefix, base_url, noindex)

    # all_built's paths already include path_prefix (built by build_space),
    # so base_url here must stay a BARE origin (no subpath) — combining
    # base_url + href_path gives the correct full public URL without
    # double-counting the prefix.
    if not noindex:
        write_sitemap(out_dir, base_url, all_built)
    write_robots_txt(out_dir, base_url, path_prefix, noindex=noindex)
    write_search_index(out_dir, all_built)
    write_search_page(out_dir, brand, path_prefix)

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
    for url_path, title, has_schema, _space_key, _space_name, _snippet in built:
        tag = " [+FAQPage schema]" if has_schema else ""
        print(f"  - {url_path}  ({title}){tag}")
