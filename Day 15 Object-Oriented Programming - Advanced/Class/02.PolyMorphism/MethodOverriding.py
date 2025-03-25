# Method Overriding
class A:
    def show(self):
        print('I am in class A show')
class B(A):
    pass
    def show(self):
        print('I am in class B show')
obj=B()
obj.show()