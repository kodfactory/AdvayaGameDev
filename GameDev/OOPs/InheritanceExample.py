# Inheritance

class Animal:
    def typeOfAnimal(self):
        print("Animcal can be of different types")

    def walk(self):
        print("They can walk")


# Single level inheritance
class Lion(Animal):
    def info(self):
        print("Lion is the King of Jungle")

# Multi level inheritance
class ChildLion(Lion):
    def cry(self):
        print("They are new born, so they are crying...")

print(issubclass(Lion, ChildLion)) # False
print(issubclass(ChildLion, Lion)) # True

# obj = Lion()

# obj.info()
# obj.walk()
# obj.typeOfAnimal()

# obj1 = ChildLion()

# obj1.info()
# obj1.cry()

# obj1.typeOfAnimal()
# obj1.walk()


