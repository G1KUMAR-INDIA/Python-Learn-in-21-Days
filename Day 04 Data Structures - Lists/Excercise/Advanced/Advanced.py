'''
Advanced:
    1.Implement a function to reverse a list without using the built-in reverse() method.
    2.Implement a function to find the second largest element in a list.
    3.Given two lists, create a new list that contains only the elements that are common to both lists.
    4.Given a list of numbers, create a new list that contains only the even numbers.
    5.Implement a simple "to-do" list application using lists. Allow users to add, remove, and view tasks.
'''


def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

list1 = [1, 2, 3, 4, 5]
reversed_list = reverse_list(list1)
print(reversed_list)

def find_second_largest(lst):
    largest = lst[0]
    second_largest = lst[0]
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

list2 = [1, 2, 3, 4, 5]
second_largest = find_second_largest(list2)
print(second_largest)

def common_elements(list1, list2):
    common = []
    for num in list1:
        if num in list2:
            common.append(num)
    return common

list3 = [1, 2, 3, 4, 5]
list4 = [3, 4, 5, 6, 7]
common_elements = common_elements(list3, list4)
print(common_elements)

def even_numbers(lst):
    even = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    return even

list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = even_numbers(list5)
print(even_numbers)

def to_do_list():
    tasks = []
    while True:
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not found")
        elif choice == "3":
            print("Tasks:")
            for task in tasks:
                print(task)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

to_do_list()