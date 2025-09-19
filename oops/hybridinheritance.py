class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
class sportsman:
    def __init__(self,game):
        self.game=game
    def show(self):
        print(f"The game name is {self.game}")

class SportStudent(Student,sportsman):
    def __init__(self, name, age,game):
        self.name=name
        self.age=age
        self.game=game

class Cricketer(SportStudent):
    def __init__(self, name, age, game,salary):
        self.salary=salary
        super().__init__(name, age, game)

    def show(self):
        print(f"Cricketer {self.name} he loves to play {self.game} and he got salary of {self.salary} , right now he is only {self.age}")



s1=SportStudent("Guru",20,"Cricket")
s1.show()

c1=Cricketer("Sambit",20,"Cricket",50000)
c1.show()