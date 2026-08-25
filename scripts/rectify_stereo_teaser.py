from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
TEASERS = ROOT / "public" / "teasers"

# Interior corners of the photographed trapezoid, clockwise from top-left.
SOURCE_QUAD = np.array(
    [[245.0, 319.0], [611.0, 319.0], [756.0, 778.0], [96.0, 778.0]],
    dtype=np.float64,
)

# Keep the existing cyan destination border and coral corner markers untouched.
DEST_BOX = (887, 318, 1582, 782)


def perspective_coefficients(width: int, height: int) -> tuple[float, ...]:
    destination = np.array(
        [[0.0, 0.0], [float(width), 0.0], [float(width), float(height)], [0.0, float(height)]],
        dtype=np.float64,
    )
    matrix = []
    values = []
    for (x, y), (u, v) in zip(destination, SOURCE_QUAD):
        matrix.extend(
            [
                [x, y, 1.0, 0.0, 0.0, 0.0, -u * x, -u * y],
                [0.0, 0.0, 0.0, x, y, 1.0, -v * x, -v * y],
            ]
        )
        values.extend([u, v])
    return tuple(np.linalg.solve(np.asarray(matrix), np.asarray(values)))


def rectify(path: Path) -> None:
    image = Image.open(path).convert("RGB")
    pixels = np.asarray(image)
    cyan = (
        (pixels[:, :, 0] < 125)
        & (pixels[:, :, 1] > 65)
        & (pixels[:, :, 2] > 70)
        & (pixels[:, :, 1] > pixels[:, :, 0] * 1.15)
        & (pixels[:, :, 2] > pixels[:, :, 0] * 1.2)
    )
    expanded_mask = np.asarray(
        Image.fromarray((cyan * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(size=9))
    ) > 0
    cleaned = np.array(image.filter(ImageFilter.MedianFilter(size=15)))
    source = pixels.copy()
    source[expanded_mask] = cleaned[expanded_mask]
    source_image = Image.fromarray(source)
    left, top, right, bottom = DEST_BOX
    width, height = right - left, bottom - top
    patch = source_image.transform(
        (width, height),
        Image.Transform.PERSPECTIVE,
        perspective_coefficients(width, height),
        resample=Image.Resampling.BICUBIC,
    )
    image.paste(patch, (left, top))
    draw = ImageDraw.Draw(image, "RGBA")
    grid = (39, 199, 214, 118)
    for column in range(1, 10):
        x = left + round(width * column / 10)
        draw.line((x, top, x, bottom), fill=grid, width=1)
    for row in range(1, 7):
        y = top + round(height * row / 7)
        draw.line((left, y, right, y), fill=grid, width=1)
    draw.line((left, top, right, top), fill=(59, 216, 226, 210), width=2)
    draw.line((right, top, right, bottom), fill=(59, 216, 226, 210), width=2)
    draw.line((right, bottom, left, bottom), fill=(59, 216, 226, 210), width=2)
    draw.line((left, bottom, left, top), fill=(59, 216, 226, 210), width=2)
    draw.line((left, top + height // 2, right, top + height // 2), fill=(255, 105, 78, 210), width=2)
    image.save(path, format="PNG", optimize=True)


for variant in ("dark", "light"):
    rectify(TEASERS / f"stereo-rectification-{variant}.png")
