# python_avatars

[![Build Status](https://travis-ci.org/ibonn/python_avatars.svg?branch=main)](https://travis-ci.org/ibonn/python_avatars) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/0f0ba4f148724111a40681296d0dc740)](https://www.codacy.com/gh/ibonn/python_avatars/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ibonn/python_avatars&amp;utm_campaign=Badge_Grade) ![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/ibonn/python_avatars) [![PyPi version](https://img.shields.io/pypi/v/python_avatars)](https://img.shields.io/pypi/v/python_avatars) ![PyPI - Downloads](https://img.shields.io/pypi/dm/python_avatars) ![GitHub top language](https://img.shields.io/github/languages/top/ibonn/python_avatars) 

[![Randomly generated avatars. (View at: https://github.com/ibonn/python_avatars/blob/main/examples/random_gif_apng/avatars.png)](https://raw.githubusercontent.com/ibonn/python_avatars/main/examples/random_gif_apng/avatars.png)](https://github.com/ibonn/python_avatars/blob/main/examples/random_gif_apng/avatars.png)

> Avatar library in Python

## Table of contents
1. [Features](#features)
2. [Install](#install)
3. [Usage](#usage)
    * [Create your own avatar](#create-your-own-avatar)
    * [Create a random avatar](#create-a-random-avatar)
    * [Custom shirt text](#custom-shirt-text)
    * [Expand the library](#expand-the-library)
4. [License](#license)
5. [Acknowledgments](#acknowledgments)

## Features
* Highly customizable. Design your own clothes, hair styles, eyes... and add them to the library copying the svg files into a directory
* Vanilla Python. No external libraries needed
* The library contains some colors for clothes, hair and skin and supports user defined colors using hex encoding
* Pure SVG
* Random avatar generation


## Install
Using pip, from PyPi (latest stable release):

    pip install python-avatars

Using pip, from this repository (May not be stable!):

    git clone https://github.com/ibonn/python_avatars.git python_avatars
    cd python_avatars
    pip install -e .

## Usage
### Create your own avatar
```python
import python_avatars as pa

my_avatar = pa.Avatar(
    style=pa.AvatarStyle.CIRCLE,
    background_color=pa.BackgroundColor.BLACK,
    top=pa.HairType.STRAIGHT_2,
    eyebrows=pa.EyebrowType.DEFAULT_NATURAL,
    eyes=pa.EyeType.DEFAULT,
    nose=pa.NoseType.DEFAULT,
    mouth=pa.MouthType.EATING,
    facial_hair=pa.FacialHairType.NONE,
    # You can use hex colors on any color attribute...
    skin_color="#00FFFF",
    # Or you can use the colors provided by the library
    hair_color=pa.HairColor.BLACK,
    accessory=pa.AccessoryType.NONE,
    clothing=pa.ClothingType.HOODIE,
    clothing_color=pa.ClothingColor.HEATHER
)

# Save to a file
my_avatar.render("my_avatar.svg")
```
### Create a random avatar
```python
import python_avatars as pa

# Completely random avatar
random_avatar_1 = pa.Avatar.random()

# Completely random avatar except for the hat
random_avatar_2 = pa.Avatar.random(top=pa.HatType.HAT)  # More attributes can stay fixed

# Fixed avatar but random clothes
random_avatar_3 = pa.Avatar(
    style=pa.AvatarStyle.CIRCLE,
    hair_color=pa.HairColor.BLACK,
    accessory=pa.AccessoryType.NONE,
    clothing=pa.ClothingType.pick_random(), # The clothes are chosen randomly
)
```

### Custom shirt text
When using the graphic shirt, - _ClothingType.GRAPHIC_ - you can set a custom text if you want to.

```python
import python_avatars as pa

pa.Avatar(
    style=pa.AvatarStyle.CIRCLE,
    background_color='#FF00FF',
    # Choose graphic shirt
    clothing=pa.ClothingType.GRAPHIC_SHIRT,
    clothing_color=pa.ClothingColor.GRAY_02,
    # Important to choose this as shirt_graphic, otherwise shirt_text will be ignored
    shirt_graphic=pa.ClothingGraphic.CUSTOM_TEXT,
    shirt_text='Chess'
).render("avatar_text.svg")
```
will output the file _avatar\_text.svg_:

[![Avatar wearing shirt with custom text. (View at: https://github.com/ibonn/python_avatars/blob/main/examples/shirt_text/avatar_text.svg)](https://raw.githubusercontent.com/ibonn/python_avatars/main/examples/shirt_text/avatar_text.svg)](https://github.com/ibonn/python_avatars/blob/main/examples/shirt_text/avatar_text.svg)

### Expand the library
Suppose you have a file called _suit.svg_
that looks like this

[![Suit ready to be used by the avatar. (View at: https://github.com/ibonn/python_avatars/blob/main/examples/install/suit.svg)](https://raw.githubusercontent.com/ibonn/python_avatars/main/examples/install/suit.svg)](https://github.com/ibonn/python_avatars/blob/main/examples/install/suit.svg)

You can add it to the library just by running
```python
from python_avatars import install_part

# Install the new part
install_part("suit.svg", pa.ClothingType)
```
And then use it
```python
suit_avatar = pa.Avatar.random(
    clothing=pa.ClothingType.SUIT
)

suit_avatar.render("suit_avatar.svg")
```
Which outputs the file _suit\_avatar.svg_ that looks like this

[![Randomly generated avatar wearing the installed suit. (View at: https://github.com/ibonn/python_avatars/blob/main/examples/install/avatar_suit.svg)](https://raw.githubusercontent.com/ibonn/python_avatars/main/examples/install/avatar_suit.svg)](https://github.com/ibonn/python_avatars/blob/main/examples/install/avatar_suit.svg)

The name of the newly added value will be exactly the name of the svg file converted to uppercase replacing all non alphanumeric chars with underscores and removing all leading digits.

Uninstalling the installed part is as easy as installing it
```python
from python_avatars import uninstall_part, ClothingType

uninstall_part(ClothingType.SUIT, confirm=False)    # confirm=False will not prompt for confirmation
```

## License
This project is licensed under the MIT License - see the [LICENSE file](LICENSE) for details

## Acknowledgments
* Avatars designed by [Pablo Stanley](https://twitter.com/pablostanley) ([https://avataaars.com/](https://avataaars.com/))
* Additional avatar parts from blush.design, designed by [Pablo Stanley](https://twitter.com/pablostanley) ([https://blush.design/](https://blush.design/collections/rChdrB8vX8xQJunpDPp8/avatars/avataaar-default))