from .base_enums import AvatarColor


class HairColor(AvatarColor):
    """Hair/facial hair colors. You can use any other color using its hex code"""

    __install__ = True
    __enum_path__ = 'hair_colors.py'

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
