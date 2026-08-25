#!/usr/bin/env python3
"""Keep the incident ray visible and remove only its hidden outgoing segment."""

from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def occlude(path: Path):
    image = Image.open(path).convert("RGB")
    if image.size != (1672, 941):
        raise ValueError(f"Expected the full 1672x941 master, got {image.size}")

    arr = np.asarray(image).copy()
    yy, xx = np.indices(arr.shape[:2])

    # The ray is the line through the marked world point and pinhole. The
    # incident segment at the left must remain visible all the way to the
    # aperture; only the segment to the right of the pinhole is hidden.
    ray_y = 0.24164 * xx + 324.0
    plane = (xx >= 744) & (xx <= 929) & (yy >= 290) & (yy <= 770)
    pinhole = (xx - 836) ** 2 + (yy - 526) ** 2 <= 10 ** 2
    hidden_ray = plane & (xx > 846) & (np.abs(yy - ray_y) <= 15) & ~pinhole

    upper_y = np.clip((ray_y - 24).astype(int), 0, arr.shape[0] - 1)
    lower_y = np.clip((ray_y + 24).astype(int), 0, arr.shape[0] - 1)
    columns = np.broadcast_to(np.arange(arr.shape[1]), arr.shape[:2])
    replacement = (
        arr[upper_y, columns].astype(np.uint16)
        + arr[lower_y, columns].astype(np.uint16)
    ) // 2
    arr[hidden_ray] = replacement[hidden_ray].astype(np.uint8)
    Image.fromarray(arr).save(path, optimize=True)


if __name__ == "__main__":
    for mode in ("dark", "light"):
        occlude(ROOT / "public" / "teasers" / f"perspective-projection-{mode}.png")
