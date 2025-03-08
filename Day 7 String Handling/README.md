# Day 7: String Handling
- **Output Formatting,**
- **Taking User Input and type casting ,**
- **Multiple Inputs from users**
- **String operations and methods**
- **String formatting (f-strings, .format())**

### **String Handling in Python**  

String handling in Python is a crucial concept that involves various operations, from formatting output to taking user input and performing different manipulations. Below are some key concepts related to string handling:  

#### **1. Output Formatting**  
Output formatting allows presenting data in a readable and structured manner. The `print()` function provides several ways to format output:  

```python
name = "Jeevan"
age = 30
print("Name:", name, "Age:", age)  # Simple concatenation
print("Name: {} | Age: {}".format(name, age))  # Using .format()
print(f"Name: {name} | Age: {age}")  # Using f-strings
```

#### **2. Taking User Input and Type Casting**  
Python allows users to take input via the `input()` function. Since `input()` always returns a string, type casting is required when dealing with numeric values.  

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Type casting from string to integer
print(f"Hello {name}, you are {age} years old.")
```

#### **3. Multiple Inputs from Users**  
Users can input multiple values at once using the `split()` method.  

```python
name, age, city = input("Enter your name, age, and city (separated by spaces): ").split()
age = int(age)  # Type casting
print(f"Name: {name}, Age: {age}, City: {city}")
```

#### **4. String Operations and Methods**  
Python provides several string operations and built-in methods for manipulation:  

```python
text = "  Hello, Python!  "
print(text.lower())      # Convert to lowercase
print(text.upper())      # Convert to uppercase
print(text.strip())      # Remove leading and trailing spaces
print(text.replace("Python", "World"))  # Replace substring
print(len(text))         # Find length of string
print(text.split(","))   # Split string into a list
print(text.startswith("Hello"))  # Check if string starts with a specific word
print(text.endswith("!"))  # Check if string ends with a specific character
```

#### **5. String Formatting (f-strings, .format())**  
Python provides multiple ways to format strings efficiently:  

```python
name = "Jeevan"
age = 30

# Using .format() method
print("My name is {} and I am {} years old.".format(name, age))

# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")
```

String handling is essential in Python programming, enabling efficient input handling, formatting, and manipulation of text-based data.