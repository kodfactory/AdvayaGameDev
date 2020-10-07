# Scope of variable

# Global & Local


# Here 'a' is global variable
a = 20

def changeValue():
    global a
    a = 50
    # a = 20 # here 'a' is local variable
    print("Inside a function",a)

changeValue()

print("Outside of a function",a)
