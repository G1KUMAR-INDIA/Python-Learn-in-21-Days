'''
Sets
    •   10.1: Create a set of integers.
    •   10.2: Add a new element to the set.
    •   10.3: Check if a given number is present in the set.
    •   10.4: Create two sets and perform union and intersection operations.
'''
# Creating set of Integers
set1={1,2,3,4,5}
print(f"Set1:{set1}")

# Adding new element to the set
set1.add(6)
print(f"Set1:{set1}")

# Checking if a given number is present in the set
num=int(input("Enter a number:"))
if num in set1:
    print(f"{num} is present in set1")
else:
    print(f"{num} is not present in set1")

# Creating two sets and performing union and intersection operations
set2={3,4,5,6,7}
print(f"set1 Union set2:{set1.union(set2)}")    
print(f"set1 Intersection set2:{set1.intersection(set2)}")