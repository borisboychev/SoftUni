class Flower:

    def __init__(self, flower, required_water):
        self.flower = flower
        self.required_water = required_water
        self.is_happy = False

    def water(self, quantity):
        if quantity >= self.required_water:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f'{self.flower} is happy'
        else:
            return f'{self.flower} is not happy'


flower = Flower('Lilly' , 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())