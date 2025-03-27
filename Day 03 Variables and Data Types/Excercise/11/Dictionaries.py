'''
Dictionaries
    •   11.1: Create a dictionary to store the names and ages of three people.
    •   11.2: Access and print the age of one of the people.
    •   11.3: Add a new key-value pair to the dictionary.
    •   11.4: Update the age of one of the people in the dictionary.
'''

# Creating a dictionary to store the names and ages of three people
person={"person1":{"name": "R JEEVAN KUMAR", "age": 30},
"person2":{"name": "T KRISHNA", "age": 30},
"person3":{"name": "K RAJA", "age": 30}
}

# Accessing and printing the age of one of the people
print(f"Age of Person 1 is {person["person1"]["age"]}")

# Adding a new key-value pair to the dictionary
person["person4"]={"name":"R VIJAY KUMAR","age":28}
print(person)

# Upadting the age of one of the people in the dictionary
person["person2"]["age"]=33
print(person)
