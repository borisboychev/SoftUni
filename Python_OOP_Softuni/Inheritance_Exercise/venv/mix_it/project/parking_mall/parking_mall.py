from project.capacity_mixin import CapacityMixin

class ParkingMall(CapacityMixin):

    def __init__(self, parking_lots):
        self.parking_lots = parking_lots

    def check_availability(self):
        try:
            self.get_capacity(self.parking_lots, self.parking_lots)
            return f"Parking lots available {self.parking_lots}"
        except Exception:
            return f"There are no more parking lots!"

