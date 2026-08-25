# Working Agreement for Kosta's Visualizations

Before making any change in this repository, read this file and `context.md` completely. Treat `context.md` as the current source of truth for accepted content, asset choices, unresolved work, and final verification status.

## Product standard

- Aim for Apple Keynote-level visual polish: restrained, precise, consistent, and free of incidental visual noise.
- Preserve the user's accepted wording, links, teaser concepts, and theme behavior unless the user explicitly changes them.
- Never infer the live production site is the latest state. Compare it with `context.md` and the local working tree first.
- Do not restore older teaser generations over the accepted replacements listed in `context.md`.

## Card system invariants

- Implement geometry fixes in the shared card component/CSS unless a card truly requires distinct educational artwork.
- At each breakpoint, every visualization card must have identical width, total height, hero height, copy height, and outer corner shape.
- The outer card is the only rounded clipping boundary.
- Source teaser rasters must all have identical pixel dimensions and orthogonal/square corners. Never ship baked rounded image-panel corners.
- Teasers must meet the card's top, left, and right edges inside the card silhouette and end at one straight, consistently aligned hero-to-copy seam.
- Light and dark modes must use identical image scale, crop, and card geometry.
- Avoid negative margins, viewport-relative image widths, decorative pseudo-element overflow, or transforms that alter shared geometry.

## Asset workflow

- Keep dark and light teaser files dimensionally identical.
- When a generated teaser is accepted, record its concept in `context.md` before replacing files.
- For educational geometry, prefer deterministic construction or deterministic cleanup when a generated image introduces incorrect rays, intersections, correspondences, or occlusion.
- Preserve the original generated file when copying it into the site.

## Required verification before completion

1. Build the site successfully and run static checks.
2. Inspect every visualization card in desktop light mode.
3. Inspect every visualization card in desktop dark mode.
4. Inspect every visualization card while scrolling in mobile light mode.
5. Inspect every visualization card while scrolling in mobile dark mode.
6. Programmatically compare card width, total height, hero height, copy-top position, and border radius for all cards at each tested breakpoint.
7. Verify the compact author card in desktop and mobile layouts.
8. Check browser console errors.
9. After deployment, inspect the production URL and confirm the newest Perspective Projection, Partial Derivatives, Planar Homography, and Epipolar Geometry assets are live.
10. Update `context.md` checkboxes to reflect only checks actually completed.

Do not report completion until these checks pass. If any check fails, fix the shared underlying cause, repeat the affected checks, and then continue.

