class father:
    def __init__(self,h):
        self.house=h
    
    def display_father_properties(self):
        print('Father house is :',self.house)
class mother:
    def __init__(self,c):
        self.car=c  

    def display_mother_properties(self):
        print('Mother car is :',self.car)

class child(father,mother):
    def __init__(self,h,c,b):
        self.bike=b
        # super().__init__(h)
        father.__init__(self,h)
        mother.__init__(self,c)
        print('I am in constructor of child')

    def display_child_properties(self):
        print('Child house is :',self.house)
        print('Child car is :',self.car)
        print('Child bike is :',self.bike)

obj=child('Duplex House','Honda City','Splender')
obj.display_father_properties()
obj.display_mother_properties()
obj.display_child_properties()