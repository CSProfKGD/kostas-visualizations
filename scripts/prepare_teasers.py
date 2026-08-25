from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
TEASERS = ROOT / "public/teasers"
GENERATED = Path(
    "/Users/kosta/.codex/generated_images/"
    "01a0396b-3a11-7392-ba1d-7b8395e70743"
)
SIZE = (1672, 625)


def resize(source: Path) -> Image.Image:
    return Image.open(source).convert("RGB").resize(SIZE, Image.Resampling.LANCZOS)


def save_pair(image: Image.Image, slug: str) -> None:
    for theme in ("dark", "light"):
        image.save(TEASERS / f"{slug}-{theme}.png", optimize=True)


def sphere_assets() -> None:
    cubemap = resize(GENERATED / "exec-b3dd34aa-e572-464a-bc41-bb3e506979ad.png")
    erp = resize(GENERATED / "exec-4a029350-60e5-4701-b7c3-56c301f972d1.png")
    save_pair(cubemap, "sphere-to-cubemap")
    save_pair(erp, "sphere-to-erp")


def homography_asset() -> None:
    image = resize(ROOT / "public/masters/planar-homography-master.png")
    save_pair(image, "planar-homography")


def stereo_asset() -> None:
    image = resize(ROOT / "public/masters/parallel-stereo-master.png")
    save_pair(image, "parallel-stereo")


def perspective_asset() -> None:
    image = resize(GENERATED / "exec-840f9024-4186-425f-8082-6a34b9a9373e.png")
    draw = ImageDraw.Draw(image)

    # The opaque pinhole plate hides only the short portion centered on the
    # pinhole. The incident and post-plate portions remain fully cyan.
    draw.line((824, 246, 866, 257), fill=(57, 75, 78), width=4)
    draw.ellipse((838, 244, 854, 260), fill=(255, 164, 111), outline=(235, 239, 232), width=2)
    save_pair(image, "perspective-projection")


def epipolar_asset() -> None:
    image = Image.open(TEASERS / "epipolar-geometry-dark.png").convert("RGB")
    draw = ImageDraw.Draw(image)
    orange = (255, 101, 66)
    subdued = (117, 64, 49)

    # Re-establish bright, perfectly collinear camera-to-world rays.
    draw.line((301, 495, 838, 64), fill=orange, width=4)
    draw.line((1363, 495, 838, 64), fill=orange, width=4)

    # Dim only the portions that are directly behind the finite image-plane
    # footprints in screen space; everything before and after stays bright.
    draw.line((366, 443, 599, 256), fill=subdued, width=4)
    draw.line((1068, 279, 1306, 470), fill=subdued, width=4)

    for x, y in ((495, 335), (1196, 351), (838, 64)):
        draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill=orange, outline=(255, 210, 188), width=2)
    save_pair(image, "epipolar-geometry")


def main() -> None:
    sphere_assets()
    homography_asset()
    stereo_asset()
    perspective_asset()
    epipolar_asset()


if __name__ == "__main__":
    main()
