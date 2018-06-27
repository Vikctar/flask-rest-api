# List: Mutable and ordered
grades = [77, 88, 95, 99, 100]

# Tuple: Immutable
tuple_grades = (55, 66, 77, 88, 99, 100)

# Set: unique and unordered
set_grades = {77, 88, 99, 100, 55}

# Print out the length (number of elements in the list)
print("Length:", len(grades))

# Sum of all the elements in the list
print("Sum:", sum(grades))

print(tuple_grades)
print(set_grades)

# add an element to the list
grades.append(60)
print(grades)

# Adding an element to a tuple
tuple_grades = tuple_grades + (120,)
print(tuple_grades)

# set operation
set_grades.add(70)
print(set_grades)

# remove (pop) last item
set_grades.pop()
print(set_grades)

# Advanced set ops
lottery_numbers = {1, 2, 3, 4, 5, 6}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(lottery_numbers.union(winning_numbers))
print(lottery_numbers.intersection(winning_numbers))
print(lottery_numbers.difference(winning_numbers))
print(lottery_numbers.isdisjoint(winning_numbers))


