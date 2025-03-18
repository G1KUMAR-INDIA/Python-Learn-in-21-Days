# Day 15: Object-Oriented Programming - Advanced
- **Inheritance**
- **Polymorphism**
- **Encapsulation**
- **Static Variables, Static Method**

# Understanding Object-Oriented Programming: Advanced Concepts

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data in the form of fields (often referred to as attributes or properties) and methods (functions or procedures). As we move beyond the basics, OOP introduces advanced concepts that take programming to the next level. In this blog, we will explore four advanced OOP concepts: **Inheritance**, **Polymorphism**, **Encapsulation**, and **Static Variables/Methods**. These concepts are essential to building flexible, scalable, and maintainable applications.

### 1. Inheritance: The Power of Reusability

**Inheritance** is one of the fundamental concepts in OOP, allowing you to create new classes based on existing ones. The class that inherits the properties and behaviors is called the **subclass** (or derived class), and the class it inherits from is called the **superclass** (or base class).

#### How Inheritance Works:
- The **subclass** inherits the attributes and methods of the **superclass**.
- The **subclass** can also add its own unique attributes and methods.
- It can override the superclass's methods to modify or enhance their behavior.

#### Example:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Creating an object of Dog
dog = Dog()
dog.speak()  # Output: Dog barks
```

**Benefits of Inheritance:**
- Code Reusability: You don’t need to rewrite code for common functionalities in multiple classes.
- Extensibility: Allows you to extend or modify the behavior of existing code.

### 2. Polymorphism: One Interface, Many Implementations

**Polymorphism** means "many forms," and in the context of OOP, it allows different objects to respond to the same method call in different ways. The two most common types of polymorphism are:

- **Method Overloading**: Defining multiple methods with the same name but different parameters.
- **Method Overriding**: Subclasses provide their specific implementation of a method already defined in the superclass.

#### How Polymorphism Works:
- The same method name can behave differently depending on the object that calls it.
- This concept is especially useful for handling different data types and structures with a single interface.

#### Example:
```python
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

# Creating objects of Circle and Square
circle = Circle()
square = Square()

# Demonstrating polymorphism
shapes = [circle, square]
for shape in shapes:
    shape.draw()
```

**Benefits of Polymorphism:**
- Flexibility: Allows you to implement methods that can handle different objects in a uniform way.
- Maintenance: Changes in the codebase only need to be made once in the superclass, and they propagate to all subclasses.

### 3. Encapsulation: Protecting Data

**Encapsulation** refers to the concept of bundling the data (attributes) and methods that operate on the data into a single unit or class. It also involves controlling access to the data by using **access modifiers** to restrict direct access to some of an object's components. This helps in preventing unintended interference and misuse of the data.

#### Key Concepts in Encapsulation:
- **Private Attributes**: These are data members that cannot be accessed directly from outside the class.
- **Public Methods**: These provide controlled access to the private attributes, typically in the form of getter and setter methods.

#### Example:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance  # public method to access private attribute

# Creating an object
account = BankAccount("John", 5000)
account.deposit(1000)
print(account.get_balance())  # Output: 6000
```

**Benefits of Encapsulation:**
- Data Security: It restricts direct access to sensitive information and ensures it’s only modified in controlled ways.
- Code Maintenance: Encapsulation allows you to make changes to the internal workings of a class without affecting other parts of the program.

### 4. Static Variables and Static Methods: Class-Level Attributes and Functions

In object-oriented programming, **static variables** and **static methods** belong to the class itself rather than any individual instance of the class. They are shared across all instances of the class and can be accessed without creating an object.

- **Static Variables**: These are variables that are declared as `static` within a class and are shared among all objects of that class.
- **Static Methods**: These are methods that are bound to the class, not objects. They can be called on the class itself without needing an instance.

#### Example:
```python
class Counter:
    count = 0  # static variable

    def __init__(self):
        Counter.count += 1

    @staticmethod
    def get_count():
        return Counter.count  # static method accessing static variable

# Creating objects of Counter
c1 = Counter()
c2 = Counter()

# Accessing static method
print(Counter.get_count())  # Output: 2
```

**Benefits of Static Variables and Methods:**
- Memory Efficiency: Since static variables are shared across all instances, they help conserve memory.
- Utility Functions: Static methods are useful for utility functions that don’t need to modify or access instance-specific data.

---

### Conclusion

In this blog, we’ve covered some of the most important advanced concepts in Object-Oriented Programming: **Inheritance**, **Polymorphism**, **Encapsulation**, and **Static Variables/Methods**. Mastering these concepts is essential for writing clean, efficient, and maintainable code that scales well as your applications grow. Each concept builds on the others, enabling you to design software in a way that is modular, reusable, and adaptable to change.

By leveraging the power of OOP, developers can create robust and flexible systems that are easier to maintain and extend over time. Whether you're building simple applications or large-scale enterprise solutions, understanding and applying these advanced OOP principles will significantly improve your development process.
