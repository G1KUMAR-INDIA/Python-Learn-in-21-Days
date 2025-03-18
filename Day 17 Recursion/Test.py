a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(f"GCD OF Given Two Numbers {a} and {b} is :",gcd(a,b))