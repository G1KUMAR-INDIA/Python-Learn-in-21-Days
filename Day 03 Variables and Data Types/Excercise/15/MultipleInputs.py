'''
Multiple Inputs
    •   15.1: Take three numbers as input from the user in a single line and calculate their average.
'''

# Take three numbers as input from the user in a single line and calculate their average
num1, num2, num3 = map(float, input("Enter three numbers separated by spaces: ").split())
average = (num1 + num2 + num3) / 3
print(f"The average of {num1}, {num2}, and {num3} is: {average}")