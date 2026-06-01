#!/usr/bin/env python3
"""Generate a stable duplicate-detection key for a job listing."""

from __future__ import annotations

import argparse
import hashlib
import re
import unicodedata
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


TRACKING_PREFIXES = ("utm_",)
TRACKING_KEYS = {"fbclid", "gclid", "ref", "refid", "source"}


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return re.sub(r"\s+", " ", normalized).strip()


def normalize_url(value: str) -> str:
    if not value:
        return ""

    parts = urlsplit(value.strip())
    query = [
        (key, item)
        for key, item in parse_qsl(parts.query, keep_blank_values=True)
        if key.casefold() not in TRACKING_KEYS
        and not key.casefold().startswith(TRACKING_PREFIXES)
    ]
    path = parts.path.rstrip("/")
    return urlunsplit(
        (
            parts.scheme.casefold(),
            parts.netloc.casefold(),
            path,
            urlencode(sorted(query)),
            "",
        )
    )


def build_job_key(company: str, role: str, url: str, email: str) -> str:
    fields = (
        normalize_text(company),
        normalize_text(role),
        normalize_url(url),
        normalize_text(email),
    )
    payload = "\n".join(fields).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:20]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--url", default="")
    parser.add_argument("--email", default="")
    args = parser.parse_args()
    print(build_job_key(args.company, args.role, args.url, args.email))


if __name__ == "__main__":
    main()
