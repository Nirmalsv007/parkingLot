from datetime import datetime
from typing import Optional, Dict, Union

from exceptions import NoAvailableParkingSpotException, VehicleNotFoundException
from parking_level import ParkingLevel
from parking_manager import ParkingManager
from vehicle import Vehicle


class ParkingLot:
    def __init__(self):
        self.levels = [ParkingLevel('A', 20), ParkingLevel('B', 20)]
        self.manager = ParkingManager()
        self.allocated_vehicle_numbers = set()

    def assign_parking_spot(self, vehicle: Vehicle) -> Optional[Dict[str, Union[str, int]]]:
        if vehicle.vehicle_number in self.allocated_vehicle_numbers:
            print("Duplicate license plate detected.")
            return None

        for level in self.levels:
            spot = level.find_available_spot()
            if spot:
                entry_time = datetime.now()
                self.manager.record_entry(vehicle, spot, entry_time)
                self.allocated_vehicle_numbers.add(vehicle.vehicle_number)
                return {"level": level.level_name, "spot": spot.spot_number}
        raise NoAvailableParkingSpotException("No available parking spots.")

