'''
Type Casting
    •   12.1: Convert a string to an integer.
    •   12.2: Convert a float to an integer.
    •   12.3: Convert a list to a set.
    •   12.4: Convert an integer to a string.
'''
# Converting a string to an integer
str1=input("Enter a string:")
int1=int(str1)
print(f"Integer value of {str1} is {int1}")

# Converting a float to an integer
float1=float(input("Enter a float:"))
int2=int(float1)
print(f"Integer value of {float1} is {int2}")

# Converting a list to a set
list1=[1,2,3,4,5]
set1=set(list1)
print(f"Set value of {list1} is {set1}")

# Converting an integer to a string
int1=int(input("Enter an integer:"))
str1=str(int1)
print(f"String value of {int1} is {str1}")