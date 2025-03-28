'''
    What is Database?
    Database is a collection of data that is stored in a structured way 
    so that it can be easily accessed and managed. 

    It is used to store and retrieve information from a computer system.

    There are different types of databases, 
    such as relational databases (e.g., MySQL, PostgreSQL), 
    NoSQL databases (e.g., MongoDB), and graph databases (e.g., Neo4j).

    How to connect to a database?
    To connect to a database, you need to install the relevant database client library 
    (e.g., MySQL Connector for Python) and 
    then use the appropriate driver to establish a connection.


'''
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor=conn.cursor()
print("Database Connection Opened Successfully")

# creating table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL        
    )
''')
conn.commit()
print("Table created successfully")


# inserting data into table
cursor.execute('''
    INSERT INTO students (id, name, age, grade)
    VALUES (1, 'R JEEVAN KUMAR', 30, 'A')
''')
conn.commit()
print("Data inserted successfully")
