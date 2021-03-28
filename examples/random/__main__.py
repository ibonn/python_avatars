import random

from python_avatars import Avatar

# Set a seed
random.seed(123)

# Generate 10 random avatars
for i in range(10):
    Avatar.random().render('avatar_{}.svg'.format(i))
