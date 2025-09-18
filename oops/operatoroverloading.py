a=5
b=10
# we can add two number
print(a+b)

# we can concanate two strigs
str1="Alok"
str2="Sahu"
print(str1+str2)


# we can also use operators in our objects of class
class Student:
    def __init__(self,mark):
        self.mark=mark
    def __add__(self,other):
        return self.mark+other.mark
    def __mul__(self,other):
        return self.mark*other.mark
    def __eq__(self, other):
        return self.mark==other.mark
    def __ne__(self, value):
        return self.mark!=value.mark
    def __lt__(self,other):
        return self.mark<other.mark
    def __gt__(self,other):
        return self.mark>other.mark
    def __floordiv__(self,other):
        return self.mark//other.mark
    def __pow__(self,other):
        return self.mark**other.mark


s1=Student(50)
s2=Student(6)
print(s1+s2)
s3=s1*s2
print(s3)
print(s1==s2)
print(s1!=s2)
print(s1<s2)
print(s1>s2)
print(s1//s2)
print(s1**s2)
