'''
Numbers
    •   6.1: Perform addition, subtraction, multiplication, and division operations on two numbers.
    •   6.2: Calculate the square root of a given number using the math module.
    •   6.3: Convert a float to an integer and vice versa.
'''
import math
a=float(input("Enter First Number: "))
b=float(input("Enter Second Number: "))
print("Addition of a and b: ",a+b)
print("Subtract b from a: ",a-b)
print("Multiplication of a and b: ",a*b)
print("Division of a by b: ", a/b if b!=0 else "Undefined (division by zero)")
print("Floor Division of a by b: ", a//b if b!=0 else "Undefined (division by zero)")
print("Modulus of a and b: ",a%b if b != 0 else "Undefined (modulo by zero)")
print("Exponentiation of a of b: ",a**b)
print("Square root of a: ",math.sqrt(a))
print("Absolute value of a: ",abs(a))
print("Floor of a: ",math.floor(a))
print("Ceiling of a: ",math.ceil(a))
print("Round of a: ",round(a))
print("Round of a with 2 decimal places: ",round(a,2))

