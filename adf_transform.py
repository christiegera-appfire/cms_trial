#!/usr/bin/env python3
"""
adf_transform.py — converts ADF (Atlassian Document Format) JSON, as returned
by Confluence's real REST API v2 (GET /wiki/api/v2/pages/{id}?body-format=atlas_doc_format),
into clean static HTML.

This replaces transform.py (which worked off the Atlassian MCP tool's own
"HTML+" normalization) with something driven by the actual production API —
the format you get when a GitHub Action fetches with a real API token, not
what a chat-session tool happens to hand back.

ADF reference: https://developer.atlassian.com/cloud/confluence/adf/

Design choice carried over from transform.py: unknown/unmapped node types
render a visible marker instead of silently vanishing. Content that quietly
disappears during extraction is exactly what broke the Get Started page
audit's markdown-based approach — this pipeline deliberately fails loud.
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


def esc(text):
    return html.escape(text or "", quote=False)


def render_marks(text, marks):
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


def render_inline(nodes):
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
            parts.append(esc(node.get("attrs", {}).get("text", "")))
        elif ntype == "inlineExtension":
            parts.append(render_extension(node, inline=True))
        elif ntype == "status":
            attrs = node.get("attrs", {})
            parts.append(f'<span class="status-lozenge">{esc(attrs.get("text",""))}</span>')
        elif ntype == "date":
            ts = node.get("attrs", {}).get("timestamp")
            parts.append(f'<time>{esc(str(ts))}</time>')
        else:
            parts.append(f'<!-- unmapped inline node: {ntype} -->')
    return "".join(parts)


def youtube_embed_html(src):
    m = re.search(r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{6,})", src or "")
    if not m:
        return f'<iframe src="{html.escape(src or "", quote=True)}"></iframe>'
    video_id = m.group(1)
    m2 = re.search(r"[?&]t=(\d+)", src)
    start = f"?start={m2.group(1)}" if m2 else ""
    return (
        f'<div class="video-embed"><iframe '
        f'src="https://www.youtube.com/embed/{video_id}{start}" allowfullscreen></iframe></div>'
    )


def render_extension(node, unresolved_includes=None, inline=False):
    attrs = node.get("attrs", {})
    key = attrs.get("extensionKey")
    params = attrs.get("parameters", {}) or {}
    macro_params = params.get("macroParams", {}) or {}

    if key == "iframe":
        src = macro_params.get("src", {}).get("value") or macro_params.get("", {}).get("value")
        if src and ("youtube.com" in src or "youtu.be" in src):
            return youtube_embed_html(src)
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

    if key in ("toc", "children", "pagetree"):
        # Structural macros with no static equivalent yet — visible note, not a silent drop.
        return f'<div class="img-placeholder">[{key} macro — dynamic, needs a build-time equivalent]</div>'

    return f'<div class="img-placeholder">[Unmapped macro: {esc(key or "unknown")} — needs a transform rule]</div>'


def render_media(node):
    attrs = node.get("attrs", {})
    alt = attrs.get("alt") or attrs.get("collection") or "Image"
    return (
        f'<div class="img-placeholder"><span class="tag">Image — asset pipeline pending</span>'
        f'<br>{esc(alt)}</div>'
    )


def render_block(node, unresolved_includes=None):
    ntype = node.get("type")
    content = node.get("content", [])

    if ntype == "paragraph":
        inline = render_inline(content)
        return f"<p>{inline}</p>" if inline.strip() else ""

    if ntype == "heading":
        level = node.get("attrs", {}).get("level", 2)
        level = min(max(level, 2), 4)  # h1 reserved for page title
        return f"<h{level}>{render_inline(content)}</h{level}>"

    if ntype in ("bulletList", "orderedList"):
        tag = "ul" if ntype == "bulletList" else "ol"
        items = "".join(render_block(li, unresolved_includes) for li in content)
        return f"<{tag}>{items}</{tag}>"

    if ntype == "listItem":
        inner = "".join(render_block(c, unresolved_includes) for c in content)
        return f"<li>{inner}</li>"

    if ntype == "panel":
        panel_type = node.get("attrs", {}).get("panelType", "info")
        css_class = PANEL_TYPE_MAP.get(panel_type, "panel-note")
        inner = "".join(render_block(c, unresolved_includes) for c in content)
        return f'<div class="panel {css_class}">{inner}</div>'

    if ntype == "layoutSection":
        cols = "".join(render_block(c, unresolved_includes) for c in content)
        return f'<div class="columns">{cols}</div>'

    if ntype == "layoutColumn":
        inner = "".join(render_block(c, unresolved_includes) for c in content)
        return f"<div>{inner}</div>"

    if ntype == "mediaSingle":
        media_nodes = [c for c in content if c.get("type") == "media"]
        return "".join(render_media(m) for m in media_nodes) if media_nodes else ""

    if ntype == "mediaGroup":
        return "".join(render_media(m) for m in content if m.get("type") == "media")

    if ntype == "expand":
        title = node.get("attrs", {}).get("title", "Details")
        inner = "".join(render_block(c, unresolved_includes) for c in content)
        return f"<details><summary>{esc(title)}</summary>{inner}</details>"

    if ntype == "rule":
        return "<hr>"

    if ntype == "blockquote":
        inner = "".join(render_block(c, unresolved_includes) for c in content)
        return f"<blockquote>{inner}</blockquote>"

    if ntype == "codeBlock":
        lang = node.get("attrs", {}).get("language", "")
        text = "".join(c.get("text", "") for c in content if c.get("type") == "text")
        return f'<pre><code class="language-{lang}">{esc(text)}</code></pre>'

    if ntype == "table":
        rows = "".join(render_block(c, unresolved_includes) for c in content)
        return f"<table>{rows}</table>"

    if ntype == "tableRow":
        cells = "".join(render_block(c, unresolved_includes) for c in content)
        return f"<tr>{cells}</tr>"

    if ntype in ("tableCell", "tableHeader"):
        tag = "th" if ntype == "tableHeader" else "td"
        inner = "".join(render_block(c, unresolved_includes) for c in content)
        return f"<{tag}>{inner}</{tag}>"

    if ntype == "taskList":
        items = "".join(render_block(c, unresolved_includes) for c in content)
        return f'<ul class="task-list">{items}</ul>'

    if ntype == "taskItem":
        checked = "checked" if node.get("attrs", {}).get("state") == "DONE" else ""
        inner = render_inline(content)
        return f'<li><input type="checkbox" disabled {checked}> {inner}</li>'

    if ntype in ("bodiedExtension", "extension"):
        return render_extension(node, unresolved_includes)

    if ntype == "rule":
        return "<hr>"

    # Unknown block type — visible marker, not a silent drop.
    return f'<div class="img-placeholder">[Unmapped block: {esc(ntype or "unknown")}]</div>'


def adf_to_html(adf_doc, unresolved_includes=None):
    """
    adf_doc: parsed JSON dict with {"type": "doc", "version": 1, "content": [...]}
             (i.e. the `body.atlas_doc_format.value`, already json.loads()'d, from
             GET /wiki/api/v2/pages/{id}?body-format=atlas_doc_format)
    """
    if isinstance(adf_doc, str):
        adf_doc = json.loads(adf_doc)
    content = adf_doc.get("content", [])
    return "".join(render_block(node, unresolved_includes) for node in content)


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
        ],
    }
    out = adf_to_html(sample)
    assert "<h2>Overview</h2>" in out
    assert "panel-note" in out
    assert "<details>" in out
    print("adf_transform.py self-test passed")
    print(generate_meta_description(sample))
