#!/usr/bin/env python3
"""Convert full teaser compositions into uniform, square-corner card rasters."""

from pathlib import Path

from PIL import Image, PngImagePlugin


ROOT = Path(__file__).resolve().parents[1]
TEASERS = ROOT / "public" / "teasers"
SOURCE_SIZE = (1672, 941)
CARD_SIZE = (1672, 625)

# All generated compositions use the same visualization-panel placement. This
# final crop sits entirely inside its baked rounded outline, so the exported
# raster itself has four orthogonal corners. The ratio matches CARD_SIZE.
MASTER_CARD_CROP = (90, 278, 1582, 835)

# One-time migration for the earlier 1672×625 crops. It is the exact scaled
# equivalent of MASTER_CARD_CROP and is guarded by a PNG metadata marker so it
# cannot repeatedly zoom an already-finalized asset.
LEGACY_CARD_CROP = (60, 20, 1612, 600)
FORMAT_MARKER = "orthogonal-card-v2"


def prepare(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    if Image.open(path).info.get("card_teaser_format") == FORMAT_MARKER:
        return
    if image.size == SOURCE_SIZE:
        crop = MASTER_CARD_CROP
    elif image.size == CARD_SIZE:
        crop = LEGACY_CARD_CROP
    else:
        raise ValueError(f"Unexpected teaser size for {path.name}: {image.size}")

    card = image.crop(crop).resize(CARD_SIZE, Image.Resampling.LANCZOS)
    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("card_teaser_format", FORMAT_MARKER)
    card.save(path, optimize=True, pnginfo=metadata)


if __name__ == "__main__":
    for teaser in sorted(TEASERS.glob("*.png")):
        prepare(teaser)
