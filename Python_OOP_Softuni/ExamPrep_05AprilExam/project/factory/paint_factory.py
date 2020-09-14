from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)

    @property
    def products(self):
        return self.ingredients

    def add_ingredient(self, ingredient, quantity):
        valid_ingredient = ["white", "yellow", "blue", "green", "red"]
        if ingredient in valid_ingredient:
            if self.can_add(quantity):
                if ingredient not in self.ingredients:
                    self.ingredients[ingredient] = quantity
                else:
                    self.ingredients[ingredient] += quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {ingredient} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient, quantity):
        if ingredient not in self.ingredients:
            raise KeyError("No such ingredient in the factory")

        if not quantity <= self.ingredients[ingredient]:
            raise ValueError(f"Ingredient quantity cannot be less than zero")

        self.ingredients[ingredient] -= quantity


