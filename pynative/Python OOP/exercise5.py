class Vehicle:
    color = 'white'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print('Color:', self.color, 'Vehicle name:', self.name, 
              'Speed:', self.max_speed , 'Mileage:', self.mileage)

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

b = Bus('School Volvo', 180, 12)
c = Car('Audi Q5', 240, 18)

b.display()
c.display()
