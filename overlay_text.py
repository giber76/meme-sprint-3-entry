#!/usr/bin/env python3
"""Overlay classic meme caption text onto the generated illustration.

Top:    I TOLD MY AI AGENT / TO CUT COSTS
Bottom: IT FIRED ME.
White DejaVu Sans Bold with a thick black stroke, Impact-meme style.
Output: 1024x1024 PNG, under 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont

SRC = "/home/hatch/workspace/makefun/meme-sprint-3-work/media-generation-meme-sprint-3-base-0-fe108264-7ee8-4095-8ac2-aca977c5973e.png"
OUT = "/home/hatch/workspace/makefun/meme-sprint-3-work/entry.png"

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def draw_centered(draw, y, text, font, fill="white", stroke="black", stroke_w=6):
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_w)
    w = bbox[2] - bbox[0]
    x = (1024 - w) // 2 - bbox[0]
    draw.text((x, y), text, font=font, fill=fill, stroke_width=stroke_w,
              stroke_fill=stroke)


def main():
    img = Image.open(SRC).convert("RGB")
    if img.size != (1024, 1024):
        img = img.resize((1024, 1024), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    top_font = ImageFont.truetype(FONT, 72)
    draw_centered(draw, 18, "I TOLD MY AI AGENT", top_font, stroke_w=7)
    draw_centered(draw, 102, "TO CUT COSTS", top_font, stroke_w=7)

    bottom_font = ImageFont.truetype(FONT, 118)
    draw_centered(draw, 1024 - 150, "IT FIRED ME.", bottom_font, stroke_w=9)

    img.save(OUT, "PNG", optimize=True)
    print("saved", OUT)


if __name__ == "__main__":
    main()
