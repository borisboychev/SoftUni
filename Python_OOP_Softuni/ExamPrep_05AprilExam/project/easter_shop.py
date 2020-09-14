from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name, chocolate_factory: ChocolateFactory, egg_factory: EggFactory, paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type, quantity):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type, quantity):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type, quantity):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe):
        self.chocolate_factory.make_chocolate(recipe)
        self.storage[recipe] = self.chocolate_factory.products[recipe]

    def paint_egg(self, color, egg_type):
        available_eggs = [e for e in self.egg_factory.ingredients if e == egg_type]
        available_colors = [c for c in self.paint_factory.ingredients if c == color]

        if len(available_eggs) > 0 and len(available_colors) > 0:
            if f"{available_colors[0]} {available_eggs[0]}" not in self.storage:
                self.storage[f"{available_colors[0]} {available_eggs[0]}"] = 1
                self.egg_factory.remove_ingredient(egg_type, 1)
                self.paint_factory.remove_ingredient(color, 1)
            else:
                self.storage[f"{available_colors[0]} {available_eggs[0]}"] += 1
                self.egg_factory.remove_ingredient(egg_type, 1)
                self.paint_factory.remove_ingredient(color, 1)
        else:
            raise ValueError("Invalid commands")



    def __repr__(self):
        result = f"Shop name: {self.name}\n"
        result += f"Shop Storage:\n"
        for product, quantity in self.storage.items():
            result += f"{product}: {quantity}\n"

        return result

egg_factory = EggFactory('qicaF', 10)
paint_factory = PaintFactory('boqF', 20)
chocolate_factory = ChocolateFactory('shokoladF', 30)

shop = EasterShop("magnit", chocolate_factory, egg_factory, paint_factory)

shop.add_chocolate_ingredient('white chocolate', 5)
shop.add_chocolate_ingredient('dark chocolate', 10)
shop.add_chocolate_ingredient('white chocolate', 5)

shop.add_egg_ingredient('chicken egg', 8)
shop.add_paint_ingredient('green', 1)

chocolate_factory.add_recipe("mixed chocolate", {'white chocolate': 2, "dark chocolate":2})
chocolate_factory.add_recipe("mixed chocolate", {'white chocolate': 5, "dark chocolate":4})

shop.make_chocolate('mixed chocolate')

print(shop)
print(shop.egg_factory.ingredients)
shop.paint_egg('green', 'chicken egg')

print(shop.storage)
print(shop)

print(shop.paint_factory.products)