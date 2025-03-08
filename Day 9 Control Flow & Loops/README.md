# Day 9: Control Flow & Loops
- **Conditional statements: if- else, Nested if statement,**
- **If-elif-else , if-else on one line**
- **Ternary Condition, Case statement**
- **for loops**
- **while loops**
- **break, continue, and else in loops**

# Control Flow & Loops in Python

Control flow and loops are fundamental concepts in programming that allow us to make decisions and execute code multiple times. Python provides several control flow statements to handle conditions and loops efficiently.

## 1. Conditional Statements
Conditional statements allow the execution of specific blocks of code based on conditions. Python provides multiple ways to implement conditionals.

### **if-else Statement**
The `if-else` statement evaluates a condition and executes different code blocks based on whether the condition is `True` or `False`.

```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

### **Nested if Statement**
A nested `if` statement means an `if` statement inside another `if` statement.

```python
num = 10
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Non-positive number")
```

### **if-elif-else Statement**
When multiple conditions need to be checked, we use `if-elif-else`.

```python
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")
```

### **if-else on One Line**
Python allows writing simple `if-else` statements in a single line.

```python
age = 20
print("Adult") if age >= 18 else print("Minor")
```

### **Ternary Condition**
Ternary conditional expressions provide a shorthand for `if-else` statements.

```python
num = 5
result = "Even" if num % 2 == 0 else "Odd"
print(result)
```

### **Case Statement (Match-Case)**
Python 3.10 introduced the `match-case` statement, similar to switch-case in other languages.

```python
def get_day(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(get_day(3))  # Output: Wednesday
```

## 2. Loops
Loops are used to execute a block of code multiple times.

### **for Loop**
A `for` loop is used for iterating over a sequence (such as a list, tuple, or string).

```python
for i in range(5):
    print("Iteration:", i)
```

Looping through a list:

```python
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)
```

### **while Loop**
A `while` loop runs as long as the given condition is `True`.

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

## 3. Loop Control Statements
Loop control statements modify the execution of loops.

### **break Statement**
The `break` statement exits the loop when a condition is met.

```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

### **continue Statement**
The `continue` statement skips the rest of the loop for the current iteration.

```python
for num in range(10):
    if num == 5:
        continue
    print(num)
```

### **else with Loops**
The `else` block executes after the loop completes normally (without `break`).

```python
for num in range(3):
    print(num)
else:
    print("Loop completed")
```

```python
num = 0
while num < 3:
    print(num)
    num += 1
else:
    print("Loop ended successfully")
```

## Conclusion
Understanding control flow and loops is essential for writing efficient Python programs. The `if-else`, `for`, and `while` loops, along with loop control statements like `break` and `continue`, help in executing logic effectively. By mastering these concepts, you can write more optimized and structured code in Python.

