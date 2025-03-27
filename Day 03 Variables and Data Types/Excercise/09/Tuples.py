'''
Tuples
    •   9.1: Create a tuple of your favorite fruits.
    •   9.2: Try to modify an element within the tuple and observe the error.
    •   9.3: Access the last element of the tuple.
'''

# creating tuple of favorite fruits
favorite_fruits=("apple","banana","orange")
print(f"My favorite_fruits:{favorite_fruits}")
# trying to modify an element within the tuple
# favorite_fruits[0]="mango" # this will throw an error
# (TypeError: 'tuple' object does not support item assignment)
# accessing the last element of the tuple
print(favorite_fruits[-1])