import os

from PIL import Image
from cairosvg import svg2png
from python_avataaars import Avatar

# IMPORTANT: This example requires 'PIL (Pillow)' to work
#
#            >> pip install Pillow

# Generate 30 random avatars
imgs = []
fns = []
for i in range(30):

    fn = 'avatar_{}.gif'.format(i)

    avatar_svg = Avatar.random().render()
    svg2png(avatar_svg, write_to=fn)

    imgs.append(Image.open(fn).convert('PA'))
    fns.append(fn)

first = imgs[0]
others = imgs[1:]
first.save('avatars.gif', save_all=True, append_images=others, duration=500, disposal=2, loop=0, transparency=0)

for fn in fns:
    os.remove(fn)