class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return  f"name of the employee{self.name} and his salary is {self.salary}"
    def __repr__(self):
        return f"Employee ('{self.name}',{self.salary})"

e=Employee("harry",50000)
print(e)
print(repr(e))