# Operator Overloading
class calculator:
    def __init__(self,a,):
        self.a=a
    def __add__(self,other):
        return calculator(self.a+other.a)
obj1=calculator(10)
obj2=calculator(20)
obj3=calculator(30)
obj4=obj1+obj2+obj3
print(obj4.a)