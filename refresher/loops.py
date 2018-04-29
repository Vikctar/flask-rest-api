my_string = "Hello"

for char in my_string:  # Iterables are strings, lists, tuples and more
    print(char)

my_list = [1, 3, 5, 7, 9]

for number in my_list:
    print(number ** 2)

user_wants_number = True
while user_wants_number:
    print(10)
    user_input = input('Should we print again? (y/n)')
    if user_input == 'n' or user_input == 'N':
        user_wants_number = False
