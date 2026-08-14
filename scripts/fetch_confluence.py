#!/usr/bin/env python3
"""
fetch_confluence.py — pulls every page in a Confluence space via the real
REST API v2 and writes them to data/pages.json for generate_site.py to
build from. This is the piece that makes the site live instead of frozen.

Auth: Confluence Cloud REST API uses HTTP Basic auth with your Atlassian
account email + an API token (NOT your password). Create a token at:
  https://id.atlassian.com/manage-profile/security/api-tokens

Required environment variables (set as GitHub Actions secrets, never
committed to the repo):
  CONFLUENCE_EMAIL       -> christie.gera@appfire.com
  CONFLUENCE_API_TOKEN   -> the token itself

Usage:
  python3 fetch_confluence.py --space FOX --site appfire.atlassian.net
"""

import argparse
import json
import os
import sys
import time
import urllib.parse

import requests

API_VERSION = "v2"

MEDIA_TYPE_EXT = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/gif": ".gif",
    "image/svg+xml": ".svg",
    "image/webp": ".webp",
    "application/pdf": ".pdf",
}


def get_auth():
    email = os.environ.get("CONFLUENCE_EMAIL")
    token = os.environ.get("CONFLUENCE_API_TOKEN")
    if not email or not token:
        sys.exit(
            "Missing CONFLUENCE_EMAIL and/or CONFLUENCE_API_TOKEN environment variables.\n"
            "Set these as GitHub Actions repo secrets — never hardcode a token in this file."
        )
    return (email, token)


def get_space_id(base_url, space_key, auth):
    url = f"{base_url}/wiki/api/{API_VERSION}/spaces"
    resp = requests.get(url, params={"keys": space_key}, auth=auth, timeout=30)
    resp.raise_for_status()
    results = resp.json().get("results", [])
    if not results:
        sys.exit(f"Space key '{space_key}' not found — check the key and your account's access to it.")
    return results[0]["id"], results[0].get("name", space_key)


def get_all_pages(base_url, space_id, auth):
    """Paginate through every current page in the space, requesting ADF body content."""
    pages = []
    url = f"{base_url}/wiki/api/{API_VERSION}/spaces/{space_id}/pages"
    params = {
        "body-format": "atlas_doc_format",
        "limit": 100,
        "status": "current",
    }
    while url:
        resp = requests.get(url, params=params, auth=auth, timeout=30)
        if resp.status_code == 429:
            wait = int(resp.headers.get("Retry-After", "5"))
            print(f"Rate limited, waiting {wait}s...", file=sys.stderr)
            time.sleep(wait)
            continue
        resp.raise_for_status()
        data = resp.json()
        pages.extend(data.get("results", []))

        next_link = data.get("_links", {}).get("next")
        if next_link:
            url = base_url + next_link
            params = {}  # next_link already has query params baked in
        else:
            url = None
    return pages


def normalize_page(raw_page):
    body = raw_page.get("body", {})
    adf_raw = body.get("atlas_doc_format", {}).get("value")
    adf = None
    if adf_raw:
        try:
            adf = json.loads(adf_raw)
        except json.JSONDecodeError as e:
            print(f"WARNING: page {raw_page.get('id')} ADF failed to parse: {e}", file=sys.stderr)

    return {
        "id": raw_page.get("id"),
        "title": raw_page.get("title"),
        "parent_id": raw_page.get("parentId"),
        "version": raw_page.get("version", {}).get("number"),
        "adf": adf,
    }


def get_attachments_for_page(base_url, page_id, auth):
    """List a page's attachments via the classic REST v1 endpoint, expanding
    extensions.fileId — this is the field that (per Atlassian's docs) matches
    the `id` referenced by ADF media nodes. Untested against a real space
    until the first live run; if fileId doesn't come back or doesn't match,
    that'll show up as images staying on placeholders rather than a crash."""
    attachments = []
    url = f"{base_url}/wiki/rest/api/content/{page_id}/child/attachment"
    params = {"limit": 200, "expand": "extensions.fileId,metadata.mediaType"}
    while url:
        resp = requests.get(url, params=params, auth=auth, timeout=30)
        if resp.status_code == 429:
            wait = int(resp.headers.get("Retry-After", "5"))
            time.sleep(wait)
            continue
        if resp.status_code == 404:
            return []  # page has no attachments endpoint content, not fatal
        resp.raise_for_status()
        data = resp.json()
        attachments.extend(data.get("results", []))
        next_link = data.get("_links", {}).get("next")
        if next_link:
            url = base_url + "/wiki" + next_link if not next_link.startswith("http") else next_link
            params = {}
        else:
            url = None
    return attachments


def download_attachments(base_url, auth, pages, assets_dir):
    """Downloads every attachment referenced by the fetched pages into
    assets_dir, keyed by the ADF media fileId so generate_site.py can look
    up a local path for each <img>. Skips re-downloading files that already
    exist locally, since most images don't change between runs."""
    os.makedirs(assets_dir, exist_ok=True)
    media_map = {}
    total_pages = len(pages)

    for i, p in enumerate(pages, 1):
        page_id = p["id"]
        try:
            attachments = get_attachments_for_page(base_url, page_id, auth)
        except requests.RequestException as e:
            print(f"WARNING: could not list attachments for page {page_id}: {e}", file=sys.stderr)
            continue

        for att in attachments:
            file_id = att.get("extensions", {}).get("fileId")
            if not file_id:
                continue  # can't match this attachment to an ADF media node without it

            download_path = att.get("_links", {}).get("download")
            if not download_path:
                continue

            title = att.get("title", file_id)
            ext = os.path.splitext(title)[1]
            if not ext:
                media_type = att.get("metadata", {}).get("mediaType", "")
                ext = MEDIA_TYPE_EXT.get(media_type, "")

            local_name = f"{file_id}{ext}"
            local_path = os.path.join(assets_dir, local_name)

            if not os.path.exists(local_path):
                full_url = download_path if download_path.startswith("http") else f"{base_url}/wiki{download_path}"
                try:
                    img_resp = requests.get(full_url, auth=auth, timeout=60)
                    if img_resp.status_code == 200:
                        with open(local_path, "wb") as f:
                            f.write(img_resp.content)
                    else:
                        print(f"WARNING: attachment download failed ({img_resp.status_code}): {title}", file=sys.stderr)
                        continue
                except requests.RequestException as e:
                    print(f"WARNING: attachment download error for {title}: {e}", file=sys.stderr)
                    continue

            media_map[file_id] = f"assets/{local_name}"

        if i % 10 == 0 or i == total_pages:
            print(f"  attachments: processed {i}/{total_pages} pages, {len(media_map)} images mapped so far")

    return media_map


def fetch_one_space(site, space_key, out_path, assets_dir, auth, skip_images=False):
    """Fetches one space end-to-end: pages + attachments, writes pages.json.
    This is the same logic that used to live directly in main() — pulled out
    so --config mode can call it once per space without duplicating it."""
    base_url = f"https://{site}"

    print(f"Looking up space '{space_key}' on {site}...")
    space_id, space_name = get_space_id(base_url, space_key, auth)
    print(f"Found space: {space_name} (id={space_id})")

    print("Fetching pages (this paginates, may take a moment for large spaces)...")
    raw_pages = get_all_pages(base_url, space_id, auth)
    print(f"Fetched {len(raw_pages)} pages.")

    normalized = [normalize_page(p) for p in raw_pages]
    failed = [p["id"] for p in normalized if p["adf"] is None]
    if failed:
        print(f"WARNING: {len(failed)} pages had no usable ADF body: {failed}", file=sys.stderr)

    media_map = {}
    if not skip_images:
        print("Downloading images (skips files already on disk)...")
        media_map = download_attachments(base_url, auth, normalized, assets_dir)
        print(f"Mapped {len(media_map)} images to local files.")
    else:
        print("--skip-images set, leaving all images as placeholders.")

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({
            "space_key": space_key,
            "space_id": space_id,
            "pages": normalized,
            "media": media_map,
        }, f, indent=2)

    print(f"Wrote {out_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to sites.json — fetches every space listed in it")
    parser.add_argument("--space", help="Single-space mode: Confluence space key, e.g. FOX")
    parser.add_argument("--site", help="Single-space mode: e.g. appfire.atlassian.net")
    parser.add_argument("--out", default="data/pages.json", help="Single-space mode: output path")
    parser.add_argument("--data-dir", default="data", help="Config mode: base dir; writes {data-dir}/{space_key}/pages.json")
    parser.add_argument("--assets-dir", default="assets", help="Where downloaded images are saved (shared across spaces — fileIds are globally unique, so no collision risk)")
    parser.add_argument("--skip-images", action="store_true", help="Skip attachment download (faster, for debugging)")
    args = parser.parse_args()

    auth = get_auth()

    if args.config:
        with open(args.config) as f:
            config = json.load(f)
        site = config["confluence_site"]
        spaces = config["spaces"]
        print(f"Config mode: fetching {len(spaces)} space(s) from {site}")
        for space_cfg in spaces:
            space_key = space_cfg["space_key"]
            out_path = os.path.join(args.data_dir, space_key, "pages.json")
            fetch_one_space(site, space_key, out_path, args.assets_dir, auth, args.skip_images)
            print()
    else:
        if not args.space or not args.site:
            sys.exit("Either --config sites.json, or both --space and --site, are required.")
        fetch_one_space(args.site, args.space, args.out, args.assets_dir, auth, args.skip_images)


if __name__ == "__main__":
    main()
