class parent:
    def __init__(self,h,c):
        self.house=h
        self.car=c
    def display_Parent_properties(self):
        print('Parent house is :',self.house)
        print('Parent car is :',self.car)
class child_1(parent):
    def __init__(self,h,c):
        super().__init__(h,c)
        print('I am in constructor of child 1')
    def display_child_1_properties(self):
        print('Child 1 house is :',self.house)
class child_2(parent):
    def __init__(self,h,c):
        super().__init__(h,c)
        print('I am in constructor of child 2')
    def display_child_2_properties(self):
        print('Child 2 car is :',self.car)
obj=child_1('Duplex House','BMW')
obj.display_Parent_properties()
obj.display_child_1_properties()
obj=child_2('Duplex House','BMW')
obj.display_Parent_properties()
obj.display_child_2_properties()
