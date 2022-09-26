import os

import python_avatars as pa
from cairosvg import svg2png
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# The script used to generate the social preview image for this repository
# NOTE By default it will generate the image without the text overlay. 
# If you wish to generate it with text, you will need to set the variable
# below to `True` and place the ttf files for Roboto in examples/banner/roboto/
add_text_overlay = False

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

# Add text overlay
if add_text_overlay:
    rect = (0, 0, 1280, 200)
    font_title = ImageFont.truetype('examples/banner/roboto/Roboto-Black.ttf', 65)
    font_main = ImageFont.truetype('examples/banner/roboto/Roboto-Regular.ttf', 40)
    font_small = ImageFont.truetype('examples/banner/roboto/Roboto-Thin.ttf', 30)

    overlay = Image.new('RGBA', (1280, 640), (0, 0, 0, 0))
    id = ImageDraw.Draw(overlay)

    # Blur rectangle
    crop_rect = image.crop(rect)
    crop_rect = crop_rect.filter(ImageFilter.BLUR)
    image.paste(crop_rect, rect)

    # Draw semi-transparent overlay over the blurred part
    id.rectangle(rect, fill=(255, 255, 255, 200))

    # Draw text
    start_y = 20
    texts = [
        ("python-avatars", font_title, (54, 69, 79)),
        ("SVG avatar package for Python", font_main, (79, 79, 79)),
        (f"Version {pa.__version__}", font_small, (0, 0, 0)),
    ]
    for text, font, color in texts:
        id.text((30, start_y), text, fill=color, font=font)
        width, height = font.getsize(text)
        start_y += height

    # Combine image and overlay
    image = Image.alpha_composite(image, overlay)

image.save("banner.png", "PNG")

# Remove all the generated png files
for fn in fns:
    os.remove(fn)
