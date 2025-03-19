# Abstraction
class student:
    def __init__(self,name,phone,pwd):
        self.name=name
        self._phone=phone
        self.__pwd=pwd
    def set_phone(self,phone):
        self._phone=phone
    def get_mob(self):
        return self._phone
    def set_pwd(self,pwd):
        self.__pwd=pwd
    def get_pwd(self):
        return self.__pwd
obj=student('G1Kumar',8501891921,"G1@1234")
print(obj.name)
# print(obj._phone)
# print(obj.__pwd) 
print(obj.get_mob())
print(obj.get_pwd())