class vowels:

    def __init__(self, string : str):
        self.string = string
        self.vowels = ['a', 'e', 'o', 'u', 'i', 'y']
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if not self.counter == len(self.string):
            if self.string[self.counter].lower() in self.vowels:
                return self.string[self.counter]
            else:
                return self.__next__()
        raise StopIteration()

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)