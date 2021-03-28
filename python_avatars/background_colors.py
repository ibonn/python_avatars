from .base_enums import AvatarColor


class BackgroundColor(AvatarColor):
    """Background colors. You can use any other color using its hex code"""

    __install__ = True
    __enum_path__ = 'background_colors.py'

    DEFAULT = '#65C9FF'
    BLACK = '#262E33'
    WHITE = '#FFFFFF'
