from .base_enums import AvatarPart


class FacialHairType(AvatarPart):
    """Facial hair types"""

    __install__ = True
    __enum_path__ = 'facial_hair_types.py'
    __path__ = 'avatar_parts/facial_hair'

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
