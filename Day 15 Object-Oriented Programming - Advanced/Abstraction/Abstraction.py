# Abstraction
class student:
    def __init__(self,name,phone,pwd):
        self.name=name
        self._phone=phone
        self.__pwd=pwd
    def set_phone(self,phone):
        self._phone=phone
    def get_mob(self,phone):
        return self._phone
    def set_pwd(self,pwd):
        self.__pwd=pwd
    def get_pwd(self):
        return self.__pwd
obj=student('G1Kumar',31313646,'123')
print(obj.name)
print(obj._phone)
# print(obj.get_phone())
# print(obj.get_pwd())