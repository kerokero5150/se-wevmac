# Draw the app icon: a compact Mac on a rounded tile, in the page's colors.
# Run:  python3 art/make_icon.py && npx tauri icon art/icon.png
from PIL import Image, ImageDraw

S = 1024
im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(im)

# Tile, inset the way macOS icons are
d.rounded_rectangle((100, 100, 924, 924), radius=185, fill=(31, 111, 92, 255))

# Mac body and foot
d.rounded_rectangle((290, 190, 734, 760), radius=40, fill=(207, 203, 189, 255), outline=(143, 139, 126, 255), width=10)
d.rounded_rectangle((318, 750, 706, 820), radius=18, fill=(184, 180, 166, 255), outline=(143, 139, 126, 255), width=10)

# Screen with the checkered desktop and a menu bar
sx0, sy0, sx1, sy1 = 346, 250, 678, 500
d.rounded_rectangle((sx0 - 14, sy0 - 14, sx1 + 14, sy1 + 14), radius=22, fill=(21, 23, 26, 255))
cell = 12
for y in range(sy0, sy1, cell):
    for x in range(sx0, sx1, cell):
        on = ((x - sx0) // cell + (y - sy0) // cell) % 2 == 0
        d.rectangle((x, y, min(x + cell, sx1) - 1, min(y + cell, sy1) - 1), fill=(244, 245, 241, 255) if on else (150, 153, 148, 255))
d.rectangle((sx0, sy0, sx1 - 1, sy0 + 34), fill=(244, 245, 241, 255))
d.rectangle((sx0, sy0 + 35, sx1 - 1, sy0 + 38), fill=(21, 23, 26, 255))

# A window on the desktop
d.rectangle((400, 330, 624, 460), fill=(244, 245, 241, 255), outline=(21, 23, 26, 255), width=5)
for y in range(340, 358, 6):
    d.rectangle((410, y, 614, y + 2), fill=(21, 23, 26, 255))
d.rectangle((400, 362, 624, 366), fill=(21, 23, 26, 255))

# Floppy slot and the badge spot
d.rounded_rectangle((520, 610, 690, 628), radius=6, fill=(60, 58, 52, 255))
d.rectangle((336, 606, 372, 642), fill=(31, 111, 92, 255))

im.save("art/icon.png")
