class Math:
    def __init__(self,num):
        self._num=num
    def sub(self,a,b):
        return a-b
    @staticmethod
    def add(a,b):
        return a+b

m=Math(5)
print(m._num)

print(m.sub(5,2))
print(Math.add(10,90))