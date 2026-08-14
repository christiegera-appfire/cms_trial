#!/usr/bin/env python3
"""
adf_transform.py — converts ADF (Atlassian Document Format) JSON, as returned
by Confluence's real REST API v2 (GET /wiki/api/v2/pages/{id}?body-format=atlas_doc_format),
into clean static HTML.

v3 changes: real TOC macro support (built from the page's own headings, since
we control the whole render pass — no need for a dynamic macro when the data
is right there), Page Properties macro rendering, and a generic fallback for
unmapped *bodied* macros: if a macro we haven't explicitly mapped has real
content inside it, render that content instead of hiding it behind an
"unmapped" box. Most Confluence macros are wrappers around ordinary content
(excerpts, layout helpers, etc.) — rendering the body is usually the right
approximation of "what's actually in Confluence," which is the actual goal
here, not a fully faithful macro engine.

ADF reference: https://developer.atlassian.com/cloud/confluence/adf/

Design choice carried over from earlier versions: truly unknown, content-free
node types still render a visible marker instead of silently vanishing.
Content that quietly disappears during extraction is exactly what broke the
Get Started page audit's markdown-based approach — this pipeline deliberately
fails loud, except for the specific macros in SILENT_MACROS known to have no
visual output at all.
"""

import datetime
import html
import json
import re


MARK_TAGS = {
    "strong": "strong",
    "em": "em",
    "code": "code",
    "strike": "s",
    "underline": "u",
}

PANEL_TYPE_MAP = {
    "info": "panel-note",
    "note": "panel-note",
    "warning": "panel-warning",
    "error": "panel-warning",
    "success": "panel-success",
}

# Macros with no visible output on the real site — vanish silently rather
# than show an "unmapped macro" box, since a box would wrongly imply
# something is missing.
SILENT_MACROS = {
    "appfire-confluence-analytics",
}

# Macros that are pure wrappers around ordinary content — render the content
# directly with no extra wrapper div, since these don't need special styling.
TRANSPARENT_CONTENT_MACROS = {
    "excerpt",
    "excerpt-include",
    "expand",  # bodied-extension form some spaces use instead of native ADF expand
}

VIDEO_HOST_HINTS = ("youtube.com", "youtu.be", "loom.com", "vimeo.com")

INTERNAL_PAGE_LINK_RE = re.compile(r"/wiki/spaces/[^/]+/pages/(\d+)")


def render_date(node):
    """ADF date nodes store a millisecond-epoch timestamp as a string
    (e.g. "1745280000000") — displaying that raw number, as the previous
    version did, is unreadable. Converts to a real date, with a proper
    machine-readable datetime attribute for accessibility/semantics."""
    ts_raw = node.get("attrs", {}).get("timestamp")
    try:
        ts_seconds = int(ts_raw) / 1000
        dt = datetime.datetime.fromtimestamp(ts_seconds, tz=datetime.timezone.utc)
        display = dt.strftime("%B %-d, %Y") if hasattr(dt, "strftime") else str(ts_raw)
        iso = dt.strftime("%Y-%m-%d")
        return f'<time datetime="{iso}">{esc(display)}</time>'
    except (TypeError, ValueError, OSError):
        # Fails closed to showing *something* recognizable rather than
        # crashing the whole page over one malformed timestamp.
        return f'<time>{esc(str(ts_raw))}</time>'


def esc(text):
    return html.escape(text or "", quote=False)


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return slug or "section"


def unique_heading_id(text, seen_ids):
    base = slugify(text)
    slug = base
    i = 2
    while slug in seen_ids:
        slug = f"{base}-{i}"
        i += 1
    seen_ids.add(slug)
    return slug


# Confluence sometimes sends the literal shortcode as `text` even for very
# common, universally-recognized emoji (check_mark, cross_mark) rather than a
# real glyph. Unlike genuinely custom UI icons (edit-pencil, actionmenu),
# these have an obvious, standard visual equivalent — worth mapping directly
# rather than spelling out "[check mark icon]" every time, especially in
# tables like a permissions matrix where that repeats dozens of times.
KNOWN_EMOJI_GLYPHS = {
    "check_mark": "✅",
    "cross_mark": "❌",
    "white_check_mark": "✅",
    "heavy_check_mark": "✔️",
    "warning": "⚠️",
    "bulb": "💡",
    "point_right": "👉",
    "info": "ℹ️",
}


def render_emoji(node):
    attrs = node.get("attrs", {})
    text = attrs.get("text", "")
    short = attrs.get("shortName", "")
    short_key = short.strip(":") if short else ""
    if short_key in KNOWN_EMOJI_GLYPHS:
        return KNOWN_EMOJI_GLYPHS[short_key]
    # Real unicode emoji (👉, ✅, 🔢...) come through as the actual glyph in
    # `text`. Confluence's own UI icons (edit-pencil, actionmenu, history_icon)
    # have no unicode equivalent — their `text` is literally the shortcode
    # string itself, which would otherwise leak into rendered prose verbatim.
    if text and not re.match(r"^:[\w-]+:$", text):
        return esc(text)
    label = (short or text).strip(":").replace("-", " ").replace("_", " ").strip()
    if not label:
        return ""
    return f'<span class="icon-note">[{esc(label)} icon]</span>'


def _youtube_embed_html(url):
    m = re.search(r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{6,})", url or "")
    if not m:
        return f'<iframe src="{html.escape(url or "", quote=True)}" allowfullscreen></iframe>'
    video_id = m.group(1)
    m2 = re.search(r"[?&]t=(\d+)", url)
    start = f"?start={m2.group(1)}" if m2 else ""
    return (
        f'<div class="video-embed"><iframe '
        f'src="https://www.youtube.com/embed/{video_id}{start}" allowfullscreen></iframe></div>'
    )


def _loom_embed_html(url):
    m = re.search(r"loom\.com/share/([A-Za-z0-9]+)", url or "")
    if not m:
        return f'<iframe src="{html.escape(url or "", quote=True)}" allowfullscreen></iframe>'
    share_id = m.group(1)
    return (
        f'<div class="video-embed"><iframe '
        f'src="https://www.loom.com/embed/{share_id}" allowfullscreen></iframe></div>'
    )


def _generic_embed_card_html(url):
    safe = html.escape(url or "", quote=True)
    display = esc(url or "")
    return f'<p><a href="{safe}" class="embed-card-link">{display}</a></p>'


def render_embed_card(node):
    url = node.get("attrs", {}).get("url", "")
    if "youtube.com" in url or "youtu.be" in url:
        return _youtube_embed_html(url)
    if "loom.com" in url:
        return _loom_embed_html(url)
    if "vimeo.com" in url:
        return f'<div class="video-embed"><iframe src="{html.escape(url, quote=True)}" allowfullscreen></iframe></div>'
    return _generic_embed_card_html(url)


def render_inline_card(node, link_titles=None):
    url = node.get("attrs", {}).get("url", "")
    link_titles = link_titles or {}
    m = INTERNAL_PAGE_LINK_RE.search(url)
    if m and m.group(1) in link_titles:
        label = link_titles[m.group(1)]
    else:
        label = url
    safe_href = html.escape(url, quote=True)
    return f'<a href="{safe_href}">{esc(label)}</a>'


def render_marks(text, marks):
    out = esc(text)
    link_href = None
    open_tags = []
    for mark in marks or []:
        mtype = mark.get("type")
        if mtype == "link":
            link_href = mark.get("attrs", {}).get("href", "#")
        elif mtype in MARK_TAGS:
            open_tags.append(MARK_TAGS[mtype])
    for tag in open_tags:
        out = f"<{tag}>{out}</{tag}>"
    if link_href:
        safe_href = html.escape(link_href, quote=True)
        out = f'<a href="{safe_href}">{out}</a>'
    return out


def plain_text_of(nodes):
    """Flatten inline content to plain text — used for heading ids/TOC labels."""
    parts = []
    for node in nodes or []:
        if node.get("type") == "text":
            parts.append(node.get("text", ""))
        elif node.get("content"):
            parts.append(plain_text_of(node["content"]))
    return "".join(parts)


def render_inline(nodes, ctx):
    parts = []
    for node in nodes or []:
        ntype = node.get("type")
        if ntype == "text":
            parts.append(render_marks(node.get("text", ""), node.get("marks")))
        elif ntype == "hardBreak":
            parts.append("<br>")
        elif ntype == "mention":
            parts.append(f'<span class="mention">@{esc(node.get("attrs", {}).get("text", "user"))}</span>')
        elif ntype == "emoji":
            parts.append(render_emoji(node))
        elif ntype == "inlineExtension":
            parts.append(render_extension(node, ctx, inline=True))
        elif ntype == "inlineCard":
            parts.append(render_inline_card(node, ctx.get("link_titles")))
        elif ntype == "mediaInline":
            parts.append('<span class="inline-icon" title="inline icon">▢</span>')
        elif ntype == "status":
            attrs = node.get("attrs", {})
            parts.append(f'<span class="status-lozenge">{esc(attrs.get("text",""))}</span>')
        elif ntype == "date":
            parts.append(render_date(node))
        else:
            parts.append(f'<span class="img-placeholder" style="display:inline">[unmapped inline: {esc(ntype or "?")}]</span>')
    return "".join(parts)


def render_page_properties(node, ctx):
    """Page Properties macro — usually wraps a two-column table of {label: value}.
    Render its actual content (typically a table) inside a styled wrapper so it
    reads as a distinct metadata block rather than blending into body text."""
    inner = "".join(render_block(c, ctx) for c in node.get("content", []))
    return f'<div class="page-properties">{inner}</div>'


def render_extension(node, ctx, inline=False):
    attrs = node.get("attrs", {})
    key = attrs.get("extensionKey")

    if key in SILENT_MACROS:
        return ""

    params = attrs.get("parameters", {}) or {}
    macro_params = params.get("macroParams", {}) or {}
    content = node.get("content")

    if key == "iframe":
        src = macro_params.get("src", {}).get("value") or macro_params.get("", {}).get("value")
        if src and ("youtube.com" in src or "youtu.be" in src):
            return _youtube_embed_html(src)
        if src:
            return f'<iframe src="{html.escape(src, quote=True)}"></iframe>'
        return ""

    if key == "include":
        title = (macro_params.get("", {}) or {}).get("value", "").strip()
        unresolved_includes = ctx.get("unresolved_includes") or {}
        included = unresolved_includes.get(title, "").strip()
        if included and included not in ("", "<p></p>"):
            return f'<div class="included-content">{included}</div>'
        return ""

    if key == "children":
        # Resolved later by generate_site.py, which has the real page tree —
        # this function only knows the macro exists, not which page it's on.
        return "<!--CHILDREN_MACRO-->"

    if key == "toc":
        # Resolved later once the full heading list for this page is known —
        # rendering happens bottom-up per-node, but TOC needs the whole page.
        return "<!--TOC_MACRO-->"

    # MultiExcerpt is a Forge/ecosystem app, not a native Confluence macro —
    # its extensionKey is a long, installation-specific path
    # (e.g. "47fa61b6-.../4d8fa66b-.../static/multiexcerpt-fast-inline-macro")
    # rather than a short fixed string, and its own parameters live under
    # "guestParams" as plain values, not "macroParams" wrapped in {"value": ...}
    # like native macros use. Confirmed against a real page — this isn't a guess.
    key_str = key or ""
    guest_params = params.get("guestParams", {}) or {}

    if key_str.endswith("/static/multiexcerpt-fast-inline-macro") or key_str.endswith("/static/multiexcerpt"):
        # Defines a named, reusable snippet. Registered ahead of time by
        # generate_site.py's pre-scan (by both the macro's own localId and
        # by (page_id, name), since the real include macro references its
        # source primarily by exact UUID — confirmed from a real payload
        # where the include's `macro_uuid` matched the definer's `localId`
        # precisely). If the author checked "hidden" (a real MultiExcerpt
        # option — don't show this excerpt where it's defined, only where
        # it's included), respect that and render nothing here.
        features = guest_params.get("features") or []
        if "hidden" in features:
            return ""
        return "".join(render_block(c, ctx) for c in (content or []))

    if key_str.endswith("/static/multiexcerpt-include-macro"):
        macro_uuid = guest_params.get("macro_uuid")
        excerpt_name = (guest_params.get("name") or "").strip()
        source_page_id = str(guest_params.get("pageId") or "").strip()
        registry = ctx.get("multiexcerpt_registry") or {}

        raw_content = None
        if macro_uuid:
            raw_content = registry.get("by_uuid", {}).get(macro_uuid)
        if raw_content is None and source_page_id and excerpt_name:
            raw_content = registry.get("by_name", {}).get((source_page_id, excerpt_name))

        if raw_content is not None:
            return "".join(render_block(c, ctx) for c in raw_content)
        return (
            f'<div class="img-placeholder">[MultiExcerpt "{esc(excerpt_name)}" from page '
            f'{esc(source_page_id)} — not found.]</div>'
        )

    if key in ("detail", "details-macro", "page-properties"):
        return render_page_properties(node, ctx)

    if key == "pagetree":
        return '<div class="img-placeholder">[pagetree macro — dynamic multi-level tree, not yet built]</div>'

    # Generic fallback: most macros we haven't explicitly mapped are still
    # just wrapping ordinary renderable content (excerpts, custom panels,
    # third-party formatting macros — this is also how Table Plus and
    # similar Advanced Tables macros work: the real table is stored as
    # literal nested content, so this fallback already renders it correctly
    # with zero special-case code, confirmed against real data). Render
    # that content directly rather than hiding it.
    if content:
        return "".join(render_block(c, ctx) for c in content)

    return f'<div class="img-placeholder">[Unmapped macro: {esc(key or "unknown")} — no content to fall back on]</div>'


def render_media(node, ctx):
    attrs = node.get("attrs", {})
    media_id = attrs.get("id")
    alt = attrs.get("alt") or attrs.get("collection") or "Image"
    media_map = (ctx or {}).get("media_map") or {}

    local_path = media_map.get(media_id)
    if local_path:
        return f'<img src="{html.escape(local_path, quote=True)}" alt="{esc(alt)}" loading="lazy" class="doc-image">'

    return (
        f'<div class="img-placeholder"><span class="tag">Image — asset pipeline pending</span>'
        f'<br>{esc(alt)}</div>'
    )


def render_block(node, ctx):
    ntype = node.get("type")
    content = node.get("content", [])

    if ntype == "paragraph":
        inline = render_inline(content, ctx)
        return f"<p>{inline}</p>" if inline.strip() else ""

    if ntype == "heading":
        level = node.get("attrs", {}).get("level", 2)
        level = min(max(level, 2), 4)  # h1 reserved for page title
        text_html = render_inline(content, ctx)
        plain = plain_text_of(content)
        heading_id = unique_heading_id(plain, ctx["heading_ids"])
        ctx["headings"].append({"id": heading_id, "level": level, "text": plain})
        return f'<h{level} id="{heading_id}">{text_html}</h{level}>'

    if ntype in ("bulletList", "orderedList"):
        tag = "ul" if ntype == "bulletList" else "ol"
        items = "".join(render_block(li, ctx) for li in content)
        return f"<{tag}>{items}</{tag}>"

    if ntype == "listItem":
        inner = "".join(render_block(c, ctx) for c in content)
        return f"<li>{inner}</li>"

    if ntype == "panel":
        panel_type = node.get("attrs", {}).get("panelType", "info")
        css_class = PANEL_TYPE_MAP.get(panel_type, "panel-note")
        inner = "".join(render_block(c, ctx) for c in content)
        return f'<div class="panel {css_class}">{inner}</div>'

    if ntype == "layoutSection":
        columns = [c for c in content if c.get("type") == "layoutColumn"]
        if not columns:
            return ""
        n = len(columns)
        widths = [c.get("attrs", {}).get("width") or (100 / n) for c in columns]
        template = " ".join(f"{w}fr" for w in widths)
        cols_html = "".join(render_block(c, ctx) for c in columns)
        return f'<div class="columns" style="grid-template-columns: {template};">{cols_html}</div>'

    if ntype == "layoutColumn":
        inner = "".join(render_block(c, ctx) for c in content)
        return f"<div>{inner}</div>"

    if ntype == "mediaSingle":
        media_nodes = [c for c in content if c.get("type") == "media"]
        return "".join(render_media(m, ctx) for m in media_nodes) if media_nodes else ""

    if ntype == "mediaGroup":
        return "".join(render_media(m, ctx) for m in content if m.get("type") == "media")

    if ntype == "embedCard":
        return render_embed_card(node)

    if ntype == "expand":
        title = node.get("attrs", {}).get("title", "Details")
        inner = "".join(render_block(c, ctx) for c in content)
        return f"<details><summary>{esc(title)}</summary>{inner}</details>"

    if ntype == "rule":
        return "<hr>"

    if ntype == "blockquote":
        inner = "".join(render_block(c, ctx) for c in content)
        return f"<blockquote>{inner}</blockquote>"

    if ntype == "codeBlock":
        lang = node.get("attrs", {}).get("language", "")
        text = "".join(c.get("text", "") for c in content if c.get("type") == "text")
        return f'<pre><code class="language-{lang}">{esc(text)}</code></pre>'

    if ntype == "table":
        rows = "".join(render_block(c, ctx) for c in content)
        return f"<table>{rows}</table>"

    if ntype == "tableRow":
        cells = "".join(render_block(c, ctx) for c in content)
        return f"<tr>{cells}</tr>"

    if ntype in ("tableCell", "tableHeader"):
        tag = "th" if ntype == "tableHeader" else "td"
        inner = "".join(render_block(c, ctx) for c in content)
        return f"<{tag}>{inner}</{tag}>"

    if ntype == "taskList":
        items = "".join(render_block(c, ctx) for c in content)
        return f'<ul class="task-list">{items}</ul>'

    if ntype == "taskItem":
        checked = "checked" if node.get("attrs", {}).get("state") == "DONE" else ""
        inner = render_inline(content, ctx)
        return f'<li><input type="checkbox" disabled {checked}> {inner}</li>'

    if ntype in ("bodiedExtension", "extension"):
        return render_extension(node, ctx)

    # Unknown block type — visible marker, not a silent drop.
    return f'<div class="img-placeholder">[Unmapped block: {esc(ntype or "unknown")}]</div>'


def render_toc(headings):
    """Real TOC, built from the headings actually collected during render —
    no dynamic macro needed since we already walked the whole document."""
    if not headings:
        return ""
    items = "".join(
        f'<li class="toc-level-{h["level"]}"><a href="#{h["id"]}">{esc(h["text"])}</a></li>'
        for h in headings
    )
    return f'<nav class="toc"><ul>{items}</ul></nav>'


def build_multiexcerpt_registry(pages):
    """Pre-scans every page's RAW ADF (before any rendering) for
    MultiExcerpt definitions, building two lookup indexes:
      - by_uuid: {localId: raw_adf_content} — the primary, precise lookup,
        since a real MultiExcerpt Include references its source by exact
        macro UUID (confirmed against real data: the include's guestParams
        "macro_uuid" matches the definer's own "localId" attribute exactly).
      - by_name: {(page_id, excerpt_name): raw_adf_content} — fallback for
        cases where the UUID isn't available for some reason.

    Storing raw ADF rather than pre-rendered HTML means an included excerpt
    still resolves media/links using whichever page's context actually
    includes it, and page/space processing order never matters — the whole
    registry exists before any page starts rendering.

    `pages` is the list of page dicts as produced by fetch_confluence.py
    (each with "id" and "adf" keys) — can span multiple spaces, since a
    MultiExcerpt Include isn't guaranteed to stay within one space.
    """
    by_uuid = {}
    by_name = {}

    def walk(node, page_id):
        if not isinstance(node, dict):
            return
        if node.get("type") == "bodiedExtension":
            attrs = node.get("attrs", {})
            key = attrs.get("extensionKey", "") or ""
            if key.endswith("/static/multiexcerpt-fast-inline-macro") or key.endswith("/static/multiexcerpt"):
                params = attrs.get("parameters", {}) or {}
                guest_params = params.get("guestParams", {}) or {}
                excerpt_name = (guest_params.get("name") or "").strip()
                local_id = attrs.get("localId")
                excerpt_content = node.get("content", [])
                if local_id:
                    by_uuid[local_id] = excerpt_content
                if excerpt_name:
                    by_name[(str(page_id), excerpt_name)] = excerpt_content
        for child in (node.get("content") or []):
            walk(child, page_id)

    for p in pages:
        adf = p.get("adf")
        if not adf:
            continue
        for node in adf.get("content", []):
            walk(node, p.get("id"))

    return {"by_uuid": by_uuid, "by_name": by_name}


def adf_to_html(adf_doc, unresolved_includes=None, link_titles=None, media_map=None, multiexcerpt_registry=None):
    """
    adf_doc: parsed JSON dict with {"type": "doc", "version": 1, "content": [...]}
             (i.e. the `body.atlas_doc_format.value`, already json.loads()'d, from
             GET /wiki/api/v2/pages/{id}?body-format=atlas_doc_format)
    link_titles: optional {page_id: title} dict used to render inlineCard links to
                 internal pages with a real title instead of the raw URL.
    media_map: optional {media_id: local_asset_path} dict, produced by
               fetch_confluence.py's attachment downloader — when a media node's
               id is found here, a real <img> renders instead of a placeholder.
    multiexcerpt_registry: optional {(page_id, excerpt_name): raw_adf_content}
               dict, produced by build_multiexcerpt_registry() ahead of time
               across every page — lets a multiexcerpt-include macro pull in
               content defined on any other page, regardless of build order.

    Returns the rendered HTML string. Any TOC macro on the page is resolved
    using headings collected during this same render pass, so a TOC macro
    anywhere in the document (before or after its headings) works correctly.
    """
    if isinstance(adf_doc, str):
        adf_doc = json.loads(adf_doc)

    ctx = {
        "unresolved_includes": unresolved_includes,
        "link_titles": link_titles,
        "media_map": media_map,
        "multiexcerpt_registry": multiexcerpt_registry or {},
        "headings": [],
        "heading_ids": set(),
    }
    content = adf_doc.get("content", [])
    html_str = "".join(render_block(node, ctx) for node in content)

    if "<!--TOC_MACRO-->" in html_str:
        html_str = html_str.replace("<!--TOC_MACRO-->", render_toc(ctx["headings"]))

    return html_str


def generate_meta_description(adf_doc, max_len=155):
    if isinstance(adf_doc, str):
        adf_doc = json.loads(adf_doc)

    def walk_text(nodes):
        for node in nodes or []:
            if node.get("type") == "paragraph":
                text = "".join(c.get("text", "") for c in node.get("content", []) if c.get("type") == "text")
                text = re.sub(r"\s+", " ", text).strip()
                if len(text) > 40:
                    return text
            elif node.get("content"):
                found = walk_text(node["content"])
                if found:
                    return found
        return None

    text = walk_text(adf_doc.get("content", [])) or ""
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit(" ", 1)[0] + "…"


if __name__ == "__main__":
    sample = {
        "type": "doc",
        "version": 1,
        "content": [
            {"type": "extension", "attrs": {"extensionKey": "toc", "extensionType": "com.atlassian.confluence.macro.core"}},
            {"type": "heading", "attrs": {"level": 2}, "content": [{"type": "text", "text": "Overview"}]},
            {"type": "paragraph", "content": [
                {"type": "text", "text": "This is a real test paragraph long enough to become a meta description candidate."}
            ]},
            {"type": "heading", "attrs": {"level": 3}, "content": [{"type": "text", "text": "Overview"}]},  # duplicate title, tests id uniqueness
            {"type": "panel", "attrs": {"panelType": "note"}, "content": [
                {"type": "paragraph", "content": [{"type": "text", "text": "A note."}]}
            ]},
            {"type": "extension", "attrs": {"extensionKey": "detail", "extensionType": "com.atlassian.confluence.macro.core"}, "content": [
                {"type": "table", "content": [
                    {"type": "tableRow", "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Owner"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Christie"}]}]}
                    ]}
                ]}
            ]},
            {"type": "extension", "attrs": {"extensionKey": "some-random-third-party-macro", "extensionType": "x"}, "content": [
                {"type": "paragraph", "content": [{"type": "text", "text": "Fallback content should still show up."}]}
            ]},
            {"type": "extension", "attrs": {"extensionKey": "totally-empty-unknown-macro", "extensionType": "x"}},
        ],
    }
    out = adf_to_html(sample)
    assert '<nav class="toc">' in out
    assert 'href="#overview"' in out and 'href="#overview-2"' in out
    assert 'id="overview"' in out and 'id="overview-2"' in out
    assert 'page-properties' in out and 'Christie' in out
    assert "Fallback content should still show up." in out
    assert "Unmapped macro: totally-empty-unknown-macro" in out
    assert "Unmapped macro: some-random" not in out  # this one had content, shouldn't be flagged
    print("adf_transform.py v3 self-test passed")
