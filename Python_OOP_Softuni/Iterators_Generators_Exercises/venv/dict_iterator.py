class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterations  == len(self.dictionary.values()):
            self.iterations += 1

            return (list(self.dictionary.keys())[self.iterations-1],
                    list(self.dictionary.values())[self.iterations-1])
        raise StopIteration()


""""Test Code"""
result = dictionary_iter({1: "1", 2: "2", 4: 'borko', 5: 'goshko'})
for x in result:
    print(x)

