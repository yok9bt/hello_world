class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return int(super().fare()*1.1)

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())