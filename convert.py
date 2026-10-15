#!/usr/bin/env python3
"""Convert one fetched Confluence space (data/{KEY}/pages.json) into a
Docusaurus docs folder plus a conversion report.

Usage:
  python convert.py --data data/POKERADO/pages.json --assets assets --out site

Writes:
  {out}/docs/...                 MDX pages, folders mirror the page tree
  {out}/static/img/...           images copied from the assets folder
  {out}/CONVERSION_REPORT.md     what converted clean and what needs a human

This is a one-time migration tool. Anything it can't map is rendered as a
visible admonition AND listed in the report, never silently dropped.
"""
import argparse
import base64
import datetime
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict
from urllib.parse import quote, unquote

HIDDEN_PREFIXES = ("_", "[Includes]")


def is_hidden(title):
    t = title or ""
    return t.startswith(HIDDEN_PREFIXES) or t.strip().lower() == "includes"


def url_title_segment(title):
    return quote((title or "untitled").replace(" ", "+"), safe="+()")


def slugify(title, limit=60):
    s = re.sub(r"[^a-z0-9]+", "-", (title or "untitled").lower()).strip("-")
    return (s[:limit].strip("-")) or "page"


def yaml_str(s):
    return json.dumps(s or "", ensure_ascii=False)


class Report:
    def __init__(self):
        self.pages = {}
        self.totals = Counter()
        self.unmapped = Counter()

    def issue(self, page, kind, detail=""):
        self.pages.setdefault(page, []).append((kind, detail))
        self.totals[kind] += 1


class Ctx:
    def __init__(self, pages, space_key, media, hidden_by_title, report):
        self.pages = pages
        self.space_key = space_key
        self.media = media
        self.hidden = hidden_by_title
        self.report = report
        self.page = ""
        self.needed_images = set()
        self.uses_tabs = False
        self.include_depth = 0
        self.heading_shift = 0


# ---------- inline ----------

def esc(text):
    text = text.replace("\\", "\\\\")
    for ch in "*_`[]":
        text = text.replace(ch, "\\" + ch)
    text = text.replace("{", "\\{").replace("}", "\\}")
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    return text


def wrap_marks(text, marks, ctx):
    lead = text[: len(text) - len(text.lstrip())]
    trail = text[len(text.rstrip()):]
    core = text.strip()
    if not core:
        return text
    for m in marks:
        t = m.get("type")
        if t == "code":
            core = "`" + core.replace("`", "'") + "`"
        elif t == "strong":
            core = f"**{core}**"
        elif t == "em":
            core = f"*{core}*"
        elif t == "strike":
            core = f"~~{core}~~"
        elif t == "underline":
            core = f"<u>{core}</u>"
        elif t == "subsup":
            tag = "sub" if (m.get("attrs") or {}).get("type") == "sub" else "sup"
            core = f"<{tag}>{core}</{tag}>"
        elif t == "link":
            href = rewrite_href((m.get("attrs") or {}).get("href", ""), ctx)
            core = f"[{core}]({href})"
        # textColor, backgroundColor, alignment, indentation: dropped
    return lead + core + trail


PAGE_RE = re.compile(r"/wiki/spaces/([^/]+)/pages/(\d+)")


def rewrite_href(href, ctx):
    m = PAGE_RE.search(href or "")
    if not m:
        if href and "/wiki/x/" in href:
            ctx.report.issue(ctx.page, "unresolved short link", href)
        return href or "#"
    key, pid = m.group(1), m.group(2)
    if key == ctx.space_key and pid in ctx.pages:
        return page_path(pid, ctx)
    ctx.report.issue(ctx.page, "cross-space link", href)
    return href


def page_path(pid, ctx):
    return f"/space/{ctx.space_key}/{pid}/{url_title_segment(ctx.pages[pid]['title'])}/"


def inline(nodes, ctx):
    out = []
    for n in nodes or []:
        t = n.get("type")
        if t == "text":
            out.append(wrap_marks(esc(n.get("text", "")), n.get("marks") or [], ctx))
        elif t == "hardBreak":
            out.append("<br />")
        elif t == "mention":
            out.append("@" + esc((n.get("attrs") or {}).get("text", "user").lstrip("@")))
        elif t == "emoji":
            a = n.get("attrs") or {}
            out.append(a.get("text") or a.get("shortName") or "")
        elif t == "status":
            out.append("`" + (n.get("attrs") or {}).get("text", "").replace("`", "'") + "`")
        elif t == "date":
            ts = (n.get("attrs") or {}).get("timestamp")
            try:
                d = datetime.datetime.fromtimestamp(int(ts) / 1000, datetime.timezone.utc)
                out.append(d.strftime("%B %-d, %Y"))
            except Exception:
                out.append("")
        elif t == "inlineCard":
            url = (n.get("attrs") or {}).get("url", "")
            href = rewrite_href(url, ctx)
            m = PAGE_RE.search(url)
            label = ctx.pages[m.group(2)]["title"] if m and m.group(2) in ctx.pages and m.group(1) == ctx.space_key else url
            out.append(f"[{esc(label)}]({href})")
        elif t == "inlineExtension":
            out.append(extension_inline(n, ctx))
        elif t == "mediaInline":
            ctx.report.issue(ctx.page, "inline media dropped")
        else:
            ctx.report.issue(ctx.page, "unmapped inline node", t)
    return "".join(out)


def extension_inline(n, ctx):
    key = (n.get("attrs") or {}).get("extensionKey", "")
    ctx.report.unmapped[key] += 1
    ctx.report.issue(ctx.page, "unmapped inline macro", key)
    return f"`[unmapped macro: {key.split('/')[-1]}]`"


# ---------- blocks ----------

def indent(lines, n):
    pad = " " * n
    return [(pad + ln) if ln.strip() else "" for ln in lines]


def blocks(nodes, ctx):
    """Render a list of block nodes to a list of lines, blank line between."""
    out = []
    for n in nodes or []:
        lines = block(n, ctx)
        if lines:
            if out:
                out.append("")
            out.extend(lines)
    return out


def block(n, ctx):
    t = n.get("type")
    c = n.get("content") or []
    a = n.get("attrs") or {}

    if t == "paragraph":
        s = inline(c, ctx).strip()
        return [s] if s else []
    if t == "heading":
        lvl = min(6, max(1, a.get("level", 2)) + ctx.heading_shift)
        return ["#" * lvl + " " + inline(c, ctx).strip()]
    if t in ("bulletList", "orderedList"):
        return list_lines(n, ctx)
    if t == "taskList":
        out = []
        for item in c:
            done = (item.get("attrs") or {}).get("state") == "DONE"
            out.append(f"- [{'x' if done else ' '}] " + inline(item.get("content"), ctx).strip())
        return out
    if t == "codeBlock":
        text = "".join(x.get("text", "") for x in c)
        lang = (a.get("language") or "").lower()
        lang = "" if lang in ("none", "text", "plain") else re.sub(r"[^a-z0-9+#-]", "", lang)
        fence = "````" if "```" in text else "```"
        return [fence + lang] + text.split("\n") + [fence]
    if t == "rule":
        return ["---"]
    if t == "blockquote":
        return ["> " + ln if ln else ">" for ln in blocks(c, ctx)]
    if t == "panel":
        return panel(a.get("panelType", "info"), "", blocks(c, ctx), ctx)
    if t in ("expand", "nestedExpand"):
        return details(a.get("title", ""), blocks(c, ctx))
    if t in ("mediaSingle", "mediaGroup"):
        out = []
        for m in c:
            if m.get("type") == "media":
                out.append(media(m, ctx))
            elif m.get("type") == "caption":
                out.append("*" + inline(m.get("content"), ctx).strip() + "*")
        return [x for x in out if x]
    if t == "table":
        return table(n, ctx)
    if t == "layoutSection":
        cols = [x for x in c if x.get("type") == "layoutColumn"]
        if len(cols) > 1:
            ctx.report.issue(ctx.page, "multi-column layout flattened", f"{len(cols)} columns")
        return blocks([b for col in cols for b in (col.get("content") or [])], ctx)
    if t == "embedCard":
        return embed(a.get("url", ""), ctx)
    if t in ("extension", "bodiedExtension"):
        return extension(n, ctx)
    ctx.report.issue(ctx.page, "unmapped block node", t or "?")
    return [":::caution", f"Unmapped block: {t}", ":::"]


def list_lines(n, ctx):
    ordered = n.get("type") == "orderedList"
    start = (n.get("attrs") or {}).get("order", 1) or 1
    out = []
    for i, item in enumerate(n.get("content") or []):
        marker = f"{start + i}. " if ordered else "- "
        body = []
        for child in item.get("content") or []:
            lines = block(child, ctx)
            if not lines:
                continue
            if body and child.get("type") not in ("bulletList", "orderedList"):
                body.append("")
            body.extend(lines)
        if not body:
            continue
        first = True
        for ln in body:
            if first:
                out.append(marker + ln)
                first = False
            else:
                out.append((" " * len(marker) + ln) if ln.strip() else "")
    return out


def panel(ptype, title, body, ctx):
    kind = {"info": "info", "note": "note", "warning": "warning",
            "error": "danger", "success": "tip", "custom": "note"}.get(ptype, "note")
    if ptype == "custom":
        ctx.report.issue(ctx.page, "custom panel color dropped")
    head = f":::{kind}[{title}]" if title else f":::{kind}"
    return [head, ""] + body + ["", ":::"]


def details(title, body):
    return ["<details>", f"<summary>{esc(title) or 'Details'}</summary>", ""] + body + ["", "</details>"]


def media(m, ctx):
    a = m.get("attrs") or {}
    alt = (a.get("alt") or "").replace("[", "(").replace("]", ")").replace("\n", " ")
    if a.get("type") == "external" and a.get("url"):
        return f"![{alt}]({a['url']})"
    mid = a.get("id")
    local = ctx.media.get(mid)
    if local:
        fname = os.path.basename(local)
        ctx.needed_images.add(fname)
        return f"![{alt}](/img/{fname})"
    ctx.report.issue(ctx.page, "image not in media map", str(mid))
    return f":::caution\nMissing image: {alt or mid}\n:::"


def embed(url, ctx):
    src = None
    m = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)", url)
    if m:
        src = f"https://www.youtube.com/embed/{m.group(1)}"
    m = re.search(r"vimeo\.com/(\d+)", url)
    if m:
        src = f"https://player.vimeo.com/video/{m.group(1)}"
    m = re.search(r"loom\.com/share/([\w]+)", url)
    if m:
        src = f"https://www.loom.com/embed/{m.group(1)}"
    if src:
        return [f'<iframe src="{src}" title="Video" width="100%" height="400" allowFullScreen></iframe>']
    return [f"[{url}]({url})"]


def cell_text(cell, ctx):
    parts, lossy = [], False
    for child in cell.get("content") or []:
        t = child.get("type")
        if t == "paragraph":
            s = inline(child.get("content"), ctx).strip()
            if s:
                parts.append(s)
        elif t in ("bulletList", "orderedList"):
            lossy = True
            for ln in list_lines(child, ctx):
                parts.append(ln.strip())
        else:
            lossy = True
            parts.extend(x.strip() for x in block(child, ctx) if x.strip())
    return "<br />".join(parts).replace("|", "\\|"), lossy


def table(n, ctx):
    rows = []
    merged = block_cells = False
    for r in n.get("content") or []:
        row = []
        for cell in r.get("content") or []:
            a = cell.get("attrs") or {}
            if (a.get("colspan") or 1) > 1 or (a.get("rowspan") or 1) > 1:
                merged = True
            txt, lossy = cell_text(cell, ctx)
            block_cells = block_cells or lossy
            row.append(txt)
        rows.append(row)
    if not rows:
        return []
    if merged:
        ctx.report.issue(ctx.page, "table has merged cells (merge lost)")
    if block_cells:
        ctx.report.issue(ctx.page, "table cell with lists or blocks (flattened)")
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return out


def params_of(attrs):
    p = attrs.get("parameters") or {}
    return p.get("macroParams") or {}, p.get("guestParams") or {}


def mp(macro_params, key):
    return ((macro_params.get(key) or {}).get("value") or "").strip()


def group_flat(content, marker_key, label_fn):
    groups, label, cur = [], None, []
    for ch in content or []:
        ca = ch.get("attrs") or {}
        if ch.get("type") == "extension" and ca.get("extensionKey") == marker_key:
            if label is not None:
                groups.append((label, cur))
            label, cur = label_fn(ca), []
        elif label is not None:
            cur.append(ch)
    if label is not None:
        groups.append((label, cur))
    return groups


def decode_aura(raw):
    try:
        return json.loads(unquote(base64.b64decode(raw).decode("utf-8")))
    except Exception:
        return {}


def extension(n, ctx):
    a = n.get("attrs") or {}
    key = a.get("extensionKey", "") or ""
    short = key.split("/")[-1]
    macro_params, guest = params_of(a)
    content = n.get("content") or []

    if key in ("toc", "appfire-confluence-analytics", "anchor", "contentbylabel", "livesearch", "children"):
        ctx.report.issue(ctx.page, f"macro dropped: {key}")
        return []
    if key == "include":
        title = mp(macro_params, "")
        src = ctx.hidden.get(title)
        if src and ctx.include_depth < 3:
            ctx.include_depth += 1
            lines = blocks((src.get("adf") or {}).get("content"), ctx)
            ctx.include_depth -= 1
            ctx.report.issue(ctx.page, "include inlined", title)
            return lines
        ctx.report.issue(ctx.page, "include not found", title)
        return []
    if key == "iframe":
        src = mp(macro_params, "src") or mp(macro_params, "")
        return embed(src, ctx) if src else []
    if key == "aura-html":
        cfg = decode_aura(mp(macro_params, "params"))
        if "legacy-redirect-notice" in (cfg.get("htmlCode") or ""):
            return []
        ctx.report.issue(ctx.page, "raw HTML macro dropped (aura-html)")
        return [":::caution", "Raw HTML block (aura-html) was not converted.", ":::"]
    if key == "aura-panel":
        return panel("info", mp(macro_params, "summary"), blocks(content, ctx), ctx)
    if key in ("aura-inline-button", "aura-button"):
        label = mp(macro_params, "summary") or "Button"
        cfg = decode_aura(mp(macro_params, "params"))
        u = cfg.get("url") or cfg.get("href") or cfg.get("link")
        if isinstance(u, dict):
            u = u.get("href") or u.get("url") or u.get("value")
        return [f"[{esc(label)}]({u})"] if isinstance(u, str) and u else [f"**{esc(label)}**"]
    if key == "aura-tab-collection":
        tabs = group_flat(content, "aura-tab", lambda ca: mp(params_of(ca)[0], "summary") or "Tab")
        if not tabs:
            return []
        ctx.uses_tabs = True
        out = ["<Tabs>"]
        for title, nodes in tabs:
            out += [f'<TabItem value={json.dumps(slugify(title))} label={json.dumps(title)}>', ""]
            out += blocks(nodes, ctx)
            out += ["", "</TabItem>"]
        return out + ["</Tabs>"]
    if key == "refined-steps":
        steps = group_flat(content, "refined-step", lambda ca: mp(params_of(ca)[0], "text") or "1")
        out = []
        for i, (num, nodes) in enumerate(steps):
            body = blocks(nodes, ctx) or [""]
            marker = f"{num if num.isdigit() else i + 1}. "
            for j, ln in enumerate(body):
                out.append(marker + ln if j == 0 else ((" " * len(marker) + ln) if ln.strip() else ""))
        return out
    if key == "refined-expands":
        out = []
        for title, nodes in group_flat(content, "refined-expand", lambda ca: mp(params_of(ca)[0], "title") or "Details"):
            if out:
                out.append("")
            out += details(title, blocks(nodes, ctx))
        return out
    if key in ("refined-step", "refined-expand"):
        return []
    if short in ("table-plus", "csv-table", "json-table", "attachment-table"):
        ctx.report.issue(ctx.page, "Table Plus converted to plain table (sorting and filters lost)")
        return blocks(content, ctx)
    if key in ("excerpt", "detail", "details", "page-properties", "panel", "info", "note", "warning", "tip"):
        if key in ("info", "note", "warning", "tip"):
            return panel({"tip": "success"}.get(key, key), mp(macro_params, "title"), blocks(content, ctx), ctx)
        if key == "excerpt" and mp(macro_params, "hidden") == "true":
            ctx.report.issue(ctx.page, "hidden excerpt dropped")
            return []
        return blocks(content, ctx)

    # unmapped
    ctx.report.unmapped[short or key] += 1
    ctx.report.issue(ctx.page, "unmapped macro", short or key)
    if content:
        return [":::caution[Unmapped macro: " + (short or key) + "]", ""] + blocks(content, ctx) + ["", ":::"]
    return [":::caution", f"Unmapped macro: {short or key}", ":::"]


# ---------- site build ----------

def build(args):
    with open(args.data) as f:
        data = json.load(f)
    space_key = data.get("space_key") or "SPACE"
    media_map = data.get("media") or {}
    raw = data.get("pages") or []
    report = Report()

    hidden_by_title = {p["title"]: p for p in raw if is_hidden(p.get("title")) and p.get("adf")}
    pages = {p["id"]: p for p in raw if p.get("adf") and not is_hidden(p.get("title"))}
    skipped = [p for p in raw if not p.get("adf") and not is_hidden(p.get("title"))]
    for p in skipped:
        report.issue(p.get("title", "?"), "page has no body (skipped)")

    children = defaultdict(list)
    roots = []
    for pid, p in pages.items():
        parent = p.get("parent_id")
        (children[parent] if parent in pages else roots).append(pid)
    pos = lambda i: (pages[i].get("position") is None, pages[i].get("position") or 0, pages[i]["title"])
    for k in children:
        children[k].sort(key=pos)
    roots.sort(key=pos)

    ctx = Ctx(pages, space_key, media_map, hidden_by_title, report)
    docs = os.path.join(args.out, "docs")
    if os.path.isdir(docs):
        shutil.rmtree(docs)
    os.makedirs(docs)
    needed = set()
    written = [0]

    def write_page(pid, path, position, slug):
        p = pages[pid]
        ctx.page = p["title"]
        ctx.uses_tabs = False
        adf = p["adf"].get("content") or []
        ctx.heading_shift = 1 if any(n.get("type") == "heading" and (n.get("attrs") or {}).get("level") == 1 for n in adf) else 0
        body = "\n".join(blocks(adf, ctx)).strip() + "\n"
        needed.update(ctx.needed_images)
        ctx.needed_images = set()
        fm = ["---", f"title: {yaml_str(p['title'])}", f"slug: {slug}"]
        if position is not None:
            fm.append(f"sidebar_position: {position}")
        fm.append(f"custom_edit_url: https://{args.site}/wiki/spaces/{space_key}/pages/{pid}")
        lu = (p.get("last_updated") or "")[:10]
        if lu:
            fm.append(f"last_update:\n  date: {lu}")
        fm.append("---\n\n")
        imports = "import Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\n\n" if ctx.uses_tabs else ""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write("\n".join(fm) + imports + body)
        written[0] += 1

    def unique(names, base, pid):
        n = base
        if n in names:
            n = f"{base}-{pid}"
        names.add(n)
        return n

    def walk(pid, folder, position, is_home=False):
        p = pages[pid]
        slug = "/" if is_home else f"/space/{space_key}/{pid}/{url_title_segment(p['title'])}"
        kids = children.get(pid, [])
        if kids and not is_home:
            d = os.path.join(folder, names_for(folder, slugify(p["title"]), pid))
            write_page(pid, os.path.join(d, "index.mdx"), position, slug)
            with open(os.path.join(d, "_category_.json"), "w") as f:
                json.dump({"label": p["title"], "position": position}, f)
            names = set()
            for i, k in enumerate(kids, 1):
                walk_child(k, d, i, names)
        elif is_home:
            write_page(pid, os.path.join(folder, "index.mdx"), 0, slug)
        else:
            write_page(pid, os.path.join(folder, names_for(folder, slugify(p["title"]), pid) + ".mdx"), position, slug)

    used = defaultdict(set)

    def names_for(folder, base, pid):
        return unique(used[folder], base, pid)

    def walk_child(pid, folder, position, _names):
        walk(pid, folder, position)

    for i, r in enumerate(roots):
        if i == 0:
            walk(r, docs, 0, is_home=True)
            for j, k in enumerate(children.get(r, []), 1):
                walk(k, docs, j)
        else:
            walk(r, docs, len(children.get(roots[0], [])) + i)

    # images
    img_dir = os.path.join(args.out, "static", "img")
    os.makedirs(img_dir, exist_ok=True)
    copied = missing = 0
    for fname in sorted(needed):
        src = os.path.join(args.assets, fname)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(img_dir, fname))
            copied += 1
        else:
            missing += 1
            report.issue("(site-wide)", "image file missing from assets folder", fname)

    write_report(args, space_key, raw, pages, hidden_by_title, report, copied, missing, written[0])
    print(f"{space_key}: wrote {written[0]} pages, {copied} images ({missing} missing). See {os.path.join(args.out, 'CONVERSION_REPORT.md')}")


def write_report(args, space_key, raw, pages, hidden, report, copied, missing, written):
    clean = [t for t in (p["title"] for p in pages.values()) if t not in report.pages]
    lines = [f"# Conversion report: {space_key}", "",
             f"- Pages in space: {len(raw)} ({len(hidden)} hidden include pages excluded)",
             f"- Pages written: {written}",
             f"- Converted with no issues: {len(clean)}",
             f"- Pages with issues: {len([k for k in report.pages if k in {p['title'] for p in pages.values()}])}",
             f"- Images copied: {copied}, missing: {missing}", ""]
    if report.totals:
        lines += ["## Issue totals", ""]
        lines += [f"- {k}: {v}" for k, v in report.totals.most_common()]
        lines.append("")
    if report.unmapped:
        lines += ["## Unmapped macros (build components for these first)", ""]
        lines += [f"- `{k}`: {v} uses" for k, v in report.unmapped.most_common()]
        lines.append("")
    lines += ["## Pages needing review", ""]
    for title, items in sorted(report.pages.items()):
        lines.append(f"### {title}")
        for kind, detail in items:
            lines.append(f"- {kind}" + (f": {detail}" if detail else ""))
        lines.append("")
    with open(os.path.join(args.out, "CONVERSION_REPORT.md"), "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="path to data/{KEY}/pages.json")
    ap.add_argument("--assets", default="assets", help="repo assets folder holding downloaded images")
    ap.add_argument("--out", default="site", help="Docusaurus project folder to write into")
    ap.add_argument("--site", default="appfire.atlassian.net", help="Confluence host, used for Edit this page links")
    build(ap.parse_args())
