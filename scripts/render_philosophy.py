from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parents[1]
FONT_PATH = REPO_ROOT / "assets" / "fonts" / "FenwickWoodtype.ttf"
OUTPUT_PATH = REPO_ROOT / "assets" / "philosophy.png"

TEXT_COLOR = (212, 197, 169, 255)
BORDER_COLOR = (139, 105, 20, 255)
BACKGROUND_COLOR = (0, 0, 0, 0)

FONT_SIZE = 34
LINE_SPACING = 14
PARAGRAPH_SPACING = 24
MAX_TEXT_WIDTH = 920
HORIZONTAL_PADDING = 28
VERTICAL_PADDING = 16
BORDER_WIDTH = 5
BORDER_GAP = 16


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current_line = ""

    for word in words:
        candidate = word if not current_line else f"{current_line} {word}"
        line_width = draw.textbbox((0, 0), candidate, font=font)[2]

        if line_width <= max_width:
            current_line = candidate
            continue

        if current_line:
            lines.append(current_line)
        current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def measure_wrapped_text(
    draw: ImageDraw.ImageDraw,
    paragraphs: list[str],
    font: ImageFont.FreeTypeFont,
    max_width: int,
) -> tuple[list[list[str]], int, int]:
    wrapped_paragraphs: list[list[str]] = []
    total_height = 0
    max_line_width = 0

    for paragraph_index, paragraph in enumerate(paragraphs):
        lines = wrap_text(draw, paragraph, font, max_width)
        wrapped_paragraphs.append(lines)

        for line in lines:
            line_bbox = draw.textbbox((0, 0), line, font=font)
            line_width = line_bbox[2] - line_bbox[0]
            line_height = line_bbox[3] - line_bbox[1]
            max_line_width = max(max_line_width, line_width)
            total_height += line_height + LINE_SPACING

        if paragraph_index < len(paragraphs) - 1:
            total_height += PARAGRAPH_SPACING - LINE_SPACING

    if wrapped_paragraphs:
        total_height -= LINE_SPACING

    return wrapped_paragraphs, max_line_width, total_height


def render_philosophy_image() -> None:
    paragraphs = [
        "AI is not just a tool. It's a productivity multiplier, a creativity amplifier, "
        "and a new layer of abstraction for building software.",
        "My mission is to empower every team to work like they have 10x more time and 10x more ability.",
    ]

    font = ImageFont.truetype(str(FONT_PATH), FONT_SIZE)
    probe_image = Image.new("RGBA", (MAX_TEXT_WIDTH, 200), BACKGROUND_COLOR)
    probe_draw = ImageDraw.Draw(probe_image)
    wrapped_paragraphs, text_width, text_height = measure_wrapped_text(
        probe_draw,
        paragraphs,
        font,
        MAX_TEXT_WIDTH,
    )

    image_width = BORDER_WIDTH + BORDER_GAP + text_width + HORIZONTAL_PADDING * 2
    image_height = text_height + VERTICAL_PADDING * 2

    image = Image.new("RGBA", (image_width, image_height), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)

    border_top = VERTICAL_PADDING - 4
    border_bottom = image_height - VERTICAL_PADDING + 4
    draw.rectangle(
        [(0, border_top), (BORDER_WIDTH, border_bottom)],
        fill=BORDER_COLOR,
    )

    text_x = BORDER_WIDTH + BORDER_GAP + HORIZONTAL_PADDING
    text_y = VERTICAL_PADDING

    for paragraph_index, lines in enumerate(wrapped_paragraphs):
        for line in lines:
            draw.text((text_x, text_y), line, font=font, fill=TEXT_COLOR)
            line_bbox = draw.textbbox((text_x, text_y), line, font=font)
            text_y += (line_bbox[3] - line_bbox[1]) + LINE_SPACING

        if paragraph_index < len(wrapped_paragraphs) - 1:
            text_y += PARAGRAPH_SPACING - LINE_SPACING

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT_PATH, "PNG")
    print(f"Saved {OUTPUT_PATH} ({image_width}x{image_height})")


if __name__ == "__main__":
    render_philosophy_image()
