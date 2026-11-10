#!/usr/bin/env python3
"""Build the slide site from slides/parts/ into a directory (default _site/).

Writes <out>/<part>.html for every part folder, <out>/presentation.html with the parts listed in
slides/deck.txt in that order (if any), and <out>/index.html, the preview page with one tab
per page. The output needs no network access. Usage: python3 slides/build.py [--out DIR]
"""
import argparse
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAME = re.compile(r"^[a-z0-9][a-z0-9-]*$")
ID = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""")
ONLINE = [
    (re.compile(r"""\b(src|href)\s*=\s*["']\s*(https?:)?//""", re.I), "loads a file from the network"),
    (re.compile(r"""url\(\s*["']?\s*(https?:)?//""", re.I), "loads a file from the network"),
    (re.compile(r"""@import"""), "uses @import"),
    (re.compile(r"""\bfetch\s*\("""), "uses fetch(), which fails from file://"),
    (re.compile(r"""type\s*=\s*["']module["']"""), "uses an ES module, which fails from file://"),
]
ES_JS = [(re.compile(r"""^\s*(import|export)\s""", re.M), "uses an ES module, which fails from file://")]
RESERVED = {"deck", "presentation", "index", "common", "vendor", "parts"}

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<link rel="icon" href="data:,">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="vendor/katex/katex.min.css">
<link rel="stylesheet" href="common/deck.css">
{css}
</head>
<body>
<div class="deck">
{slides}{chrome}
</div>
<script src="vendor/katex/katex.min.js"></script>
<script src="vendor/katex/auto-render.min.js"></script>
<script src="common/deck.js"></script>
{js}
<script>Deck.start();</script>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<link rel="icon" href="data:,">
<title>slides preview</title>
<style>
html, body {{ margin: 0; height: 100%; font-family: Arial, Helvetica, sans-serif; }}
body {{ display: flex; flex-direction: column; }}
nav {{ display: flex; gap: 2px; padding: 4px; border-bottom: 1px solid #ccc; font-size: 14px; }}
nav a {{ padding: 4px 10px; color: #000; text-decoration: none; border: 1px solid #ccc; }}
nav a.on {{ background: #000; color: #fff; }}
nav .open {{ margin-left: auto; }}
iframe {{ flex: 1; border: 0; width: 100%; }}
</style>
</head>
<body>
<nav>{tabs}<a class="open" id="open" href="#" target="_blank">open alone</a></nav>
<iframe id="view"></iframe>
<script>
var pages = {pages};
function show() {{
  var name = location.hash.slice(1);
  if (pages.indexOf(name) < 0) name = pages[0];
  if (!name) return;
  document.querySelectorAll("nav a[data-page]").forEach(function (a) {{
    a.classList.toggle("on", a.getAttribute("data-page") === name);
  }});
  var f = document.getElementById("view");
  f.onload = function () {{ f.contentWindow.focus(); }};
  f.src = name + ".html";
  document.getElementById("open").href = name + ".html";
}}
window.addEventListener("hashchange", show);
show();
</script>
</body>
</html>
"""


def fail(msg):
    sys.exit("build.py: " + msg)


def read_part(name):
    d = ROOT / "parts" / name
    src = d / "part.html"
    if not src.is_file():
        fail(f"parts/{name}/ has no part.html")
    body = src.read_text(encoding="utf-8")
    for f in [src, d / "part.css", d / "part.js"]:
        if f.is_file():
            text = f.read_text(encoding="utf-8")
            checks = ONLINE + (ES_JS if f.suffix == ".js" else [])
            for pat, why in checks:
                if pat.search(text):
                    fail(f"parts/{name}/{f.name} {why}; see slides/FORMAT.md")
    for i in ID.findall(body):
        if not i.startswith(name + "-"):
            fail(f'parts/{name}/part.html: id "{i}" must start with "{name}-"')
    return {
        "name": name,
        "body": body.strip(),
        "css": (d / "part.css").is_file(),
        "js": (d / "part.js").is_file(),
        "ids": ID.findall(body),
    }


# Stitched presentation only: a thin progress bar along the bottom, with a knob the mouse can
# drag to seek, and the time of day, bottom left.
CHROME = """
<div class="deck-progress"><div class="deck-progress-track"><div class="deck-progress-fill"></div></div><div class="deck-progress-knob"></div></div>
<div class="deck-clock"></div>"""


def page(title, parts, chrome=False):
    seen = set()
    for p in parts:
        for i in p["ids"]:
            if i in seen:
                fail(f'id "{i}" occurs twice in {title}')
            seen.add(i)
    return PAGE.format(
        title=html.escape(title),
        css="\n".join(f'<link rel="stylesheet" href="parts/{p["name"]}/part.css">' for p in parts if p["css"]),
        slides="\n".join(f'<!-- part: {p["name"]} -->\n{p["body"]}' for p in parts),
        js="\n".join(f'<script src="parts/{p["name"]}/part.js"></script>' for p in parts if p["js"]),
        chrome=CHROME if chrome else "",
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_site")
    out = Path(ap.parse_args().out)
    names = sorted(d.name for d in (ROOT / "parts").iterdir() if d.is_dir())
    for n in names:
        if not NAME.match(n) or n in RESERVED:
            fail(f"part folder name {n!r}: use lower case, digits and hyphens, and not one of {sorted(RESERVED)}")
    parts = {n: read_part(n) for n in names}

    order = []
    deck_txt = ROOT / "deck.txt"
    if deck_txt.is_file():
        for line in deck_txt.read_text().splitlines():
            line = line.split("#", 1)[0].strip()
            if line:
                if line not in parts:
                    fail(f"deck.txt names {line!r}, which has no folder in parts/")
                order.append(line)

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for sub in ["common", "vendor", "parts"]:
        shutil.copytree(ROOT / sub, out / sub, ignore=shutil.ignore_patterns("part.html"))
    (out / ".nojekyll").write_text("")

    pages = []
    if order:
        (out / "presentation.html").write_text(page("presentation", [parts[n] for n in order], chrome=True),
                                               encoding="utf-8")
        pages.append("presentation")
    for n in names:
        (out / f"{n}.html").write_text(page(n, [parts[n]]), encoding="utf-8")
        pages.append(n)
    tabs = "".join(f'<a data-page="{p}" href="#{p}">{p}</a>' for p in pages)
    (out / "index.html").write_text(INDEX.format(tabs=tabs, pages=repr(pages).replace("'", '"')),
                                    encoding="utf-8")
    print(f"built {len(pages)} page(s) into {out}: {', '.join(pages) or 'none'}")


if __name__ == "__main__":
    main()
