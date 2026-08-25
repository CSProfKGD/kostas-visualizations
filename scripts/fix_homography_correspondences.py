#!/usr/bin/env python3
"""Replace decorative homography guides with exact corner correspondences."""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "teasers"
SOURCE = [(280, 352), (594, 443), (594, 730), (278, 760)]
TARGET = [(1002, 358), (1539, 358), (1539, 760), (1002, 760)]
COLORS = [
    (255, 105, 76),   # top-left: coral
    (255, 203, 84),   # top-right: gold
    (202, 102, 255),  # bottom-right: violet
    (76, 214, 255),   # bottom-left: sky blue
]


def fix(path: Path):
    image = Image.open(path).convert("RGB")
    arr = np.asarray(image)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    # Select the coral correspondence graphics, not the cyan quadrilateral.
    mask = (r > 185) & (g > 45) & (g < 175) & (b < 145) & ((r.astype(int) - g.astype(int)) > 70)
    mask_img = Image.fromarray((mask * 255).astype("uint8")).filter(ImageFilter.MaxFilter(11))
    clean = image.filter(ImageFilter.MedianFilter(15))
    image.paste(clean, mask=mask_img)

    draw = ImageDraw.Draw(image)
    for source, target, color in zip(SOURCE, TARGET, COLORS):
        for x, y in (source, target):
            draw.ellipse((x - 13, y - 13, x + 13, y + 13), fill=color,
                         outline=(245, 248, 250), width=2)
    image.save(path, quality=96)


if __name__ == "__main__":
    fix(OUT / "planar-homography-dark.png")
    fix(OUT / "planar-homography-light.png")
