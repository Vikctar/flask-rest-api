# Grades list
grades = [77, 88, 98, 95, 100]

# Grades tuple
tuple_grades = (77, 88, 98, 95, 100)

# Grades set
set_grades = {77, 88, 98, 95, 100}

# Length of the list
print(len(grades))

# Sum of its elements
print(sum(grades))

print(type(grades))

print(set_grades)

# Add an element to a list
grades.append(66)

print(grades)

tuple_grades += (200,)
print(tuple_grades)

set_grades.add(60)
print(set_grades)

# Set operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# Numbers that are in both sets
print(your_lottery_numbers.intersection(winning_numbers))

# All the numbers in the two sets
print(your_lottery_numbers.union(winning_numbers))

# Unique elements in the two sets (only appears in one of the sets)
# Opposite of intersection
print(your_lottery_numbers.difference(winning_numbers))

# quiz
# Create a list called my_list, with three numbers. The total of the numbers added together should be 100
my_list = [10, 20, 70]

# Create a tuple, called my_tuple with a single value in it
my_tuple = (7,)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 9, 12, 77}

print(set1.intersection(set2))
