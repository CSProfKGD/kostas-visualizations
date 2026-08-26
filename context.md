# Kosta's Visualizations — Current State

Updated: 2026-08-25

## Production

- Site: https://kostas-visualizations.csprofkgd.chatgpt.site/
- The current production site is an older deployment. Do not treat its visible teaser images or card sizing as the accepted local state.
- Publish only after all checks under **Final verification** pass.

## Authoritative shared card state

- Twelve cards in a three-column desktop grid, two-column tablet grid, and one-column mobile grid.
- Every card uses the same outer radius, width, total height, hero height, and copy height at a given breakpoint.
- All cards must have exactly the same dimensions at a given breakpoint, and all four outer corners must use exactly the same shape/radius.
- The outer `.visualization-card` is the only rounded clipping boundary.
- Every teaser raster must have exactly the same pixel dimensions.
- Every teaser raster is a rectangular image with orthogonal/square corners (not rounded); no baked rounded panel corners.
- Hero images reach the card's left/right/top edges inside the outer silhouette.
- The hero-to-copy boundary is one straight horizontal seam, aligned across every card in a row.
- No light/dark scale shift, no strip or mismatched background under a teaser.
- Teaser URLs carry a release query string so browsers cannot reuse superseded raster assets after publishing.
- The complete card is clickable; no arrow or “Open visualization” label.

## Accepted content and replacements

- Perspective Projection: use the new photoreal scene with tree/rocks, opaque pinhole plane, one ray, and inverted image-plane projection. The incident ray remains visible from the world point to the pinhole; only the outgoing portion directly behind the opaque plane is subdued, and full cyan resumes exactly at the projected plane boundary before continuing to the image point.
- Sphere to Cubemap and Sphere to Equirectangular Projection: use the outpainted compositions with black background at every raster edge and modest breathing room around the complete globe and mapping diagram. Preserve every legitimate cyan latitude/longitude arc and every cyan cubemap/ERP segment outline. Remove the orange/coral vertical meridian and all associated glow from both representations.
- Parallel Stereo: use the user-supplied final raster `codex-clipboard-0e483603-2620-413f-b22a-191a02cb7226.png` for both dark and light teaser assets.
- Stereo Rectification uses the user-supplied final raster `codex-clipboard-f95718d9-d220-469a-b67a-32e735d792ae.png` for both dark and light teaser assets. Epipolar Geometry, Local Minimum, and Parallel Stereo use outpainted compositions with black background at every raster edge and breathing room around all cameras, points, surfaces, paths, and image planes.
- Partial Derivatives: use the new simplified saddle, one vertical slice plane, true intersection curve, and tangent line. Do not use the older two-plane image.
- Planar Homography: no correspondence lines. Use the exact author portrait from the hero card on the wall plane. The right portrait must be the direct deterministic projective warp of the exact selected left quadrilateral—not a fresh crop or regenerated portrait—with all four uniquely colored corner pairs and the same shoulder features touching the corresponding bottom corners.
- Epipolar Geometry: use the clean outline-only triangle through the cameras and one world point. Remove the misleading translucent interior overlap and draw no epipolar line on either image plane; retain the cameras, baseline, rays, and one projection point per image plane. Both image-plane quadrilaterals must have complete lower boundaries. Only the short ray portions directly behind the image planes are subdued.
- Local Minimum subtitle: “Why local minima are rarely the problem.”
- System of Equations card title: “Linear Systems as Geometry”.
- Last four card order: Epipolar Geometry, Planar Homography, Perspective Projection, Correlation (aka "Convolution").
- Sphere to Cubemap and Sphere to Equirectangular Projection use the tighter accepted framing with reduced left/right empty margin while retaining modest breathing room and black raster edges.
- Partial Derivatives uses the vertically outpainted accepted framing with additional top/bottom breathing room.
- Correlation title: `Correlation (aka "Convolution")` and multiplication symbol `*` in the teaser. The active sliding 3×3 kernel over the input must use the same white-center/gray-cross/dark-corner weights as the displayed kernel immediately to the right of `*`.
- Author card: compact approximately 600px-wide card with no excess blank area on the right.

## Typography and page content

- Hero title: `#KostasVisualizations`, native kerning and subtly tightened tracking.
- Hero topics: `Computer Vision · Machine Learning · Optimization`.
- Collection heading: `See it. Move it. Understand it.`
- Collection right paragraph remains vertically centered against the entire left label-plus-headline block.
- Topics: projective geometry, optimization, linear algebra, signal processing, calculus.

## Final verification (must all pass)

- [x] Desktop light: visually inspect all 12 cards and author card.
- [x] Desktop dark: visually inspect all 12 cards and author card.
- [x] Mobile light: scroll through all 12 cards; verify top corners, side clipping, seams, and equal dimensions.
- [x] Mobile dark: scroll through all 12 cards; verify top corners, side clipping, seams, and equal dimensions.
- [x] Programmatically compare hero height, copy-top Y position, and total card height for every row.
- [x] Verify all source teaser files have identical dimensions and square raster corners.
- [x] Do not complete or deploy until every requested change has been visually verified in the rendered page.
- [x] Verify no browser errors in the validated local build. Confirm the production replacement assets immediately after deployment.
