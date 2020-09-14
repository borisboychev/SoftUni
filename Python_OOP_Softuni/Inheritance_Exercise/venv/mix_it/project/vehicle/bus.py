from project.vehicle.vehicle import Vehicle

class Bus(Vehicle):


    def __init__(self, available_seats, ticket_price):
        Vehicle.__init__(self, available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = 0

    def get_ticket(self, tickets_count):
        try:
            self.get_capacity(self.available_seats, tickets_count)
            self.available_seats -= tickets_count
            self.tickets_sold += tickets_count
        except Exception as e:
            return str(e)

    def get_total_profit(self):
        return self.tickets_sold * self.ticket_price

# bus = Bus(10, 5)
# print(bus.get_ticket(9))
# print(bus.get_ticket(11))
# print(bus.get_total_profit())