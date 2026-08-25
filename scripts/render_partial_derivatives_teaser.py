#!/usr/bin/env python3
"""Render the partial-derivatives teaser from exact world-space geometry."""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "teasers"
W, H = 1672, 941
PANEL = (32, 240, 1640, 876)


def camera_basis():
    eye = np.array([5.4, -7.3, 4.2], dtype=float)
    target = np.array([0.0, 0.0, 0.0])
    forward = target - eye
    forward /= np.linalg.norm(forward)
    right = np.cross(forward, np.array([0.0, 0.0, 1.0]))
    right /= np.linalg.norm(right)
    up = np.cross(right, forward)
    return eye, forward, right, up


EYE, FORWARD, RIGHT, UP = camera_basis()


def project(points):
    pts = np.asarray(points, dtype=float)
    rel = pts - EYE
    depth = rel @ FORWARD
    u = rel @ RIGHT
    v = rel @ UP
    focal = 8.8 / np.maximum(depth, 0.1)
    x = 836 + 122 * u * focal
    y = 565 - 122 * v * focal
    return np.column_stack([x, y])


def surface_z(x, y):
    return 0.43 * (x * x - y * y)


def line(draw, points, fill, width):
    xy = project(points)
    draw.line([tuple(p) for p in xy], fill=fill, width=width, joint="curve")


def glow_line(base, points, color, width=5, glow=18):
    glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    xy = project(points)
    coords = [tuple(p) for p in xy]
    gd.line(coords, fill=(*color, 180), width=glow, joint="curve")
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(glow / 2))
    base.alpha_composite(glow_layer)
    ImageDraw.Draw(base).line(coords, fill=(*color, 255), width=width, joint="curve")


def render_panel():
    panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(panel, "RGBA")
    x0, y0, x1, y1 = PANEL
    draw.rounded_rectangle(PANEL, radius=42, fill=(7, 10, 12, 255), outline=(20, 42, 47, 255), width=2)

    # Subtle floor grid.
    for q in np.linspace(-3.0, 3.0, 13):
        line(draw, [[-3.2, q, -2.45], [3.2, q, -2.45]], (10, 77, 89, 75), 1)
        line(draw, [[q, -3.2, -2.45], [q, 3.2, -2.45]], (10, 77, 89, 75), 1)

    # One vertical slice plane y=c, drawn before the surface so the shared
    # seam and the cyan mesh remain legible through it.
    c = 0.55
    plane = np.array([
        [-2.45, c, -2.55], [2.45, c, -2.55],
        [2.45, c, 2.70], [-2.45, c, 2.70],
    ])
    pxy = project(plane)
    draw.polygon([tuple(p) for p in pxy], fill=(255, 101, 72, 34), outline=(255, 126, 91, 190), width=3)

    # Saddle fill, then exact wireframe z = .43(x²-y²).
    grid = np.linspace(-2.35, 2.35, 25)
    cells = []
    for i in range(len(grid) - 1):
        for j in range(len(grid) - 1):
            xa, xb = grid[i], grid[i + 1]
            ya, yb = grid[j], grid[j + 1]
            poly = np.array([
                [xa, ya, surface_z(xa, ya)],
                [xb, ya, surface_z(xb, ya)],
                [xb, yb, surface_z(xb, yb)],
                [xa, yb, surface_z(xa, yb)],
            ])
            depth = np.mean((poly - EYE) @ FORWARD)
            cells.append((depth, poly))
    for _, poly in sorted(cells, reverse=True):
        draw.polygon([tuple(p) for p in project(poly)], fill=(3, 30, 37, 80))

    cyan = (0, 201, 224, 170)
    samples = np.linspace(-2.35, 2.35, 180)
    for q in np.linspace(-2.35, 2.35, 19):
        line(draw, [[t, q, surface_z(t, q)] for t in samples], cyan, 2)
        line(draw, [[q, t, surface_z(q, t)] for t in samples], cyan, 2)

    curve_x = np.linspace(-2.35, 2.35, 300)
    curve = np.column_stack([curve_x, np.full_like(curve_x, c), surface_z(curve_x, c)])
    glow_line(panel, curve, (255, 102, 74), width=6, glow=24)

    # Exact tangent to z=.43(x²-c²) at x=t0.
    t0 = -0.72
    z0 = surface_z(t0, c)
    slope = 0.86 * t0
    tangent_x = np.linspace(t0 - 0.95, t0 + 0.95, 120)
    tangent = np.column_stack([
        tangent_x,
        np.full_like(tangent_x, c),
        z0 + slope * (tangent_x - t0),
    ])
    glow_line(panel, tangent, (245, 248, 250), width=5, glow=18)

    point = project([[t0, c, z0]])[0]
    draw = ImageDraw.Draw(panel, "RGBA")
    r = 8
    draw.ellipse((point[0]-r, point[1]-r, point[0]+r, point[1]+r), fill=(255, 112, 82, 255), outline=(255, 255, 255, 255), width=2)
    # The art is clipped to the established visualization panel; nothing may
    # bleed into the preserved title region.
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).rounded_rectangle(PANEL, radius=42, fill=255)
    clipped = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    clipped.paste(panel, (0, 0), mask)
    return clipped


def make_variant(mode):
    source = OUT / f"partial-derivatives-{mode}.png"
    original = Image.open(source).convert("RGBA")
    panel = render_panel()
    # Preserve the established title/subtitle region exactly; replace only art.
    base = original.copy()
    base.paste((250, 247, 243, 255) if mode == "light" else (0, 0, 0, 255), PANEL)
    base.alpha_composite(panel)
    base.convert("RGB").save(source, quality=96)


if __name__ == "__main__":
    make_variant("dark")
    make_variant("light")
