class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, **kwargs):
        return cls(friend_name, origin.school, **kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary


james = WorkingStudent("James", "Pathways Academy", 20000, "Software Developer")

barry = WorkingStudent.friend(james, "Barry", salary=17000, job_title='Software Developer')
print(barry.school)
print(james.salary)