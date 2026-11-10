---
id: t04-gw231123
title: GW231123 slides
short_name: gw231123
type: task
status: active
privacy: public
summary: Title and spin posterior of the LVK GW231123 paper, then its zoomed sphere at the actual viewing
  angle beside the whitened waveform.
verification: unverified
---

# GW231123 slides

<!-- opsci:node-table: generated from the front matter by `opsci map build`; edit the front matter, not this table -->

| task | `t04-gw231123` |
|---|---|
| **short name** | `gw231123` |
| **status** | active |
| **privacy** | public |
| **verification** | unverified |
| **summary** | Title and spin posterior of the LVK GW231123 paper, then its zoomed sphere at the actual viewing angle beside the whitened waveform. |

<!-- /opsci:node-table -->

Last updated: 2026-11-02

<!-- The state of this task now, edited in place. At most 200 lines. A fresh agent given
AGENTS.md, the project context.md and this file must be able to take the correct next
action. Detail and history go in subcontext/ and log.md. -->

## Goal

Slide part slides/parts/gw231123/: slide `gw231123-paper` (title line and spin disk of the LVK paper) and slide
`gw231123-sphere` (zoomed sphere seen straight on along the viewing direction; whitened traces).

## Current state

First version built and committed. Data come from `../prec/gw231123_nrsur7dq4_sphere.html`, an earlier
visualizer: NRSur7dq4, maximum-likelihood sample (its index 15328), L frame at $f_{\rm ref}=10$ Hz, 2500 tiles,
$\pm0.14$ s around the peak. `S1/export_sphere_data.py` extracts them to `assets/data.js` (0.78 MB), keeping 682 of the
2500 tiles, at least $5.8^\circ$ apart.

Rulings (2026-11-02): one paper figure only: the spin disk, from both detectors; no title text beyond the
paper's own title line. Sphere: zoomed, straight on, the actual direction highlighted by a red circle (radius 48 px, around the longest bar); one highlight at a time, as on the sphere part; no side panel on this slide.

Choices:
- Viewing direction: source tile 1749 (index 478 in `data.js`), $\theta=113.6^\circ$, $\phi=338.9^\circ$, the visualizer's
  nearest tile to $(\iota, \pi/2-\phi_{\rm ref})$. The source's tile spacing is about $4^\circ$; the source tile numbers
  in this file are the visualizer's.
- Fewer bars (ruling 2026-11-02): every third tile was tried first and rejected, because it leaves visible arcs and gaps
  on the lower part of the sphere. Kept tiles are chosen going outward from tile 1749 along the source's spiral, each at
  least $5.8^\circ$ from those kept. The surface uses the same 682 tiles.
- Bars are the stretch axis, $\cos\psi\,e_\theta+\sin\psi\,e_\phi$, $h=h_+-ih_\times$. The visualizer's shader starts $\psi$
  from $e_\phi$ with sign $-e_\theta$, 90 deg from this (a derivation from its code, not run against a test case).
- Frames to $t\le+0.06$ s, 205 of 287: max $|h|$ of the dropped frames 0.062 of the peak. Played at 24 data
  frames/s, about 1/41 of real time, 1 s hold at the end. Bars and surface use the global scale: $|h|\le1$.
- Surface (ruling 2026-11-03): one gray level per tile, gray $1-0.36\,s$, $s=1+\log|h|/\log(1/0.03)$, filled over the
  tile's spherical Voronoi cell (682 cells, 1360 vertices, from `S1/export_sphere_data.py`), so the surface has the
  bars' resolution. It replaces a smooth $256\times256$ image interpolated from the same tiles. Cells are drawn 4% larger
  about their tile to cover seams, over a disc of gray `#ebebeb`, with no clip and no stroke. Traces: data gray, NRSur 90%
  band blue, maximum-likelihood waveform black, red time cursor.

Checks (`../scratchpad_nbi/gw231123/los_test.py`, `../scratchpad_nbi/rev2/check3.js`, `clean.js`), MEASURED:
- Which tile reproduces the maximum-likelihood waveform, by overlap of its two-detector whitened waveform:
  best tile 1804 ($\theta=116.3^\circ$, $\phi=336.0^\circ$) 0.9948; tile 1749 0.9833; controls: mirrored $\theta$ 0.359, antipode 0.249.
- Tile 1749 against the bilby waveform: correlation 0.986 H1, 0.982 L1; rms ratio 1.004, 0.994.
- Entering: 1749 highlighted at screen (640, 540), depth 1. Clicks: on, off; a second direction replaces the first.
- 25 frames/s, headless, no GPU, 1920x1080; not measured on the presenting machine. No page errors.
- 682 tiles against 2500 (`../scratchpad_nbi/rev3/`): same $h$ on the kept tiles; traces unchanged; the three nearest tiles
  of every table cell lie inside the slide's search band. Surface gray level on the facing hemisphere, frames 100 to 160,
  range 92: median difference 0.2 to 0.3, 99th percentile up to 3.4, maximum 26.4. Headless, no GPU: 22.5 to 26.5 frames/s
  against 17 to 21; first entry 64 to 88 ms against 100 to 105 ms.

- Per-tile surface (`../scratchpad_nbi/rev4/`), headless, no GPU, not measured on the presenting machine: 54 to 59 frames/s
  against 36 to 40; first entry 17 to 25 ms against 54 to 64 ms. Removing layers from the old slide: without the image 60, without
  bars 41, without traces 43 frames/s, so the image was the cost; a $128\times128$ image gave only 42 to 43. A clip on the cells gave 7 frames/s,
  strokes 39. `check.js`: gray of every cell with depth above 0.5 and inside the slide (167 or 168 cells; frames 60, 120, 146, 165, and after a drag) against the table applied to $|h|$
  from the data: worst 1/255; control, 40 frames later: worst 53 to 68. Data arrays other than the cells unchanged, by comparison with the previous `data.js`. Click: moves the
  highlight. No page errors.

Not resolved: `../GW231123_edge_on` reports $\iota=64.3^\circ$ at $f_{\rm ref}$ for its maximum-likelihood sample
(its index 6096 of `C00:NRSur7dq4`), and this sphere has $\theta\approx116^\circ$, close to $180^\circ-64.3^\circ=115.7^\circ$.
I have not established whether they are the same sample with a folded angle. The overlap above does not depend on it.

## In flight

Nothing.

## Open questions

None.

## Pointers

None.
