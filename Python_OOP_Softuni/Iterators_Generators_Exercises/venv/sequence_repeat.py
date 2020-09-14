class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            temp = self.index
            self.index += 1
            if self.index == len(self.sequence):
                self.index = 0
            self.counter += 1
            return self.sequence[temp]
        raise StopIteration()


""""Test Code"""
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
