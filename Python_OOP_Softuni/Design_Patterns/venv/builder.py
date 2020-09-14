from utils.print_props import PrintAttributes


class Animal(PrintAttributes):
    def __init__(self, name, age, species, weight):
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight


# print(Animal('Ivan', 3, 'kotka', 6))

class AnimalBuilder:
    manditory_props = {'name': str,
                       'age': int,
                       'species': str,
                       'weight': float
                       }

    def __init__(self):
        self.__props_dict = {}
        self.__reset()

    def set_name(self, name):
        self.__props_dict['name'] = name
        return self

    def set_age(self, age):
        self.__props_dict['age'] = age
        return self

    def set_species(self, species):
        self.__props_dict['species'] = species
        return self

    def set_weight(self, weight):
        self.__props_dict['weight'] = weight
        return self

    def __validate(self):
        missing = [key for (key, val) in self.manditory_props.items() if self.__props_dict[key] is None]
        if missing:
            raise ValueError(f"The following values are missing: {', '.join(x for x in missing)}")

    def __reset(self):
        for (key, val) in self.manditory_props.items():
            self.__props_dict[key] = None

    def build(self):
        self.__validate()
        result = Animal(**self.__props_dict)
        self.__reset()
        return result


builder = AnimalBuilder()
builder.set_name('Pesho')
builder.set_age(2)
builder.set_species('cat')
builder.set_weight(6)

print(builder.build())

print(builder
      .set_name('Gosho')
      .set_age(6)
      .set_species('dog')
      .set_weight(12)
      .build())
