class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show_detail(self):
        print(f"Name:{self.name}")
        print(f"Species:{self.species}")
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog")
        self.breed=breed
    def show_detail(self):
        Animal.show_detail(self)
        print(f"Breed:{self.breed}")
class DuggerMan(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name, breed="lambda")
        self.color=color
    def show_detail(self):
        Dog.show_detail(self)
        print(f"Color:{self.color}")

d1=DuggerMan("Charlie","black")
d1.show_detail()