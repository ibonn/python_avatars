from .base_enums import AvatarPart


class AccessoryType(AvatarPart):
    """Accessories (Glasses)"""

    __install__ = True
    __enum_path__ = 'accessory_types.py'
    __path__ = 'avatar_parts/accessories'

    NONE = ''
    EYEPATCH = 'eyepatch'
    KURT = 'kurt'
    PRESCRIPTION_1 = 'prescription_01'
    PRESCRIPTION_2 = 'prescription_02'
    ROUND = 'round'
    SUNGLASSES = 'sunglasses'
    WAYFARERS = 'wayfarers'
