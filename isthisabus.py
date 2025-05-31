class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(vehicle):
    pass
School_bus = Bus("school volvo", 180, 12)
print("Vehicle name:", School_bus.name, "Speed:", School_bus.max_speed,
"Mileage:", School_bus.mileage)