class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


james = WorkingStudent("James", "Pathways Academy", 20000)

barry = WorkingStudent.friend(james, "Barry", 17000)
print(barry.school)
print(james.salary)