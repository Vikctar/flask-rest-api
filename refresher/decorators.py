import functools


# Decorator is a function that's called before another function is called.

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator")

    return function_that_runs_func()


@my_decorator
def my_function():
    print("I'm in the function!")


try:
    my_function()
except TypeError:
    pass
