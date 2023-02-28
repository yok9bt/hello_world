class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def display(self):
        print('Vehicle Name:', self.name, 'Speed:', self.max_speed, 'Mileage:', self.mileage)


b = Bus('School Volvo', 180, 12)
b.display()
