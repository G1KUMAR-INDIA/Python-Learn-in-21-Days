# x=10
# y=x/0
# print(y)

try:
    x=10
    y=x/0
except NameError:
    print("Getting name error")
# except ZeroDivisionError:
#     with open("C:\\Users\\G1KUM\\OneDrive\\Desktop\\Mind2i\\00.Class\\Day 13 Exception Handling\\test.txt","w",'-1') as file:
#         file.write("Zero Divisional Error")
except IndexError:
    with open("C:\\Users\\G1KUM\\OneDrive\\Desktop\\Mind2i\\00.Class\\Day 13 Exception Handling\\test.txt","w",'-1') as file:
        file.write("Index Error")
except:
    print("Getting any error")
else:
    print("No exception")
finally:
    print("Always executed")

print("Example of exception handling")