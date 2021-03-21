import os
import re
import shutil
import json

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
from .base_enums import AvatarPart, AvatarColor

# Variables for internal usage. Paths to files/folders
_package_path = os.path.dirname(__file__)
_default_path = os.path.join(_package_path, 'default.json')
_installed_path = os.path.join(_package_path, 'installed.json')


def _check(condition, message, exception=RuntimeError):
    """
    Check wether a condition holds or not. If the condition is false, raises a RuntimeError with the provided message

    :param condition: The condition to test
    :param message: The message to show if the condition is false

    :type condition: bool
    :type message: str

    :raises RuntimeError: The error is raised if the condition in ``condition`` is false
    """
    if condition:
        raise exception(message)


def _install_enum(name, value, part_type, enum_type):
    """
    Adds a value to a enum. Returns True on success. In case if error, an exception is raised

    :param name: The name of the value to add
    :param value: The value to add
    :param part_type: The enum to extend
    :param enum_type: The type of the enum to extend

    :type name: str
    :type value: str
    :type part_type: :class:`AvatarEnum`
    :type enum_type: :class:`Avatarpart` or :class:`AvatarColor`

    :raises RuntimeError: The error is raised if the enum cannot be expanded
    :raises FileExistsError: Raised when the enum contains an item named ``name``

    :return: bool
    """
    _check(not part_type.__install__,
           "{} cannot be expanded".format(part_type.__name__))

    const_name = _sanitize(name).upper()

    # Load defaults
    with open(_default_path, 'r') as f:
        default_values = json.load(f)

    # Load installed
    if not os.path.isfile(_installed_path):
        with open(_installed_path, 'w') as f:
            json.dump({}, f)

    with open(_installed_path, 'r') as f:
        installed_values = json.load(f)

    # Combine installed with default
    if part_type.__name__ in installed_values:
        combined = {**default_values[part_type.__name__],
                    **installed_values[part_type.__name__]}
    else:
        combined = default_values[part_type.__name__]
        installed_values[part_type.__name__] = {}

    # Check wether the value exists or not
    _check(const_name in combined,
           "{}.{} already exists".format(part_type.__name__, const_name), FileExistsError)

    # Add to installed
    installed_values[part_type.__name__][const_name] = value

    # Save installed
    with open(_installed_path, 'w') as f:
        json.dump(installed_values, f, indent=4)

    # Overwrite the enum file
    combined = {**default_values[part_type.__name__],
                **installed_values[part_type.__name__]}
    _write_enum(part_type, combined, enum_type)

    return True


def _prompt_uninstall_confirmation(class_name, enum_name):
    """
    Prompt a deletion confirmation message. Returns ``True`` when the user accepted and ``False`` when declined

    :param class_name: The name of the enum from which the value will be deleted
    :param enum_name: The name of the value to delete

    :type class_name: str
    :type enum_name: str

    :return: bool
    """
    return _prompt_confirmation('Do you really want to uninstall {}.{}?'.format(class_name, enum_name))


def _prompt_confirmation(msg):
    """
    Prompt a confirmation message

    :param msg: The message to show
    :type msg: str

    :return: bool
    """
    confirm_resp = input('{} y/n: '.format(msg))
    return confirm_resp.lower().strip() == 'y'


def _uninstall_enum(part, enum_type):
    """
    Removes a value for a given enum. Returns ``True`` on success

    :param part: The name of the value to remove
    :param enum_type: The type of the enum from which the value will be removed

    :type part: :class:`AvatarEnum`
    :type enum_type: :class:`AvatarPart` or :class:`AvatarColor`

    :return: bool
    """
    if os.path.isfile(_installed_path):
        # Load installed
        with open(_installed_path, 'r') as f:
            installed_values = json.load(f)

        # Load default
        with open(_default_path, 'r') as f:
            default_values = json.load(f)

        # Delete from installed
        del installed_values[part.__class__.__name__][part.name]

        # Combine installed + default
        combined = {**default_values[part.__class__.__name__],
                    **installed_values[part.__class__.__name__]}

        # Update installed
        with open(_installed_path, 'w') as f:
            json.dump(installed_values, f)

        # Rewrite enum
        _write_enum(part.__class__, combined, enum_type)
        return True
    return False


def install_part(part_path, part_type):
    """
    Installs a part (clothing, hair type, eye type...)

    :param part_path: The path to the svg to install
    :param part_type: The enum where the new value will be installed

    :type part_path: str
    :type part_type: :class:`AvatarPart`

    :raise RuntimeError: Whenever the part_type does not have an installation path (in other words, when it is not an AvatarPart or when it is not installable)
    :raise FileNotFoundError: If the file at ``part_path`` does not exist

    :return: bool
    """
    _check(part_type.__path__ == '', "Installation path not found")
    _check(not os.path.isfile(part_path),
           "{} does not exist".format(part_path), FileNotFoundError)
    file_name = _sanitize(os.path.splitext(os.path.basename(part_path))[0])

    new_enum = _install_enum(file_name, file_name, part_type, AvatarPart)

    if new_enum:
        # Copy the file on success
        destination = _get_path(part_type, file_name)
        shutil.copy(part_path, destination)

    return True


def uninstall_part(part, confirm=True):
    """
    Removes an installed part. Returns ``True`` on success, ``False`` otherwise

    :param part: The part to uninstall
    :param confirm: Does this action require confirmation? If ``True``, the user will be asked to confirm the uninstall

    :type part: :class:`AvatarPart`
    :type confirm: bool

    :return: bool
    """
    if _prompt_uninstall_confirmation(part.__class__.__name__, part.name) and _uninstall_enum(part, AvatarPart):
        os.remove(_get_path(part.__class__, part.value))
        return True
    return False


def install_color(name, value, part_type):
    """
    Installs a color. Returns ``True`` on success

    :param name: The name of the color to install
    :param value: The value of the color, hex encoded (i.e. #AF541B)
    :param part_type: The enum where the color will be installed

    :type name: str
    :type value: str
    :type part_type: :class:`AvatarColor`

    :raises RuntimeError: If ``part_type`` is not an :class:`AvatarColor`

    :return: bool

    """
    _check(part_type.__path__ != '',
           "{} is not a color".format(part_type.__name__))

    _check(not re.match(r"^#(?:[a-f0-9]{6}|[a-f0-9]{3})$", value, re.MULTILINE | re.IGNORECASE),
           "{} is not a valid color".format(value))

    return _install_enum(name, value, part_type, AvatarColor)


def uninstall_color(color, confirm=True):
    """
    Unistalls a color. Returns ``True`` on success, ``False`` otherwise

    :param color: The color to remove
    :param confirm: Does this action require confirmation? If ``True``, the user will be asked to confirm the uninstall

    :type color: :class:`AvatarColor`
    :type confirm: bool

    :return: bool

    """
    if confirm:
        return _prompt_uninstall_confirmation(color.__class__.__name__, color.name) and _uninstall_enum(color, AvatarColor)
    return _uninstall_enum(color, AvatarColor)


def factory_reset(confirm=True):
    """
    Resets the package to its original state

    :param confirm: Does this action require confirmation? If ``True``, the user will be asked to confirm the reset
    :type confirm: bool
    """

    if confirm and _prompt_confirmation('Do you want to uninstall all the installed parts?'):
        # Load installed and remove svgs
        if os.path.isfile(_installed_path):
            with open(_installed_path, 'r') as f:
                installed_values = json.load(f)

            for enum_name, enum_values_dict in installed_values.items():
                enum = globals()[enum_name]
                for value in enum_values_dict.values():
                    svg_path = _get_path(enum, value)
                    os.remove(svg_path)

            os.remove(_installed_path)

        # Load defaults
        with open(_default_path, 'r') as f:
            default_values = json.load(f)

        for enum_name, enum_values_dict in default_values.items():
            enum_cls = type(enum_name, (object,), enum_values_dict)
            _write_enum(enum_cls, enum_values_dict,
                        AvatarPart if "__path__" in enum_values_dict else AvatarColor)


def _get_path(enum_cls, value):
    """
    Returns the path to the svg file for an AvatarPart given the enum and the name

    :param enum_cls: The enum
    :param value: The name

    :return: str
    """
    p = os.path.join(_package_path, enum_cls.__path__, '{}.svg'.format(value))
    return p


def _sanitize(value):
    """
    Prepares a string to be used as a Python identifier

    :param value: The string to convert to a valid Python identifier

    :type value: str

    :return: str
    """
    # Remove invalid Python identifier chars
    value = re.sub('[^A-Za-z0-9_]+', '_', value)

    # Remove digits from the beginning
    value = value.lstrip('0123456789')

    return value


def _write_enum(e, values_dict, t):
    """
    Writes an enum to an importable file

    :param e: The original enum to overwrite
    :param values_dict: Dictionary holding the values for the new enum
    :param t: Type of the enum

    :type e: :class:`AvatarEnum`
    :type values_dict: dict
    :type t: :class:`AvatarPart` or :class:`AvatarColor`
    """
    filename = e.__enum_path__
    name = e.__name__
    path = e.__path__ if hasattr(e, "__path__") else None
    install = e.__install__
    docstring = e.__doc__

    file_path = os.path.join(_package_path, filename)

    with open(file_path, 'w') as f:
        if t is AvatarColor:
            f.write('from .base_enums import AvatarColor\n\n\n')
            f.write('class {}(AvatarColor):\n'.format(name))
        elif t is AvatarPart:
            f.write('from .base_enums import AvatarPart\n\n\n')
            f.write('class {}(AvatarPart):\n'.format(name))
        else:
            raise RuntimeError()

        f.write('    """{}"""\n\n'.format(docstring))

        f.write("    __install__ = {}\n".format(install))
        f.write("    __enum_path__ = '{}'\n".format(filename))
        if path is not None:
            f.write("    __path__ = '{}'\n".format(path))
        f.write("\n")
        for name, value in values_dict.items():
            if name[:2] != '__':
                f.write("    {} = '{}'\n".format(name, value))
