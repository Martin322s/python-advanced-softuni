from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room is None:
            return  # not specified in requirements

        result = room.take_room(people)
        if result is not None:
            return result

        self.guests += people

    def free_room(self, room_number: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room is None:
            return  # not specified in requirements

        people_before_free = room.guests
        result = room.free_room()
        if result is not None:
            return result

        self.guests -= people_before_free

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        free_rooms_str = ", ".join(free_rooms)
        taken_rooms_str = ", ".join(taken_rooms)

        return (
            f"Hotel {self.name} has {self.guests} total guests\n"
            f"Free rooms: {free_rooms_str}\n"
            f"Taken rooms: {taken_rooms_str}"
        )