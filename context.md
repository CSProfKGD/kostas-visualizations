# Kosta's Visualizations — Current State

Updated: 2026-08-28

## Production

- Site: https://kostas-visualizations.csprofkgd.chatgpt.site/
- The current production site is an older deployment. Do not treat its visible teaser images or card sizing as the accepted local state.
- Publish only after all checks under **Final verification** pass.

## Authoritative shared card state

- Seventeen cards in a three-column desktop grid, two-column tablet grid, and one-column mobile grid.
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

- Steerable Filters: place immediately before `Correlation (aka "Convolution")`. Use title “Steerable Filters,” subtitle “A Few Filters. Infinite Orientations.,” Signal Processing category, and `https://csprofkgd.github.io/steerable-filters/`. Use the user-supplied `steerable_filters_analytic_1672x625.png` at the shared 1672×625 canvas and use the identical raster in light and dark modes.
- Goldilocks Learning Rates: place directly after “Stuck in a Bad Local Minimum?” and before “Gradient Descent.” Use the hero title “The Goldilocks Principle of Learning Rates,” subtitle “One number. Three very different outcomes.,” Optimization category, and `https://csprofkgd.github.io/goldilocks-learning-rates/`. Use the tightly framed, horizontally outpainted teddy-bear/bowl composition on the shared 1672×625 teaser canvas, with the indigo-purple scene continuing seamlessly to every raster edge and no black side bars; use the identical raster in light and dark modes.
- 2D Transformations: place immediately before “Fourier Series.” Use title “2D Transformations,” subtitle “Geometry in motion.,” Linear Algebra category, and `https://drive.google.com/file/d/1UOIV_mkT-X_syESycezc6ibneYpDvGXa/view?usp=sharing`. Use the user-supplied `2D transformations teaser.png`, normalized to the shared 1672×625 canvas and used identically in light and dark modes.
- Fourier Series: place after “2D Transformations” and before “Taylor Series Approximation.” Use title “Fourier Series,” subtitle “Complicated Shapes. Simple Ingredients.,” Signal Processing category, and `https://drive.google.com/file/d/1wQ2iaEX813kKAGonzwIgRop6bit9Utgk/view?usp=sharing`. Use the user-supplied `Fourier Series.png` on the shared 1672×625 canvas and use the identical raster in light and dark modes.
- Taylor Series Approximation: final card in the collection, after “Fourier Series.” Use title “Taylor Series Approximation,” subtitle “Local Insight. Global Impact.,” Calculus category, and `https://drive.google.com/file/d/1BNJAcvfXrMaTG_1M5yJ4OVxMfasgMo_T/view?usp=sharing`. Preserve the user-supplied `taylor_series_fx_label_raised_1696x624.png` as the master, normalize it to the shared 1672×625 canvas, and use the identical raster in light and dark modes.
- Perspective Projection: use the user-supplied `/Users/kosta/Downloads/PP_black.png`, normalized to the shared 1672×625 teaser canvas and used identically in light and dark modes.
- Sphere to Cubemap and Sphere to Equirectangular Projection: use the outpainted compositions with black background at every raster edge and modest breathing room around the complete globe and mapping diagram. Preserve every legitimate cyan latitude/longitude arc and every cyan cubemap/ERP segment outline. Remove the orange/coral vertical meridian and all associated glow from both representations.
- Parallel Stereo: use the user-supplied `/Users/kosta/Downloads/binocular.png` raster, already at the shared 1672×625 canvas, identically for both dark and light teaser assets.
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
- Mobile portrait and landscape card copy regions use a compact shared 126px height with vertically balanced copy and no excessive dead space below the descriptions.
- In mobile landscape, the author card shrink-wraps its portrait, copy, and link controls so no unused panel area remains on the right.

## Typography and page content

- Hero title: `#KostasVisualizations`, native kerning and subtly tightened tracking.
- Hero topics: `Computer Vision · Machine Learning · Optimization`.
- Collection heading: `See it. Move it. Understand it.`
- Collection right paragraph remains vertically centered against the entire left label-plus-headline block.
- Topics: projective geometry, optimization, linear algebra, signal processing, calculus.

## Final verification (must all pass)

- [x] Desktop light: visually inspect all 17 cards and author card.
- [x] Desktop dark: visually inspect all 17 cards and author card.
- [x] Mobile light: scroll through all 17 cards; verify top corners, side clipping, seams, and equal dimensions.
- [x] Mobile dark: scroll through all 17 cards; verify top corners, side clipping, seams, and equal dimensions.
- [x] Programmatically compare hero height, copy-top Y position, and total card height for every row.
- [x] Verify all source teaser files have identical dimensions and square raster corners.
- [x] Do not complete or deploy until every requested change has been visually verified in the rendered page.
- [x] Verify no browser errors in the validated local build. Confirm the production replacement assets immediately after deployment.
