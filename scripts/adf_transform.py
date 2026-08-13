#!/usr/bin/env python3
"""
adf_transform.py — converts ADF (Atlassian Document Format) JSON, as returned
by Confluence's real REST API v2 (GET /wiki/api/v2/pages/{id}?body-format=atlas_doc_format),
into clean static HTML.

v2 changes, made after reviewing the real FOX space payload from the first
live fetch (not the hand-built fixture): added embedCard (YouTube/Loom/Vimeo
smart embeds), inlineCard (inline smart links), mediaInline (small inline
icons), a real children-macro renderer backed by the actual page tree, and a
silent-skip list for macros with no visual output (internal analytics, etc).

ADF reference: https://developer.atlassian.com/cloud/confluence/adf/

Design choice carried over from v1: truly unknown node types still render a
visible marker instead of silently vanishing. Content that quietly disappears
during extraction is exactly what broke the Get Started page audit's
markdown-based approach — this pipeline deliberately fails loud, except for
the specific macros in SILENT_MACROS that are known to have no output.
"""

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

VIDEO_HOST_HINTS = ("youtube.com", "youtu.be", "loom.com", "vimeo.com")

INTERNAL_PAGE_LINK_RE = re.compile(r"/wiki/spaces/[^/]+/pages/(\d+)")


def esc(text):
    return html.escape(text or "", quote=False)


def render_emoji(node):
    attrs = node.get("attrs", {})
    text = attrs.get("text", "")
    short = attrs.get("shortName", "")
    # Real unicode emoji (👉, ✅, 🔢...) come through as the actual glyph in
    # `text`. Confluence's own UI icons (edit-pencil, actionmenu, history_icon)
    # have no unicode equivalent — their `text` is literally the shortcode
    # string itself, which would otherwise leak into rendered prose verbatim
    # (e.g. "click :edit-pencil: to..." showing up exactly like that).
    if text and not re.match(r"^:[\w-]+:$", text):
        return esc(text)
    label = (short or text).strip(":").replace("-", " ").replace("_", " ").strip()
    if not label:
        return ""
    return f'<span class="icon-note">[{esc(label)} icon]</span>'


def _is_video_url(url):
    return any(host in (url or "") for host in VIDEO_HOST_HINTS)


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
    """Non-video embed cards (e.g. Marketplace links, docs) — render as a styled card link
    rather than trying to iframe arbitrary third-party pages, which most sites block anyway."""
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


def render_marks(text, marks, link_titles=None):
    """Wrap escaped text in the tags implied by its marks (bold/italic/code/link)."""
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


def render_inline(nodes, unresolved_includes=None, link_titles=None):
    parts = []
    for node in nodes or []:
        ntype = node.get("type")
        if ntype == "text":
            parts.append(render_marks(node.get("text", ""), node.get("marks"), link_titles))
        elif ntype == "hardBreak":
            parts.append("<br>")
        elif ntype == "mention":
            parts.append(f'<span class="mention">@{esc(node.get("attrs", {}).get("text", "user"))}</span>')
        elif ntype == "emoji":
            parts.append(render_emoji(node))
        elif ntype == "inlineExtension":
            parts.append(render_extension(node, unresolved_includes, link_titles, inline=True))
        elif ntype == "inlineCard":
            parts.append(render_inline_card(node, link_titles))
        elif ntype == "mediaInline":
            # Small inline icon within a sentence — not worth a full placeholder block,
            # but shouldn't vanish silently either.
            parts.append('<span class="inline-icon" title="inline icon">▢</span>')
        elif ntype == "status":
            attrs = node.get("attrs", {})
            parts.append(f'<span class="status-lozenge">{esc(attrs.get("text",""))}</span>')
        elif ntype == "date":
            ts = node.get("attrs", {}).get("timestamp")
            parts.append(f'<time>{esc(str(ts))}</time>')
        else:
            parts.append(f'<span class="img-placeholder" style="display:inline">[unmapped inline: {esc(ntype or "?")}]</span>')
    return "".join(parts)


def render_extension(node, unresolved_includes=None, link_titles=None, inline=False):
    attrs = node.get("attrs", {})
    key = attrs.get("extensionKey")

    if key in SILENT_MACROS:
        return ""

    params = attrs.get("parameters", {}) or {}
    macro_params = params.get("macroParams", {}) or {}

    if key == "iframe":
        src = macro_params.get("src", {}).get("value") or macro_params.get("", {}).get("value")
        if src and ("youtube.com" in src or "youtu.be" in src):
            return _youtube_embed_html(src)
        if src:
            return f'<iframe src="{html.escape(src, quote=True)}"></iframe>'
        return ""

    if key == "include":
        title = (macro_params.get("", {}) or {}).get("value", "").strip()
        unresolved_includes = unresolved_includes or {}
        included = unresolved_includes.get(title, "").strip()
        if included and included not in ("", "<p></p>"):
            return f'<div class="included-content">{included}</div>'
        return ""

    if key == "children":
        # We have the real page tree at generate time — render_children_list()
        # in generate_site.py replaces this placeholder with an actual nested
        # list once it knows which page this macro lives on. Leave a marker
        # extension can't resolve on its own (it doesn't know "this page's id").
        return "<!--CHILDREN_MACRO-->"

    if key in ("toc", "pagetree"):
        return f'<div class="img-placeholder">[{esc(key)} macro — dynamic, no static equivalent yet]</div>'

    return f'<div class="img-placeholder">[Unmapped macro: {esc(key or "unknown")} — needs a transform rule]</div>'


def render_media(node):
    attrs = node.get("attrs", {})
    alt = attrs.get("alt") or attrs.get("collection") or "Image"
    return (
        f'<div class="img-placeholder"><span class="tag">Image — asset pipeline pending</span>'
        f'<br>{esc(alt)}</div>'
    )


def render_block(node, unresolved_includes=None, link_titles=None):
    ntype = node.get("type")
    content = node.get("content", [])

    if ntype == "paragraph":
        inline = render_inline(content, unresolved_includes, link_titles)
        return f"<p>{inline}</p>" if inline.strip() else ""

    if ntype == "heading":
        level = node.get("attrs", {}).get("level", 2)
        level = min(max(level, 2), 4)  # h1 reserved for page title
        return f"<h{level}>{render_inline(content, unresolved_includes, link_titles)}</h{level}>"

    if ntype in ("bulletList", "orderedList"):
        tag = "ul" if ntype == "bulletList" else "ol"
        items = "".join(render_block(li, unresolved_includes, link_titles) for li in content)
        return f"<{tag}>{items}</{tag}>"

    if ntype == "listItem":
        inner = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f"<li>{inner}</li>"

    if ntype == "panel":
        panel_type = node.get("attrs", {}).get("panelType", "info")
        css_class = PANEL_TYPE_MAP.get(panel_type, "panel-note")
        inner = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f'<div class="panel {css_class}">{inner}</div>'

    if ntype == "layoutSection":
        columns = [c for c in content if c.get("type") == "layoutColumn"]
        if not columns:
            return ""
        n = len(columns)
        widths = [c.get("attrs", {}).get("width") or (100 / n) for c in columns]
        template = " ".join(f"{w}fr" for w in widths)
        cols_html = "".join(render_block(c, unresolved_includes, link_titles) for c in columns)
        return f'<div class="columns" style="grid-template-columns: {template};">{cols_html}</div>'

    if ntype == "layoutColumn":
        inner = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f"<div>{inner}</div>"

    if ntype == "mediaSingle":
        media_nodes = [c for c in content if c.get("type") == "media"]
        return "".join(render_media(m) for m in media_nodes) if media_nodes else ""

    if ntype == "mediaGroup":
        return "".join(render_media(m) for m in content if m.get("type") == "media")

    if ntype == "embedCard":
        return render_embed_card(node)

    if ntype == "expand":
        title = node.get("attrs", {}).get("title", "Details")
        inner = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f"<details><summary>{esc(title)}</summary>{inner}</details>"

    if ntype == "rule":
        return "<hr>"

    if ntype == "blockquote":
        inner = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f"<blockquote>{inner}</blockquote>"

    if ntype == "codeBlock":
        lang = node.get("attrs", {}).get("language", "")
        text = "".join(c.get("text", "") for c in content if c.get("type") == "text")
        return f'<pre><code class="language-{lang}">{esc(text)}</code></pre>'

    if ntype == "table":
        rows = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f"<table>{rows}</table>"

    if ntype == "tableRow":
        cells = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f"<tr>{cells}</tr>"

    if ntype in ("tableCell", "tableHeader"):
        tag = "th" if ntype == "tableHeader" else "td"
        inner = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f"<{tag}>{inner}</{tag}>"

    if ntype == "taskList":
        items = "".join(render_block(c, unresolved_includes, link_titles) for c in content)
        return f'<ul class="task-list">{items}</ul>'

    if ntype == "taskItem":
        checked = "checked" if node.get("attrs", {}).get("state") == "DONE" else ""
        inner = render_inline(content, unresolved_includes, link_titles)
        return f'<li><input type="checkbox" disabled {checked}> {inner}</li>'

    if ntype in ("bodiedExtension", "extension"):
        return render_extension(node, unresolved_includes, link_titles)

    # Unknown block type — visible marker, not a silent drop.
    return f'<div class="img-placeholder">[Unmapped block: {esc(ntype or "unknown")}]</div>'


def adf_to_html(adf_doc, unresolved_includes=None, link_titles=None):
    """
    adf_doc: parsed JSON dict with {"type": "doc", "version": 1, "content": [...]}
             (i.e. the `body.atlas_doc_format.value`, already json.loads()'d, from
             GET /wiki/api/v2/pages/{id}?body-format=atlas_doc_format)
    link_titles: optional {page_id: title} dict used to render inlineCard links to
                 internal pages with a real title instead of the raw URL.
    """
    if isinstance(adf_doc, str):
        adf_doc = json.loads(adf_doc)
    content = adf_doc.get("content", [])
    return "".join(render_block(node, unresolved_includes, link_titles) for node in content)


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
            {"type": "heading", "attrs": {"level": 2}, "content": [{"type": "text", "text": "Overview"}]},
            {"type": "paragraph", "content": [
                {"type": "text", "text": "This is a real test paragraph long enough to become a meta description candidate."}
            ]},
            {"type": "panel", "attrs": {"panelType": "note"}, "content": [
                {"type": "paragraph", "content": [{"type": "text", "text": "A note."}]}
            ]},
            {"type": "expand", "attrs": {"title": "Click to expand"}, "content": [
                {"type": "paragraph", "content": [{"type": "text", "text": "Hidden content."}]}
            ]},
            {"type": "embedCard", "attrs": {"url": "https://www.youtube.com/watch?v=abc123XYZ_9"}},
            {"type": "embedCard", "attrs": {"url": "https://www.loom.com/share/c28eb97f6aa74a938e08"}},
            {"type": "paragraph", "content": [
                {"type": "text", "text": "See "},
                {"type": "inlineCard", "attrs": {"url": "https://appfire.atlassian.net/wiki/spaces/FOX/pages/12345"}},
                {"type": "text", "text": " for details."},
            ]},
            {"type": "extension", "attrs": {
                "extensionKey": "appfire-confluence-analytics",
                "extensionType": "com.atlassian.confluence.macro.core",
                "parameters": {},
            }},
        ],
    }
    out = adf_to_html(sample, link_titles={"12345": "Some Other Page"})
    assert "<h2>Overview</h2>" in out
    assert "panel-note" in out
    assert "<details>" in out
    assert "youtube.com/embed/abc123XYZ_9" in out
    assert "loom.com/embed/c28eb97f6aa74a938e08" in out
    assert "Some Other Page</a>" in out
    assert "appfire-confluence-analytics" not in out  # silent macro should vanish entirely
    assert "Unmapped" not in out
    print("adf_transform.py v2 self-test passed")
    print(generate_meta_description(sample))
