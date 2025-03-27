# Day 19: Advanced Python – Decorators, Iterators
- **Introduction to decorators, Writing custom decorators**
- **Introduction to Iterators, Iterators vs Iterables, Create an Iterator**
- **Looping through an Iterator, Stop Iteration**
- **Socket Programming**
- **Types of Sockets, Getting started with sockets in python ,**
- **Building TCP Server-Client Program, Understanding UDP communication**

# Day 19: Advanced Python – Decorators, Iterators

## Introduction to Decorators

Decorators in Python are a powerful tool that allows developers to modify the behavior of functions or methods without changing their actual code. They are widely used for logging, authentication, enforcing access control, instrumentation, and caching.

A decorator in Python is a function that takes another function as an argument and extends or alters its behavior.

### Writing Custom Decorators

We can create custom decorators using functions or classes. Here is an example of a simple function-based decorator:

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

In this example:
- `my_decorator` is a decorator function.
- The `wrapper` function extends the behavior of `say_hello`.
- Using `@my_decorator`, we apply the decorator to `say_hello`.

We can also create parameterized decorators by using function arguments:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
```

## Introduction to Iterators

Iterators in Python are objects that allow traversal through a sequence of elements one at a time. They implement two special methods:
- `__iter__()` to return the iterator object itself.
- `__next__()` to return the next item in the sequence.

### Iterators vs Iterables

| Feature        | Iterable                  | Iterator                  |
|---------------|--------------------------|--------------------------|
| Definition    | Object that contains data which can be iterated over | Object that produces data one item at a time |
| Implementation | Implements `__iter__()` | Implements both `__iter__()` and `__next__()` |
| Example       | List, Tuple, String      | Generator functions, Custom iterators |

All iterators are iterables, but not all iterables are iterators.

### Creating an Iterator

Here is an example of a custom iterator that generates a sequence of even numbers:

```python
class EvenNumbers:
    def __init__(self, max_n):
        self.max_n = max_n
        self.n = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > self.max_n:
            raise StopIteration
        else:
            self.n += 2
            return self.n - 2

# Using the iterator
numbers = EvenNumbers(10)
for num in numbers:
    print(num)
```

### Looping through an Iterator

Iterators can be looped through using `for` loops or manually using `next()`:

```python
nums = iter([1, 2, 3])
print(next(nums))  # 1
print(next(nums))  # 2
print(next(nums))  # 3
```

### Handling StopIteration

When an iterator reaches the end, calling `next()` raises a `StopIteration` exception. This can be handled using a `try-except` block:

```python
try:
    print(next(nums))  # Raises StopIteration
except StopIteration:
    print("No more elements.")
```

## Socket Programming

Socket programming allows two networked computers to communicate with each other. Python provides a built-in `socket` module to facilitate network communication.

### Types of Sockets

1. **Stream Sockets (TCP)**: Reliable and connection-oriented.
2. **Datagram Sockets (UDP)**: Faster but unreliable and connectionless.

### Getting Started with Sockets in Python

To create a simple socket, use:

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created successfully")
```

### Building a TCP Server-Client Program

#### Server Code:

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")
conn.sendall(b'Hello, Client!')
conn.close()
```

#### Client Code:

```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
msg = client_socket.recv(1024)
print(msg.decode())
client_socket.close()
```

### Understanding UDP Communication

#### UDP Server Code:

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Server is waiting for messages...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
    server_socket.sendto(b'ACK', addr)
```

#### UDP Client Code:

```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b'Hello, Server!', ('localhost', 12345))
data, server = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")
client_socket.close()
```

## Conclusion

In this blog, we explored:
- **Decorators**, which help modify function behavior without changing its code.
- **Iterators**, which allow traversal through data elements efficiently.
- **Socket Programming**, which enables network communication using TCP and UDP.

Understanding these concepts enhances your Python programming skills, enabling you to build robust applications with efficient data processing and network communication capabilities.

