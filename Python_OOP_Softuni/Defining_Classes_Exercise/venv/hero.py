class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def heal(self, increase_with):
        self.health += increase_with

    def defend(self, damage):
        if self.health - damage <= 0:
            self.health = 0
            return f'{self.name} was defeated'
        else:
            self.health -= damage

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))