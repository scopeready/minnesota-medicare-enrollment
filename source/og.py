"""Builds og-image.png (1200x630) — the social-share card — with Pillow.
Run from the repo root: python3 source/og.py"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1200, 630
LAKE, LAKE_DARK, GOLD, PAPER, SPRUCE = (29, 79, 110), (20, 58, 82), (231, 196, 134), (244, 242, 236), (31, 61, 51)

def font(size, bold=True):
    candidates = [
        "/mnt/skills/examples/canvas-design/canvas-fonts/IBMPlexSerif-Bold.ttf" if bold else "/mnt/skills/examples/canvas-design/canvas-fonts/IBMPlexSerif-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def sans(size):
    for c in ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
# sky gradient
for y in range(H):
    t = y / H
    c = tuple(int(PAPER[i] * (1 - t) + (219, 230, 238)[i] * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)
# sun
d.ellipse([940, 60, 1080, 200], fill=(231, 196, 134))
# far ridge, near ridge, pines, lake
d.polygon([(0, 430), (200, 400), (420, 420), (700, 392), (960, 416), (1200, 396), (1200, 630), (0, 630)], fill=(201, 214, 217))
d.polygon([(0, 470), (260, 440), (520, 474), (800, 452), (1040, 472), (1200, 456), (1200, 630), (0, 630)], fill=(111, 154, 138))
def pine(x, base, h, w, fill=SPRUCE):
    step = h / 4
    for i in range(3):
        top = base - h + i * step
        ww = w * (0.45 + 0.28 * i)
        d.polygon([(x, top), (x + ww, top + step * 1.35), (x - ww, top + step * 1.35)], fill=fill)
    d.rectangle([x - 3, base - 10, x + 3, base + 2], fill=(16, 37, 29))
for x, b, h, w in [(60, 480, 120, 34), (120, 486, 92, 26), (1120, 478, 126, 36), (1170, 484, 84, 24)]:
    pine(x, b, h, w)
d.polygon([(0, 500), (300, 492), (600, 506), (900, 496), (1200, 504), (1200, 630), (0, 630)], fill=LAKE)
# north star mark
cx, cy, r = 120, 120, 54
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=LAKE)
star = [(cx, cy - 34), (cx + 9, cy - 9), (cx + 34, cy), (cx + 9, cy + 9), (cx, cy + 34), (cx - 9, cy + 9), (cx - 34, cy), (cx - 9, cy - 9)]
d.polygon(star, fill=GOLD)
# text
d.text((200, 78), "ECOS Medicare Solutions", font=sans(30), fill=(70, 83, 94))
d.text((200, 118), "Medicare help in", font=font(74), fill=(28, 38, 48))
d.text((200, 200), "Minnesota", font=font(96), fill=LAKE)
d.text((200, 318), "Plain-English, no-cost guidance from a licensed independent agent,", font=sans(26), fill=(70, 83, 94))
d.text((200, 352), "gerontologist and Air Force veteran. Statewide, by phone or video.", font=sans(26), fill=(70, 83, 94))
d.rounded_rectangle([200, 536, 664, 592], radius=28, fill=LAKE_DARK)
d.text((226, 549), "minnesotamedicareenrollment.com", font=sans(24), fill=(255, 255, 255))
d.text((690, 552), "Darin Weidauer, MBA, RSSA · NPN 18580338", font=sans(20), fill=(244, 242, 236))
img.save(ROOT / "og-image.png", optimize=True)
print("wrote og-image.png", (ROOT / "og-image.png").stat().st_size, "bytes")
