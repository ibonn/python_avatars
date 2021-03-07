from python_avataaars import Avatar

# Generate 3 random avatars
for i in range(3):
    Avatar.random().render('avatar_{}.svg'.format(i))
