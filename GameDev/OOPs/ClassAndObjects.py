# OOP : Object Oriented Programming

# To merge with real world entity

# Class : It's a group of objects (Variables and functions) and it's a virtual entity
# Object : It's a copy of a class
# Inheritance
# Polymorphism
# Encapsulation

class Student:
    age = 6
    height = 3
    rollNo = 0
    std = 2

    def printStudentDetails(self):
        print(self.age, self.height, self.rollNo, self.std)


# using this objects we can access variables/functions of the class Student
obj1 = Student()

obj1.age = 10
obj1.height = 4
obj1.rollNo = 8
obj1.std = 4

obj1.printStudentDetails()

obj2 = Student()

obj2.age = 20
obj2.height = 6
obj2.rollNo = 27
obj2.std = 12

obj2.printStudentDetails()













