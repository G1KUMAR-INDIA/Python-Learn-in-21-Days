# What is Iterators?
# An Iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, 
# meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object that implements the iterator protocol,
# which consists of the methods __iter__() and __next__().
# Lists, tuples, dictionaries, and sets are all iterable objects in Python.

# tuple,iter,next
my_typle=("apple","banana","cherry")
my_iter=iter(my_typle)
print(next(my_iter)) # output apple
print(next(my_iter)) # output banana
print(next(my_iter)) # output cherry
# print(next(my_iter)) # output error