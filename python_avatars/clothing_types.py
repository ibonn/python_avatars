from .base_enums import AvatarPart


class ClothingType(AvatarPart):
    """Clothing types"""

    __install__ = True
    __enum_path__ = 'clothing_types.py'
    __path__ = 'avatar_parts/clothes'

    NONE = ''
    BLAZER_SHIRT = 'blazer_shirt'
    BLAZER_SWEATER = 'blazer_sweater'
    COLLAR_SWEATER = 'collar_sweater'
    GRAPHIC_SHIRT = 'graphic_shirt'
    HOODIE = 'hoodie'
    OVERALL = 'overall'
    SHIRT_CREW_NECK = 'shirt_crew_neck'
    SHIRT_SCOOP_NECK = 'shirt_scoop_neck'
    SHIRT_V_NECK = 'shirt_v_neck'
    ASTRONAUT_SUIT = 'astronaut_suit'
    BOND_SUIT = 'bond_suit'
    CHEF = 'chef'
    GLADIATOR = 'gladiator'
    JEDI_ROBE = 'jedi_robe'
    SHIRT_WICK = 'shirt_wick'
