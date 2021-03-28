from .base_enums import AvatarPart


class HatType(AvatarPart):
    """Hat types"""

    __install__ = True
    __enum_path__ = 'hat_types.py'
    __path__ = 'avatar_parts/top/hat'

    HAT = 'hat'
    HIJAB = 'hijab'
    TURBAN = 'turban'
    WINTER_HAT_1 = 'winter_hat_1'
    WINTER_HAT_2 = 'winter_hat_2'
    WINTER_HAT_3 = 'winter_hat_3'
    WINTER_HAT_4 = 'winter_hat_4'
