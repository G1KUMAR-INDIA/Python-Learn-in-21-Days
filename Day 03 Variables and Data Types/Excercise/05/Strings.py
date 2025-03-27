'''
Strings
    •   5.1: Create a string variable and use the .upper() and .lower() methods.
    •   5.2: Extract a substring from a given string.
    •   5.3: Count the number of occurrences of a specific character in a string.
    •   5.4: Replace a substring within a string with another string.
    •   5.5: Check if a string starts or ends with a specific substring.
'''

# 5.1: Create a string variable and use the .upper() and .lower() methods.
my_string = "Hello, World!"
upper_string = my_string.upper()
lower_string = my_string.lower()
print("Original String:", my_string)
print("Uppercase String:", upper_string)
print("Lowercase String:", lower_string)

# 5.2: Extract a substring from a given string.
my_string = "Hello, World!"
substring = my_string[7:12]
print("Substring:", substring)

# 5.3: Count the number of occurrences of a specific character in a string.
my_string = "Hello, World!"
count = my_string.count("l")
print("Number of 'l' characters:", count)

# 5.4: Replace a substring within a string with another string.
my_string = "Hello, World!"
replaced_string = my_string.replace("World", "Universe")
print("Replaced String:", replaced_string)

# 5.5: Check if a string starts or ends with a specific substring.
my_string = "Hello, World!"
starts_with = my_string.startswith("Hello")
ends_with = my_string.endswith("World!")
print("Starts with 'Hello':", starts_with)
print("Ends with 'World!':", ends_with)

# data=dir(int)+dir(float)+dir(str)
# # print(data)
# with open("data.txt","a") as f:
#     f.write(str(data))
#     print("Data written to file")
