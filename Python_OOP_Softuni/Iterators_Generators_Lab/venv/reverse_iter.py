class reverse_iter:

    def __init__(self, list):
        self.list = list
        self.start = -1
        self.end = len(self.list)
        self.index = self.end

    def __iter__(self):
        return self

    def __next__(self):
        #len(self.list) - 1 on first iteration
        self.end -= 1
        if not self.end == self.start:
            return self.list[self.end]
        raise StopIteration()

reverse_list = reverse_iter([1,2,3,4])

for i in reverse_list:
    print(i)
