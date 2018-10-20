"""
Create a dictionary variable called student.
Modify a variable, grades, so it contains the value of a dictionary's key
Implement a function calculating a total average grade for a class of students.
"""

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
}


# Assume the argument, data, is a dictionary
def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)


# Implement the function below.
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(students_list):
    total = 0
    count = 0

    for student in students_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count


print(average_grade(student))

school = [
    {
        'name': 'Jose',
        'school': 'Computing',
        'grades': (66, 77, 88)
    },
    {
        'name': 'Kalf',
        'school': 'Computing',
        'grades': (88, 98, 99)
    }
]

# Don't try running the second method without passing it a list that contains dictionaries
print(average_grade_all_students(school))
