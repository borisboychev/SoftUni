from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        Factory.__init__(self, name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient, quantity):
        valid_ingredient = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]
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
            raise KeyError("No such product in the factory")

        if not quantity <= self.ingredients[ingredient]:
            raise ValueError(f"Ingredient quantity cannot be less than zero")

        self.ingredients[ingredient] -= quantity

    def add_recipe(self, recipe_name, recipe):
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = recipe
        else:
            self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name):
        if recipe_name in self.recipes:
            if recipe_name not in self.products:
                quantity = self.quantity_able_to_produce(recipe_name)
                self.products[recipe_name] = quantity // len(self.recipes[recipe_name])
            else:
                quantity = self.quantity_able_to_produce(recipe_name)
                self.products[recipe_name] += quantity // len(self.recipes[recipe_name])
        else:
            raise TypeError("No such recipe")

    # Loops through the ingredients and returns how many
    # products can be produces devised by the length of
    # the recipe because quantity is increased for every
    # product available
    def quantity_able_to_produce(self, recipe_name):
        quantity = 0
        no_more_products = False
        while not no_more_products:
            for product, quantity_product in self.recipes[recipe_name].items():
                try:
                    self.remove_ingredient(product, quantity_product)
                    quantity += 1
                except ValueError:
                    no_more_products = True
                    break
        return quantity

