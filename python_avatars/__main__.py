"""
CLI utility to manage the library

Install/uninstall colors and parts
"""
import argparse
# from . import install_part
# from . accessory_types import AccessoryType

if __name__ == "__main__":
    

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--factory-reset",
        help="Reset the library to its starting values, uninstalling all installed parts and colors.",
        action="store_true"
    )

    iu_group = parser.add_argument_group()
    
    iu_group.add_argument(
        'value',
        nargs=1,
        help="The path to the svg to install in case of installing a part, the hex value of the color in case of installing a color or the name of the value to remove in case of uninstalling."
    )

    iu_keywords = iu_group.add_mutually_exclusive_group()
    iu_types = iu_group.add_mutually_exclusive_group()

    iu_keywords.add_argument(
        "--install",
        help="Install a part/color",
        action="store_true"
    )

    iu_keywords.add_argument(
        "--uninstall",
        help="Uninstall a part/color",
        action="store_true"
    )

    iu_types.add_argument(
        "--style",
        help="Select the AvatarStyle enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--bg-color",
        help="Select the BackgroundColor enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--fabric-color",
        help="Select the ClothingColor enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--graphic",
        help="Select the ClothingGraphic enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--clothes",
        help="Select the ClothingType enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--eyes",
        help="Select the EyesType enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--eyebrows",
        help="Select the EyebrowsType enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--facial-hair",
        help="Select the FacialHairType enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--hair-color",
        help="Select the HairColor enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--hairstyle",
        help="Select the HairType enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--hat",
        help="Select the HatType enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--mouth",
        help="Select the MouthType enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--nose",
        help="Select the NoseType enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--skin-color",
        help="Select the SkinColor enum as the target of the install/uninstall process",
        action="store_true"
    )

    iu_types.add_argument(
        "--accessory",
        help="Select the Accesory enum as the target of the install/uninstall process",
        action="store_true"
    )

    args = parser.parse_args()

    if args.factory_reset:
        factory_reset(confirm=True)
        exit(0)

    elif args.value is None:
        print("Error: A value is required to be installed/uninstalled")
    else:
        if args.install_accessory:
            install_part(args.value, AccessoryType)
        