#Types of variables

class Bike:
    def __init__(self):
        self.brand="RE"             #Instance Variable
        self.color="Black"          #Instance Variable

    def sound(self):
        print("Bike is good")
        self.price=250000           #Instance Variable
        tyre=2                      #Local Variable
        print(tyre)                 #tyre is a local Variable, it can only access inside the function
B=Bike()                            #Reference Variable
B.sound()
print(B.color)
B.mileage=30                        #Instance Variable
B1=B                                #Reference Variable
B2=B1                               #Reference Variable
print(B1.brand)
B2.color="Red"
print(B2.color)
