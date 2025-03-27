# Create a variable to store a number. Check if the number is even or odd.
number = int(input("Enter a number: "))
if number>0:
    if number %2==0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
else:
    print("Error: Invalid input! Please enter a valid number.")        