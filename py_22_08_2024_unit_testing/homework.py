class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class Teacher:
    def __init__(self, first, last, profession):
        self.first = first
        self.last = last
        self.profession = profession


class School:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students: [Student] = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, first, last):
        for s in self.students:
            if s.first == first and s.last == last:
                return s
        raise ValueError('student not found')
