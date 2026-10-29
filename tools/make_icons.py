"""
Build the custom menu icons in apps/menu/pictures from the artwork in assets/custom.

Run from the repo root with Pillow installed:  python3 -I tools/make_icons.py

Item thumbnails are shrunk as they are. Rune artwork has a textured background, so the
glyph is pulled out (light or dark strokes, whichever is the minority) and saved as white
on transparent, the same way the menu's built-in icons are drawn.
"""

from PIL import Image, ImageChops, ImageDraw, ImageFilter

SOURCE = "assets/custom"
OUTPUT = "apps/menu/pictures"
SIZE = 56

THUMBNAILS = {
    "con_tools": "Caryll Runes.png",
    "games": "Gems.png",
    "graphics": "Attire.png",
}
RUNES = {
    "badge": "65. Hunter Oath.png",
    "contacts": "66. Corruption Oath.png",
}


def otsu(histogram):
    total = sum(histogram)
    everything = sum(level * count for level, count in enumerate(histogram))
    best, threshold, below, below_sum = 0, 128, 0, 0
    for level in range(256):
        below += histogram[level]
        if below == 0 or below == total:
            continue
        below_sum += level * histogram[level]
        spread = below * (total - below) * (below_sum / below - (everything - below_sum) / (total - below)) ** 2
        if spread > best:
            best, threshold = spread, level
    return threshold


def rune_glyph(path):
    picture = Image.open(path).convert("RGB")
    width, height = picture.size
    luma = picture.convert("L").filter(ImageFilter.GaussianBlur(1.2))
    background = luma.filter(ImageFilter.GaussianBlur(max(width, height) / 5))
    flat = ImageChops.subtract(luma, background, scale=1, offset=128)
    disc = Image.new("L", (width, height), 0)
    ImageDraw.Draw(disc).ellipse((width * 0.14, height * 0.14, width * 0.86, height * 0.86), fill=255)
    histogram = flat.histogram(disc)
    threshold = otsu(histogram)
    dark = sum(histogram[: threshold + 1]) < sum(histogram[threshold + 1 :])
    mask = flat.point(lambda value: 255 if (value <= threshold) == dark else 0)
    mask = ImageChops.multiply(mask, disc).filter(ImageFilter.MedianFilter(7))
    box = mask.getbbox()
    if box:
        mask = mask.crop(box)
    side = max(mask.size) + 6
    square = Image.new("L", (side, side), 0)
    square.paste(mask, ((side - mask.width) // 2, (side - mask.height) // 2))
    square = square.filter(ImageFilter.GaussianBlur(1.0)).point(lambda value: 255 if value > 110 else 0)
    alpha = square.resize((SIZE, SIZE), Image.LANCZOS)
    glyph = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 0))
    glyph.putalpha(alpha)
    return glyph


for name, source in THUMBNAILS.items():
    Image.open(f"{SOURCE}/{source}").convert("RGBA").resize((SIZE, SIZE), Image.LANCZOS).save(f"{OUTPUT}/{name}.png")
for name, source in RUNES.items():
    rune_glyph(f"{SOURCE}/{source}").save(f"{OUTPUT}/{name}.png")
print("wrote", sorted(list(THUMBNAILS) + list(RUNES)))
