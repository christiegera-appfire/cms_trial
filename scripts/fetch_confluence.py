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
import subprocess
import sys
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

# Real docs screenshots/diagrams are always well under this — anything
# bigger is almost certainly a video or some other large binary that isn't
# a normal inline documentation image, and downloading it would risk
# blowing past GitHub's hard 100MB-per-file push limit (confirmed against
# a real 1.4GB .avi that got swept up as if it were a screenshot).
MAX_ATTACHMENT_SIZE_BYTES = 20 * 1024 * 1024  # 20MB

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
        "position": raw_page.get("position"),
        "version": raw_page.get("version", {}).get("number"),
        "adf": adf,
    }


def page_has_read_restriction(base_url, page_id, auth):
    """Checks whether a page has any explicit read restriction (specific
    users or groups) applied. This is necessary — and not automatic —
    because a token with real access to a restricted page gets it back
    completely normally from the regular page-listing endpoint, with
    nothing flagging that it's restricted. Since the static site has no
    login layer of its own, any restricted page needs to be excluded
    explicitly here or it would get published as fully public content,
    silently bypassing whatever restriction someone set on it in Confluence."""
    url = f"{base_url}/wiki/rest/api/content/{page_id}/restriction/byOperation/read"
    try:
        resp = requests.get(url, auth=auth, timeout=30)
    except requests.RequestException as e:
        print(f"WARNING: restriction check failed for page {page_id}: {e} — excluding it to be safe.", file=sys.stderr)
        return True  # fail closed: if we can't confirm it's safe to publish, don't publish it

    if resp.status_code == 404:
        return False  # no restrictions configured at all
    if not resp.ok:
        print(f"WARNING: restriction check returned {resp.status_code} for page {page_id} — excluding it to be safe.", file=sys.stderr)
        return True  # fail closed here too

    data = resp.json()
    restrictions = data.get("restrictions", {})
    users = restrictions.get("user", {}).get("results", [])
    groups = restrictions.get("group", {}).get("results", [])
    return bool(users or groups)


def filter_out_restricted_pages(base_url, raw_pages, auth, max_workers=10):
    """Returns (publishable_pages, excluded_count).

    Checked with a thread pool now, not one page at a time — this was
    explicitly flagged as a bottleneck at real platform scale (many
    hundreds of pages per space) when originally built, and 18+ spaces
    including some large, long-established products is exactly that
    scale. Restriction checks are independent, read-only HTTP calls, so
    parallelizing them is safe; max_workers is kept conservative (10) to
    avoid tripping Atlassian's own rate limits rather than trading a slow,
    reliable fetch for a fast, flaky one.

    Results are collected keyed by page ID and then filtered back into
    the ORIGINAL page order — not the order threads happen to finish in.
    Downstream logic (which page becomes the homepage redirect target in
    single-space mode, specifically) depends on page order being stable
    and deterministic across runs, not on whichever HTTP request happened
    to come back first.

    Note this only speeds up THIS step. Page-content fetching itself and
    the restriction check both still run fully fresh on every single
    build — there's no caching of "this page's permissions/content hasn't
    changed since last time," so this doesn't make repeat runs skip work
    that was already done, only faster on each run."""
    restricted_by_id = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_page_id = {
            executor.submit(page_has_read_restriction, base_url, p.get("id"), auth): p.get("id")
            for p in raw_pages
        }
        for future in as_completed(future_to_page_id):
            page_id = future_to_page_id[future]
            restricted_by_id[page_id] = future.result()

    publishable = [p for p in raw_pages if not restricted_by_id.get(p.get("id"))]
    excluded = sum(1 for v in restricted_by_id.values() if v)
    return publishable, excluded


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


def process_page_attachments(base_url, auth, page_id, assets_dir):
    """Lists and downloads all of one page's attachments, returning
    {file_id: local_relative_path} for this page only. Deliberately returns
    a fresh dict per call rather than mutating any shared state — that's
    what makes it safe to run many of these concurrently across pages: each
    thread writes only to its own uniquely-named files on disk and returns
    its own dict, merged into the real media_map afterward in the main
    thread where there's no concurrency to worry about."""
    result = {}
    try:
        attachments = get_attachments_for_page(base_url, page_id, auth)
    except requests.RequestException as e:
        print(f"WARNING: could not list attachments for page {page_id}: {e}", file=sys.stderr)
        return result

    for att in attachments:
        file_id = att.get("extensions", {}).get("fileId")
        if not file_id:
            continue  # can't match this attachment to an ADF media node without it

        download_path = att.get("_links", {}).get("download")
        if not download_path:
            continue

        file_size = att.get("extensions", {}).get("fileSize")
        if file_size and file_size > MAX_ATTACHMENT_SIZE_BYTES:
            print(
                f"WARNING: skipping oversized attachment '{att.get('title', file_id)}' "
                f"({file_size / (1024*1024):.1f}MB, over the {MAX_ATTACHMENT_SIZE_BYTES // (1024*1024)}MB limit) "
                f"— will show as a placeholder rather than a real image.",
                file=sys.stderr,
            )
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

        result[file_id] = f"assets/{local_name}"

    return result


def download_attachments(base_url, auth, pages, assets_dir, max_workers=8):
    """Downloads every attachment referenced by the fetched pages into
    assets_dir, keyed by the ADF media fileId so generate_site.py can look
    up a local path for each <img>. Skips re-downloading files that already
    exist locally, since most images don't change between runs.

    Parallelized across pages with a thread pool — this was the actual
    bottleneck at real scale (confirmed against a real run: one space with
    280 pages produced 2,479 images, sequentially, one download at a time).
    max_workers is more conservative than the restriction-check's (8 vs 10)
    since each unit of work here can itself involve several HTTP requests
    (list + multiple downloads for a page with many images), so the real
    concurrent request count is higher than max_workers alone suggests."""
    os.makedirs(assets_dir, exist_ok=True)
    media_map = {}
    total_pages = len(pages)
    completed = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_page = {
            executor.submit(process_page_attachments, base_url, auth, p["id"], assets_dir): p["id"]
            for p in pages
        }
        for future in as_completed(future_to_page):
            page_media = future.result()
            media_map.update(page_media)
            completed += 1
            if completed % 10 == 0 or completed == total_pages:
                print(f"  attachments: processed {completed}/{total_pages} pages, {len(media_map)} images mapped so far")

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

    print("Checking page-level read restrictions (drafts/private pages get excluded)...")
    raw_pages, excluded_count = filter_out_restricted_pages(base_url, raw_pages, auth)
    if excluded_count:
        print(f"Excluded {excluded_count} restricted page(s) — not published to the public site.")
    else:
        print("No restricted pages found — publishing everything in this space.")

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
            "space_name": space_name,
            "space_id": space_id,
            "pages": normalized,
            "media": media_map,
        }, f, indent=2)

    print(f"Wrote {out_path}")


def remove_oversized_files(*dirs, max_bytes=95 * 1024 * 1024):
    """Defense-in-depth backstop: scans for and deletes any file over
    max_bytes before staging, in case something unexpectedly large ever
    slips past the size check in process_page_attachments (e.g. fileSize
    missing from the API response for some attachment). Kept comfortably
    under GitHub's real 100MB hard limit rather than exactly at it."""
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for root, _dirs, files in os.walk(d):
            for name in files:
                path = os.path.join(root, name)
                try:
                    size = os.path.getsize(path)
                except OSError:
                    continue
                if size > max_bytes:
                    print(
                        f"WARNING: removing oversized file before commit: {path} "
                        f"({size / (1024*1024):.1f}MB) — this should have been caught "
                        f"earlier; investigate why it wasn't.",
                        file=sys.stderr,
                    )
                    os.remove(path)


def commit_space_progress(space_key, data_dir, assets_dir):
    """Commits and pushes just-fetched data for one space immediately, not
    at the end of the whole run. This exists because of a real failure
    mode: a run covering many spaces (some very large — one space alone
    produced 2,479 images) can run long enough to risk a timeout or need
    cancelling partway through, and without this, EVERY space fetched so
    far would be lost with nothing to show for it, since nothing used to
    get committed until the entire run finished. Committing space by space
    means a cancelled or interrupted run still keeps whatever it actually
    completed.

    Silently does nothing if there's nothing new to commit (e.g., a space
    with no actual content changes since last time) — this is the normal
    case for most spaces on most runs, not an error."""
    try:
        remove_oversized_files(data_dir, assets_dir)
        subprocess.run(["git", "add", "-A", "--", data_dir, assets_dir], check=True)
        result = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if result.returncode == 0:
            print(f"  (no changes to commit for {space_key})")
            return
        subprocess.run(
            ["git", "commit", "-m", f"Fetch {space_key} from Confluence"],
            check=True,
        )
        subprocess.run(["git", "push"], check=True)
        print(f"  Committed and pushed {space_key}'s fetched data.")
    except subprocess.CalledProcessError as e:
        # Fetching already succeeded and is safely on disk even if the git
        # commands themselves fail for some reason — print the problem
        # loudly rather than silently losing the commit, but don't crash
        # the whole run over a git hiccup on one space when there might
        # be 17 more still to go.
        print(f"WARNING: git commit/push failed for {space_key}: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to sites.json — fetches every space listed in it")
    parser.add_argument("--space", help="Single-space mode: Confluence space key, e.g. FOX")
    parser.add_argument("--site", help="Single-space mode: e.g. appfire.atlassian.net")
    parser.add_argument("--out", default="data/pages.json", help="Single-space mode: output path")
    parser.add_argument("--data-dir", default="data", help="Config mode: base dir; writes {data-dir}/{space_key}/pages.json")
    parser.add_argument("--assets-dir", default="assets", help="Where downloaded images are saved (shared across spaces — fileIds are globally unique, so no collision risk)")
    parser.add_argument("--skip-images", action="store_true", help="Skip attachment download (faster, for debugging)")
    parser.add_argument("--only-space", help="Config mode: fetch only this one space key from sites.json, leaving every other space's cached data untouched — for a targeted single-space refresh instead of rebuilding everything")
    parser.add_argument("--commit-incrementally", action="store_true", help="Commit and push each space's data immediately after fetching it, rather than waiting until the whole run finishes — only meaningful when running in the actual git-tracked repo (e.g. in CI), not for local testing")
    args = parser.parse_args()

    auth = get_auth()

    if args.config:
        with open(args.config) as f:
            config = json.load(f)
        site = config["confluence_site"]
        spaces = config["spaces"]

        if args.only_space:
            spaces = [s for s in spaces if s["space_key"] == args.only_space]
            if not spaces:
                sys.exit(f"--only-space '{args.only_space}' isn't in {args.config}'s spaces list — check the exact key (case-sensitive).")

        print(f"Config mode: fetching {len(spaces)} space(s) from {site}")
        for space_cfg in spaces:
            space_key = space_cfg["space_key"]
            out_path = os.path.join(args.data_dir, space_key, "pages.json")
            fetch_one_space(site, space_key, out_path, args.assets_dir, auth, args.skip_images)
            if args.commit_incrementally:
                commit_space_progress(space_key, args.data_dir, args.assets_dir)
            print()
    else:
        if not args.space or not args.site:
            sys.exit("Either --config sites.json, or both --space and --site, are required.")
        fetch_one_space(args.site, args.space, args.out, args.assets_dir, auth, args.skip_images)


if __name__ == "__main__":
    main()
