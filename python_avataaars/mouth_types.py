from .base_enums import AvatarPart


class MouthType(AvatarPart):
    """Mouth types"""

    __install__ = True
    __enum_path__ = 'mouth_types.py'
    __path__ = 'avatar_parts/mouth'

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
