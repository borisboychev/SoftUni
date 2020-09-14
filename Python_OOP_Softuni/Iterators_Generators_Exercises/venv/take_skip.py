class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = 0
        self.counter = -self.step  # to start from 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterations == self.count:
            self.iterations += 1
            self.counter += self.step
            return self.counter
        raise StopIteration()


""""Test Code"""
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
