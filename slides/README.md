# Slides

The slide sources. `python3 slides/build.py` builds them into `_site/`: one page per part
(`slides/parts/<name>/`), `presentation.html` with the parts in the order of `deck.txt`, and
`index.html`, a preview page. `FORMAT.md` is the format every part follows.

The build needs KaTeX in `slides/vendor/katex/`, which the public copy of this repository
leaves out: from the `dist/` folder of the npm package `katex` 0.18.9, copy `katex.min.js`,
`katex.min.css`, `contrib/auto-render.min.js` (to `auto-render.min.js`) and `fonts/*.woff2`.
