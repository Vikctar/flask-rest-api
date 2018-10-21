def my_method(arg1, arg2):
    return arg1 + arg2


my_method(5, 4)


def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7


my_long_method(2, 3, 4, 5, 6, 7, 8, )


def addition_simplified(*args):
    return sum(args)


def what_are_kwargs(*args, **kwargs):
    print(args) # Will be a tuple of the arguments
    print(kwargs) # will be a set of the arguments if empty or a dictionary if it contains any values


what_are_kwargs(12, 34, 56)
