class grand_parent:
    def __init__(self,h):
        self.house=h
        print('I am in constructor of grand parent') 
    def display_GP_properties(self):
        print('Grand Parent house is :',self.house)

class parent(grand_parent):
    def __init__(self,h,c):
        self.car=c
        super().__init__(h)
        print('I am in constructor of parent')
    def display_Parent_properties(self):
        print('Parent house is :',self.house)
        print('Parent car is :',self.car)
class child(parent):
    def __init__(self,h,c,b):
        self.bike=b
        super().__init__(h,c)
        print('I am in constructor of child')
    def display_Child_properties(self):
        print('Child house is :',self.house)
        print('Child car is :',self.car)
        print('Child bike is :',self.bike)
# obj=parent('Duplex House','BMW')
obj=child('Duplex House','BMW','Royal Enfield')
obj.display_GP_properties()
obj.display_Parent_properties()
obj.display_Child_properties()