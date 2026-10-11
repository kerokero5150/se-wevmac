# Draw the app icon: a compact Mac showing the Kero's Mac Mods logo, on a red rounded tile.
# Run:  python3 art/make_icon.py && npx tauri icon art/icon.png
from PIL import Image, ImageDraw

S = 1024
RED = (196, 30, 36, 255)
im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(im)

# Tile, inset the way macOS icons are
d.rounded_rectangle((100, 100, 924, 924), radius=185, fill=RED)

# Mac body and foot
d.rounded_rectangle((290, 190, 734, 760), radius=40, fill=(207, 203, 189, 255), outline=(143, 139, 126, 255), width=10)
d.rounded_rectangle((318, 750, 706, 820), radius=18, fill=(184, 180, 166, 255), outline=(143, 139, 126, 255), width=10)

# Screen showing the Kero's Mac Mods logo
sx0, sy0, sx1, sy1 = 346, 250, 678, 520
d.rounded_rectangle((sx0 - 14, sy0 - 14, sx1 + 14, sy1 + 14), radius=22, fill=(21, 23, 26, 255))
d.rectangle((sx0, sy0, sx1 - 1, sy1 - 1), fill=(244, 245, 241, 255))
logo = Image.open("web/logo.png")
h = sy1 - sy0 - 28
logo = logo.resize((round(logo.width * h / logo.height), h), Image.LANCZOS)
im.alpha_composite(logo, ((sx0 + sx1 - logo.width) // 2, sy0 + 14))

# Floppy slot and the badge spot
d.rounded_rectangle((520, 610, 690, 628), radius=6, fill=(60, 58, 52, 255))
d.rectangle((336, 606, 372, 642), fill=RED)

im.save("art/icon.png")
