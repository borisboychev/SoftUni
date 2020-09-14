class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if val is None:
            raise ValueError('Name must be non-empty string')
        self.__name = val

    def get_greeting(self):
        return f'Hello! My name is {self.name} and Im {self.age} years old!'


# name = input()
# age = int(input())
#
# p = Person(name, age)
# print(p.get_greeting())

# def test_valid_name_and_valid_age_should_greet():
#     name = 'testuser'
#     age = 12
#
#     p = Person(name, age)
#     actual = p.get_greeting()
#     expected = f'Hello! My name is {name} and Im {age} years old!'
#
#     if actual != expected:
#         raise ValueError('Invalid Test')


#test_valid_name_and_valid_age_should_greet()
  



