from .base_enums import AvatarPart


class ClothingGraphic(AvatarPart):
    """Clothing graphics. The graphics printed on the clothing if the selected
clothing type is ClothingType.GRAPHIC_SHIRT"""

    __install__ = True
    __enum_path__ = 'clothing_graphics.py'
    __path__ = 'avatar_parts/clothes/graphic'

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
