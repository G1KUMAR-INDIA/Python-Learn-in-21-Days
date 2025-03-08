# Day 10 : Functions
- **Defining functions**
- **Function arguments and return values**
- **Default and keyword arguments**

# Functions in Python

Functions are an essential part of Python programming that help in organizing code, making it reusable, and improving readability. In this blog, we will explore how to define functions, work with function arguments and return values, and use default and keyword arguments effectively.

## Defining Functions

A function in Python is defined using the `def` keyword, followed by the function name and parentheses containing optional parameters. A function body is indented and contains the logic to be executed when the function is called.

### Syntax:
```python
def function_name(parameters):
    """Optional docstring to describe the function."""
    # Function body
    return result  # Optional return statement
```

### Example:
```python
def greet():
    print("Hello, Welcome to Python Functions!")

# Calling the function
greet()
```

### Output:
```
Hello, Welcome to Python Functions!
```

## Function Arguments and Return Values

Functions can take inputs (arguments) and return results using the `return` statement.

### Example:
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("Sum:", result)
```

### Output:
```
Sum: 15
```

Here, `add_numbers(5, 10)` passes two arguments to the function, which returns their sum.

## Default and Keyword Arguments

Python allows functions to have default values for parameters. If an argument is not provided, the default value is used.

### Example of Default Arguments:
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Passing an argument
greet()  # Using default argument
```

### Output:
```
Hello, Alice!
Hello, Guest!
```

### Example of Keyword Arguments:
Keyword arguments allow passing values using parameter names, making the function calls more readable.

```python
def person_info(name, age):
    print(f"Name: {name}, Age: {age}")

person_info(age=25, name="Bob")  # Order doesn't matter
```

### Output:
```
Name: Bob, Age: 25
```

### Combining Positional and Keyword Arguments:
```python
def employee_details(id, name, department="IT"):
    print(f"ID: {id}, Name: {name}, Department: {department}")

employee_details(101, "John")  # Uses default department
employee_details(102, "Emma", department="HR")  # Overriding default
```

### Output:
```
ID: 101, Name: John, Department: IT
ID: 102, Name: Emma, Department: HR
```

## Conclusion

Functions in Python enhance code reusability, modularity, and readability. By understanding function definitions, arguments, return values, and default/keyword arguments, you can write more efficient and flexible Python programs. Start experimenting with functions to see their power in action!

