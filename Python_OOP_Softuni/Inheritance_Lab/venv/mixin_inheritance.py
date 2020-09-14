from statistics import mean


class CalculateAverageMixin:

    def get_average(self, values):
        return mean(values)


class MathUtils:

    def get_average(self, values):
        return mean(values)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person, CalculateAverageMixin):

    def __init__(self, name, age, grades):
        Person.__init__(self, name, age)
        self.grades = grades

    def get_average_grades(self):
        return MathUtils().get_average(self.grades)


class Employee(Person, CalculateAverageMixin):

    def __init__(self, name, age, daily_working_hours):
        Person.__init__(self, name, age)
        self.daly_working_hours = daily_working_hours


""""Test Code"""
st = Student("Pesho", 3, [2, 2, 3, 4, 6, 6, 6, 6, 6, 6])
print(st.get_average(st.grades))
print(st.get_average_grades())
