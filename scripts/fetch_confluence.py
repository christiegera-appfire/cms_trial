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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--space", required=True, help="Confluence space key, e.g. FOX")
    parser.add_argument("--site", required=True, help="e.g. appfire.atlassian.net")
    parser.add_argument("--out", default="data/pages.json")
    args = parser.parse_args()

    base_url = f"https://{args.site}"
    auth = get_auth()

    print(f"Looking up space '{args.space}' on {args.site}...")
    space_id, space_name = get_space_id(base_url, args.space, auth)
    print(f"Found space: {space_name} (id={space_id})")

    print("Fetching pages (this paginates, may take a moment for large spaces)...")
    raw_pages = get_all_pages(base_url, space_id, auth)
    print(f"Fetched {len(raw_pages)} pages.")

    normalized = [normalize_page(p) for p in raw_pages]
    failed = [p["id"] for p in normalized if p["adf"] is None]
    if failed:
        print(f"WARNING: {len(failed)} pages had no usable ADF body: {failed}", file=sys.stderr)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as f:
        json.dump({"space_key": args.space, "space_id": space_id, "pages": normalized}, f, indent=2)

    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
