from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(
    "/Users/kosta/.codex/generated_images/"
    "01a0396b-3a11-7392-ba1d-7b8395e70743/"
    "exec-b92797f8-8ba9-449d-88a5-6752f0e2b429.png"
)
OUTPUT = ROOT / "public/masters/planar-homography-master.png"


def main() -> None:
    image = Image.open(SOURCE).convert("RGB")

    # Source quadrilateral, ordered UL, UR, LR, LL. These are the cyan
    # quadrilateral corners beneath the marker centers in the master render.
    ul = (248, 101)
    ur = (656, 221)
    lr = (656, 604)
    ll = (246, 649)

    # Destination rectified image, ordered UL, UR, LR, LL.
    dul = (1197, 104)
    dur = (1919, 104)
    dlr = (1919, 649)
    dll = (1197, 649)
    width = dur[0] - dul[0]
    height = dll[1] - dul[1]

    # PIL QUAD expects source UL, LL, LR, UR for a rectangular output. This
    # is a single projective resampling of the selected source patch, not an
    # independently recomposed portrait.
    patch = image.transform(
        (width, height),
        Image.Transform.QUAD,
        (ul[0], ul[1], ll[0], ll[1], lr[0], lr[1], ur[0], ur[1]),
        resample=Image.Resampling.BICUBIC,
    )
    image.paste(patch, dul)

    draw = ImageDraw.Draw(image)
    cyan = (29, 219, 239)
    stroke = 5

    # The generated source already contains a slightly offset yellow marker at
    # the destination's upper-right corner. Clear that small source artifact
    # before rebuilding the border and drawing the single canonical marker.
    draw.rectangle((1888, 78, 1940, 140), fill=(0, 0, 0))
    draw.rectangle((dul[0], dul[1], dur[0], dlr[1]), outline=cyan, width=stroke)

    markers = [
        (dul, (255, 103, 67)),
        (dur, (255, 195, 57)),
        (dll, (42, 195, 232)),
        (dlr, (153, 111, 229)),
    ]
    radius = 17
    for (x, y), color in markers:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)

    image.save(OUTPUT, optimize=True)


if __name__ == "__main__":
    main()
