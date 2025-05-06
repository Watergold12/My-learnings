import random
import time

class Vehicle:
    def __init__(self, vehicle_id, latitude, longitude):
        self.vehicle_id = vehicle_id
        self.latitude = latitude
        self.longitude = longitude

    def update_location(self):
        # Simulate GPS updates
        self.latitude += random.uniform(-0.001, 0.001)
        self.longitude += random.uniform(-0.001, 0.001)

    def get_location(self):
        return self.latitude, self.longitude

class VehicleTrackingSystem:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle_id, latitude, longitude):
        if vehicle_id not in self.vehicles:
            self.vehicles[vehicle_id] = Vehicle(vehicle_id, latitude, longitude)
        else:
            print("Vehicle ID already exists.")

    def update_vehicle_location(self, vehicle_id):
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id].update_location()
        else:
            print("Vehicle ID not found.")

    def get_vehicle_location(self, vehicle_id):
        if vehicle_id in self.vehicles:
            return self.vehicles[vehicle_id].get_location()
        else:
            print("Vehicle ID not found.")

# Example Usage
vts = VehicleTrackingSystem()

# Add vehicles
vts.add_vehicle("V1", 37.7749, -122.4194)
vts.add_vehicle("V2", 40.7128, -74.0060)
vts.add_vehicle("V3", 40.7128, -78.0060)
vts.add_vehicle("V4", 60.4851, -30.4500)

# Simulate GPS updates for 10 iterations
for _ in range(10):
    vts.update_vehicle_location("V1")
    vts.update_vehicle_location("V2")
    time.sleep(1)  # Simulate updates every second

# Simulate GPS updates for 15 iterations
for _ in range(15):
    vts.update_vehicle_location("V3")
    vts.update_vehicle_location("V4")
    time.sleep(2)  # Simulate updates every 2 seconds

# Get vehicle locations
print("Vehicle V1 Location:", vts.get_vehicle_location("V1"))
print("Vehicle V2 Location:", vts.get_vehicle_location("V2"))
print("Vehicle V3 Location:", vts.get_vehicle_location("V3"))
print("Vehicle V4 Location:", vts.get_vehicle_location("V4"))