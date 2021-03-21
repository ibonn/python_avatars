import python_avataaars as pa

# IMPORTANT: You should run install.py before running this script, otherwise it won't work.

try:
    # Generate a random avatar wearing the new installed clothes
    pa.Avatar.random(clothing=pa.ClothingType.SUIT).render("avatar_suit.svg")
except AttributeError:
    print("The part is not installed. Please run install.py to install it")
