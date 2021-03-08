import os
import re
import shutil
import json

from .base_enums import AvatarPart, AvatarColor

def install_part(part_path, part_type, print_messages=False):

    if not part_type.__install__:
        raise RuntimeError("The part type {} cannot be expanded".format(part_type.__name__))

    if part_type.__path__ == '':
        raise RuntimeError("Installation path not found")

    file_name = os.path.splitext(os.path.basename(part_path))[0]
    const_name = _sanitize(file_name)

    # Load defaults
    with open('default.json', 'r') as f:
        default_values = json.load(f)

    # Load installed
    if not os.path.isfile('installed.json'):
        with open('installed.json', 'w') as f:
            json.dump({}, f)

    with open('installed.json', 'r') as f:
        installed_values = json.load(f)

    # Combine installed with default
    if part_type.__name__ in installed_values:
        combined = {**default_values[part_type.__name__], **installed_values[part_type.__name__]}
    else:
        combined = default_values[part_type.__name__]
        installed_values[part_type.__name__] = {}

    # Check wether the value exists or not
    if const_name in combined:
        raise RuntimeError("The part {}.{} already exists".format(part_type.__name__, const_name))

    # Add to installed
    installed_values[part_type.__name__][const_name] = file_name

    # Save installed
    with open('installed.json', 'w') as f:
        json.dump(installed_values, f)

    # Copy the file
    destination = _get_path(part_type, file_name)
    shutil.copy(part_path, destination)

    # Overwrite the enum file
    combined = {**default_values[part_type.__name__], **installed_values[part_type.__name__]}
    _write_enum(part_type.__enum_path__, part_type.__name__, part_type.__path__, part_type.__install__, combined, AvatarPart)

    if print_messages:
        print('"{}" installed at "{}" as {}.{}. Reload the library to use it'.format(part_path, destination, part_type.__name__, file_name))

def uninstall_part(part, confirm=True):
    pass

def install_color(name, value, print_messages=False):
    pass

def uninstall_color(color, confirm=True):
    pass

def factory_reset(confirm=True):
    pass

def _get_path(enum_cls, value):
    package_path = os.path.dirname(__file__)
    p = os.path.join(package_path, enum_cls.__path__, '{}.svg'.format(value))
    return p

def _sanitize(value):
    value = re.sub('[^A-Za-z0-9_]+', '_', value)    # Remove invalid Python identifier chars
    value = value.lstrip('0123456789')              # Remove digits fro the beginning
    return value.upper()                            # Return uppercase

def _write_enum(filename, name, path, install, values_dict, t):
    with open(filename, 'w') as f:
        if t is AvatarColor:
            f.write('from .base_enums import AvatarColor\n')
            f.write('class {}(AvatarColor):\n'.format(name))
        elif t is AvatarPart:
            f.write('from .base_enums import AvatarPart\n')
            f.write('class {}(AvatarPart):\n'.format(name))
        else:
            raise RuntimeError()

        f.write('   __install__ = {}\n'.format(install))
        f.write('   __enum_path__ = {}\n'.format(filename))
        f.write('   __path__ = {}\n'.format(path))
        f.write('\n')
        for name, value in values_dict.items():
            f.write("   {} = '{}'\n".format(name, value))
        