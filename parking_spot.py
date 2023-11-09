class ParkingSpot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        self.is_occupied = False
        self.vehicle = None

    def park(self, vehicle):
        if not self.is_occupied:
            self.is_occupied = True
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        if self.is_occupied:
            self.is_occupied = False
            self.vehicle = None
            return True
        return False
