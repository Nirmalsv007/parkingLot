class ParkingManager:
    def __init__(self):
        self.entry_log = {}
        self.exit_log = {}

    def record_entry(self, vehicle, spot, entry_time):
        self.entry_log[vehicle.vehicle_number] = entry_time
        spot.park(vehicle)

    def record_exit(self, vehicle, spot, exit_time):
        self.exit_log[vehicle.vehicle_number] = exit_time
        spot.remove_vehicle()
