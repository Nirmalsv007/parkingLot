from parking_spot import ParkingSpot


class ParkingLevel:
    def __init__(self, level_name, capacity):
        self.level_name = level_name
        self.capacity = capacity
        self.spots = [ParkingSpot(i) for i in range(1, capacity + 1)]

    def find_available_spot(self):
        for spot in self.spots:
            if not spot.is_occupied:
                return spot
        return None
