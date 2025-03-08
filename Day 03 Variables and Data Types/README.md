# Day 3: Variables and Data Types :
 - **Variables, keywords, Indentation, Comments**
 - **String, Numbers, Boolean, List, Tuples**
 - **Sets, Dictionary, Arrays.**

# Python Variables and Data Types

Python is one of the most popular programming languages due to its simplicity and versatility. Understanding variables and data types is fundamental to mastering Python. This blog will cover the basics of Python variables, keywords, indentation, comments, and its core data types like strings, numbers, booleans, lists, tuples, sets, dictionaries, and arrays.

## 1. Variables, Keywords, Indentation, and Comments

### Variables
A variable in Python is a symbolic name assigned to a value. Unlike statically typed languages, Python allows dynamic typing, meaning you don't need to declare the data type explicitly.

```python
a=10
# Everything in Python is an object
# Identifier is a, value is 10, type is Integer
a="Python"
# Identifier is a, value is"Python" and type is String.
a=1.2
# Identifier is a, value is 1.2 and type is Float.
# Variable Name should not start with Number
# Variable Name should not start with keywords
# Variable can start with alphabets and '_'
```

```python
name = "John"  # String variable
age = 25       # Integer variable
price = 99.99  # Float variable
is_active = True  # Boolean variable
```

### Keywords
Keywords are reserved words in Python that cannot be used as variable names. Some common Python keywords include `if`, `else`, `while`, `for`, `import`, `def`, `return`, etc.

To see all Python keywords, use:

```python
import keyword
print(keyword.kwlist)
```

### Indentation
Python uses indentation (whitespace) to define blocks of code instead of braces `{}` as in other languages. Proper indentation is necessary for the code to run correctly.

```python
def addition:
    a=10
    b=20
    c=a+b
    print("Addition of a and b",c)
addition()
```

```python
if age > 18:
    print("You are an adult.")  # Indented correctly
```

### Comments
Comments are used to make code more readable and are ignored by the Python interpreter.

- **Single-line comment:**
  ```python
  # This is a single-line comment
  ```

- **Multi-line comment:**
  ```python
  """
  This is a multi-line comment.
  It spans multiple lines.
  """
  ```

## 2. Python Data Types
- **Numerical, Sequential, Mapping, Boolean, Binary and None Type Data Types**
- **Numerical Data Types are Integer, Float and Complex**
- **Sequential Data Types are String, list, tuple and range**
- **Python provides several built-in data types. Let's explore them.**

### String

A **string** is a sequence of characters enclosed in single or double quotes.

```python
text = "Hello, Python!"
print(type(text))
print(text[0])  # Output: H
print(text[-1])  # Negative Indexing:!
print(text[0:5])  # Output: Hello
print(len(text))  # Output: 13

Str="Python Training Session"
print(dir(Str))
# print(Str[Starting_Index:Ending_Index+1])
print(Str[7:]) # or print(Str[7:Ending Index])
print(Str[0:15]) # or print(Str[:15])
print(Str.capitalize())
print(Str.count('s'))
```

### Numbers
Python supports different numerical data types:
- **Integer (`int`)**: Whole numbers.
- **Float (`float`)**: Decimal numbers.
- **Complex (`complex`)**: Numbers with real and imaginary parts.

```python
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex
print(type(x),type(y),type(z))
```

### Boolean
Boolean values represent `True` or `False`, often used in conditions.

```python
is_python_fun = True
print(type(is_python_fun))  # Output: <class 'bool'>
```

### List
A **list** is an ordered, mutable collection of elements.

```python
List1=[1,2,3,4,5.6,'how are you',True]
print(List1)
print(List1[5])
print(List1[6])
List[6]=False
print(List1[6])
print(List1[0:3])
print(5.6 in List1)
print(8.1 not in List1)
lst1=[1,2,3]
lst2=[4,5,6]
lst3=lst1+lst+2
print(lst3)
print(lst1)
print(lst1*3)
print(dir(lst1))
print(lst1)
print(lst1.append(8.9))
print(lst1.count(1))
print(lst1.insert(3,4))
```

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana
fruits.append("mango")  # Adds an item
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'mango']
```

### Tuple
A **tuple** is an ordered, immutable collection of elements.

```python
dimensions = (200, 50)
print(dimensions[0])  # Output: 200
```

## 3. Sets, Dictionary, and Arrays

### Set
A **set** is an unordered collection of unique elements.
Indicated by {}

```python
basket={'apple','banana','orange','mango','mango','mango','mango'}
print(basket)
a=set()
a.add(1)
a.add(2)
print(a)
b={}
print(type(a),type(b))
#  frozen set
fs=frozenset(a)
print(fs)
# fs.add(1)
print(type(fs))

print(3 in a)
print(3 not in a)
x={'a','b','c'}
y={'a','g','h'}
print(x|y)
print(x&y)
print(x-y)

unique_numbers = {1, 2, 3, 3, 4, 5}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
```

### Dictionary
A **dictionary** is an unordered collection of key-value pairs.
It is Mutable
It is not Index based and it is key and value based
Dic={'key':'value'}


```python
country={'IND':'India','PAK':'Pakisthan','AUS':'Australia'}
print(country['IND'])
country['IND']='Bharat'
print(country['IND'])
del country['PAK']
print(country)
country.clear()
print(country)
del country
print(country)

person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])  # Output: John
```

### Arrays
Python does not have built-in support for arrays like other languages, but we can use the `list` data type or the `array` module.

Using the `array` module:
```python
import array as arr
numbers = arr.array('i', [1, 2, 3, 4])
print(numbers[0])  # Output: 1
```

## Conclusion
Understanding Python variables and data types is crucial for writing efficient programs. Whether working with strings, numbers, lists, tuples, sets, or dictionaries, each data type has its unique characteristics and use cases. Mastering these concepts will help you write better Python code!


