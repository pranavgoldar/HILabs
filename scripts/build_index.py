#!/usr/bin/env python3
"""Build index.html (the page Vercel serves) from the prototype source.

The source file, HiLabs_Workbench_Prototype_V3.html, is written as page
content only (no <!doctype>, <html>, <head> or <body>) so it can also be
published as a Claude artifact. This script wraps it in a full HTML document.

Run after every edit to the source:  python3 scripts/build_index.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "HiLabs_Workbench_Prototype_V3.html"
OUT = ROOT / "index.html"

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' rx='8' fill='%230053EF'/%3E"
    "%3Ctext x='16' y='21' font-family='Arial' font-weight='700' font-size='13' "
    "fill='white' text-anchor='middle'%3ECW%3C/text%3E%3C/svg%3E"
)

body = SRC.read_text(encoding="utf-8")
body = body.replace('<script src="assets/annex-data.js"></script>', '<script>\n' + (ROOT / 'assets/annex-data.js').read_text(encoding='utf-8') + '</script>')
head_end = body.index("</style>") + len("</style>")
head_part, page_part = body[:head_end], body[head_end:]

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta property="og:title" content="Care Workbench · HiLabs APM case 2026–27">
<meta property="og:description" content="Clickable concept prototype: a nurse case manager's work queue, Member 360 and call-and-note screens for five fictional members.">
<meta property="og:type" content="website">
<link rel="icon" href="{FAVICON}">
<style>[hidden]{{display:none!important}}img{{max-width:100%}}</style>
{head_part.strip()}
</head>
<body>
{page_part.strip()}
</body>
</html>
"""
OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT.relative_to(ROOT)} ({len(html):,} bytes)")

# Download artifact uses the same source; Vercel redirects the legacy root URL.
DOWNLOAD = ROOT / "downloads" / SRC.name
DOWNLOAD.parent.mkdir(exist_ok=True)
DOWNLOAD.write_text(body, encoding="utf-8")
