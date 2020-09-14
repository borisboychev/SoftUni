from abc import ABC, abstractmethod

class Factory(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient, quantity):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient, quantity):
        pass

    def can_add(self, value):
        return value <= self.capacity
