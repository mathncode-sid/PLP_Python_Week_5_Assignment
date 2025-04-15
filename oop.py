class MasculineMan:
    material = input("What is his wealth?")
    money = input("Does he have the other Ms?")
    muscle = input("Is he lean or skinny?")
    mind = input("Enter the kind of mind he possesses:")
    men = input("Enter the kind of circle he has:")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Inheritance of attributes of class MasculineMan by class Person
class Masculine(Person, MasculineMan):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.material = MasculineMan.material
        self.money = MasculineMan.money
        self.muscle = MasculineMan.muscle
        self.mind = MasculineMan.mind
        self.men = MasculineMan.men

#Create instance
masculine_man = Masculine("John", 30)

#Print out attributes
print(f"Name: {masculine_man.name}")
print(f"Age: {masculine_man.age}")
print(f"Material: {masculine_man.material}")
print(f"Money: {masculine_man.money}")
print(f"Muscle: {masculine_man.muscle}")
print(f"Mind: {masculine_man.mind}")
print(f"Men: {masculine_man.men}")