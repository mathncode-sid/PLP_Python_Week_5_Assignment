class Donkey:
    def move(self):
        return "Walking"
    
class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"
    
for vehicle in [Donkey(), Car(), Plane()]:
    print(vehicle.move())