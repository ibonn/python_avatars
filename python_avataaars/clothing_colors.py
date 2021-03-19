from .base_enums import AvatarColor


class ClothingColor(AvatarColor):
    """Clothing colors. You can use any other color using its hex code"""

    __install__ = True
    __enum_path__ = 'clothing_colors.py'

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
    PASTEL_YELLOW = '#FFFFB1'
    PINK = '#FF488E'
    RED = '#FF5C5C'
    WHITE = '#FFFFFF'
