from exceptions import ParkingLotException
from parking_lot import ParkingLot
from vehicle import Vehicle

if __name__ == "__main__":
    parking_lot = ParkingLot()

    while True:
        print("1. Assign Parking Spot")
        print("2. Retrieve Parking Spot")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            vehicle_size = input("Enter vehicle size: ")
            vehicle = Vehicle(vehicle_number, vehicle_size)
            try:
                assigned_spot = parking_lot.assign_parking_spot(vehicle)
                print("Assigned spot:", assigned_spot)
            except ParkingLotException as e:
                print(f"Error: {e}")

        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            try:
                found_spot = parking_lot.retrieve_parking_spot(vehicle_number)
                print("Found spot:", found_spot)
            except ParkingLotException as e:
                print(f"Error: {e}")

        elif choice == "3":
            break
