class reverse_txt:

    def __init__(self, txt):
        self.txt = txt
        self.start = 0
        self.end = len(self.txt)

    def __iter__(self):
        return self

    def __next__(self):
        self.end -= 1
        if self.end >= self.start:
            return self.txt[self.end]
        raise StopIteration()


def reverse_text(txt):
    for letter in reverse_txt(txt):
        yield letter

for char in reverse_text("pets"):
    print(char, end='')