basket={'apple','banana','orange','mango','mango','mango','mango'}
print(basket)
a=set()
a.add(1)
a.add(2)
print(a)
b={}
print(type(a),type(b))
#  frozen set
fs=frozenset(a)
print(fs)
# fs.add(1)
print(type(fs))

print(3 in a)
print(3 not in a)
x={'a','b','c'}
y={'a','g','h'}
print(x|y)
print(x&y)
print(x-y)