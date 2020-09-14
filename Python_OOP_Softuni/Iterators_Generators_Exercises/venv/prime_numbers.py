def check_if_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def get_primes(numbers):
    for n in numbers:
        print(n)
        if check_if_prime(n):
<<<<<<< HEAD
            yield n


""""Test Code"""
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
=======
            yield n
>>>>>>> d79c1c8db2dfefe6e4c829e5cb5aa8db78b2579e
