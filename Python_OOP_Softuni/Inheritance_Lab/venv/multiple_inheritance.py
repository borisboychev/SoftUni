class Person:
    def sleep(self):
        return "sleeping..."


class Employee:
    def get_fired(self):
        return "fired..."


class Teacher(Employee, Person):
    def teach(self):
        return "teaching..."


""""Test Code"""

p = Person()
print(p.sleep())

e = Employee()
print(e.get_fired())

t = Teacher()
print(t.sleep())
print(t.get_fired())
print(t.teach())
