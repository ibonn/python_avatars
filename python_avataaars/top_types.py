from .base_enums import AvatarPart
from .hair_types import HairType
from .hat_types import HatType


class TopType(AvatarPart):
    """
    Hair/top of head types
    """
    __install__ = False
    __enum_path__ = 'top_types.py'
    __path__ = 'avatar_parts/top'

    @staticmethod
    def get_all():
        return list(HairType) + list(HatType)
