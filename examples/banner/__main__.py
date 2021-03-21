import os

from PIL import Image
from cairosvg import svg2png

import python_avataaars as pa

# The script used to generate the social preview image for this repository

image = Image.new('RGBA', (1280, 640), (255, 255, 255, 255))

fns = []
x = -100
y = -100
row = 0
for i in range(40):
    # Store filename
    fn = "avatar_{}.png".format(i)
    fns.append(fn)

    # Convert and save png
    svg = pa.Avatar.random(
        style=pa.AvatarStyle.pick_random(
            favor=pa.AvatarStyle.TRANSPARENT)

    ).render()
    svg2png(svg, write_to=fn)

    # Load png
    avatar_img = Image.open(fn)

    # Create the point where the image will be pasted
    pt = (x, y)
    x += int(avatar_img.size[0] * 0.7)
    if x >= image.size[0]:
        if row % 2 == 0:
            x = 0
        else:
            x = -avatar_img.size[0] // 2
        y += int(avatar_img.size[1] * 0.6)
        row += 1

    # Paste the image
    image.paste(avatar_img, pt, mask=avatar_img)

image.save("banner.png", "PNG")

# Remove all the generated png files
for fn in fns:
    os.remove(fn)
