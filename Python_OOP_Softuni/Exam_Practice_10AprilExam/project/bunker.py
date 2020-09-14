from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_objects = [x for x in self.supplies if x.__class__.__name__ == "FoodSupply"]
        if len(food_objects) == 0:
            raise IndexError("There are no food supplies left!")
        return food_objects

    @property
    def water(self):
        water_objects = [x for x in self.supplies if x.__class__.__name__ == "WaterSupply"]
        if len(water_objects) == 0:
            raise IndexError("There are no water supplies left!")
        return water_objects

    @property
    def painkillers(self):
        painkiller_objects = [x for x in self.medicine if x.__class__.__name__ == "Painkiller"]
        if len(painkiller_objects) == 0:
            raise IndexError("There are no painkillers left!")
        return painkiller_objects

    @property
    def salves(self):
        salves_objects = [x for x in self.medicine if x.__class__.__name__ == "Salve"]
        if len(salves_objects) == 0:
            raise IndexError("There are no salves left!")
        return salves_objects

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            if medicine_type == "Salve":
                last_med = self.salves.pop()
            elif medicine_type == "Painkiller":
                last_med = self.painkillers.pop()
            self.medicine.pop()
            last_med.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"
        return

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                last_supply = self.food.pop()
            elif sustenance_type == "WaterSupply":
                last_supply = self.water.pop()
            self.supplies.pop()
            last_supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"
        return

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for s in self.survivors:
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")
