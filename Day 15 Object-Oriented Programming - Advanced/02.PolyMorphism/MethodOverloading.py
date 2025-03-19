# Handling one parameter
# class student:
#     def student_details(self,name="Ram"):
#         print(f"Student name is :{name}!")
# obj=student()
# obj.student_details()

# Handling Multiple Parameters
# class student:
#     def student_details(self,*names):
#         for name in names:
#             print(f"Student name is :{name}!")
#         # print(f"Student name is :{name}!")
# obj=student()
# obj.student_details('G1Kumar','G2Kumar','G3Kumar')

# Handling type checking
class student:
    def student_details(self,name):
        if isinstance(name,str):
            print(f"Student name is :{name}!")
        elif isinstance(name,list):
            for n in name:
                print(f"Student name is :{n}!")
        else:
            print("Hello,He is not a student.")

obj=student()
obj.student_details("Ram")
obj.student_details(["G1Kumar","G2Kumar","G3Kumar"])
obj.student_details(215)