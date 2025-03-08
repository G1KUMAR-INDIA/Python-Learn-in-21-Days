# Day 4: Data Structures - Lists
- **Introduction to lists**
- **Common list methods (append(), remove(), pop(), slicing,insert(),extend())**

# Data Structures - Lists

## Introduction to Lists

A **list** is one of the most commonly used data structures in Python. It is an ordered, mutable collection that can hold elements of different data types. Lists are dynamic, meaning they can grow or shrink as needed, and they support various operations such as adding, removing, and modifying elements.

### Characteristics of Lists:
- Ordered collection (elements maintain their insertion order)
- Mutable (can be changed after creation)
- Allows duplicate values
- Can store different data types
- Indexed (supports positive and negative indexing)

Lists are defined using square brackets `[]`, and elements are separated by commas.

#### Example of a List:
```python
my_list = [1, 2, 3, "apple", "banana", 4.5]
print(my_list)  # Output: [1, 2, 3, 'apple', 'banana', 4.5]
```

---

## Common List Methods

Python provides several built-in methods to manipulate lists efficiently. Here are some of the most commonly used methods:

### 1. `append()` – Adding Elements to a List
The `append()` method adds an element to the end of the list.

#### Example:
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

---

### 2. `remove()` – Removing an Element
The `remove()` method removes the first occurrence of a specified element in the list.

#### Example:
```python
numbers = [1, 2, 3, 4, 2]
numbers.remove(2)
print(numbers)  # Output: [1, 3, 4, 2]
```

---

### 3. `pop()` – Removing an Element by Index
The `pop()` method removes an element at a given index and returns the removed value. If no index is specified, it removes the last element.

#### Example:
```python
colors = ["red", "blue", "green"]
removed_color = colors.pop(1)
print(colors)  # Output: ['red', 'green']
print(removed_color)  # Output: 'blue'
```

---

### 4. Slicing – Accessing a Portion of the List
List slicing allows extracting a part of the list using the `start:stop:step` syntax.

#### Example:
```python
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3]
print(numbers[:3])   # Output: [0, 1, 2]
print(numbers[::2])  # Output: [0, 2, 4, 6]
```

---

### 5. `insert()` – Inserting an Element at a Specific Position
The `insert()` method adds an element at a specified index.

#### Example:
```python
languages = ["Python", "Java", "C++"]
languages.insert(1, "JavaScript")
print(languages)  # Output: ['Python', 'JavaScript', 'Java', 'C++']
```

---

### 6. `extend()` – Extending a List with Another List
The `extend()` method adds elements from another iterable (e.g., list, tuple) to the end of the list.

#### Example:
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]
```

---

## Conclusion
Lists are a fundamental data structure in Python, providing flexibility and ease of manipulation. With built-in methods like `append()`, `remove()`, `pop()`, `insert()`, `extend()`, and slicing, Python lists offer powerful ways to store and manage collections of data efficiently. Understanding these methods is essential for working with data structures effectively in Python programming.

