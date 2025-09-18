class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"employee name is {self.name}")
class Dance:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")

class DancerEmployee(Employee,Dance):
    def __init__(self, name,dance):
        self.name=name
        self.dance=dance

d1=DancerEmployee("alok","Hip-Hop")
d1.show()
