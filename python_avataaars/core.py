import os
import re
import shutil
import json

from .base_enums import AvatarPart, AvatarColor

_package_path = os.path.dirname(__file__)
_default_path = os.path.join(_package_path, 'default.json')
_installed_path = os.path.join(_package_path, 'installed.json')

def install_part(part_path, part_type, print_messages=False):

    if not part_type.__install__:
        raise RuntimeError("The part type {} cannot be expanded".format(part_type.__name__))

    if part_type.__path__ == '':
        raise RuntimeError("Installation path not found")

    file_name = os.path.splitext(os.path.basename(part_path))[0]
    const_name = _sanitize(file_name) 
    
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
    with open(_installed_path, 'w') as f:
        json.dump(installed_values, f, indent=4)

    # Copy the file
    destination = _get_path(part_type, file_name)
    shutil.copy(part_path, destination)

    # Overwrite the enum file
    combined = {**default_values[part_type.__name__], **installed_values[part_type.__name__]}
    _write_enum(part_type, combined, AvatarPart)

    if print_messages:
        print('"{}" installed at "{}" as {}.{}. Reload the library to use it'.format(part_path, destination, part_type.__name__, const_name))

def uninstall_part(part, confirm=True):
    if os.path.isfile(_installed_path):
        # Load installed
        with open(_installed_path, 'r') as f:
            installed_values = json.load(f)

        # Load default
        with open(_default_path, 'r') as f:
            default_values = json.load(f)

        
        if confirm:
            confirm_resp = input('Do you really want to uninstall {}.{}? y/n: '.format(part.__class__.__name__, part.name))
            if confirm_resp.lower().strip() != 'y':
                return False

        # Delete svg
        os.remove(_get_path(part.__class__, part.value))

        # Delete from installed
        del installed_values[part.__class__.__name__][part.name]

        # Combine installed + default
        combined = {**default_values[part.__class__.__name__], **installed_values[part.__class__.__name__]}

        # Update installed
        with open(_installed_path, 'w') as f:
            json.dump(installed_values, f)

        # Rewrite enum
        _write_enum(part.__class__, combined, AvatarPart)
        return True

def install_color(name, value, print_messages=False):
    raise NotImplementedError("TODO")   # TODO
    # Load installed.json
    # Load default.json
    # Combine installed + default
    # Check conflicts
    # Check installable
    # Add value to installed
    # Combine installed + default
    # Rewrite enum

def uninstall_color(color, confirm=True):
    raise NotImplementedError("TODO")   # TODO
    # Load installed.json
    # Delete from installed
    # Combine installed + default
    # Rewrite enum

def factory_reset(confirm=True):
    raise NotImplementedError("TODO")   # TODO

    # Load installed and remove svgs
    if os.path.isfile(_installed_path):
        with open(_installed_path, 'r') as f:
            installed_values = json.load(f)

        for enum_name, enum_values_dict in installed_values.items():
            for name, value in enum_values_dict.items():
                _get_path()

    # Load defaults
    with open(_default_path, 'r') as f:
        default_values = json.load(f)

    for enum_name, enum_values_dict in default_values.items():
        enum_path = os.path.join(_package_path, enum_values_dict['__path__'])
        _write_enum()

def _get_path(enum_cls, value):
    p = os.path.join(_package_path, enum_cls.__path__, '{}.svg'.format(value))
    return p

def _sanitize(value):
    value = re.sub('[^A-Za-z0-9_]+', '_', value)    # Remove invalid Python identifier chars
    value = value.lstrip('0123456789')              # Remove digits fro the beginning
    return value.upper()                            # Return uppercase

def _write_enum(e, values_dict, t):

    filename = e.__enum_path__
    name = e.__name__
    path = e.__path__
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
        f.write("    __path__ = '{}'\n".format(path))
        f.write("\n")
        for name, value in values_dict.items():
            if name[:2] != '__':
                f.write("    {} = '{}'\n".format(name, value))
        