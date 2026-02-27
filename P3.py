class Customer():
    def __init__(self):
        self.id=18
        self.name="Virat"
        self.age=42
    def shop(self):
        print("Product is purchased")
        print(self)
C=Customer()
print(C.id)
print(C.name)
C.shop()
print(C)