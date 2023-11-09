# This is a sample Python script.
from exceptions import NoAvailableParkingSpotException, VehicleNotFoundException
from parking_lot import ParkingLot
from vehicle import Vehicle


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
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
            except NoAvailableParkingSpotException as e:
                print(f"Error: {e}")

        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            try:
                found_spot = parking_lot.retrieve_parking_spot(vehicle_number)
                print("Found spot:", found_spot)
            except VehicleNotFoundException as e:
                print(f"Error: {e}")

        elif choice == "3":
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
