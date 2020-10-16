# Polymorphism: poly + morphism
# Same name but different meaning is called polymorphism

class Bank:
    def getROI(self):
        print("Current ROI is 8%")


class ICICI(Bank):
    def healthInsurance(self):
        print("Good bank for health insurance")
    
    # We will create a function with same name but different logic
    # Function overloading: Which is example of polymorphism (Runtime polymorphism)
    def getROI(self):
        print("Current ROI is 9.5%")

class HDFC(Bank):
    def homeLoan(self):
        print("Good bank for home loan")

    def getROI(self):
        print("Current ROI is 10%")

class SBI(Bank):
    def government(self):
        print("Government bank")

    def getROI(self):
        print("Current ROI is 7%")

obj = ICICI()
obj.getROI()

obj1 = HDFC()
obj1.getROI()

obj2 = SBI()
obj2.getROI()


