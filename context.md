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
- The complete card is clickable; no arrow or “Open visualization” label.

## Accepted content and replacements

- Perspective Projection: use the new photoreal scene with tree/rocks, opaque pinhole plane, one ray, and inverted image-plane projection. The incident ray remains visible from the world point to the pinhole, is hidden only while passing behind the opaque plane, and reappears after clearing the plane to continue to the projected image point.
- Sphere to Cubemap and Sphere to Equirectangular Projection: use the outpainted compositions with black background at every raster edge and modest breathing room around the complete globe and mapping diagram. Do not restore CSS downscaling that exposes the card surface.
- Parallel Stereo: keep both rendered views unchanged. Each projection ray is one collinear world-point → rendered pixel → camera-center line. Epipolar lines pass through the projected pixels and use symmetric inward-converging orientations consistent with the converging cameras.
- Stereo Rectification, Epipolar Geometry, Local Minimum, and Parallel Stereo use outpainted compositions with black background at every raster edge and breathing room around all cameras, points, surfaces, paths, and image planes.
- Partial Derivatives: use the new simplified saddle, one vertical slice plane, true intersection curve, and tangent line. Do not use the older two-plane image.
- Planar Homography: no correspondence lines. Use four uniquely colored paired corner points on source and rectified image.
- Epipolar Geometry: use the clean outline-only triangle through the cameras and one world point. Remove the misleading translucent interior overlap and draw no epipolar line on either image plane; retain the cameras, baseline, rays, and one projection point per image plane.
- Local Minimum subtitle: “Why local minima are rarely the problem.”
- System of Equations card title: “Linear Systems as Geometry”.
- Final row order: Perspective Projection, Epipolar Geometry, Correlation (aka "Convolution").
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
- [ ] Verify no browser errors and production deployment renders the replacement Perspective Projection and Partial Derivatives teasers.
