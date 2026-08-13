#!/usr/bin/env python3
"""
transform.py — generic Confluence HTML+ -> static semantic HTML converter.

This is the actual reusable piece: feed it the raw `body` string that
Atlassian:getConfluencePage returns (contentFormat="html") for ANY page,
and it produces clean HTML. Nothing here is specific to any one page's
content — that's the whole point.

Handles the data-type vocabulary we've seen in the FOX space so far:
  - section[data-type="layout-two-equal"] / div[data-type="column"]  -> .columns grid
  - div[data-type="panel-note|panel-success|...]                    -> .panel divs
  - figure[data-type="media-single"] > div[data-type="media"]       -> placeholder (no binary fetch yet)
  - details/summary                                                 -> passed through as-is (already semantic)
  - div[data-type="extension"][data-extension-key="iframe"]         -> real <iframe> (YouTube etc.)
  - div[data-type="extension"][data-extension-key="include"]        -> resolved by caller (footer include), stripped if empty
  - div[data-type="embed-card"] > iframe (youtube watch url)        -> rewritten to real embeddable /embed/ url

Anything not recognized is passed through unchanged rather than dropped,
so the transformer degrades safely on macro types we haven't mapped yet
instead of silently eating content (the exact failure mode we hit with
the markdown-extraction approach on the Get Started audit).
"""

import json
import re
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup


PANEL_CLASSES = {
    "panel-note": "panel panel-note",
    "panel-success": "panel panel-success",
    "panel-warning": "panel panel-warning",
    "panel-info": "panel panel-note",
    "panel-error": "panel panel-warning",
}


def _youtube_id_from_url(url):
    """Extract a YouTube video ID from either a watch or embed URL, plus start time if present."""
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    video_id = None
    start = None
    if "youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc:
        if "/embed/" in parsed.path:
            video_id = parsed.path.split("/embed/")[-1]
        elif parsed.path == "/watch":
            video_id = qs.get("v", [None])[0]
        elif "youtu.be" in parsed.netloc:
            video_id = parsed.path.lstrip("/")
        if "t" in qs:
            m = re.match(r"(\d+)", qs["t"][0])
            if m:
                start = m.group(1)
        if "si" in qs and video_id and "?" in video_id:
            video_id = video_id.split("?")[0]
    return video_id, start


def transform_body(raw_html, unresolved_includes=None):
    """
    raw_html: the `body` string from Atlassian:getConfluencePage (contentFormat="html")
    unresolved_includes: optional dict of {page_title: html_string} to inline "Include Page" macros.
    Returns: clean semantic HTML string ready to drop into the page shell's <main>.
    """
    soup = BeautifulSoup(raw_html, "html.parser")
    unresolved_includes = unresolved_includes or {}

    # --- Layout sections -> .columns grid -------------------------------
    for section in soup.find_all("section", attrs={"data-type": lambda v: v and v.startswith("layout-")}):
        columns = section.find_all("div", attrs={"data-type": "column"}, recursive=False)
        section.name = "div"
        section["class"] = section.get("class", []) + ["columns"]
        del section["data-type"]
        for col in columns:
            col.name = "div"
            for attr in list(col.attrs):
                del col[attr]

    # --- Panels -----------------------------------------------------------
    for panel_type, css_class in PANEL_CLASSES.items():
        for panel in soup.find_all("div", attrs={"data-type": panel_type}):
            panel.name = "div"
            panel["class"] = css_class.split()
            del panel["data-type"]

    # --- Media figures -> placeholder (no binary fetch yet) --------------
    for figure in soup.find_all("figure", attrs={"data-type": "media-single"}):
        media_div = figure.find("div", attrs={"data-type": "media"})
        caption = media_div.get_text(strip=True) if media_div else "Image"
        placeholder = soup.new_tag("div", attrs={"class": "img-placeholder"})
        tag = soup.new_tag("span", attrs={"class": "tag"})
        tag.string = "Image — asset pipeline pending"
        placeholder.append(tag)
        placeholder.append(soup.new_tag("br"))
        placeholder.append(caption)
        figure.replace_with(placeholder)

    # --- Extension macros ---------------------------------------------------
    for ext in soup.find_all("div", attrs={"data-type": "extension"}):
        ext_key = ext.get("data-extension-key")
        params_raw = ext.get("data-parameters", "{}")
        try:
            params = json.loads(params_raw)
        except (json.JSONDecodeError, TypeError):
            params = {}

        if ext_key == "iframe":
            macro_params = params.get("macroParams", {})
            src = macro_params.get("src", {}).get("value")
            if src:
                video_id, start = _youtube_id_from_url(src)
                if video_id:
                    embed = soup.new_tag("div", attrs={"class": "video-embed"})
                    iframe_src = f"https://www.youtube.com/embed/{video_id}"
                    if start:
                        iframe_src += f"?start={start}"
                    iframe = soup.new_tag("iframe", src=iframe_src, allowfullscreen="")
                    embed.append(iframe)
                    ext.replace_with(embed)
                    continue
                else:
                    iframe = soup.new_tag("iframe", src=src)
                    ext.replace_with(iframe)
                    continue
            ext.decompose()

        elif ext_key == "include":
            macro_params = params.get("macroParams", {})
            included_title = macro_params.get("", {}).get("value", "").strip()
            included_html = unresolved_includes.get(included_title, "").strip()
            if included_html and included_html not in ("", "<p></p>"):
                include_div = soup.new_tag("div", attrs={"class": "included-content"})
                include_div.append(BeautifulSoup(included_html, "html.parser"))
                ext.replace_with(include_div)
            else:
                ext.decompose()  # empty include, nothing to render

        else:
            # Unknown macro type — leave a visible marker instead of silently dropping it,
            # so future build passes know there's a macro type to map.
            note = soup.new_tag("div", attrs={"class": "img-placeholder"})
            note.string = f"[Unmapped macro: {ext_key or 'unknown'} — needs a transform rule]"
            ext.replace_with(note)

    # --- embed-card iframes (raw YouTube watch URLs) -----------------------
    for card in soup.find_all("div", attrs={"data-type": "embed-card"}):
        iframe = card.find("iframe")
        if iframe and iframe.get("src"):
            video_id, start = _youtube_id_from_url(iframe["src"])
            if video_id:
                embed = soup.new_tag("div", attrs={"class": "video-embed"})
                iframe_src = f"https://www.youtube.com/embed/{video_id}"
                if start:
                    iframe_src += f"?start={start}"
                new_iframe = soup.new_tag("iframe", src=iframe_src, allowfullscreen="")
                embed.append(new_iframe)
                card.replace_with(embed)
                continue
        card.unwrap()

    # --- details/summary: already semantic, leave as-is ---------------------
    # (no transformation needed — this is the whole reason FAQ pages are easy)

    # --- data-card-appearance inline links: strip the attribute, keep the link
    for a in soup.find_all("a", attrs={"data-card-appearance": True}):
        del a["data-card-appearance"]

    return str(soup)


def generate_meta_description(body_html, max_len=155):
    """Very simple auto-generated fallback meta description: first real paragraph, trimmed.
    In production this is the same job your SEO auditor's Claude-API step already does —
    swap this for that call once we're past the pilot."""
    soup = BeautifulSoup(body_html, "html.parser")
    for p in soup.find_all("p"):
        text = p.get_text(" ", strip=True)
        text = re.sub(r"\s+", " ", text)
        if len(text) > 40:
            if len(text) <= max_len:
                return text
            return text[:max_len].rsplit(" ", 1)[0] + "…"
    return ""


if __name__ == "__main__":
    # Smoke test against a tiny fixture so this can be verified without hitting the API.
    sample = '''<section data-type="layout-two-equal"><div data-type="column" data-width="50">
    <h2>Overview</h2><p>This is a real test paragraph long enough to become a meta description candidate for sure.</p>
    </div><div data-type="column" data-width="50"><p></p></div></section>
    <div data-type="panel-note"><p>A note.</p></div>
    <figure data-type="media-single"><div data-type="media">A caption</div></figure>'''
    out = transform_body(sample)
    assert "columns" in out
    assert "panel-note" in out
    assert "img-placeholder" in out
    print("transform.py self-test passed")
    print(generate_meta_description(sample))
