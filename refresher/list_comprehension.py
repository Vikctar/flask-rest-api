my_list = [0, 1, 2, 3, 4]
list_one = [x for x in range(5)]

print(list_one)

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

print([n for n in range(10) if n % 2 == 0])

people_list = ['Kalf', 'kimi', 'seb', 'GREG']
people_list_normalized = [person.strip().lower() for person in people_list]

print(people_list_normalized)
