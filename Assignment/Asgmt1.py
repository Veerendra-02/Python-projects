class Food():
    def __init__(self):
        self.name="Biryani"
        self.price = 200
        self.rating=5

    def taste(self):
        print("Biryani is Spicy")

    def order(self):
        print("Order is confirmed")
        print(self)

F=Food()
print(F.name)
print(F.price)
print(F.rating)
F.taste()
F.order()
print(F)
