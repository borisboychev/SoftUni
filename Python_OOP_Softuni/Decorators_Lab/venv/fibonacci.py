class Fibonacci:

    def __init__(self):
        self.cache = {0: 0,
                      1: 1, }

    def __call__(self, n):
        if n in self.cache:
            return self.cache[n]

        result = self(n-1) + self(n-2)
        self.cache[n] = result
        return result


fib = Fibonacci()
print(fib(7))
print(fib.cache)
