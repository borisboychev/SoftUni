class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Person):

    def __init__(self, name, age):
        super().__init__(name, age)


# """"Test Code"""
# child = Child('Boris', 18)
# print(child.__dict__)