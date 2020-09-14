class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return not len(self.data) >= 1

    def __str__(self):
        return f'[{", ".join(str(x) for x in self.data[::-1])}]'


"""Test Code"""

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.is_empty())
print(stack)
