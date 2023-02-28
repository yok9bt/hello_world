class Vehicle:
    def __init__(self) -> None:
        self.max_speed = 150
        self.mileage = 50000

v = Vehicle()
print(v.max_speed, v.mileage)