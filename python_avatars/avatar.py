import enum

from .accessory_types import AccessoryType
from .avatar_styles import AvatarStyle
from .background_colors import BackgroundColor
from .clothing_colors import ClothingColor
from .clothing_graphics import ClothingGraphic
from .clothing_types import ClothingType
from .eye_types import EyeType
from .eyebrow_types import EyebrowType
from .facial_hair_types import FacialHairType
from .hair_colors import HairColor
from .hair_types import HairType
from .hat_types import HatType
from .mouth_types import MouthType
from .nose_types import NoseType
from .skin_colors import SkinColor
from .top_types import TopType

from . svg_parser import SVGParser
from . core import _get_path


class Avatar:
    """
    Avatar. Create a new avatar using this class.
    """

    def __init__(
        self,
        style=AvatarStyle.TRANSPARENT,
        background_color=BackgroundColor.DEFAULT,
        top=HairType.SHORT_FLAT,
        hat_color=ClothingColor.HEATHER,
        eyebrows=EyebrowType.DEFAULT,
        eyes=EyeType.DEFAULT,
        nose=NoseType.DEFAULT,
        mouth=MouthType.DEFAULT,
        facial_hair=FacialHairType.NONE,
        skin_color=SkinColor.LIGHT,
        hair_color=HairColor.BROWN,
        facial_hair_color=HairColor.BROWN,
        accessory=AccessoryType.NONE,
        clothing=ClothingType.pick_random(),
        clothing_color=ClothingColor.HEATHER,
        shirt_graphic=ClothingGraphic.SKULL,
        shirt_text='Hola!',
        title=None,
    ):
        self.style = style
        self.background_color = background_color

        self.top = top
        self.hat_color = hat_color
        self.eyebrows = eyebrows
        self.eyes = eyes
        self.nose = nose
        self.mouth = mouth
        self.facial_hair = facial_hair

        self.skin_color = skin_color
        self.hair_color = hair_color
        self.facial_hair_color = facial_hair_color

        self.accessory = accessory
        self.clothing = clothing
        self.clothing_color = clothing_color
        self.shirt_graphic = shirt_graphic
        self.shirt_text = shirt_text

        self.title = title

    @staticmethod
    def random(
        style=None,
        background_color=None,
        top=None,
        hat_color=None,
        eyebrows=None,
        eyes=None,
        nose=None,
        mouth=None,
        facial_hair=None,
        skin_color=None,
        hair_color=None,
        facial_hair_color=None,
        accessory=None,
        clothing=None,
        clothing_color=None,
        shirt_graphic=None,
        shirt_text=None,
        title=None,
    ):
        """
        Generates a random avatar. The parameters for this method are exactly the same
        as for the constructor. If none of them are specified, the values are chosen
        randomly. The values for the specified parameters will stay fixed
        """
        return Avatar(
            style=AvatarStyle.pick_random() if style is None else style,
            background_color=BackgroundColor.pick_random(
            ) if background_color is None else background_color,
            top=TopType.pick_random() if top is None else top,
            hat_color=ClothingColor.pick_random() if hat_color is None else hat_color,
            eyebrows=EyebrowType.pick_random() if eyebrows is None else eyebrows,
            eyes=EyeType.pick_random() if eyes is None else eyes,
            nose=NoseType.pick_random() if nose is None else nose,
            mouth=MouthType.pick_random() if mouth is None else mouth,
            facial_hair=FacialHairType.pick_random(
                favor=FacialHairType.NONE) if facial_hair is None else facial_hair,

            skin_color=SkinColor.pick_random() if skin_color is None else skin_color,
            hair_color=HairColor.pick_random() if hair_color is None else hair_color,
            facial_hair_color=HairColor.pick_random(
            ) if facial_hair_color is None else facial_hair_color,


            accessory=AccessoryType.pick_random(
                favor=AccessoryType.NONE) if accessory is None else accessory,
            clothing=ClothingType.pick_random() if clothing is None else clothing,
            clothing_color=ClothingColor.pick_random(
            ) if clothing_color is None else clothing_color,
            shirt_graphic=ClothingGraphic.pick_random(
            ) if shirt_graphic is None else shirt_graphic,
            shirt_text=shirt_text,

            title=title,
        )

    def render(self, path=None):
        """
        Render the avatar to svg. Always returns the resulting svg as a string

        :param path: The path where the svg file will be saved. If ``None``, no file is saved
        :type path: str
        :return: str
        """

        # Load the base template based on the avatar style
        avatar = SVGParser(_get_path(AvatarStyle, self.style))

        if self.title is not None:
            avatar.get_element_by_id("Title").set_content(self.title)

        # Set style params
        bg_color = avatar.get_element_by_id("Background-Color")
        if bg_color is not None:
            bg_color.set_attr("fill", self.background_color)

        # Set skin color
        avatar.get_element_by_id(
            'Skin-Color').set_attr('fill', self.skin_color)

        # Set top
        if not self.__is_empty(self.top):

            if isinstance(self.top, HairType):
                top = SVGParser(_get_path(HairType, self.top))

                hair_color = top.get_element_by_id(
                    'Hair-Color'
                )

                if hair_color is not None:
                    hair_color.set_attr('fill', self.hair_color)

            else:
                top = SVGParser(_get_path(HatType, self.top))
                hat_color = top.get_element_by_id("Fabric-Color")
                if hat_color is not None:
                    hat_color.set_attr('fill', self.hat_color)

            # Set facial hair (top)
            if not self.__is_empty(self.facial_hair):
                top_facial_hair = top.get_element_by_id('Facial-Hair')
                if top_facial_hair:
                    facial_hair = SVGParser(
                        _get_path(FacialHairType, self.facial_hair)
                    )

                    facial_hair.get_element_by_id(
                        'Facial-Hair-Color'
                    ).set_attr('fill', self.facial_hair_color)

                    top_facial_hair.set_content(facial_hair.children())

            # Set accessories (top)
            self.__get_part(top, self.accessory, AccessoryType, 'Accessory')

            avatar.get_element_by_id('Top').set_content(top.children())

        # Set eyebrows
        self.__get_part(avatar, self.eyebrows, EyebrowType, 'Eyebrow')

        # Set eyes
        self.__get_part(avatar, self.eyes, EyeType, 'Eyes')

        # Set nose
        self.__get_part(avatar, self.nose, NoseType, 'Nose')

        # Set mouth
        self.__get_part(avatar, self.mouth, MouthType, 'Mouth')

        # Set clothes
        if not self.__is_empty(self.clothing):
            clothes = SVGParser(_get_path(ClothingType, self.clothing))
            fabric_color = clothes.get_element_by_id('Fabric-Color')
            if fabric_color:
                fabric_color.set_attr('fill', self.clothing_color)

            if self.clothing == ClothingType.GRAPHIC_SHIRT and not self.__is_empty(self.shirt_graphic):
                graphic = SVGParser(
                    _get_path(ClothingGraphic, self.shirt_graphic)
                )

                if self.shirt_graphic == ClothingGraphic.CUSTOM_TEXT:
                    graphic.get_element_by_id(
                        'Graphic-Text'
                    ).children('tspan')[0].set_content(self.shirt_text)

                clothes.get_element_by_id(
                    'Graphic'
                ).set_content(graphic.children())

            avatar.get_element_by_id(
                'Clothing'
            ).set_content(clothes.children())

        return avatar.render(path)

    def __get_part(self, avatar, part, part_enum, svg_id):
        if not self.__is_empty(part):
            part_svg = SVGParser(_get_path(part_enum, part))
            avatar.get_element_by_id(svg_id).set_content(part_svg.children())

    def happy(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.RAISED_EXCITED_NATURAL, EyebrowType.RAISED_EXCITED),
            eyes=EyeType.HAPPY,
            nose=self.nose,
            mouth=MouthType.SMILE,
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def sad(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.SAD_CONCERNED_NATURAL, EyebrowType.SAD_CONCERNED),
            eyes=EyeType.DEFAULT,
            nose=self.nose,
            mouth=MouthType.SAD,
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def frightened(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.RAISED_EXCITED_NATURAL, EyebrowType.RAISED_EXCITED),
            eyes=EyeType.SQUINT,
            nose=self.nose,
            mouth=MouthType.SCREAM_OPEN,
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def disgusted(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.SAD_CONCERNED_NATURAL, EyebrowType.SAD_CONCERNED),
            eyes=EyeType.HAPPY,
            nose=self.nose,
            mouth=MouthType.VOMIT,
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def angry(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.ANGRY_NATURAL, EyebrowType.ANGRY),
            eyes=self.eyes,
            nose=self.nose,
            mouth=MouthType.SAD,
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def surprised(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.RAISED_EXCITED_NATURAL, EyebrowType.RAISED_EXCITED),
            eyes=EyeType.SURPRISED,
            nose=self.nose,
            mouth=MouthType.DISBELIEF,
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def confused(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.UP_DOWN_NATURAL, EyebrowType.UP_DOWN),
            eyes=EyeType.SQUINT,
            nose=self.nose,
            mouth=MouthType.SERIOUS,    # TODO find adequate mouth type
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def worried(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.SAD_CONCERNED_NATURAL, EyebrowType.SAD_CONCERNED),
            eyes=EyeType.SQUINT,
            nose=self.nose,
            mouth=MouthType.CONCERNED,
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def neutral(self):
        return Avatar(
            style=self.style,
            background_color=self.background_color,
            top=self.top,
            hat_color=self.hat_color,
            eyebrows=self.__get_eyebrows(EyebrowType.DEFAULT_NATURAL, EyebrowType.DEFAULT),
            eyes=EyeType.DEFAULT,
            nose=self.nose,
            mouth=MouthType.SERIOUS,
            facial_hair=self.facial_hair,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            facial_hair_color=self.facial_hair_color,
            accessory=self.accessory,
            clothing=self.clothing,
            clothing_color=self.clothing_color,
            shirt_graphic=self.shirt_graphic,
            shirt_text=self.shirt_text,
        )

    def serious(self):
        return self.neutral()

    def scared(self):
        return self.frightened()

    def shocked(self):
        return self.surprised()

    def __get_eyebrows(self, natural, default):
        if 'natural' in self.eyebrows.name.lower():
            return natural
        else:
            return default

    @staticmethod
    def __is_empty(value):
        """
        Check wether a value is set or not for an attribute

        :param value: The value to test
        :type value: str or :class:`AvatarEnum`
        :return: bool
        """
        return value is None or value == '' or isinstance(value, enum.Enum) and value.value == ''

    def __hash__(self):
        return hash(
            (
                self.style,
                self.background_color,
                self.top,
                self.hat_color,
                self.eyebrows,
                self.eyes,
                self.nose,
                self.mouth,
                self.facial_hair,
                self.skin_color,
                self.hair_color,
                self.facial_hair_color,
                self.accessory,
                self.clothing,
                self.clothing_color,
                self.shirt_graphic,
                self.shirt_text,
                self.title,
            )
        )

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        """
        String representation for the avatar
        """
        return str(self.__dict__)
