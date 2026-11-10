---
id: t02-polar
title: Polarization and segment notation slides
short_name: polar
type: task
status: active
privacy: public
summary: Ring of test masses beside the line-segment notation, for circular and plus polarization.
verification: unverified
---

# Polarization and segment notation slides

<!-- opsci:node-table: generated from the front matter by `opsci map build`; edit the front matter, not this table -->

| task | `t02-polar` |
|---|---|
| **short name** | `polar` |
| **status** | active |
| **privacy** | public |
| **verification** | unverified |
| **summary** | Ring of test masses beside the line-segment notation, for circular and plus polarization. |

<!-- /opsci:node-table -->

Last updated: 2026-11-02

<!-- The state of this task now, edited in place. At most 200 lines. A fresh agent given
AGENTS.md, the project context.md and this file must be able to take the correct next
action. Detail and history go in subcontext/ and log.md. -->

## Goal

Slide part slides/parts/polar/: slides polar-circular and polar-plus. Ring of 24 test masses
(left) beside the stretch-whisker segment (right), which stands for the same wave; a slider sets
the amplitude of both.

## Current state

Second version built and committed. Stage 0 is the ring alone; stage 1 adds the segment on the same
clock. Constants as gw-ring ($R_0=300$, $N=24$, DOT=11, PERIOD=4000), with $\phi = 2\pi t /$ PERIOD
from slide entry and no ramp. Centres at (510, 590) and (1410, 590). Segment half-length
$300\,|h|/0.26$, width 18 px, black, butt ends.

Ruling (2026-11-02): a mouse slider sets the amplitude: left end $h=0$ (circle, no segment), right
end $h=0.36$; $h=0.26$ on entering a slide. Bottom centre, x 660 to 1260, y 1000, no label.

Checks (`../scratchpad_nbi/rev2/check.js`, viewport 1280x720, real mouse drags), MEASURED:
- Slider at left, both slides: all 24 masses at radius $300 \pm 10^{-13}$ px; 0 inked pixels in the
  right half of the canvas. Control, default and right end: radius range 261-339 and 246-354 px
  (circular, at the frames sampled), inked pixels $> 2\times10^4$.
- First version's check of the segment axis against rendered ring pixels: largest difference
  0.190 deg circular, 0.091 deg plus (`../scratchpad_nbi/polar/check.js`); the drawing of the wave did
  not change except for the amplitude.
- Forward and back through the presentation: no page errors.

## In flight

Nothing.

## Open questions

None.

## Pointers

- Revised checks: ../scratchpad_nbi/rev2/check.js
- Screenshots: ../scratchpad_nbi/polar/shots/
