from .base_enums import AvatarPart


class FacialHairType(AvatarPart):
    """Facial hair types"""

    __install__ = True
    __enum_path__ = 'facial_hair_types.py'
    __path__ = 'avatar_parts/facial_hair'

    NONE = ''
    BEARD_LIGHT = 'beard_light'
    BEARD_MAGESTIC = 'beard_magestic'
    BEARD_MEDIUM = 'beard_medium'
    MOUSTACHE_FANCY = 'moustache_fancy'
    MOUSTACHE_MAGNUM = 'moustache_magnum'
