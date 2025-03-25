# name="G1KUMAR"

# age=30

# print(f'This is {name} and my age is {age}')

# radius=5
# pi=3.14
# area=pi*radius**2
# f-string method: Latest Method
# print('area of circle with radius:{radius} is: {area:.2f}')
# print(f'area of circle with radius:{radius} is: {area:.2f}')

# format method: 
# print('area of circle with radius:{0} is: {1:.2f}'.format(radius,area))

# name='G1Kumar'
# city="Palamaneru"
# print("My name is {name1} and I live in {city1}".format(name1=name,city1=city))

# print('The cooordinates are ({},{})'.format(10,20))
# print('{1} is older than {0}'.format("Vijay","G1Kumar"))

# % Formatting :Oldest Method
# name="G1Kumar"
# salary=20000
# print("My name is %s and my salary is %d"%(name,salary))

# Taking user input and type casting
# name=input("Enter your name:")
# age=int(input("Enter your age:"))
# print(f'Your name is {name} and your age is {age}')

# Multiple user input
name,age=input("Enter your name and age:").split(",")
print(f'Your name is {name} and your age is {age}')
