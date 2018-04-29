numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Modify the method below to make sure only even numbers are returned
def even_numbers():
    evens = []
    for number in numbers:
        evens.append(number)
    return evens


# Modify the below method so that 'Quit' is returned if the choice parameter is 'q'
def user_menu(choice):
    if choice == 'a':
        return "Add"
