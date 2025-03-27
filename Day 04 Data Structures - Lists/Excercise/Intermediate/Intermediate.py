'''
Intermediate:
    1.Given a list of numbers, find the sum of all the numbers.
    2.Given a list of strings, concatenate all the strings together.
    3.Given a list of numbers, find the largest and smallest numbers.
    4.Given a list of names, sort the list in alphabetical order.
    5.Given a list of numbers, remove all duplicates from the list.
'''
list1=[1,2,3,4,5]
sum=0
for i in list1:
    sum+=i
print(sum)

list2=["a","b","c","d","e"]
str1=""
for i in list2:
    str1+=i
print(str1)

list3=[1,2,3,4,5,6,7,8,9,10]
max=list3[0]
min=list3[0]
for i in list3:
    if i>max:
        max=i
    if i<min:
        min=i
print(max)
print(min)

list4=["a","b","c","d","e","f","g","h","i","j"]
list4.sort()
print(list4)

list5=[1,2,3,4,5,6,7,8,9,10]
list5=list(set(list5))
print(list5)