"""Builds a slideshow GIF from the AI License Manager screenshots."""

from pathlib import Path

from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = REPO_ROOT / "assets" / "Screenshots"
OUTPUT_PATH = REPO_ROOT / "assets" / "ai-license-manager-demo.gif"

# Ordered for a natural walkthrough: scorecard -> dashboard overview -> full
# dashboard -> metrics detail -> requests table.
SOURCE_FILES = [
    "scorecard.png",
    "dashboard.png",
    "dashboard_full.png",
    "metrics_full.png",
    "requests.png",
]

TARGET_WIDTH = 800
MAX_FRAME_HEIGHT = 620
FRAME_DURATION_MS = 1800
HOLD_LAST_FRAME_MS = 2600


def load_resize_and_crop(path: Path, width: int, max_height: int) -> Image.Image:
    image = Image.open(path).convert("RGB")
    scale = width / image.width
    resized_height = round(image.height * scale)
    resized = image.resize((width, resized_height), Image.LANCZOS)

    if resized_height <= max_height:
        return resized

    # Long, scrolled screenshots: keep the top viewport (header + first content)
    # instead of squeezing the whole page into every frame.
    return resized.crop((0, 0, width, max_height))


def build_gif() -> None:
    frames = [load_resize_and_crop(SOURCE_DIR / name, TARGET_WIDTH, MAX_FRAME_HEIGHT) for name in SOURCE_FILES]

    palette_frames = [frame.convert("P", palette=Image.ADAPTIVE, colors=256) for frame in frames]
    durations = [FRAME_DURATION_MS] * (len(palette_frames) - 1) + [HOLD_LAST_FRAME_MS]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    palette_frames[0].save(
        OUTPUT_PATH,
        save_all=True,
        append_images=palette_frames[1:],
        duration=durations,
        loop=0,
        optimize=False,
    )
    print(f"Saved {OUTPUT_PATH} ({TARGET_WIDTH}x{MAX_FRAME_HEIGHT}, {len(palette_frames)} frames)")


if __name__ == "__main__":
    build_gif()
