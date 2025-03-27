# What is Decorators?
# A decorator takes in a function, adds some kind of functionality, 
# and returns another function.
# A decorator is a function that takes another function as an argument, 
# adds some kind of functionality and returns another function.

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display function ran")
display()
