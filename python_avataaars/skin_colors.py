from .base_enums import AvatarColor


class SkinColor(AvatarColor):
    """Skin colors. You can use any other color using its hex code"""

    __install__ = True
    __enum_path__ = 'skin_colors.py'

    TANNED = '#FD9841'
    YELLOW = '#F8D25C'
    PALE = '#FFDBB4'
    LIGHT = '#EDB98A'
    BROWN = '#D08B5B'
    DARK_BROWN = '#AE5D29'
    BLACK = '#614335'
