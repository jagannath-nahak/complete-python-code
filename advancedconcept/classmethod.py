# class Animal:
#     species="Mammal"
    
#     @classmethod
#     def get_species(cls):
#         return cls.species
    
#     @classmethod
#     def set_species(cls,new_species):
#         cls.species=new_species

# print(Animal.get_species())
# Animal.set_species("Reptile")
# print(Animal.get_species())

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,data):
        return cls(data.split("-")[0],data.split("-")[1])

data="Alok-20"
p1=Person.from_string(data)
print(p1.name)
print(p1.age)


