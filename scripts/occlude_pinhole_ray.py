#!/usr/bin/env python3
"""Render a pinhole ray whose dim segment ends exactly at the plane edge."""

from pathlib import Path
import sys

import numpy as np
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]


def occlude(source: Path, output: Path):
    image = Image.open(source).convert("RGB")
    if image.size != (1672, 941):
        raise ValueError(f"Expected the full 1672x941 master, got {image.size}")

    arr = np.asarray(image).copy()
    yy, xx = np.indices(arr.shape[:2])

    # The ray is the line through the marked world point and pinhole. The
    # incident segment remains visible. The source artwork already contains a
    # subdued outgoing segment behind the opaque plane; restore full cyan at
    # the exact projected right boundary so the dim segment cannot overrun it.
    ray_y = 0.24164 * xx + 324.0
    restored = Image.fromarray(arr)
    draw = ImageDraw.Draw(restored, "RGBA")
    plane_right_x = 929
    image_point_x = 1383
    draw.line(
        (
            plane_right_x,
            float(ray_y[0, plane_right_x]),
            image_point_x,
            float(ray_y[0, image_point_x]),
        ),
        fill=(24, 232, 246, 255),
        width=4,
    )

    # Export only the visualization region used by every teaser card.
    restored.crop((0, 258, 1672, 883)).save(output, optimize=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: occlude_pinhole_ray.py SOURCE_MASTER OUTPUT")
    occlude(Path(sys.argv[1]), Path(sys.argv[2]))
