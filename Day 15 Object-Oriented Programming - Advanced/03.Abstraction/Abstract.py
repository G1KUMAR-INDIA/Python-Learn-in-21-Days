from abc import ABC, abstractmethod

class car (ABC):
    @abstractmethod
    def manifacture(self):
        pass
class user_of_car(car):
    def manifacture(self):
        print('I am the content of manifacture method')
obj=user_of_car()
obj.manifacture()

class manifactureteam:
    def work(self,com):
        com.manifacture()
obj_user=user_of_car()
obj_manf=manifactureteam()
obj_manf.work(obj_user) # Duck typing