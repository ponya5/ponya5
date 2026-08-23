from pathlib import Path

import numpy as np
from PIL import Image

ICONS_DIR = Path(__file__).resolve().parents[1] / "assets" / "icons"
WHITE_THRESHOLD = 235


def replace_white_with_black(frame: Image.Image) -> Image.Image:
    rgb_frame = frame.convert("RGB")
    pixel_array = np.array(rgb_frame)
    white_mask = (
        (pixel_array[:, :, 0] >= WHITE_THRESHOLD)
        & (pixel_array[:, :, 1] >= WHITE_THRESHOLD)
        & (pixel_array[:, :, 2] >= WHITE_THRESHOLD)
    )
    pixel_array[white_mask] = [0, 0, 0]
    return Image.fromarray(pixel_array, "RGB")


def process_gif(gif_path: Path) -> None:
    source_image = Image.open(gif_path)
    rgb_frames = []
    frame_durations = []

    for frame_index in range(source_image.n_frames):
        source_image.seek(frame_index)
        rgb_frames.append(replace_white_with_black(source_image))
        frame_durations.append(source_image.info.get("duration", 100))

    palette_frames = [
        frame.convert("P", palette=Image.ADAPTIVE, colors=256) for frame in rgb_frames
    ]

    palette_frames[0].save(
        gif_path,
        save_all=True,
        append_images=palette_frames[1:],
        duration=frame_durations,
        loop=source_image.info.get("loop", 0),
        disposal=2,
        optimize=False,
    )
    print(f"Processed {gif_path.name} ({len(palette_frames)} frames)")


def main() -> None:
    for gif_file in sorted(ICONS_DIR.glob("*.gif")):
        process_gif(gif_file)

    test_file = ICONS_DIR / "_test_frame0.png"
    if test_file.exists():
        test_file.unlink()


if __name__ == "__main__":
    main()
