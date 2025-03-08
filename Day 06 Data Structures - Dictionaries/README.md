Day 6: Data Structures - Dictionaries
 Key-value pairs
 Dictionary methods (keys(), values(), items())

# Data Structures - Dictionaries

Dictionaries are one of the most powerful and commonly used data structures in programming, especially in Python. They store data in a **key-value** format, allowing fast lookups, insertions, and deletions. This makes dictionaries an ideal choice when working with structured and associative data.

## Key-Value Pairs

A **dictionary** consists of key-value pairs, where each key is unique, and each key maps to a specific value. In Python, dictionaries are created using curly braces `{}` or the `dict()` function.

### Example:
```python
# Creating a dictionary
student = {
    "name": "John",
    "age": 22,
    "course": "Computer Science"
}

# Accessing values using keys
print(student["name"])  # Output: John
print(student["age"])   # Output: 22
```

### Important Points:
- **Keys** must be immutable (e.g., strings, numbers, tuples) and unique.
- **Values** can be of any data type.
- Dictionary elements are accessed using keys, not indices like lists.

## Dictionary Methods
Dictionaries come with built-in methods to help with data manipulation and retrieval. Let’s explore some of the most commonly used methods:

### 1. `keys()` - Retrieving All Keys
The `keys()` method returns a view object containing all the keys in the dictionary.

#### Example:
```python
student = {"name": "John", "age": 22, "course": "Computer Science"}
keys_list = student.keys()
print(keys_list)  # Output: dict_keys(['name', 'age', 'course'])
```

### 2. `values()` - Retrieving All Values
The `values()` method returns a view object of all the values stored in the dictionary.

#### Example:
```python
values_list = student.values()
print(values_list)  # Output: dict_values(['John', 22, 'Computer Science'])
```

### 3. `items()` - Retrieving Key-Value Pairs
The `items()` method returns a view object that contains all key-value pairs as tuples.

#### Example:
```python
items_list = student.items()
print(items_list)  # Output: dict_items([('name', 'John'), ('age', 22), ('course', 'Computer Science')])
```

## Why Use Dictionaries?
- **Fast Lookups**: Accessing a value by key is faster than searching in lists.
- **Organized Data**: Ideal for structured and relational data.
- **Flexible Storage**: Supports various data types as values, including lists and other dictionaries.

## Conclusion
Dictionaries are an essential data structure, providing an efficient way to store and retrieve data using key-value pairs. Understanding dictionary methods like `keys()`, `values()`, and `items()` can help you work with data more efficiently in programming. Mastering dictionaries will enable you to write more optimized and readable code!

