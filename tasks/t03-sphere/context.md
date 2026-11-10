---
id: t03-sphere
title: All-sky sphere slide
short_name: sphere
type: task
status: active
privacy: public
summary: Binary with rings at four directions, then segments, then a draggable sphere of segments on a
  white background.
verification: unverified
---

# All-sky sphere slide

<!-- opsci:node-table: generated from the front matter by `opsci map build`; edit the front matter, not this table -->

| task | `t03-sphere` |
|---|---|
| **short name** | `sphere` |
| **status** | active |
| **privacy** | public |
| **verification** | unverified |
| **summary** | Binary with rings at four directions, then segments, then a draggable sphere of segments on a white background. |

<!-- /opsci:node-table -->

Last updated: 2026-11-02

<!-- The state of this task now, edited in place. At most 200 lines. A fresh agent given
AGENTS.md, the project context.md and this file must be able to take the correct next
action. Detail and history go in subcontext/ and log.md. -->

## Goal

Slide part slides/parts/sphere/: slide `sphere-slide`, three stages, and slide `sphere-precess`, two
stages (the precessing binary with axes; then the sphere around it). No text except axis labels.

## Current state

Third version built and committed. One 3D scene with $x$, $y$, $z$ axes at every stage; dragging turns
the camera at every stage. Stage 0: binary and four rings at $\pm z$, $\pm x$, each in the plane
perpendicular to the line to the binary, on a nearly opaque square. Stage 1: bars along the stretch axis
in those planes. Stage 2: 600-point sphere of segments, shaded by $\log|h|$, with the binary inside.

Ruling (2026-11-02): rings are true 3D, not drawn facing the viewer; axes on all stages; orbit dotted
and orbital plane a square, inside the sphere and below the near surface; surface gray scale
logarithmic in $|h|$, white at the nodes. Ruling (2026-11-02): planes and surface hide what is behind
them, axes are light and thin, so that depth can be read and objects do not merge.

Rulings (2026-11-02): a click (no drag) on a direction puts a red circle around its ring, bar or segment, in the
tangent plane; the object stays black. One highlight at a time: the same direction clears it, another moves it.
Entering a slide clears it. On the sphere stages of both slides, the highlighted direction opens a side panel: a
large ring with the stretch bar, a toy L, and the detector's output.

Side panel (right of the sphere, centre $x=1670$): the tangent plane seen from outside, turned to the rotation
closest to the camera's right and up, so it has the orientation shown on the sphere. Arms $u=\cos\alpha\,a_1+\sin\alpha\,a_2$,
$v=-\sin\alpha\,a_1+\cos\alpha\,a_2$, $a_1=e_\phi$, $a_2=-e_\theta$; output $s=\frac12(u\cdot h\cdot u-v\cdot h\cdot v)=-h_+\cos2\alpha-h_\times\sin2\alpha$.
The detector is a toy Michelson (ruling 2026-11-02): red laser, beam splitter at the fixed origin, two end
mirrors, an output beam whose brightness follows $|s|$. Each mirror moves by the full $\frac12\,0.45\,h\cdot x$, also sideways, so at $45^\circ$ to
a linear polarization the arms shear with equal length, and for circular polarization the mirrors go round circles. Beams are drawn straight to the
moved mirror, a schematic. Dragging within 185 px of the detector changes $\alpha$, not the camera; no visible handle. A new direction starts at $\alpha=0$. The trace covers the last 6 s, stored as $Q(t)$
and recomputed each frame for the present $\alpha$, so that rotating the L changes the whole trace at once.

`sphere-precess`: the same scene with the state of the precess part (the PHYSICS block is a copy; equal up
to the name of the period, MEASURED by string comparison). The field is the instantaneous quadrupole of
the tilted orbit, a schematic: no retardation, and the plane's own motion is not differentiated. The four
nodes lie in the current orbital plane and tilt with it.

Conventions (R01, R04; constants at the top of part.js):
- Field: $h_+ = Q_{\theta\theta} - Q_{\phi\phi}$, $h_\times = 2Q_{\theta\phi}$ with
  $Q = \frac12[\cos 2\Phi(e_1e_1 - e_2e_2) + \sin 2\Phi(e_1e_2 + e_2e_1)]$; for $e_1=x$, $e_2=y$:
  $h_+ = \frac{1+\cos^2\theta}{2}\cos 2(\Phi-\phi)$, $h_\times = \cos\theta\sin 2(\Phi-\phi)$,
  $\psi = \frac12\mathrm{atan2}(h_\times, h_+)$ from $e_\theta$ towards $e_\phi$. Nodes: four points on the
  equator at $\phi = \Phi + 45^\circ + k\,90^\circ$, turning with the orbit.
- Clock: $\Phi = 2\pi(t-t_0)/4000$ ms. Camera: orthographic, starts at elevation 28 deg, yaw $-35$ deg so
  that the $\pm x$ rings are not edge on; drag 0.008 rad per slide px; yaw free; pitch $-\pi$ (from below)
  to 0 (from above); reset on entering the slide.
- Rings at 360 px, $R_0$ 100, 24 masses, display strain 0.45, bar half-length $100|h|$ px, width 11,
  plane half-size 150. Sphere radius 360, segment length $0.14 R|h|$. Orbit radius 120, hole radius 30,
  orbital square half-size 190 (corners at 269 px, inside the sphere). Axis half-length 470.
- Plates (ring squares, orbital square): fill rgba(233,233,233,0.82), edge #c4c4c4. Axes: #b8b8b8, width 2; labels #8a8a8a.
- Surface: gray level $1 - 0.34\,s$, $s = 1 + \log|h|/\log(1/0.12)$ clipped to 0..1: $|h| \le 0.12$ white,
  $|h|=0.5$ level 197/255, $|h|=1$ level 168/255; opacity 0.66, so the inside is visible but clearly behind it.
  Near hemisphere only: far shading shows through a near node and makes it gray.
- Draw order, back to front: far outer axes, far rings, far $z$ axis, orbital plate, far $x$, $y$ on the plate,
  orbit and holes, near inner axes, surface, segments, near rings, near outer axes. The plates do not
  meet, so ordering rings by the depth of their centres holds from every direction.
- `_check` on the widget hooks is not used by the engine; it exposes the closed form and camera to the checks.

Checks (`../scratchpad_nbi/rev2/`), MEASURED:
- `check.js`: 96 masses against an independent TT projection of the $3\times3$ quadrupole, 5 cameras
  including from above and below, 2 phases each: worst $2.5\times10^{-13}$ px; control $h\to-h$: 25-45 px.
- `check_shade.js`: shading image against $|h|=\sqrt{\mathrm{tr}\,h^2/2}$ of that projection, 5592 pixels, 3
  cameras: worst 1/255 (rounding); control $\Phi+45^\circ$: 59/255. Node pixels 255, equatorial maxima 197.
- `check.js`: real mouse drag moves the camera by the expected amounts (yaw 1.2, pitch 0.24 rad);
  pitch stops at $-\pi$. Forward and back through the presentation: no page errors.
- `../scratchpad_nbi/sphere/check_field.js` (closed form against the eigenproblem): max $|h|$ difference $10^{-15}$.
- `check3.js`: `sphere-precess` shading image against TT of the tilted $Q$, 5592 pixels, 3 times: worst
  1/255; control with an untilted orbit: 70/255. Hole on the screen within 0.000 px of the expected place.
  Clicks: on, off, a drag does not toggle, an empty corner does nothing.
- `check4.js`: panel output against $u\cdot h\cdot u$, $v\cdot h\cdot v$ of an independent TT projection, 20 frames, both slides: worst
  $2\times10^{-16}$; control sign flip 1.4-1.8. Equator $+x$, max $|s|$ over the trace: 0.500 at 0 deg, 0.354 at 22.5, 0.000 at 45, 0.500 at 90.
  Pole $+z$ (circular): 1.000 at every angle. A real 45-deg drag on the guide: $\Delta\alpha=45.00$ deg, camera unchanged.
- `check6.js`: mirror motion. Along-arm parts equal $\pm0.45\cdot75\,s$ px, errors $10^{-14}$. Equator $+x$ at $45^\circ$: along arm 0.0 px, sideways 16.8 px.
  At $0^\circ$: along 16.9, sideways 0.0. Pole: mirror distance from rest 33.7-33.8 px at all times, a circle.
- `check5.js`: one highlight at a time on the sphere, precessing and GW231123 slides; clearing closes the panel.
- `clean.js`: `sphere-precess` stage 1 at 51 frames/s, headless, no GPU, 1920x1080; not measured on the
  presenting machine; measured without the panel open. All slides forward and back through the presentation: no page errors.

## In flight

Nothing.

## Open questions

None.

## Pointers

Source of grid, camera and drag: `sphere_template.html` in a separate, older visualisation project,
prepare_sphere.py (`fibonacci_sphere`).
