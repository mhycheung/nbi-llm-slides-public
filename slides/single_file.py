#!/usr/bin/env python3
"""Pack a built page into one self-contained HTML file.

Inlines every stylesheet, script and image that the page names (src/href attributes and CSS
url()), as text or base64 data URIs, so that the file works alone: from a download, an email
or a chat attachment. Run slides/build.py first.
Usage: python3 slides/single_file.py [--site _site] [--page presentation] [--out FILE]
"""
import argparse
import base64
import mimetypes
import re
import sys
from pathlib import Path

ATTR = re.compile(r"""\b(src|href)\s*=\s*"([^"#:]+)\"""")
CSS_URL = re.compile(r"""url\(\s*["']?([^"')]+)["']?\s*\)(\s*format\(["'][^"']+["']\))?""")
TAG = re.compile(r"""<(link|script)\b([^>]*)>(\s*</script>)?""", re.I)
MIME = {".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".js": "text/javascript"}


def fail(msg):
    sys.exit(f"single_file: {msg}")


def data_uri(f):
    mime = MIME.get(f.suffix) or mimetypes.guess_type(f.name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + base64.b64encode(f.read_bytes()).decode()


def inline_css(css, base):
    def url(m):
        ref = m.group(1)
        if ref.startswith("data:"):
            return m.group(0)
        f = (base / ref).resolve()
        if not f.is_file():
            return ""  # a missing font fallback (KaTeX ships woff2 only); dropped below
        return f"url({data_uri(f)})" + (m.group(2) or "")
    css = CSS_URL.sub(url, css)
    # src lists of @font-face lose their missing entries: "a, , b" -> "a, b"
    css = re.sub(r",\s*(?=[,;}])", "", css)
    return css


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="_site")
    ap.add_argument("--page", default="presentation")
    ap.add_argument("--out")
    a = ap.parse_args()
    site = Path(a.site)
    page = site / f"{a.page}.html"
    if not page.is_file():
        fail(f"{page} not found; run slides/build.py first")
    html = page.read_text()

    def tag(m):
        name, attrs = m.group(1).lower(), m.group(2)
        r = ATTR.search(attrs)
        if not r:
            return m.group(0)
        f = site / r.group(2)
        if not f.is_file():
            fail(f"{page.name} names {r.group(2)}, which does not exist")
        if name == "link":
            if "stylesheet" not in attrs:
                return m.group(0)
            return "<style>\n" + inline_css(f.read_text(), f.parent) + "\n</style>"
        return "<script>\n" + f.read_text().replace("</script", "<\\/script") + "\n</script>"

    def attr(m):
        f = site / m.group(2)
        if not f.is_file():
            fail(f"{page.name} names {m.group(2)}, which does not exist")
        return f'{m.group(1)}="{data_uri(f)}"'

    # Images and other tags first, while the page holds no inlined code whose strings could match.
    html = re.sub(r"<(?!link\b|script\b)[a-z][^>]*>", lambda m: ATTR.sub(attr, m.group(0)), html, flags=re.I)
    html = re.sub(r"<style>(.*?)</style>", lambda m: "<style>" + inline_css(m.group(1), site) + "</style>",
                  html, flags=re.S)
    html = TAG.sub(tag, html)
    left = re.findall(r"""["'(]((?:parts|vendor|common)/[^"')\s]+\.(?:png|jpe?g|gif|svg|webp|js|css|woff2?))""", html)
    if left:
        fail(f"file paths left after inlining (a JS string?): {sorted(set(left))[:5]}")
    out = Path(a.out or site / f"{a.page}_single.html")
    out.write_text(html)
    print(f"wrote {out} ({out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
