---
id: t01-precess
title: Precessing binary slides
short_name: precess
type: task
status: active
privacy: public
summary: Slides comparing a non-precessing and a precessing Newtonian binary, then face-on and edge-on
  detectors around the precessing one.
verification: unverified
---

# Precessing binary slides

<!-- opsci:node-table: generated from the front matter by `opsci map build`; edit the front matter, not this table -->

| task | `t01-precess` |
|---|---|
| **short name** | `precess` |
| **status** | active |
| **privacy** | public |
| **verification** | unverified |
| **summary** | Slides comparing a non-precessing and a precessing Newtonian binary, then face-on and edge-on detectors around the precessing one. |

<!-- /opsci:node-table -->

Last updated: 2026-11-02

<!-- The state of this task now, edited in place. At most 200 lines. A fresh agent given
AGENTS.md, the project context.md and this file must be able to take the correct next
action. Detail and history go in subcontext/ and log.md. -->

## Goal

Slide part slides/parts/precess/: slide `precess-compare` (title; stage 1: non-precessing and
precessing binaries side by side) and slide `precess-detectors` (precessing binary, $x$, $y$, $z$
axes, one Earth on $z$ along $\mathbf{J}$, one Earth on $x$ perpendicular to it, credits; dragging
turns the camera).

## Current state

Third version built and committed. Files: `slides/parts/precess/part.html`, `part.css`, `part.js`,
`assets/earth_mask.js` (see `assets/README`).

Ruling (2026-11-02): both slides show the orbit as a dotted line; on `precess-detectors` the LIGO
detectors are replaced by Earths, the binary is smaller, the axes are shown, and the view is draggable.

Parameters (declared at the top of `part.js`). Units: $|\mathbf{L}| = 1$, time in seconds.
- Orbit: period 4 s in both panels, same phase; radius 210 px (scale 1), hole radius 40 px.
- Precession: $d\mathbf{L}/dt = k\,\mathbf{S}\times\mathbf{L}$, $d\mathbf{S}_i/dt = k\,\mathbf{L}\times\mathbf{S}_i$, $k = 0.13777$ /s (from 5 orbits per precession).
- Opening angle $\mathbf{L}$-$\mathbf{J}$ 30 deg; $|\mathbf{S}| = 1.5$, 19.5 deg from $\mathbf{J}$ on the far side from $\mathbf{L}$, $|\mathbf{J}| = 2.2802$.
- $|\mathbf{S}_1| = |\mathbf{S}_2| = 0.8089$, each 22 deg from $\mathbf{S}$.
- RK4, fixed step 1/120 s; the orbit basis is transported without twist.
- Dotted circle: the holes' current orbit, in the current orbital plane, so it tilts with $\mathbf{L}$.
- Camera: orthographic. First slide fixed, 38 deg above the plane perpendicular to $\mathbf{J}$.
  Second slide starts at elevation 28 deg, yaw $-30$ deg; drag 0.008 rad per slide px, yaw free,
  pitch $-\pi$ (from below) to 0 (from above), reset on entering the slide.
- Scale 0.84 on `precess-compare`, 0.55 on `precess-detectors`.
- Axes: half-length 280 px. Earths: radius 52 px, 410 px from the binary, north along $z$, same
  orientation (orthographic camera, so they share one image), redrawn when the camera moves.
  Plate: fill rgba(233,233,233,0.82), edge #c4c4c4, so that it hides what is behind it (ruling
  2026-11-02). Axes #b8b8b8, width 2; labels #8a8a8a. Half axes, Earths and spin arrows on the far side of
  the plate from the camera are drawn before it, and the rest after it, each side far to near.
  The Earth's size and distance are not to scale.

Checks (scripts in `../scratchpad_nbi/precess/` and `../scratchpad_nbi/rev2/`): the PHYSICS block
of `part.js` did not change in this version, so the first version's results hold: $\mathbf{J}$ direction
drift max $1.9\times10^{-14}$ over 4 h simulated, precession period 20.008 s, MEASURED by
`check_physics.js`. New: `rev2/shot.js` screenshots at the first view, after dragging to above and to the
side, no page errors; the map is the right way round by eye (Europe above Africa, Arabia to the east).

## In flight

Nothing.

## Open questions

None.

## Pointers

Screenshots and scripts: `../scratchpad_nbi/precess/` (not committed).
