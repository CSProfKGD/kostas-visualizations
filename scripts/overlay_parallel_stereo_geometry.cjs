const sharp = require("sharp");

const [inputPath, outputPath] = process.argv.slice(2);

if (!inputPath || !outputPath) {
  throw new Error("Usage: node overlay_parallel_stereo_geometry.cjs INPUT OUTPUT");
}

const width = 2051;
const height = 767;

const worldPoint = { x: 1644, y: 124 };
const cameraCenters = [
  { x: 676, y: 541 },
  { x: 1084, y: 588 },
];

// Same normalized vertical coordinate (v = 0.8) in the two parallel planes.
const scanlines = [
  [{ x: 545, y: 451 }, { x: 845, y: 486 }],
  [{ x: 991, y: 502 }, { x: 1307, y: 535 }],
];

// Screen-space outlines of the two rendered image planes. The ray is dimmed
// only while it is visually behind the plane, from the projected pixel to the
// exact boundary where it exits toward the 3D world point.
const imagePlanes = [
  [
    { x: 545, y: 320 },
    { x: 845, y: 350 },
    { x: 845, y: 520 },
    { x: 548, y: 486 },
  ],
  [
    { x: 991, y: 366 },
    { x: 1307, y: 398 },
    { x: 1307, y: 570 },
    { x: 991, y: 535 },
  ],
];

function intersection(a, b, c, d) {
  const denominator = (a.x - b.x) * (c.y - d.y) -
    (a.y - b.y) * (c.x - d.x);
  const x = ((a.x * b.y - a.y * b.x) * (c.x - d.x) -
    (a.x - b.x) * (c.x * d.y - c.y * d.x)) / denominator;
  const y = ((a.x * b.y - a.y * b.x) * (c.y - d.y) -
    (a.y - b.y) * (c.x * d.y - c.y * d.x)) / denominator;
  return { x, y };
}

const imagePoints = cameraCenters.map((center, index) =>
  intersection(center, worldPoint, scanlines[index][0], scanlines[index][1]),
);

function segmentIntersection(a, b, c, d) {
  const denominator = (a.x - b.x) * (c.y - d.y) -
    (a.y - b.y) * (c.x - d.x);
  if (Math.abs(denominator) < 1e-9) return null;
  const t = ((a.x - c.x) * (c.y - d.y) -
    (a.y - c.y) * (c.x - d.x)) / denominator;
  const u = -((a.x - b.x) * (a.y - c.y) -
    (a.y - b.y) * (a.x - c.x)) / denominator;
  if (t < 1e-4 || t > 1 || u < 0 || u > 1) return null;
  return {
    point: {
      x: a.x + t * (b.x - a.x),
      y: a.y + t * (b.y - a.y),
    },
    t,
  };
}

const planeExits = imagePoints.map((point, index) => {
  const polygon = imagePlanes[index];
  const hits = polygon
    .map((corner, edgeIndex) =>
      segmentIntersection(
        point,
        worldPoint,
        corner,
        polygon[(edgeIndex + 1) % polygon.length],
      ),
    )
    .filter(Boolean)
    .sort((a, b) => a.t - b.t);
  if (!hits.length) throw new Error(`No plane exit found for camera ${index}`);
  return hits[0].point;
});

const line = (a, b, attributes) =>
  `<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" ${attributes}/>`;

const marker = (point, radius = 7) => `
  <circle cx="${point.x}" cy="${point.y}" r="${radius + 3}" fill="#ff684a" opacity="0.22"/>
  <circle cx="${point.x}" cy="${point.y}" r="${radius}" fill="#ff684a" stroke="#fff2e8" stroke-width="2.5"/>
`;

const svg = `
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
  <g fill="none" stroke="#25d8ea" stroke-width="2.4" stroke-dasharray="10 8" opacity="0.9">
    ${line(scanlines[0][0], scanlines[0][1], "")}
    ${line(scanlines[1][0], scanlines[1][1], "")}
  </g>
  <g fill="none" stroke="#ff684a" stroke-width="3.6" stroke-linecap="round">
    ${line(cameraCenters[0], imagePoints[0], "")}
    ${line(cameraCenters[1], imagePoints[1], "")}
    ${line(planeExits[0], worldPoint, "")}
    ${line(planeExits[1], worldPoint, "")}
  </g>
  <g fill="none" stroke="#ff684a" stroke-width="3.6" stroke-linecap="round" opacity="0.28">
    ${line(imagePoints[0], planeExits[0], "")}
    ${line(imagePoints[1], planeExits[1], "")}
  </g>
  ${marker(imagePoints[0])}
  ${marker(imagePoints[1])}
  ${marker(worldPoint, 8)}
</svg>`;

sharp(inputPath)
  .composite([{ input: Buffer.from(svg), top: 0, left: 0 }])
  .png()
  .toFile(outputPath);
