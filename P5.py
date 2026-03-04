class Employee:
    def __init__(self):
        self.id=11
        self.name="Veera"
        self.gfName="Sundri"

    def work(self):
        print("Veera loves Sundri")

E=Employee()
print(E.name)
E.work()
E.gfName="Munni" #Modification
print(E.gfName)
E.salary =50000 #Addition
print(E.salary)
del E.name #Deletion
print(E.name)
