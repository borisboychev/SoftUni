#from hotel_rooms.project.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.free_room()

    def print_status(self):
        self.guests = sum(x.guests for x in self.rooms if x.is_taken)
        print(f"Hotel {self.name} has {self.guests} total guests")
        free_rooms = [x.number for x in self.rooms if not x.is_taken]
        taken_rooms = [x.number for x in self.rooms if x.is_taken]
        print(f"Free rooms: {', '.join([str(x) for x in free_rooms])}")
        print(f"Taken rooms: {', '.join([str(x) for x in taken_rooms])}")


# """Test Code"""
#
# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()
