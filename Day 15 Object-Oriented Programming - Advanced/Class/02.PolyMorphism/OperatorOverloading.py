# Operator Overloading
class calculator:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return calculator(self.a+other.a)
    def __gt__(self,other):
        if self.a>other.a:
            return True
        else:
            return False
    def __lt__(self,other):
        if self.a<other.a:
            return True
        else:
            return False
obj1=calculator(10)
obj2=calculator(20)
# obj3=calculator(30)
# obj4=obj1+obj2+obj3
obj3=obj1>obj2
obj4=obj1+obj2
obj5=obj1<obj2
print(obj3,obj4.a,obj5)