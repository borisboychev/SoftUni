class PizzaDelivery:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price * quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients:
            if int(self.ingredients[ingredient]) >= quantity:
                self.ingredients[ingredient] -= quantity
                self.price -= ingredient_price * quantity
                return
            else:
                return f"Please check again the desired quantity of {ingredient}!"
        else:
            return f"Wrong ingredient selected! We dont use {ingredient} in {self.name}!"

    def pizza_ordered(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join('{}: {}'.format(k, v) for (k, v) in self.ingredients.items())} " \
               f"and the price will be {self.price}lv."


Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
Margarita.add_extra('mozzarella', 1, 1)
Margarita.add_extra('cheese', 1, 1)
Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 1, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)
print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))
