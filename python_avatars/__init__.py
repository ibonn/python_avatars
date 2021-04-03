"""
SVG avatar generation library

More info @ https://github.com/ibonn/python_avatars
"""

__version__ = "1.3.0"

# Enums
from .accessory_types import AccessoryType
from .avatar_styles import AvatarStyle
from .background_colors import BackgroundColor
from .clothing_colors import ClothingColor
from .clothing_graphics import ClothingGraphic
from .clothing_types import ClothingType
from .eye_types import EyeType
from .eyebrow_types import EyebrowType
from .facial_hair_types import FacialHairType
from .hair_colors import HairColor
from .hair_types import HairType
from .hat_types import HatType
from .mouth_types import MouthType
from .nose_types import NoseType
from .skin_colors import SkinColor
from .top_types import TopType

# Classes
from .avatar import Avatar

# Core functions
from .core import install_part
from .core import install_color
from .core import uninstall_part
from .core import uninstall_color
from .core import factory_reset
