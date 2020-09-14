from project.vehicle.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        Vehicle.__init__(self, available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if self.fuel_tank >= value:
            self.__fuel = value
            return
        self.__fuel = 50

    def drive(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if fuel_needed <= self.fuel:
            self.__fuel -= fuel_needed
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        try:
            diff = self.get_capacity(self.fuel_tank, self.fuel + liters)
            self.fuel += diff
            return self.fuel_tank - self.fuel
        except Exception as e:
            return str(e)

