import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

def vehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

v = Vehicle('myBMW', 'V8 600hp', '200 000 $')
print(v)
vJsonString = json.dumps(v, cls=VehicleEncoder)
print(vJsonString)
v2 = json.loads(vJsonString, object_hook=vehicleDecoder)

print(type(v2))
print(v2.name)
