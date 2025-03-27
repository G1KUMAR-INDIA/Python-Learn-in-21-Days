'''
Lists
    •   8.1: Create a list of your favorite colors.
    •   8.2: Add a new color to the list.
    •   8.3: Remove the first element from the list.
    •   8.4: Access and print the second element of the list.
    •   8.5: Modify the third element of the list.
'''
# creating list of favorite colors
favorite_colors=["red","pink","orange"]
print(f"My favorite_colors:{favorite_colors}")
favorite_colors.append("gray")
print(f"My favorite_colors:{favorite_colors}")



# removing first element from the list
favorite_colors.pop(0)
print(f"My favorite_colors:{favorite_colors}")

# accessing and printing the second element of the list
print(favorite_colors[1])

# modifying the third element of the list
favorite_colors[2]="blue"
print(f"My favorite_colors:{favorite_colors}")

