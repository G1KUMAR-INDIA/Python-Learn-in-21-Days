# Day 8: Python Operators
- **Arithmetic Operators,**
- **Comparison Operators,**
- **Logical Operators,**
- **Bitwise Operators,**
- **Assignment Operators,**
- **Membership and Identity Operators—“in” and “is” operator**

# Understanding Python Operators

Python operators are special symbols that perform operations on variables and values. Operators are fundamental in programming as they enable us to manipulate data efficiently. In this blog, we will explore different types of operators in Python, including arithmetic, comparison, logical, bitwise, assignment, and membership & identity operators.

## 1. Arithmetic Operators

Arithmetic operators perform basic mathematical operations:

| Operator | Description  | Example | Output |
|----------|--------------|---------|--------|
| + | Addition | `5 + 3` | `8` |
| - | Subtraction | `5 - 3` | `2` |
| * | Multiplication | `5 * 3` | `15` |
| / | Division | `5 / 3` | `1.6667` |
| % | Modulus | `5 % 3` | `2` |
| ** | Exponentiation | `5 ** 3` | `125` |
| // | Floor Division | `5 // 3` | `1` |

## 2. Comparison Operators

Comparison operators compare two values and return a Boolean result (`True` or `False`):

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| == | Equal to | `5 == 3` | `False` |
| != | Not equal to | `5 != 3` | `True` |
| > | Greater than | `5 > 3` | `True` |
| < | Less than | `5 < 3` | `False` |
| >= | Greater than or equal to | `5 >= 3` | `True` |
| <= | Less than or equal to | `5 <= 3` | `False` |

## 3. Logical Operators

Logical operators are used to combine conditional statements:

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| and | Returns True if both conditions are True | `(5 > 3) and (3 < 4)` | `True` |
| or | Returns True if at least one condition is True | `(5 > 3) or (3 > 4)` | `True` |
| not | Reverses the logical state | `not(5 > 3)` | `False` |

## 4. Bitwise Operators

Bitwise operators perform operations on binary representations of integers:

| Operator | Description | Example (5 = 0101, 3 = 0011) | Output |
|----------|-------------|--------------------------------|--------|
| & | AND | `5 & 3` (0101 & 0011) | `1` (0001) |
| \| | OR | `5 | 3` (0101 | 0011) | `7` (0111) |
| ^ | XOR | `5 ^ 3` (0101 ^ 0011) | `6` (0110) |
| ~ | NOT | `~5` (~0101) | `-6` |
| << | Left shift | `5 << 1` | `10` |
| >> | Right shift | `5 >> 1` | `2` |

## 5. Assignment Operators

Assignment operators assign values to variables:

| Operator | Description | Example | Equivalent To |
|----------|-------------|---------|--------------|
| = | Assign | `x = 5` | `x = 5` |
| += | Add and assign | `x += 3` | `x = x + 3` |
| -= | Subtract and assign | `x -= 3` | `x = x - 3` |
| *= | Multiply and assign | `x *= 3` | `x = x * 3` |
| /= | Divide and assign | `x /= 3` | `x = x / 3` |
| %= | Modulus and assign | `x %= 3` | `x = x % 3` |
| **= | Exponent and assign | `x **= 3` | `x = x ** 3` |
| //= | Floor divide and assign | `x //= 3` | `x = x // 3` |
| &= | Bitwise AND and assign | `x &= 3` | `x = x & 3` |
| \|= | Bitwise OR and assign | `x |= 3` | `x = x | 3` |
| ^= | Bitwise XOR and assign | `x ^= 3` | `x = x ^ 3` |
| <<= | Left shift and assign | `x <<= 3` | `x = x << 3` |
| >>= | Right shift and assign | `x >>= 3` | `x = x >> 3` |

## 6. Membership and Identity Operators

### Membership Operators (`in`, `not in`)
Membership operators check if a value is present in a sequence (list, tuple, string, etc.).

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| in | Returns True if value is in sequence | `5 in [1, 2, 3, 4, 5]` | `True` |
| not in | Returns True if value is not in sequence | `6 not in [1, 2, 3, 4, 5]` | `True` |

### Identity Operators (`is`, `is not`)
Identity operators check if two variables refer to the same object in memory.

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| is | Returns True if two variables refer to the same object | `x is y` | Depends on reference |
| is not | Returns True if two variables do not refer to the same object | `x is not y` | Depends on reference |

Example:
```python
x = [1, 2, 3]
y = x
t = [1, 2, 3]
print(x is y)  # True (same reference)
print(x is t)  # False (different objects with same values)
```

## Conclusion

Python provides a variety of operators to handle different types of operations efficiently. Understanding these operators will help you write more effective and optimized code. Keep practicing and experimenting with these operators in your Python projects!

