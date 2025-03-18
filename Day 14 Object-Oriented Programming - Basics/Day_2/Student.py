# class student:
#     college="JNTUA"
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         # print("I am in constructor")
#     def display(self):
#         self.pincode=517408
#     # Class level Variable
#     @classmethod
#     def collegedetails(cls):
#         print(student.college)
#         print(f"College name is {cls.college}")
# # obj=student("G1KUMAR",215)
# # instance method
# # obj.display()
# # assigning value outside of a class using object 
# # obj.address="Palamaneru"
# print(student.college)
# print(obj.__dict__)
# # obj2=student()
# # print(obj2.__dict__)

class my_class:
    static_var=0
    x=517408
    def __init__(self):
        my_class.static_var+=1
        self.instance_var=my_class.static_var
    @staticmethod
    def getpincode(x):
        print('The pincode is: ',x)

obj=my_class()
obj.getpincode(my_class.x)
obj2=my_class()
obj2.getpincode(my_class.x)
# obj3=my_class()
# print(obj.instance_var)
# print(obj2.instance_var)
# print(obj3.instance_var)