def read_next(*args):
    for seq in args:
        for el in seq:
<<<<<<< HEAD
            yield el


""""Test Code"""
for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
=======
            yield el
>>>>>>> d79c1c8db2dfefe6e4c829e5cb5aa8db78b2579e
