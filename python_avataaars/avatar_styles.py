from .base_enums import AvatarPart


class AvatarStyle(AvatarPart):
    """Avatar styles"""

    __install__ = True
    __enum_path__ = 'avatar_styles.py'
    __path__ = 'avatar_parts/styles'

    TRANSPARENT = 'transparent'
    CIRCLE = 'circle'
