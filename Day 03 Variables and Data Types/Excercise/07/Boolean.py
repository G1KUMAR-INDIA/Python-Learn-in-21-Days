'''
Boolean
    •   7.1: Write a program to check if a given number is greater than 10 using boolean logic.
    •   7.2: Create a program to check if a given character is a vowel.
'''
# Given number is greater than 10 or not using boolean logic
num=int(input("Enter a number:"))
# converting given number to boolean
result=num>10
print(f"result:{result} for Given num:{num} is greater than 10")

# Checking if a given character is a vowel
char=input("Enter a string:")
vowels="aeiouAEIOU"
if char in vowels:
    print("Given character is belongs to vowels")
else:
    print("Given character is not belongs to vowel.")


