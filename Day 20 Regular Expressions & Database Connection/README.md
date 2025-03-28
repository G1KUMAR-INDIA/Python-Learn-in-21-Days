Day 20: Regular Expressions & Database Connection
1. Database Connectivity in Python
Introduction to Databases in Python
- **What is a database?**
- **Why use databases in Python?**
- **Types of databases (SQL & NoSQL)**
2. SQLite with Python
- **Introduction t- **SQLite**
- **Connecting t- **an SQLite database**
- **Creating a table using Python**
- **Inserting, updating, and deleting records**
- **Querying data from the database**
- **Using parameterized queries**
- **Closing database connections**
3. MySQL with Python (Using MySQL Connector)
- **Installing MySQL connector (pip install mysql-connector-python)**
- **Connecting t- **a MySQL database**
- **Creating and selecting a database**
- **Performing CRUD (Create, Read, Update, Delete) operations**
- **Handling transactions and committing changes**
- **Using connection pooling for better performance**
4. PostgreSQL with Python (Using psycopg2)
- **Installing psycopg2**
- **Connecting to a PostgreSQL database**
- **Performing CRUD operations**
- **Handling database transactions**
2. Regular Expressions (Regex) in Python
Regular expressions are used for pattern matching and text processing
in Python using the re module.
1. Introduction to Regex
- **What is a Regular Expression?**
- **Why use Regular Expressions?**
- **How to import the re module**
2. Common Regex Methods in Python**
- **re.match() – Match a pattern at the beginning of a string**
- **re.search() – Search for a pattern anywhere in a string**
- **re.findall() – Find all occurrences of a pattern in a string**
- **re.finditer() – Find all occurrences and return an iterator**
- **re.split() – Split a string using a regex pattern**
- **re.sub() – Replace text using a regex pattern**
3. Regex Metacharacters & Special Sequences
- **Metacharacters (. ^ $ * + ? { } [ ] \ | ( ))**
- **Special sequences (\d, \w, \s, \b, etc.)**
- **Using quantifiers (+, *, ?, {m,n})**
=========================================================
# Regular Expressions & Database Connection in Python

## Database Connectivity in Python

### Introduction to Databases in Python

#### What is a Database?
A database is an organized collection of data that allows users to store, retrieve, and manage information efficiently. It provides structured data storage and enables quick access to large amounts of information.

#### Why Use Databases in Python?
Python offers several libraries for interacting with databases, making it a popular choice for database-driven applications. Using databases in Python helps to:
- Store and retrieve structured data efficiently
- Maintain data consistency and integrity
- Enable complex data operations with minimal code
- Support multiple database management systems (SQL & NoSQL)

#### Types of Databases (SQL & NoSQL)
- **SQL Databases**: These databases store data in structured tables with predefined schemas. Examples: MySQL, PostgreSQL, SQLite.
- **NoSQL Databases**: These databases store data in flexible, non-tabular formats like key-value, document, or graph. Examples: MongoDB, Firebase.

## SQLite with Python

### Introduction to SQLite
SQLite is a lightweight, file-based SQL database that does not require a separate server. It is widely used for small applications, testing, and prototyping.

### Connecting to an SQLite Database
```python
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
```

### Creating a Table Using Python
```python
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()
```

### Inserting, Updating, and Deleting Records
```python
# Insert
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# Update
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
conn.commit()

# Delete
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
conn.commit()
```

### Querying Data from the Database
```python
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
```

### Using Parameterized Queries
```python
cursor.execute("SELECT * FROM users WHERE age > ?", (20,))
print(cursor.fetchall())
```

### Closing Database Connections
```python
conn.close()
```

## MySQL with Python (Using MySQL Connector)

### Installing MySQL Connector
```bash
pip install mysql-connector-python
```

### Connecting to a MySQL Database
```python
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='password', database='testdb')
cursor = conn.cursor()
```

### Creating and Selecting a Database
```python
cursor.execute("CREATE DATABASE testdb")
cursor.execute("USE testdb")
```

### Performing CRUD Operations
```python
# Create Table
cursor.execute("""CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)""")

# Insert Data
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 30))
conn.commit()
```

### Handling Transactions and Committing Changes
```python
try:
    cursor.execute("UPDATE users SET age = %s WHERE name = %s", (35, "Bob"))
    conn.commit()
except:
    conn.rollback()
```

### Using Connection Pooling
```python
from mysql.connector import pooling
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, host='localhost', user='root', password='password', database='testdb')
conn = pool.get_connection()
```

## PostgreSQL with Python (Using psycopg2)

### Installing psycopg2
```bash
pip install psycopg2
```

### Connecting to a PostgreSQL Database
```python
import psycopg2
conn = psycopg2.connect(database="testdb", user="postgres", password="password", host="localhost", port="5432")
cursor = conn.cursor()
```

### Performing CRUD Operations
```python
# Create Table
cursor.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100), age INT)")
conn.commit()

# Insert Data
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Eve", 28))
conn.commit()
```

### Handling Database Transactions
```python
try:
    cursor.execute("DELETE FROM users WHERE name = %s", ("Eve",))
    conn.commit()
except:
    conn.rollback()
```

## Regular Expressions (Regex) in Python

Regular expressions are used for pattern matching and text processing in Python using the `re` module.

### Introduction to Regex

#### What is a Regular Expression?
A Regular Expression (Regex) is a sequence of characters that define a search pattern for matching strings.

#### Why Use Regular Expressions?
- Pattern matching
- Data validation (email, phone numbers, etc.)
- Text processing and replacement

#### Importing the `re` Module
```python
import re
```

### Common Regex Methods in Python

#### `re.match()` – Match a Pattern at the Beginning of a String
```python
result = re.match(r'hello', 'hello world')
print(result.group())
```

#### `re.search()` – Search for a Pattern Anywhere in a String
```python
result = re.search(r'world', 'hello world')
print(result.group())
```

#### `re.findall()` – Find All Occurrences of a Pattern
```python
print(re.findall(r'\d+', 'Numbers: 123 456 789'))
```

#### `re.finditer()` – Find All Occurrences and Return an Iterator
```python
for match in re.finditer(r'\d+', '123 456 789'):
    print(match.group())
```

#### `re.split()` – Split a String Using a Regex Pattern
```python
print(re.split(r'\s+', 'Split this sentence'))
```

#### `re.sub()` – Replace Text Using a Regex Pattern
```python
print(re.sub(r'\d+', 'NUM', 'Replace 123 with text'))
```

### Regex Metacharacters & Special Sequences

#### Metacharacters
`. ^ $ * + ? { } [ ] \ | ( )`

#### Special Sequences
- `\d` – Digits
- `\w` – Alphanumeric characters
- `\s` – Whitespace
- `\b` – Word boundary

#### Using Quantifiers
- `+` – One or more
- `*` – Zero or more
- `?` – Zero or one
- `{m,n}` – Between m and n times

---
This blog provides a comprehensive overview of database connectivity and regular expressions in Python. With these concepts, you can efficiently work with databases and perform advanced text processing tasks.


