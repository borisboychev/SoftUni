def fibonacci():
    a, b = 0, 1
    while True:
        yield a
<<<<<<< HEAD
        a, b = b, a + b


""""Test Code"""
generator = fibonacci()
for i in range(5):
    print(next(generator))
=======
        a, b = b, a + b
>>>>>>> d79c1c8db2dfefe6e4c829e5cb5aa8db78b2579e
