from pathlib import Path

import numpy as np
from PIL import Image

ICONS_DIR = Path(__file__).resolve().parents[1] / "assets" / "icons"
TRANSPARENT_INDEX = 255


def build_transparency_mask(red: np.ndarray, green: np.ndarray, blue: np.ndarray) -> np.ndarray:
    brightness = (red.astype(np.int16) + green.astype(np.int16) + blue.astype(np.int16)) / 3
    saturation = (
        np.maximum(red, np.maximum(green, blue)).astype(np.int16)
        - np.minimum(red, np.minimum(green, blue)).astype(np.int16)
    )

    near_black_canvas = (red <= 20) & (green <= 20) & (blue <= 20)
    pure_white = (red >= 235) & (green >= 235) & (blue >= 235)
    light_blue_white = (red >= 180) & (green >= 180) & (blue >= 200)
    bright_low_saturation = (brightness >= 215) & (saturation < 55)

    return near_black_canvas | pure_white | light_blue_white | bright_low_saturation


def frame_to_transparent_palette(rgba_frame: Image.Image) -> Image.Image:
    alpha_channel = rgba_frame.split()[3]
    palette_frame = rgba_frame.convert("RGB").convert("P", palette=Image.ADAPTIVE, colors=255)
    transparency_mask = Image.eval(alpha_channel, lambda alpha: 255 if alpha <= 128 else 0)
    palette_frame.paste(TRANSPARENT_INDEX, transparency_mask)
    return palette_frame


def make_frame_transparent(frame: Image.Image) -> Image.Image:
    rgba_frame = frame.convert("RGBA")
    pixel_array = np.array(rgba_frame)
    red = pixel_array[:, :, 0]
    green = pixel_array[:, :, 1]
    blue = pixel_array[:, :, 2]

    transparency_mask = build_transparency_mask(red, green, blue)
    pixel_array[transparency_mask, 3] = 0
    return Image.fromarray(pixel_array)


def process_gif(gif_path: Path) -> None:
    source_image = Image.open(gif_path)
    transparent_frames = []
    frame_durations = []

    for frame_index in range(source_image.n_frames):
        source_image.seek(frame_index)
        transparent_frames.append(make_frame_transparent(source_image))
        frame_durations.append(source_image.info.get("duration", 100))

    palette_frames = [frame_to_transparent_palette(frame) for frame in transparent_frames]

    palette_frames[0].save(
        gif_path,
        save_all=True,
        append_images=palette_frames[1:],
        duration=frame_durations,
        loop=source_image.info.get("loop", 0),
        disposal=2,
        transparency=TRANSPARENT_INDEX,
        optimize=False,
    )
    print(f"Processed {gif_path.name} ({len(palette_frames)} frames)")


def main() -> None:
    for gif_file in sorted(ICONS_DIR.glob("*.gif")):
        process_gif(gif_file)


if __name__ == "__main__":
    main()
