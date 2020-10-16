# Abstraction : Data hiding

class Employee:
    # Below is data abstraction
    __salary = 10000

    def displaySalary(self):
        print(Employee.__salary)

obj = Employee()
# print(obj.__salary)

obj.displaySalary()

# print("Employee salary is",obj.salary)

