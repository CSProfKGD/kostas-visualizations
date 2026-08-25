from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(
    "/Users/kosta/.codex/generated_images/"
    "01a0396b-3a11-7392-ba1d-7b8395e70743/"
    "exec-c291136d-f265-471d-9994-1dab0fdcc46f.png"
)
OUTPUT = ROOT / "public/masters/parallel-stereo-master.png"


def erase_cyan_dashes(image: Image.Image, x0: int, x1: int, y_at_x) -> None:
    pixels = image.load()
    original = image.copy().load()
    for x in range(x0, x1 + 1):
        center_y = round(y_at_x(x))
        for y in range(center_y - 10, center_y + 11):
            r, g, b = original[x, y]
            if r < 70 and g > 105 and b > 105:
                samples = []
                for delta in (-13, -11, 11, 13):
                    sr, sg, sb = original[x, y + delta]
                    if not (sr < 70 and sg > 105 and sb > 105):
                        samples.append((sr, sg, sb))
                if samples:
                    pixels[x, y] = tuple(sum(v[i] for v in samples) // len(samples) for i in range(3))


def dashed_line(draw: ImageDraw.ImageDraw, start, end, fill, width=3, dash=11, gap=8) -> None:
    x0, y0 = start
    x1, y1 = end
    length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    position = 0.0
    while position < length:
        stop = min(position + dash, length)
        a = position / length
        b = stop / length
        draw.line(
            (
                x0 + (x1 - x0) * a,
                y0 + (y1 - y0) * a,
                x0 + (x1 - x0) * b,
                y0 + (y1 - y0) * b,
            ),
            fill=fill,
            width=width,
        )
        position += dash + gap


def line_through_point_parallel_to_edge(edge_start, edge_end, point):
    x0, y0 = edge_start
    x1, y1 = edge_end
    px, py = point
    slope = (y1 - y0) / (x1 - x0)
    return (x0, py + slope * (x0 - px)), (x1, py + slope * (x1 - px)), slope


def main() -> None:
    image = Image.open(SOURCE).convert("RGB")

    # Existing generative dashes, used only to identify and remove cyan pixels.
    erase_cyan_dashes(image, 217, 540, lambda x: 625 + (655 - 625) * (x - 217) / (540 - 217))
    erase_cyan_dashes(image, 704, 1032, lambda x: 668 + (690 - 668) * (x - 704) / (1032 - 704))

    draw = ImageDraw.Draw(image)
    cyan = (0, 226, 230)
    red = (238, 55, 43)
    marker_outline = (247, 245, 231)

    left_point = (368, 638)
    right_point = (850, 676)
    left_start, left_end, _ = line_through_point_parallel_to_edge((217, 501), (540, 534), left_point)
    right_start, right_end, _ = line_through_point_parallel_to_edge((704, 547), (1032, 578), right_point)

    dashed_line(draw, left_start, left_end, cyan)
    dashed_line(draw, right_start, right_end, cyan)

    for x, y in (left_point, right_point, (1409, 433)):
        draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=red, outline=marker_outline, width=3)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, optimize=True)


if __name__ == "__main__":
    main()
