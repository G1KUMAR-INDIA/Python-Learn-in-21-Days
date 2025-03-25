# recursion
# recursive function is a function that calls itself
# 1. base case
# 2. recursive case
# 3. return statement

n=int(input("Enter a number:"))

# printing numbers from 1 to n in reverse
# def count(n):
#     if n==0:
#         print("Blastoff!")
#         return
#     else:
#         print(n)
#         count(n-1)

# count(n)

# factorial of a given number
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(n))

# fibanacci series

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(n))