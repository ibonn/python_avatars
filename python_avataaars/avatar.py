import enum

from .accessory_types import AccessoryType
from .avatar_styles import AvatarStyle
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
    '''
    The main avatar class
    '''

    def __init__(
        self,
        style=AvatarStyle.TRANSPARENT,
        top=HairType.SHORT_FLAT,
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
    ):
        self.style = style

        self.top = top
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

    @staticmethod
    def random(
        style=None,
        top=None,
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
    ):
        return Avatar(
            style=AvatarStyle.pick_random() if style is None else style,
            top=TopType.pick_random() if top is None else top,
            eyebrows=EyebrowType.pick_random() if eyebrows is None else eyebrows,
            eyes=EyeType.pick_random() if eyes is None else eyes,
            nose=NoseType.pick_random() if nose is None else nose,
            mouth=MouthType.pick_random() if mouth is None else mouth,
            facial_hair=FacialHairType.pick_random() if facial_hair is None else facial_hair,

            skin_color=SkinColor.pick_random() if skin_color is None else skin_color,
            hair_color=HairColor.pick_random() if hair_color is None else hair_color,
            facial_hair_color=HairColor.pick_random() if facial_hair_color is None else facial_hair_color,


            accessory=AccessoryType.pick_random() if accessory is None else accessory,
            clothing=ClothingType.pick_random() if clothing is None else clothing,
            clothing_color=ClothingColor.pick_random() if clothing_color is None else clothing_color,
            shirt_graphic=ClothingGraphic.pick_random() if shirt_graphic is None else shirt_graphic,
            shirt_text = shirt_text,
        )

    def render(self, path=None):

        # Load the base template based on the avatar style
        avatar = SVGParser(_get_path(AvatarStyle, self.style))

        # Set skin color
        avatar.get_element_by_id('Skin-Color').set_attr('fill', self.skin_color)

        # Set top
        if not self.__is_empty(self.top):
            
            if isinstance(self.top, HairType):
                top = SVGParser(_get_path(HairType, self.top))
                top.get_element_by_id('Hair-Color').set_attr('fill', self.hair_color)
            else:
                top = SVGParser(_get_path(HatType, self.top))
                # TODO change hat color

            # Set facial hair (top)
            if not self.__is_empty(self.facial_hair):
                top_facial_hair = top.get_element_by_id('Facial-Hair')
                if top_facial_hair:
                    facial_hair = SVGParser(_get_path(FacialHairType, self.facial_hair))
                    facial_hair.get_element_by_id('Facial-Hair-Color').set_attr('fill', self.facial_hair_color)
                    top_facial_hair.set_content(facial_hair.children())

            # Set accessories (top)
            if not self.__is_empty(self.accessory):
                accessories = SVGParser(_get_path(AccessoryType, self.accessory))
                top.get_element_by_id('Accessory').set_content(
                    accessories.children())

            avatar.get_element_by_id('Top').set_content(top.children())

        # Set eyebrows
        if not self.__is_empty(self.eyebrows):
            eyebrow = SVGParser(_get_path(EyebrowType, self.eyebrows))
            avatar.get_element_by_id('Eyebrow').set_content(eyebrow.children())

        # Set eyes
        if not self.__is_empty(self.eyes):
            eyes = SVGParser(_get_path(EyeType, self.eyes))
            avatar.get_element_by_id('Eyes').set_content(eyes.children())

        # Set nose
        if not self.__is_empty(self.nose):
            nose = SVGParser(_get_path(NoseType, self.nose))
            avatar.get_element_by_id('Nose').set_content(nose.children())

        # Set mouth
        if not self.__is_empty(self.mouth):
            mouth = SVGParser(_get_path(MouthType, self.mouth))
            avatar.get_element_by_id('Mouth').set_content(mouth.children())

        # Set clothes
        if not self.__is_empty(self.clothing):
            clothes = SVGParser(_get_path(ClothingType, self.clothing))
            fabric_color = clothes.get_element_by_id('Fabric-Color')
            if fabric_color:
                fabric_color.set_attr('fill', self.clothing_color)

            # TODO Set graphic to all clothes
            if self.clothing == ClothingType.GRAPHIC_SHIRT and not self.__is_empty(self.shirt_graphic):
                graphic = SVGParser(_get_path(ClothingGraphic, self.shirt_graphic))
                if self.shirt_graphic == ClothingGraphic.CUSTOM_TEXT:
                    graphic.get_element_by_id('Graphic-Text').children('tspan')[0].set_content(self.shirt_text)

                clothes.get_element_by_id('Graphic').set_content(graphic.children())

            avatar.get_element_by_id('Clothing').set_content(clothes.children())
        

        return avatar.render(path)

    @staticmethod
    def __is_empty(value):
        return value is None or value == '' or isinstance(value, enum.Enum) and value.value == ''

    def __str__(self):
        return str(self.__dict__)