class Room:
    def __init__(self, room_id: str, name: str, capacity: int):
        self.room_id = room_id
        self.name = name
        self.capacity = capacity
        self.occupied = False

    def occupy(self):
        self.occupied = True

    def free(self):
        self.occupied = False