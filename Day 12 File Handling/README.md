# Day 12: File Handling
- **Reading from and writing to files**
- **Context manager (with statement)**

# File Handling in Python: A Comprehensive Guide

File handling is an essential aspect of programming that allows us to read from and write to files efficiently. Python provides built-in functions to handle files seamlessly. In this blog, we will explore:

- Reading from and writing to files
- Using the `with` statement (context manager) for better file handling

## 1. Reading from and Writing to Files

Python provides several modes to handle files:

| Mode  | Description |
|-------|-------------|
| `r`   | Read (default mode) |
| `w`   | Write (creates a new file if it doesn't exist, overwrites if it does) |
| `a`   | Append (adds content to the end of a file) |
| `r+`  | Read and Write |
| `w+`  | Write and Read (overwrites existing content) |
| `a+`  | Append and Read |

### Reading from a File
To read data from a file, we use the `open()` function in **read (`r`) mode**:

```python
# Opening and reading a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

Alternatively, you can read the file **line by line**:

```python
file = open("example.txt", "r")
for line in file:
    print(line.strip())
file.close()
```

### Writing to a File
To write to a file, we open it in **write (`w`) mode**:

```python
file = open("example.txt", "w")
file.write("Hello, Python file handling!")
file.close()
```

If the file **already exists,** this will overwrite the content. To append data instead of overwriting, use **append (`a`) mode**:

```python
file = open("example.txt", "a")
file.write("\nAppending new data!")
file.close()
```

## 2. Using the Context Manager (`with` statement)

Manually opening and closing files can lead to errors if the program terminates unexpectedly. The `with` statement automatically **handles closing** the file, ensuring proper resource management.

### Reading a File Using `with`
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Writing to a File Using `with`
```python
with open("example.txt", "w") as file:
    file.write("Using context manager for writing!")
```

### Why Use `with`?
- **Automatic file closing**: No need to explicitly call `file.close()`.
- **Better readability and structure**.
- **Prevents resource leakage**, ensuring the file is properly closed even if an error occurs.

## Conclusion
Python's file handling features make it easy to work with files efficiently. Using the `with` statement is the recommended approach as it provides better safety and code clarity. Whether reading, writing, or appending, Python offers flexible options to manage files effectively.

Happy coding! 🚀

