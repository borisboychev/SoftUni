class Animal:

    def eat(self):
        return "eating..."


class Dog(Animal):

    def bark(self):
        return "barking..."


class Cat(Animal):

    def meow(self):
        return "meowing..."


"""Test Code"""
a = Animal()
print(a.eat())

d = Dog()
print(d.bark())
print(d.eat())

c = Cat()
print(c.meow())
print(c.eat())
