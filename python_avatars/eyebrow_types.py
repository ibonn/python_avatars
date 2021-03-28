from .base_enums import AvatarPart


class EyebrowType(AvatarPart):
    """Eyebrow types"""

    __install__ = True
    __enum_path__ = 'eyebrow_types.py'
    __path__ = 'avatar_parts/eyebrows'

    NONE = ''
    ANGRY_NATURAL = 'angry_natural'
    ANGRY = 'angry'
    DEFAULT_NATURAL = 'default_natural'
    DEFAULT = 'default'
    FLAT_NATURAL = 'flat_natural'
    FROWN_NATURAL = 'frown_natural'
    RAISED_EXCITED_NATURAL = 'raised_excited_natural'
    RAISED_EXCITED = 'raised_excited'
    SAD_CONCERNED_NATURAL = 'sad_concerned_natural'
    SAD_CONCERNED = 'sad_concerned'
    UNIBROW_NATURAL = 'unibrow_natural'
    UP_DOWN_NATURAL = 'up_down_natural'
    UP_DOWN = 'up_down'
