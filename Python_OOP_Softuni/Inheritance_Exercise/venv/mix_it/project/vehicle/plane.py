from project.vehicle.vehicle import Vehicle

class Plane(Vehicle):

    def __init__(self, available_seats, rows, seats_per_row):
        Vehicle.__init__(self, available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}

    @staticmethod
    def is_valid_row(row_number, rows):
        return row_number in range(1,rows+1)

    def buy_tickets(self,row_number, tickets_count):
        if not self.is_valid_row(row_number, self.rows):
            return f"There is no {row_number} in the plane!"
        try:
            seats = self.seats_available[row_number] if row_number in self.seats_available else self.seats_per_row
            self.get_capacity(seats, tickets_count)
            self.seats_available[row_number] = tickets_count - self.seats_per_row
            self.available_seats -= tickets_count
            return tickets_count
        except Exception as e:
            return f"Not enough tickets on {row_number}!"


# plane = Plane(20, 4, 5)
# print(plane.buy_tickets(5, 10))
# print(plane.buy_tickets(4, 6))
# print(plane.buy_tickets(4, 4))


