class my_class:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
obj=my_class(10,20) # object creation
result_add=obj.addition() # Calling the method using object
result_sub=obj.subtraction()
result_mul=obj.multiplication()
result_div=obj.division()
print('Result of addition',result_add)
print('Result of subtraction',result_sub)
print('Result of multiplication',result_mul)
print('Result of division',result_div)