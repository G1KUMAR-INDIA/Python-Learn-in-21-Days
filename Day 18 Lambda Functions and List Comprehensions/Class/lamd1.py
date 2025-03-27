'''
# lamda function and list comprehension

# lambda function
# lamda arguments:expression

x=lambda a:a+10
print(x(5)) # output 15

y=lambda a,b:a*b
print(y(10,20)) # output 200

z=lambda a,b:a if a>b else b
print(z(10,20)) # output 20

# checking even or odd using lambda function
even=lambda x:x%2==0
print(even(5))

# using lamda function in higher order function

# map function
# map(function, iterable)
# map() function applies a function to each item in an iterable and returns a new iterable
l=[1,2,3,4,5,6,7,8,9,10]
l1=list(map(lambda x:x+10,l))
double=list(map(lambda x:x*2,l))
print(l1,double)

# filter function
# filter(function, iterable)
# filter() function filters the elements of an iterable based on a function that returns True or False
l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda x:x%2==0 !=0,l))
print(l1)
l2=[1,2,3,4,5,6,7,8,9,10]
l3=list(filter(lambda x:x%2 !=0,l2))
print(l3)

# sorting using lamda function
l=[1,2,3,4,5,6,7,8,9,10]
l1=sorted(l)
print(l1)
l2=[1,2,3,4,5,6,7,8,9,10]
l3=sorted(l2,reverse=True)
print(l3)


# list comprehension
# list comprehension is an element way to define and create a lists based on existing lists.
# creating a list of squares using traditional way
# squares=[]
# for i in range 10:
#     squares.append(i**2)
# print(squares)
# creating a list of squares using list comprehension
# squares=[i**2 for i in range(10)]
# print(squares)

l=[1,2,3,4,5,6,7,8,9,10]
l1=[i*2 for i in l]
print(l1)
l2=[i for i in l if i%2==0]
print(l2)

# filtering words from a given list of words
words=['apple','banana','cherry','date','elderberry']
words1=[i for i in words if len(i)>5]
print(words1) # output ['banana', 'cherry', 'elderberry']

# creating list of tuples like (number,square of number)
numbers=[1,2,3,4,5]
squares=[(i,i**2) for i in numbers]
print(squares)

# flatening a nested list
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
flattened_list=[num for row in nested_list for num in row]
print(flattened_list)

# combining lamda function with list comprehension
numbers5=[1,2,3,4,5]
squares5=list(map(lambda x:x**2,numbers5))
print(squares5)
'''
# filtering even numbers using lamda function inside list comprehension
numbers6=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0,numbers6))
print(even_numbers)

'''
# using map and filter together in list comprehension
numbers7=[1,2,3,4,5,6,7,8,9,10]
squares7=list(map(lambda x:x**2,filter(lambda x:x%2==0,numbers7)))
print(squares7)
'''