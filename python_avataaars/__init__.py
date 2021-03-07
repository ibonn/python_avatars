import random
import enum

from . svg_parser import SVGParser


class AvatarEnum(enum.Enum):
    '''
    Base enum for the library. Allows picking random elements from the avatar
    '''
    @classmethod
    def get_all(cls):
        return list(cls)

    @classmethod
    def pick_random(cls):
        return random.choice(cls.get_all())


class AvatarPart(AvatarEnum):
    '''
    Base enum for avatar parts
    '''

    def __str__(self):
        return self.value


class AvatarColor(AvatarEnum):
    '''
    Base enum for avatar colors
    '''

    def __str__(self):
        return self.value


class SkinColor(AvatarColor):
    '''
    Skin colors available by the library. You can use any other color using its hex code
    '''
    TANNED = '#FD9841'
    YELLOW = '#F8D25C'
    PALE = '#FFDBB4'
    LIGHT = '#EDB98A'
    BROWN = '#D08B5B'
    DARK_BROWN = '#AE5D29'
    BLACK = '#614335'


class HairColor(AvatarColor):
    '''
    Hair/facial hair colors
    '''
    AUBURN = '#A55728'
    BLACK = '#2C1B18'
    BLONDE = '#B58143'
    BLONDE_GOLDEN = '#D6B370'
    BROWN = '#724133'
    BROWN_DARK = '#4A312C'
    PASTEL_PINK = '#F59797'
    PLATINUM = '#ECDCBF'
    RED = '#C93305'
    SILVER_GRAY = '#E8E1E1'


class ClothingColor(AvatarColor):
    '''
    Clothing colors
    '''
    BLACK = '#262E33'
    BLUE_01 = '#65C9FF'
    BLUE_02 = '#5199E4'
    BLUE_03 = '#25557C'
    GRAY_01 = '#E6E6E6'
    GRAY_02 = '#929598'
    HEATHER = '#3C4F5C'
    PASTEL_BLUE = '#B1E2FF'
    PASTEL_GREEN = '#A7FFC4'
    PASTEL_ORANGE = '#FFDEB5'
    PASTEL_YELLOW = '#FFAFB9'
    PINK = '#FF488E'
    RED = '#FF5C5C'
    WHITE = '#FFFFFF'


class AvatarStyle(AvatarPart):
    '''
    Avatar styles
    '''
    TRANSPARENT = 'transparent'
    CIRCLE = 'circle'


class ClothesGraphic(AvatarPart):
    NONE = ''
    BAT = 'bat'
    BEAR = 'bear'
    CUMBIA = 'cumbia'
    CUSTOM_TEXT = 'custom_text'
    DEER = 'deer'
    DIAMOND = 'diamond'
    HOLA = 'hola'
    PIZZA = 'pizza'
    RESIST = 'resist'
    SELENA = 'selena'
    SKULL_OUTLINE = 'skull_outline'
    SKULL = 'skull'


class Clothing(AvatarPart):
    '''
    Clothing types
    '''
    NONE = ''
    BLAZER_SHIRT = 'blazer_shirt'
    BLAZER_SWEATER = 'blazer_sweater'
    COLLAR_SWEATER = 'collar_sweater'
    GRAPHIC_SHIRT = 'graphic_shirt'
    HOODIE = 'hoodie'
    OVERALL = 'overall'
    SHIRT_CREW_NECK = 'shirt_crew_neck'
    SHIRT_SCOOP_NECK = 'shirt_scoop_neck'
    SHIRT_V_NECK = 'shirt_v_neck'


class Eyebrows(AvatarPart):
    '''
    Eyebrow types
    '''
    NONE = ''
    ANGRY_NATURAL = 'angry_natural'
    ANGRY = 'angry'
    DEFAULT_NATURAL = 'default_natural'
    DEFAULT = 'default'
    FLAT_NATURAL = 'flat_natural'
    FROWN_NATURAL = 'frown_natural'
    RAISED_EXCITED_NATURAL = 'raised_excited_natural'
    RAISED_EXCITED = 'raised_excited'
    SAD_CONCERNED_NATURAL = 'sad_concerned_natural'
    SAD_CONCERNED = 'sad_concerned'
    UNIBROW_NATURAL = 'unibrow_natural'
    UP_DOWN_NATURAL = 'up_down_natural'
    UP_DOWN = 'up_down'


class Eyes(AvatarPart):
    '''
    Eye types
    '''
    CLOSED = 'closed'
    CRY = 'cry'
    DEFAULT = 'default'
    EYE_ROLL = 'eye_roll'
    HAPPY = 'happy'
    HEART = 'heart'
    SIDE = 'side'
    SQUINT = 'squint'
    SURPRISED = 'surprised'
    WINK_WACKY = 'wink_wacky'
    WINK = 'wink'
    X_DIZZY = 'x_dizzy'


class FacialHair(AvatarPart):
    '''
    Facial hair types
    '''
    NONE = ''
    BEARD_LIGHT = 'beard_light'
    BEARD_MAGESTIC = 'beard_magestic'
    BEARD_MEDIUM = 'beard_medium'
    MOUSTACHE_FANCY = 'moustache_fancy'
    MOUSTACHE_MAGNUM = 'moustache_magnum'

    # To avoid facial hair appearing on most avatars, use a different pick_random
    @classmethod
    def pick_random(cls):
        r = random.uniform(0, 1)
        if r > 0.5:
            return random.choice(list(cls))
        return FacialHair.NONE


class Mouth(AvatarPart):
    '''
    Mouth types
    '''
    CONCERNED = 'concerned'
    DEFAULT = 'default'
    DISBELIEF = 'disbelief'
    EATING = 'eating'
    GRIMACE = 'grimace'
    SAD = 'sad'
    SCREAM_OPEN = 'scream_open'
    SERIOUS = 'serious'
    SMILE = 'smile'
    TONGUE = 'tongue'
    TWINKLE = 'twinkle'
    VOMIT = 'vomit'


class Nose(AvatarPart):
    '''
    Nose types
    '''
    DEFAULT = 'default'


class Top(AvatarPart):
    '''
    Hair/top of head types
    '''
    @staticmethod
    def get_all():
        return list(Hair) + list(Hat)


class Hair(AvatarPart):
    NONE = 'no_hair'
    BIG_HAIR = 'big_hair'
    BOB = 'bob'
    BUN = 'bun'
    CAESAR_SIDE_PART = 'caesar_side_part'
    CAESAR = 'caesar'
    CURLY = 'curly'
    CURVY = 'curvy'
    DREADS = 'dreads'
    FRIDA = 'frida'
    FRIZZLE = 'frizzle'
    FRO_BAND = 'fro_band'
    FRO = 'fro'
    LONG_NOT_TOO_LONG = 'long_not_too_long'
    MIA_WALLACE = 'mia_wallace'
    SHAGGY_MULLET = 'shaggy_mullet'
    SHAGGY = 'shaggy'
    # SHAVED_SIDES = 'shaved_sides' # FIXME no tiene color y da error al intentar asignarselo
    SHORT_CURLY = 'short_curly'
    SHORT_DREADS_1 = 'short_dreads_1'
    SHORT_DREADS_2 = 'short_dreads_2'
    SHORT_FLAT = 'short_flat'
    SHORT_ROUND = 'short_round'
    SHORT_WAVED = 'short_waved'
    SIDES = 'sides'
    STRAIGHT_1 = 'straight_1'
    STRAIGHT_2 = 'straight_2'
    STRAIGHT_STRAND = 'straight_strand'


class Hat(AvatarPart):
    HAT = 'hat'
    HIJAB = 'hijab'
    TURBAN = 'turban'
    WINTER_HAT_1 = 'winter_hat_1'
    WINTER_HAT_2 = 'winter_hat_2'
    WINTER_HAT_3 = 'winter_hat_3'
    WINTER_HAT_4 = 'winter_hat_4'


class Accessory(AvatarPart):
    '''
    Accessories (Glasses)
    '''
    NONE = ''
    EYEPATCH = 'eyepatch'
    KURT = 'kurt'
    PRESCRIPTION_1 = 'prescription_01'
    PRESCRIPTION_2 = 'prescription_02'
    ROUND = 'round'
    SUNGLASSES = 'sunglasses'
    WAYFARERS = 'wayfarers'


class Avatar:
    '''
    The main avatar class
    '''

    def __init__(
        self,
        style=AvatarStyle.TRANSPARENT,
        top=Hair.SHORT_FLAT,
        eyebrows=Eyebrows.DEFAULT,
        eyes=Eyes.DEFAULT,
        nose=Nose.DEFAULT,
        mouth=Mouth.DEFAULT,
        facial_hair=FacialHair.NONE,
        skin_color=SkinColor.LIGHT,
        hair_color=HairColor.BROWN,
        facial_hair_color=HairColor.BROWN,
        accessory=Accessory.NONE,
        clothing=Clothing.pick_random(),
        clothing_color=ClothingColor.HEATHER,
        shirt_graphic=ClothesGraphic.SKULL,
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
            top=Top.pick_random() if top is None else top,
            eyebrows=Eyebrows.pick_random() if eyebrows is None else eyebrows,
            eyes=Eyes.pick_random() if eyes is None else eyes,
            nose=Nose.pick_random() if nose is None else nose,
            mouth=Mouth.pick_random() if mouth is None else mouth,
            facial_hair=FacialHair.pick_random() if facial_hair is None else facial_hair,

            skin_color=SkinColor.pick_random() if skin_color is None else skin_color,
            hair_color=HairColor.pick_random() if hair_color is None else hair_color,
            facial_hair_color=HairColor.pick_random() if facial_hair_color is None else facial_hair_color,


            accessory=Accessory.pick_random() if accessory is None else accessory,
            clothing=Clothing.pick_random() if clothing is None else clothing,
            clothing_color=ClothingColor.pick_random() if clothing_color is None else clothing_color,
            shirt_graphic=ClothesGraphic.pick_random() if shirt_graphic is None else shirt_graphic,
            shirt_text = shirt_text,
        )

    def render(self, path=None):

        # Load the base template based on the avatar style
        avatar = SVGParser('avatar_parts/styles/avataaar_{}.svg'.format(self.style))

        # Set skin color
        avatar.get_element_by_id('Skin-Color').set_attr('fill', self.skin_color)

        # Set top
        if self.top is not None and self.top.value != '':
            top = SVGParser('avatar_parts/top/{}.svg'.format(self.top))
            if isinstance(self.top, Hair):
                top.get_element_by_id('Hair-Color').set_attr('fill', self.hair_color)
            else:
                pass  # TODO change hat color

            # Set facial hair (top)
            if self.facial_hair is not None and self.facial_hair.value != '':
                top_facial_hair = top.get_element_by_id('Facial-Hair')
                if top_facial_hair:
                    facial_hair = SVGParser('avatar_parts/facial_hair/{}.svg'.format(self.facial_hair))
                    facial_hair.get_element_by_id('Facial-Hair-Color').set_attr('fill', self.facial_hair_color)
                    top_facial_hair.set_content(facial_hair.children())

            # Set accessories (top)
            if self.accessory is not None and self.accessory.value != '':
                accessories = SVGParser(
                    'avatar_parts/accessories/{}.svg'.format(self.accessory))
                top.get_element_by_id('Accessory').set_content(
                    accessories.children())

            avatar.get_element_by_id('Top').set_content(top.children())

        # Set eyebrows
        if self.eyebrows is not None and self.eyebrows.value != '':
            eyebrow = SVGParser(
                'avatar_parts/eyebrows/{}.svg'.format(self.eyebrows))
            avatar.get_element_by_id('Eyebrow').set_content(eyebrow.children())

        # Set eyes
        if self.eyes is not None and self.eyes.value != '':
            eyes = SVGParser('avatar_parts/eyes/{}.svg'.format(self.eyes))
            avatar.get_element_by_id('Eyes').set_content(eyes.children())

        # Set nose
        if self.nose is not None and self.nose.value != '':
            nose = SVGParser('avatar_parts/nose/{}.svg'.format(self.nose))
            avatar.get_element_by_id('Nose').set_content(nose.children())

        # Set mouth
        if self.mouth is not None and self.mouth.value != '':
            mouth = SVGParser('avatar_parts/mouth/{}.svg'.format(self.mouth))
            avatar.get_element_by_id('Mouth').set_content(mouth.children())

        # Set clothes
        if self.clothing is not None and self.clothing.value != '':
            clothes = SVGParser('avatar_parts/clothes/{}.svg'.format(self.clothing))
            clothes.get_element_by_id('Fabric-Color').set_attr('fill', self.clothing_color)

            # TODO Set graphic to all clothes
            if self.clothing == Clothing.GRAPHIC_SHIRT and self.shirt_graphic is not None and self.shirt_graphic != ClothesGraphic.NONE and self.shirt_graphic != '':
                graphic = SVGParser('avatar_parts/clothes/graphic/{}.svg'.format(self.shirt_graphic))
                if self.shirt_graphic == ClothesGraphic.CUSTOM_TEXT:
                    graphic.get_element_by_id('Graphic-Text').children('tspan')[0].set_content(self.shirt_text)

                clothes.get_element_by_id('Graphic').set_content(graphic.children())

            avatar.get_element_by_id('Clothing').set_content(clothes.children())
        

        return avatar.render(path)

    def __str__(self):
        return str(self.__dict__)