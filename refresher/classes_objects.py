class LotteryPlayer:
    # self: This is the object that we are creating
    def __init__(self):
        self.name = 'Kalf'
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average_marks(self):
        return sum(self.marks) / len(self.marks)


anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(88)
anna.marks.append(99)
anna.marks.append(96)

print(anna.marks)
print(anna.average_marks())
