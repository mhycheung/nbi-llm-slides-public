# Slide format

Every slide part follows this guide, so that the parts can be stitched into one deck without
changes. Rules R08–R12 (`rules/README.md`) apply.

## Look

- White background, black text, Arial. Nothing else in the chrome: no logos, footers,
  slide numbers or decorations. The stitched presentation (`presentation.html`) alone adds a faint progress bar along the
  bottom edge, with a knob the mouse drags to jump between slides, and the time of day,
  small, bottom left; keep the bottom 26 px and the bottom-left corner (about 60×50 px)
  free of anything that matters.
- **No text unless the user asks for it.** That includes titles, labels, captions and
  axis labels. A demo placeholder is not a reason to add text.
- A title, when the user asks for one, is `<h1 class="title">…</h1>` as the first child of
  the slide: top centre, 64 px. Do not restyle it.
- The canvas is 1920×1080 px, scaled to the window by the engine. Position content in
  these pixels (absolute positioning is fine). Body text is 40 px.
- Math is LaTeX, rendered by KaTeX: `$…$` inline, `$$…$$` display. In JS, `katex.render`
  is available. The math font is the only exception to Arial.
- Colour only when the content needs it (for example, telling two curves apart).
- **Citations (R11).** A figure from another paper, and anything the user says to cite,
  gets a gray credit `<span class="cite">Smith+ (2401.12345)</span>`: first author's last
  name, `+`, and the arXiv number in parentheses. A LIGO–Virgo–KAGRA collaboration paper is
  `LVK (2111.03606)`. Nothing else: no journal, year, title or "et al.". Place it next to
  the figure it credits, directly below it unless the user says otherwise. The credit is
  the size of body text (40 px); do not shrink it.
  When Mark Cheung (the presenter) is a coauthor but not the first author, the credit also
  names Cheung: `Baibhav, Cheung+ (2302.03050)` when Cheung is second author, `Berti, ..., Cheung+
  (2505.23895)` when Cheung comes later. "Cheung" is always underlined, first author or not:
  `<span class="cite"><u>Cheung</u>+ (2310.04489)</span>`. Check the author list (arXiv)
  before writing a credit. The engine turns every credit with one arXiv number into a
  link to its arXiv abstract page (`https://arxiv.org/abs/<number>`); do not add the link
  yourself.
- **Ongoing work (R12).** A slide that shows ongoing work carries
  `<div class="ongoing">ongoing work</div>` as a child of the slide: bold red, top right.
  Do not restyle it.

## Files

A part is a folder `slides/parts/<name>/` (lower case, digits, hyphens):

| file | what |
|---|---|
| `part.html` | only `<section class="slide" id="<name>-…">` elements (and library `<script>` lines, below) |
| `part.css` | optional; every selector starts with a `.<name>-…` class or `#<name>-…` id |
| `part.js` | optional; classic script wrapped in `(function () { … })();` — no globals |
| `assets/` | optional; images, data, bundled libraries |

- Every `id` and every class the part defines starts with `<name>-` (the build refuses
  unprefixed ids and duplicate ids).
- Paths are relative to the site root: `parts/<name>/assets/fig.png`, in HTML, CSS and JS.
- An image that JS draws on a canvas is an `<img id="<name>-…" style="display:none">` in
  `part.html`, read with `getElementById`, not a `new Image()`: a browser's "save page"
  copies only the files the HTML names.
- **Offline:** nothing is loaded from the network. No CDN links, no `fetch()`, no ES
  modules (`import`/`export`, `type="module"`), which fail from `file://`. A library
  (a UMD/minified build) is downloaded once into `assets/` and loaded by a
  `<script src="parts/<name>/assets/lib.min.js"></script>` line at the top of `part.html`,
  the one thing besides sections allowed there; record its version and licence in
  `assets/README`. Data goes in a `.js` file that sets a variable under the part's prefix,
  not a `.json` file read with `fetch()`.
- Do not edit `slides/common/`, `slides/vendor/`, `slides/build.py`, `slides/deck.txt` or
  another part's folder. A change the engine needs is asked of the user.

## Navigation (handled by the engine; do not reimplement)

- → , Space, PageDown: next step, or next slide after the last step. ←, PageUp: back.
- These keys never reach a widget, even when it has focus. Widgets use the mouse only.
- Mouse clicks never turn pages, except on the presentation's progress bar (dragged to seek).

## Steps

- An element with `data-step="k"` is hidden (keeping its space) until step `k` of its slide.
- A widget with stages registers them:

```js
Deck.widget("<name>-slide-id", {
  steps: 3,                          // number of stages after the arrival state
  enter: function (slide) { … },     // slide became visible: set up, start loops
  leave: function (slide) { … },     // slide hidden: stop timers and animation frames
  step: function (slide, k, dir) { … } // show stage k (0..steps); dir = +1 forward, -1 back
});
```

- Stage 0 is the state on arrival. Going back from the next slide lands on the last stage,
  with `dir = -1`: draw the final state at once, without animating.
- `step` must be able to show any stage from any state (it is called after `enter` and on
  every key press), so draw from scratch rather than patching the previous stage.
- A slide's number of steps is the larger of its highest `data-step` and its widget's `steps`.
- Stop every `requestAnimationFrame` and timer in `leave`.

## Build and check

```bash
python3 slides/build.py            # writes _site/: one page per part, presentation.html, index.html
```

Open `_site/<name>.html` in a browser (works from `file://`). `#3` in the URL opens slide 3.
`slides/parts/example/` shows every feature: title, math, `data-step`, a staged animation
and a mouse widget.

## Committing

Parts are made in parallel by separate sessions in the same checkout. Commit only your own
paths: `git commit -m "…" -- slides/parts/<name> tasks/<task-id>`. Never `git add -A` or
`git commit -a`. Each commit on `main` is pushed and published to the preview site
automatically (R10), where each part has its own tab.
