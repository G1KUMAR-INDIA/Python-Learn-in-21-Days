# Day 16: Working with JSON
- **Reading and writing JSON files**
- **JSON serialization and deserialization**

# Working with JSON in Python

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy to read and write for humans and machines. It's widely used for data exchange between servers and web applications, and it's also easy to work with in Python. Python provides a built-in `json` module that makes it simple to parse and manipulate JSON data. In this blog, we'll explore how to read, write, serialize, and deserialize JSON in Python.

## Table of Contents
1. [Reading JSON Files](#reading-json-files)
2. [Writing JSON to Files](#writing-json-to-files)
3. [JSON Serialization and Deserialization](#json-serialization-and-deserialization)

---

## Reading JSON Files

To work with JSON data in Python, the first step is to read the JSON file into Python's data structures. You can use the `json.load()` function for this task. This function takes a file object as an argument and returns the JSON data as a Python dictionary or list, depending on the structure of the JSON.

### Example: Reading JSON from a File
Suppose you have a file named `data.json` with the following content:

```json
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

You can read this JSON file and load it into a Python dictionary as follows:

```python
import json

# Open the JSON file for reading
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the content as a Python dictionary
print(data)
```

**Output:**

```python
{'name': 'John', 'age': 30, 'city': 'New York'}
```

In this example, we opened the file using Python's `open()` function and then used `json.load()` to parse the JSON data. The content is returned as a Python dictionary.

---

## Writing JSON to Files

Writing JSON data to a file is equally simple. You can use the `json.dump()` function, which serializes a Python object and writes it to a file.

### Example: Writing JSON to a File

Let's assume we have a Python dictionary and want to write it to a file:

```python
import json

# Sample data to write
data = {
    "name": "Jane",
    "age": 25,
    "city": "San Francisco"
}

# Open a file for writing and use json.dump() to serialize and write the data
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data written to output.json")
```

This will create a new file named `output.json` with the following content:

```json
{
    "name": "Jane",
    "age": 25,
    "city": "San Francisco"
}
```

The `indent` parameter in `json.dump()` helps format the JSON data to be more human-readable by adding indentation.

---

## JSON Serialization and Deserialization

### Serialization

Serialization is the process of converting a Python object into a JSON string. Python provides the `json.dumps()` method to serialize a Python object to a JSON formatted string.

### Example: Serializing Python Object to JSON String

```python
import json

# Sample Python dictionary
data = {
    "name": "Alice",
    "age": 28,
    "city": "Los Angeles"
}

# Serialize Python dictionary to JSON string
json_string = json.dumps(data)

# Print the JSON string
print(json_string)
```

**Output:**

```json
{"name": "Alice", "age": 28, "city": "Los Angeles"}
```

The `json.dumps()` method converts the Python dictionary into a JSON string. You can pass additional parameters, such as `indent`, to make the output more readable:

```python
json_string = json.dumps(data, indent=4)
print(json_string)
```

**Output:**

```json
{
    "name": "Alice",
    "age": 28,
    "city": "Los Angeles"
}
```

### Deserialization

Deserialization is the opposite of serialization—it's the process of converting a JSON string into a Python object. The `json.loads()` method is used for this purpose.

### Example: Deserializing JSON String to Python Object

```python
import json

# JSON string
json_string = '{"name": "Bob", "age": 35, "city": "Chicago"}'

# Deserialize JSON string to Python dictionary
data = json.loads(json_string)

# Print the Python dictionary
print(data)
```

**Output:**

```python
{'name': 'Bob', 'age': 35, 'city': 'Chicago'}
```

The `json.loads()` method converts the JSON string back into a Python dictionary.

---

## Practical Example: Combining Reading, Writing, Serialization, and Deserialization

Let's combine the concepts discussed and create a complete flow that reads a JSON file, serializes the data, and then writes it to a new file.

```python
import json

# Step 1: Read JSON from file
with open('input.json', 'r') as file:
    data = json.load(file)

# Step 2: Serialize the data to a JSON string
json_string = json.dumps(data, indent=4)

# Step 3: Write the serialized JSON string to a new file
with open('output.json', 'w') as file:
    file.write(json_string)

print("Data read, serialized, and written to output.json")
```

In this example, we read data from `input.json`, serialize it using `json.dumps()`, and write the serialized JSON string to `output.json`.

---

## Conclusion

Python's `json` module makes it incredibly easy to work with JSON data. Whether you're reading from or writing to files, or serializing and deserializing data, Python provides all the tools you need. By understanding the basic concepts of reading and writing JSON files, as well as serialization and deserialization, you can efficiently handle JSON data in your Python applications.

I hope this guide has helped you better understand how to work with JSON in Python. Happy coding!