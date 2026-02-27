class Fan:
    def __init__(self):
        self.color="black"
        self.brand="Usha"
        self.price=1200

    def rotate(self):
        print("Fan is rotating")

F=Fan()
print(F.color)
print(F.brand)
print(F.price)
F.rotate()