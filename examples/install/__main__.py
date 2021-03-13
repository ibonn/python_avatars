import python_avataaars as pa

# IMPORTANT: You should run install.py before running this script, otherwise it won't work.

# Generate a random avatar wearing the new installed clothes
pa.Avatar.random(clothing=pa.ClothingType.SUIT).render("avatar_suit.svg")
