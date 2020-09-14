class Person:
    id = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.id = Person.id
        Person.id += 1

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f'Person {self.id}: {self.name} {self.surname}'

    def __str__(self):
        return self.name + ' ' + self.surname



class Group:
    def __init__(self, name: str, people: Person):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(self.name, self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"

    def __getitem__(self, item):
        return self.people[item].__repr__()


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])

second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
