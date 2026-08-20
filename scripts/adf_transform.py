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


def decode_aura_params(raw_value):
    """Aura macros store their visual config as base64(urlencode(JSON)) in a
    'params' macroParam — confirmed against real data (Aura Panel, Button,
    Tab Group all use this exact encoding). Returns {} on any failure,
    since this is styling config, not content — losing it should degrade
    gracefully to plain default styling, never break the page."""
    try:
        import base64
        from urllib.parse import unquote
        decoded = base64.b64decode(raw_value).decode("utf-8")
        return json.loads(unquote(decoded))
    except Exception:
        return {}


def group_flat_marker_sequence(content, marker_key, param_extractor):
    """Generic version of the flat marker+content grouping pattern first
    solved for Aura Tab Group — several different macro families
    (Refined's own step/expand macros included) use the exact same
    structure: a content-free marker extension holding just a label,
    with everything that follows it (until the next marker) being that
    item's real content, all sitting flat in the parent's content array
    rather than nested. param_extractor(child_attrs) -> label lets each
    caller pull whatever field it actually cares about (a step number, an
    expand title, etc.) without duplicating the grouping logic itself."""
    groups = []
    current_label = None
    current_nodes = []
    for child in content:
        child_attrs = child.get("attrs", {}) or {}
        if child.get("type") == "extension" and child_attrs.get("extensionKey") == marker_key:
            if current_label is not None:
                groups.append((current_label, current_nodes))
            current_label = param_extractor(child_attrs)
            current_nodes = []
        elif current_label is not None:
            current_nodes.append(child)
    if current_label is not None:
        groups.append((current_label, current_nodes))
    return groups


def render_refined_steps(node, ctx):
    """Refined's own numbered-step macro (distinct from Confluence's native
    step macros) — confirmed against real content: each step's NUMBER is
    already given directly as the marker's "text" param (not something we
    need to auto-generate), with the actual instructional text following
    as flat sibling content."""
    content = node.get("content", []) or []
    steps = group_flat_marker_sequence(
        content, "refined-step",
        lambda attrs: ((attrs.get("parameters", {}) or {}).get("macroParams", {}) or {}).get("text", {}).get("value", "").strip(),
    )
    if not steps:
        return ""
    items = "".join(
        f'<li class="refined-step"><span class="refined-step-number">{esc(number)}</span>'
        f'<div class="refined-step-content">{"".join(render_block(c, ctx) for c in nodes)}</div></li>'
        for number, nodes in steps
    )
    return f'<ol class="refined-steps">{items}</ol>'


def render_refined_expands(node, ctx):
    """Refined's own expand/accordion macro (distinct from Confluence's
    native expand macro, which we already handle separately) — same flat
    marker+content structure, with each marker's "title" param giving the
    real question/summary text directly. Rendered as native <details>, same
    approach as the native expand macro — a real, if simplified,
    trade-off: Refined's own version supports a strict one-open-at-a-time
    accordion mode, which native <details> elements don't replicate, but
    <details> needs no custom JS and degrades safely."""
    content = node.get("content", []) or []
    items_grouped = group_flat_marker_sequence(
        content, "refined-expand",
        lambda attrs: ((attrs.get("parameters", {}) or {}).get("macroParams", {}) or {}).get("title", {}).get("value", "").strip(),
    )
    if not items_grouped:
        return ""
    items = "".join(
        f"<details><summary>{esc(title)}</summary>{''.join(render_block(c, ctx) for c in nodes)}</details>"
        for title, nodes in items_grouped
    )
    return f'<div class="refined-expands">{items}</div>'


def render_aura_tab_group(node, ctx):
    """Aura's tab structure (confirmed against real data) is NOT nested —
    each tab is a plain, content-free 'aura-tab' extension marker holding
    only a title, and everything that follows it (until the next marker)
    is that tab's actual content, all sitting flat inside the parent
    'aura-tab-collection'. This walks that flat sequence and groups it
    into real tabs."""
    content = node.get("content", []) or []
    tabs = []
    current_title = None
    current_nodes = []
    for child in content:
        child_attrs = child.get("attrs", {}) or {}
        if child.get("type") == "extension" and child_attrs.get("extensionKey") == "aura-tab":
            if current_title is not None:
                tabs.append((current_title, current_nodes))
            child_params = (child_attrs.get("parameters", {}) or {}).get("macroParams", {}) or {}
            current_title = (child_params.get("summary", {}) or {}).get("value", "").strip() or f"Tab {len(tabs) + 1}"
            current_nodes = []
        elif current_title is not None:
            current_nodes.append(child)
        # Content appearing before any tab marker shouldn't happen in
        # practice, and is dropped rather than guessed at.
    if current_title is not None:
        tabs.append((current_title, current_nodes))

    if not tabs:
        return ""

    ctx["tab_group_count"] = ctx.get("tab_group_count", 0) + 1
    group_id = f"aura-tabs-{ctx['tab_group_count']}"

    buttons, panels = [], []
    for i, (title, nodes) in enumerate(tabs):
        active = " active" if i == 0 else ""
        panel_id = f"{group_id}-panel-{i}"
        buttons.append(f'<button type="button" class="aura-tab-btn{active}" data-target="{panel_id}">{esc(title)}</button>')
        panel_html = "".join(render_block(c, ctx) for c in nodes)
        panels.append(f'<div class="aura-tab-panel{active}" id="{panel_id}">{panel_html}</div>')

    return (
        f'<div class="aura-tab-group" id="{group_id}">'
        f'<div class="aura-tab-buttons">{"".join(buttons)}</div>'
        f'<div class="aura-tab-panels">{"".join(panels)}</div>'
        f"</div>"
    )


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

    # Aura (a third-party formatting suite, not an Appfire product) uses
    # short native-style extensionKeys under extensionType
    # "com.atlassian.confluence.macro.core" — unlike the Forge-based
    # ecosystem apps (Table Plus, MultiExcerpt) which use long UUID paths
    # and guestParams. Aura's visual config lives in a base64+URL-encoded
    # "params" macroParam; confirmed against real data.
    if key == "aura-panel":
        title = (macro_params.get("summary", {}) or {}).get("value", "").strip()
        inner = "".join(render_block(c, ctx) for c in (content or []))
        title_html = f'<div class="aura-panel-title">{esc(title)}</div>' if title else ""
        return f'<div class="aura-panel">{title_html}{inner}</div>'

    if key in ("aura-inline-button", "aura-button"):
        label = (macro_params.get("summary", {}) or {}).get("value", "").strip() or "Button"
        params_raw = (macro_params.get("params", {}) or {}).get("value", "")
        config = decode_aura_params(params_raw)
        # Confirmed against real data: a linked button's url field can be a
        # nested object (e.g. {"href": "...", "target": "..."}), not always
        # a plain string like our test button (which had no link at all).
        # Handle both shapes rather than assuming one.
        url_raw = config.get("url") or config.get("href") or config.get("link")
        if isinstance(url_raw, dict):
            url = url_raw.get("href") or url_raw.get("url") or url_raw.get("value")
        elif isinstance(url_raw, str):
            url = url_raw
        else:
            url = None
        bg_color = ((config.get("states", {}) or {}).get("idle", {}) or {}).get("colors", {}).get("background", {})
        bg = bg_color.get("light") if isinstance(bg_color, dict) else None
        style = f' style="background-color:{esc(bg)}"' if bg else ""
        if url and isinstance(url, str):
            safe_url = html.escape(url, quote=True)
            return f'<a class="aura-button" href="{safe_url}"{style}>{esc(label)}</a>'
        return f'<span class="aura-button aura-button-static"{style}>{esc(label)}</span>'

    if key == "aura-tab-collection":
        return render_aura_tab_group(node, ctx)

    if key == "refined-steps":
        return render_refined_steps(node, ctx)

    if key == "refined-expands":
        return render_refined_expands(node, ctx)

    if key in ("refined-step", "refined-expand"):
        # These are pure markers, meaningfully rendered only inside their
        # real parent container above — if one ever appears bare (malformed
        # content), there's nothing meaningful to show standalone, so this
        # suppresses cleanly rather than showing broken placeholder text.
        return ""

    if key == "aura-html":
        params_raw = (macro_params.get("params", {}) or {}).get("value", "")
        config = decode_aura_params(params_raw)
        html_code = config.get("htmlCode", "") or ""
        css_code = config.get("cssCode", "") or ""
        if "legacy-redirect-notice" in html_code:
            # Confirmed against real content: a "this content moved to
            # support.appfire.com" banner, added to point Confluence
            # readers toward the old Refined-hosted site. Rendering it
            # here would be actively backwards — this new pipeline IS the
            # intended long-term replacement for exactly the place this
            # banner points to. It's meta-content about the migration
            # itself, not real product documentation, so it's suppressed
            # rather than rendered.
            return ""
        output = html_code
        if css_code:
            output = f"<style>{css_code}</style>{output}"
        return output

    if key == "contentbylabel":
        # Native Confluence macro that dynamically lists other pages
        # matching a label/CQL query. Confirmed via real content (PSJC's
        # SIL function reference pages use this for "See also" links to
        # related functions). Real support would need page labels, which
        # aren't currently fetched — a real feature to add later, not
        # something to fake. For now this suppresses cleanly rather than
        # showing broken placeholder text, which was actually leaking into
        # Google-facing FAQ structured data before this fix.
        return ""

    if key == "livesearch":
        # Native Confluence macro embedding a live, JS-driven search box
        # scoped to specific spaces — meaningless in a static site with no
        # Confluence backend behind it. Rather than just suppressing it,
        # this points to our own real, working search page instead, which
        # is a genuinely better replacement, not just a safe fallback.
        search_url = f"{ctx.get('path_prefix', '')}/search/"
        return f'<a class="livesearch-replacement" href="{search_url}">Search our docs →</a>'

    if key == "anchor":
        # Native Confluence macro creating a same-page jump target. Our
        # link-rewriting doesn't resolve in-page "#anchor-name" references
        # to begin with, so a real anchor id wouldn't currently be linked
        # to from anywhere — suppressing cleanly avoids a visible broken
        # placeholder for something with no functional effect either way.
        return ""

    if key == "excerpt":
        # Native Confluence excerpt — distinct from MultiExcerpt (a
        # separate Forge app). Confirmed against real content: this macro
        # supports a "hidden" flag, same concept as MultiExcerpt's, which
        # suppresses the excerpt at its OWN definition site while still
        # letting excerpt-include pull the content in elsewhere (the
        # registry captures it regardless, via the pre-scan). A
        # non-hidden excerpt is just normal visible content, rendered
        # inline as-is.
        hidden = (macro_params.get("hidden", {}) or {}).get("value") == "true"
        if hidden:
            return ""
        return "".join(render_block(c, ctx) for c in (content or []))

    if key == "excerpt-include":
        # Confirmed against real content: the source page is referenced
        # by TITLE (via an unusual empty-string parameter key), resolved
        # within the including page's own space by default — genuinely
        # different from MultiExcerpt's include, which always carries an
        # explicit source pageId and never needs to know its own context.
        title_ref = (macro_params.get("", {}) or {}).get("value", "").strip()
        excerpt_name = (macro_params.get("name", {}) or {}).get("value", "").strip()
        registry = ctx.get("excerpt_registry") or {}
        space_key = ctx.get("current_space_key")

        source_page_id = None
        if title_ref and space_key:
            source_page_id = registry.get("title_to_page_id", {}).get((space_key, title_ref))

        raw_content = None
        if source_page_id:
            if excerpt_name:
                raw_content = registry.get("by_page_and_name", {}).get((str(source_page_id), excerpt_name))
            if raw_content is None:
                raw_content = registry.get("by_page_unnamed", {}).get(str(source_page_id))

        if raw_content is not None:
            return "".join(render_block(c, ctx) for c in raw_content)
        return (
            f'<div class="img-placeholder">[Excerpt "{esc(excerpt_name)}" from page '
            f'"{esc(title_ref)}" not found]</div>'
        )

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

    if key_str.endswith("/static/table-plus") or key_str.endswith("/static/csv-table") or key_str.endswith("/static/json-table") or key_str.endswith("/static/attachment-table"):
        # Advanced Tables (Table Plus and siblings) — the real table data is
        # always present as literal nested content (confirmed against real
        # data), but the interactive behavior (sort, computed totals,
        # highlight) is normally rendered by the macro's own script and
        # isn't stored anywhere to extract. Reconstructing it as real
        # client-side JS instead of losing it: wrap the table with the
        # actual guestParams config as data-attributes, and a shared script
        # (embedded once per page) does the sorting/totals/highlighting.
        # A nested "table" node here would otherwise ALSO get wrapped in
        # the generic wide-table-wrapper (applied to every table site-wide)
        # — functionally harmless since the sorting JS uses a descendant
        # selector, but visually redundant (two nested bordered boxes
        # around the same table). This flag suppresses that specifically
        # inside an Advanced Table, which already has its own wrapper.
        ctx["_inside_advanced_table"] = ctx.get("_inside_advanced_table", 0) + 1
        table_html = "".join(render_block(c, ctx) for c in (content or []))
        ctx["_inside_advanced_table"] -= 1
        ctx["advanced_table_count"] = ctx.get("advanced_table_count", 0) + 1
        table_id = f"adv-table-{ctx['advanced_table_count']}"
        enable_sorting = "true" if guest_params.get("enableSorting") else "false"
        auto_total = "true" if guest_params.get("autoTotal") else "false"
        enable_highlighting = "true" if guest_params.get("enableHighlighting") else "false"
        highlight_color = esc(guest_params.get("highlightColor", "") or "")
        return (
            f'<div class="advanced-table" id="{table_id}" '
            f'data-enable-sorting="{enable_sorting}" '
            f'data-auto-total="{auto_total}" '
            f'data-enable-highlighting="{enable_highlighting}" '
            f'data-highlight-color="{highlight_color}">{table_html}</div>'
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
        lang = node.get("attrs", {}).get("language", "") or "text"
        text = "".join(c.get("text", "") for c in content if c.get("type") == "text")
        return (
            '<div class="code-block">'
            '<div class="code-block-header">'
            f'<span class="code-block-lang">{esc(lang)}</span>'
            '<button class="copy-code-btn" type="button">Copy</button>'
            '</div>'
            f'<pre><code class="language-{esc(lang)}">{esc(text)}</code></pre>'
            "</div>"
        )

    if ntype == "table":
        rows = "".join(render_block(c, ctx) for c in content)
        if ctx.get("_inside_advanced_table"):
            return f"<table>{rows}</table>"
        return (
            '<div class="wide-table-wrapper">'
            f'<div class="wide-table-scroll"><table>{rows}</table></div>'
            '<p class="wide-table-note">This table scrolls sideways →</p>'
            "</div>"
        )

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


def build_excerpt_registry(pages):
    """Pre-scans every page's RAW ADF for native Confluence "excerpt"
    macro definitions (extensionKey == "excerpt", extensionType
    com.atlassian.confluence.macro.core) — distinct from MultiExcerpt,
    which is a separate Forge/ecosystem app with its own different
    extensionKeys and a reference-by-explicit-pageId convention.

    Confirmed against real content: native excerpt-include references its
    source by PAGE TITLE (e.g. "Get started"), not by ID, and Confluence
    resolves an unqualified title within the including page's OWN space
    by default — so this also builds a (space_key, title) -> page_id
    index, which MultiExcerpt never needed since it always carries an
    explicit pageId.

    `pages` must have "_space_key" injected onto each page dict by the
    caller, since raw page data alone doesn't carry which space it came
    from once flattened across all spaces.

    Returns a dict with three indexes:
      - by_page_and_name: {(page_id, excerpt_name): raw_adf_content} for
        named excerpts (a page can define more than one).
      - by_page_unnamed: {page_id: raw_adf_content} — the first excerpt
        found with no name parameter, used as the fallback default when
        an include doesn't specify (or can't match) a name.
      - title_to_page_id: {(space_key, title): page_id} for resolving an
        excerpt-include's title reference.
    """
    by_page_and_name = {}
    by_page_unnamed = {}
    title_to_page_id = {}

    for p in pages:
        space_key = p.get("_space_key")
        title = p.get("title")
        page_id = p.get("id")
        if space_key and title and page_id:
            title_to_page_id[(space_key, title)] = page_id

    def walk(node, page_id):
        if not isinstance(node, dict):
            return
        if node.get("type") == "bodiedExtension":
            attrs = node.get("attrs", {}) or {}
            key = attrs.get("extensionKey", "") or ""
            if key == "excerpt":
                params = attrs.get("parameters", {}) or {}
                macro_params = params.get("macroParams", {}) or {}
                name = (macro_params.get("name", {}) or {}).get("value", "").strip()
                content = node.get("content", [])
                if name:
                    by_page_and_name[(str(page_id), name)] = content
                elif page_id not in by_page_unnamed:
                    by_page_unnamed[str(page_id)] = content
        for child in (node.get("content") or []):
            walk(child, page_id)

    for p in pages:
        adf = p.get("adf")
        if adf:
            walk(adf, p.get("id"))

    return {
        "by_page_and_name": by_page_and_name,
        "by_page_unnamed": by_page_unnamed,
        "title_to_page_id": title_to_page_id,
    }


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


def adf_to_html(adf_doc, unresolved_includes=None, link_titles=None, media_map=None, multiexcerpt_registry=None, path_prefix="", excerpt_registry=None, current_space_key=None):
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

    Returns (html_str, headings) — headings is the list of {id, level, text}
    dicts collected during this render, used both for any inline TOC macro
    on the page AND to build a real, always-present "On this page" panel
    that doesn't depend on whether the Confluence author happened to
    insert a {toc} macro at all.
    """
    if isinstance(adf_doc, str):
        adf_doc = json.loads(adf_doc)

    ctx = {
        "unresolved_includes": unresolved_includes,
        "link_titles": link_titles,
        "media_map": media_map,
        "multiexcerpt_registry": multiexcerpt_registry or {},
        "path_prefix": path_prefix,
        "excerpt_registry": excerpt_registry or {},
        "current_space_key": current_space_key,
        "headings": [],
        "heading_ids": set(),
    }
    content = adf_doc.get("content", [])
    html_str = "".join(render_block(node, ctx) for node in content)

    if "<!--TOC_MACRO-->" in html_str:
        html_str = html_str.replace("<!--TOC_MACRO-->", render_toc(ctx["headings"]))

    return html_str, ctx["headings"]


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
    out, _headings = adf_to_html(sample)
    assert '<nav class="toc">' in out
    assert 'href="#overview"' in out and 'href="#overview-2"' in out
    assert 'id="overview"' in out and 'id="overview-2"' in out
    assert 'page-properties' in out and 'Christie' in out
    assert "Fallback content should still show up." in out
    assert "Unmapped macro: totally-empty-unknown-macro" in out
    assert "Unmapped macro: some-random" not in out  # this one had content, shouldn't be flagged
    print("adf_transform.py v3 self-test passed")
