# Day 13: Exception Handling
- **try, except, finally
- **Handling multiple exceptions
- **Raising exceptions

# Exception Handling in Python

Exception handling is a crucial concept in Python that allows developers to manage and respond to runtime errors gracefully. Without proper exception handling, a program may crash unexpectedly, leading to poor user experience. In this blog, we will explore exception handling in Python with key concepts including `try`, `except`, `finally`, handling multiple exceptions, and raising exceptions.

## 1. Understanding `try`, `except`, and `finally`

In Python, exceptions are handled using `try` and `except` blocks. The `try` block contains the code that may raise an exception, while the `except` block handles the error.

### Basic Example:
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
finally:
    print("Execution completed.")
```
### Explanation:
- **`try` block**: Contains the code that might raise an exception.
- **`except` block**: Catches and handles specific exceptions.
- **`finally` block**: This block executes regardless of whether an exception occurs or not. It is useful for resource cleanup.

## 2. Handling Multiple Exceptions

Sometimes, multiple types of exceptions can occur in a program. We can handle them by specifying multiple `except` blocks or using a tuple to catch multiple exceptions in a single block.

### Example:
```python
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except (ZeroDivisionError, ValueError) as e:
    print("An error occurred:", e)
except Exception as e:
    print("Unexpected error:", e)
```
### Explanation:
- We use multiple `except` blocks to handle different types of exceptions separately.
- The `(ZeroDivisionError, ValueError)` tuple in one `except` block allows handling multiple exceptions together.
- The generic `Exception` block catches any other unexpected errors.

## 3. Raising Exceptions

Sometimes, we may want to raise exceptions manually using the `raise` keyword. This is useful when we need to enforce certain conditions in our program.

### Example:
```python
def validate_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    return "Access granted."

try:
    user_age = int(input("Enter your age: "))
    print(validate_age(user_age))
except ValueError as e:
    print("Error:", e)
```
### Explanation:
- The function `validate_age()` checks if the age is below 18.
- If the condition is met, it raises a `ValueError` with a custom message.
- The `try-except` block catches the error and displays the message.

## Conclusion

Exception handling in Python is essential for writing robust and error-free programs. By using `try`, `except`, and `finally`, we can prevent crashes and handle errors effectively. Handling multiple exceptions and raising custom exceptions further enhances the flexibility of our code.

Understanding and implementing exception handling will help you build reliable and user-friendly applications. Happy coding!

