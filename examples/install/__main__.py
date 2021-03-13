from python_avataaars import install_part, ClothingType, Avatar

# You can reload the library or assign the value returned by install_part to
# the enum to use the new value
ClothingType = install_part(
    'suit.svg',
    ClothingType,
    print_messages=True
)

# Generate a random avatar wearing the new installed clothes
Avatar.random(clothing=ClothingType.SUIT).render("avatar_suit.svg")
