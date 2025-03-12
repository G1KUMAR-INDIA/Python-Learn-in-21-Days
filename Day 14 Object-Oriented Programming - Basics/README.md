# Day 14: Object-Oriented Programming - Basics
- **Classes and objects**
- **Instance variables and methods**

# Object-Oriented Programming (OOP) - Basics

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, making it more modular, reusable, and easier to manage. It revolves around the concept of classes and objects, allowing developers to structure their programs efficiently. This blog explores the fundamental concepts of OOP, focusing on classes, objects, instance variables, and methods.

## 1. Classes and Objects
### What is a Class?
A **class** is a blueprint or template for creating objects. It defines the properties (variables) and behaviors (methods) that the objects instantiated from it will have. In simple terms, a class is a logical structure that describes the attributes and actions of real-world entities.

### What is an Object?
An **object** is an instance of a class. It is a concrete entity that holds data (attributes) and can perform actions (methods) defined in the class. Each object can have different attribute values while sharing the same structure and behavior as defined by the class.

### Example of Class and Object in Python:
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable
        self.year = year    # Instance variable
    
    def display_info(self):  # Instance method
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Creating objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

# Accessing methods
car1.display_info()  # Output: Car: Toyota Camry, Year: 2022
car2.display_info()  # Output: Car: Honda Civic, Year: 2021
```

## 2. Instance Variables and Methods
### Instance Variables
**Instance variables** are attributes that store object-specific data. They are defined inside the constructor (`__init__` method in Python) and are unique to each instance of the class. Each object can have different values for these variables.

### Instance Methods
**Instance methods** are functions defined inside a class that operate on instance variables. These methods have access to the instance (via `self`) and can modify or retrieve object-specific data.

### Example Demonstrating Instance Variables and Methods:
```python
class Student:
    # Constructor
    def __init__(self, name, age, grade):
        # Instance Variables
        self.name = name  # Instance variable
        self.age = age    # Instance variable
        self.grade = grade  # Instance variable
    # Instance methods
    def introduce(self):  # Instance method
        print(f"Hello, my name is {self.name}. I am {self.age} years old and in grade {self.grade}.")

# Creating objects
student1 = Student("Alice", 14, 9)
student2 = Student("Bob", 15, 10)

# Calling instance methods
student1.introduce()  # Output: Hello, my name is Alice. I am 14 years old and in grade 9.
student2.introduce()  # Output: Hello, my name is Bob. I am 15 years old and in grade 10.
```

### Key Takeaways:
- **Classes** define the structure and behavior of objects.
- **Objects** are instances of classes with specific attribute values.
- **Instance variables** store data unique to each object.
- **Instance methods** operate on instance variables and define object behaviors.

By understanding these fundamental OOP concepts, developers can create more organized, modular, and scalable applications. Stay tuned for more in-depth discussions on advanced OOP principles such as inheritance, polymorphism, encapsulation, and abstraction!

