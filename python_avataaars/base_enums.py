import enum
import random


class AvatarEnum(enum.Enum):
    """
    Base enum for the library. Allows picking random elements from the avatar
    """
    __path__ = ''
    __install__ = False
    __enum_path__ = 'base_enums.py'

    @classmethod
    def get_all(cls):
        """
        Get a list containing all the values for this enum
        """
        return list(cls)

    @classmethod
    def pick_random(cls, favor=None):
        """
        Pich a random value from this enum. The value in ``favor`` has
        more chances of being chosen
        """
        if favor is None:
            return cls.__pick_random()
        else:
            r = random.uniform(0, 1)
            if r > 0.5:
                return cls.__pick_random()
            else:
                return favor

    @classmethod
    def __pick_random(cls):
        return random.choice(cls.get_all())

    def __str__(self):
        return self.value


class AvatarPart(AvatarEnum):
    """
    Base enum for avatar parts
    """
    pass


class AvatarColor(AvatarEnum):
    """
    Base enum for avatar colors
    """
    pass
