class Faculty:
    def __init__(self):
        self.id=None
        self.name=None
        self.age=None

    def getdata(self):
        self.id=int(input("Enter your ID:"))
        self.name=input("Enter your name:")
        self.age=int(input("Enter your age:"))

    def display(self):

        print(f"Faculty id is {self.id}")
        print(f"Faculty name is {self.name}")
        print(f"Faculty age is {self.age}")

    def __str__(self):
        return "Faculty details are:"

obj=Faculty()
obj.getdata()
print(obj)
obj.display()

