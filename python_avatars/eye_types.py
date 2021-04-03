from .base_enums import AvatarPart


class EyeType(AvatarPart):
    """Eye types"""

    __install__ = True
    __enum_path__ = 'eye_types.py'
    __path__ = 'avatar_parts/eyes'

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
