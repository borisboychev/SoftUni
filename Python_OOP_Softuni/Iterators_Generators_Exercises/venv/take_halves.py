def solution():
    def integer():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integer():
            yield i / 2

    def take(n, seq):
        ll = []
        for num in seq:
            if len(ll) == n:
                return ll
            ll.append(num)

    return (take, halves, integer)


<<<<<<< HEAD
""""Test Code"""
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
=======
>>>>>>> d79c1c8db2dfefe6e4c829e5cb5aa8db78b2579e
