class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Programmer(Employee):
    def __init__(self, name, salary,id):
        super().__init__(name, salary)
        self.id=id

emp1=Employee("SOhan",10000)
emp2=Programmer("Shradha",15000,"201")
print(emp2.id)
print(emp2.salary)
print(emp2.name)