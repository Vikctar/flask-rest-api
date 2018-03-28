# Declare variables
a = 5
b = 10
my_variable = 56
any_variable_name = 100

string_variable = "hello"
single_quotes = 'strings can have single quotes'

# Print some stuff using print() function
print(my_variable)
print(string_variable)

# Printing values directly
print('hello directly')
print(23)

# Methods


def print_method(parameter):
    print(parameter)

print_method(single_quotes)


def multiplication_method(operand_one, operand_two):
    return operand_one * operand_two


result = multiplication_method(3, 17)
print(result)

print(multiplication_method(30, 22))

print_method(multiplication_method(22, 112))

