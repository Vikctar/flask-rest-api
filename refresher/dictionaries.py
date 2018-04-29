# set
my_set = {1, 3, 5}

# Dictionary containing strings, ints and list
my_dict = {'name': 'Kalf', 'age': 50, 'grades': [66, 77, 88]}

another_dict = {1: 10, 2: 20, 3: 30}

# dictionary containing a tuple and strings
lottery_player = {
    'name': 'Kalf',
    'numbers': (13, 44, 66, 23, 22)
}

# List containing dictionaries
universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'UON',
        'location': 'KE'
    }
]

# Access an element using keys
print(sum(lottery_player['numbers']))

print(lottery_player['name'])
