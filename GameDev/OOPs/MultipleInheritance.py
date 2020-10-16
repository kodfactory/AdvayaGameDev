class LandAnimal:
    def walk(self):
        print("They walk on land")

class SeaAnimal:
    def swim(self):
        print("They can swim")
    
class Dog(LandAnimal):
    def bark(self):
        print("Dog can bark")

class Fish(SeaAnimal):
    def die(self):
        print("They die outside water")


# Multiple inheritance
class Crocodial(LandAnimal, SeaAnimal):
    def oldest(self):
        print("They are the most oldest animals")

obj = Crocodial()

obj.walk()
obj.swim()
obj.oldest()

