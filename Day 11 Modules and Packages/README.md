# Day 11: Modules and Packages
- **Importing modules**
- **Creating custom modules**
- **Using Python libraries (e.g., math, random)**

# Modules and Packages in Python

Python is a powerful and versatile programming language that provides a modular approach to code organization. **Modules and packages** allow developers to structure their code efficiently, making it more readable, reusable, and maintainable.

## 1. Understanding Python Modules
A **module** in Python is simply a file containing Python code (functions, classes, or variables) that can be reused across different programs.

### Importing Modules
Python provides the `import` statement to bring functionality from one module into another. There are multiple ways to import modules:

#### 1.1 Importing an Entire Module
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

#### 1.2 Importing Specific Functions from a Module
```python
from math import sqrt, pi
print(sqrt(25))  # Output: 5.0
print(pi)        # Output: 3.141592653589793
```

#### 1.3 Importing a Module with an Alias
```python
import random as rnd
print(rnd.randint(1, 10))  # Generates a random number between 1 and 10
```

#### 1.4 Importing All Functions from a Module (Not Recommended)
```python
from math import *
print(sin(0))  # Output: 0.0
```
> *Note: Using `from module import *` can lead to namespace conflicts and is generally discouraged.*

---

## 2. Creating Custom Modules
You can create your own Python module by saving Python code in a `.py` file.

### Example: Creating a Simple Module
1. Create a file named `mymodule.py` with the following content:
```python
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
```

2. Import and use this module in another script:
```python
import mymodule
print(mymodule.greet("Jeevan"))  # Output: Hello, Jeevan!
print(mymodule.add(5, 3))        # Output: 8
```

Alternatively, you can import specific functions:
```python
from mymodule import greet
print(greet("Kumar"))  # Output: Hello, Kumar!
```

---

## 3. Using Built-in Python Libraries
Python provides numerous built-in modules to perform various operations efficiently. Let's explore two commonly used modules: `math` and `random`.

### 3.1 The `math` Module
The `math` module provides mathematical functions.
```python
import math
print(math.factorial(5))  # Output: 120
print(math.pow(2, 3))     # Output: 8.0
```

### 3.2 The `random` Module
The `random` module helps in generating random numbers.
```python
import random
print(random.randint(1, 100))  # Generates a random integer between 1 and 100
print(random.choice(["apple", "banana", "cherry"]))  # Randomly selects an item
```

---

## Conclusion
Modules and packages are essential in Python for writing modular, reusable, and maintainable code. Understanding how to import modules, create custom modules, and utilize built-in Python libraries helps in building efficient applications.

> *Start leveraging Python modules and packages today to enhance your programming efficiency!*

