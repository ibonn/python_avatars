from python_avataaars import *

Avatar(
    style=AvatarStyle.CIRCLE,
    top=HairType.STRAIGHT_2,
    eyebrows=EyebrowType.DEFAULT_NATURAL,
    eyes=EyeType.DEFAULT,
    nose=NoseType.DEFAULT,
    mouth=MouthType.EATING,
    facial_hair=FacialHairType.NONE,
    # You can use hex colors on any color attribute...
    skin_color='#00FFFF',
    # Or you can use the colors provided by the library
    hair_color=HairColor.BLACK,
    accessory=AccessoryType.NONE,
    clothing=ClothingType.HOODIE,
    clothing_color=ClothingColor.HEATHER
).render("my_avatar.svg")
