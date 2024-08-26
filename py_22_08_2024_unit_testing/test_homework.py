import unittest
from homework import Student, Teacher, School


class TestHomework(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher('Dan', 'Rozen', 'English')
        self.school = School('High Tech School', self.teacher)
        self.student_1 = Student('aaa', 'bbb')
        self.student_2 = Student('ccc', 'ddd')
        self.student_3 = Student('eee', 'fff')
        self.school.add_student(self.student_1)
        self.school.add_student(self.student_2)
        self.school.add_student(self.student_3)

    def test_school_and_teacher_created(self):
        self.assertEqual(self.teacher.first, self.school.teacher.first)
        self.assertEqual(self.teacher.last, self.school.teacher.last)
        self.assertEqual(self.teacher.profession, self.school.teacher.profession)

    def test_students_added(self):
        self.assertEqual(3, len(self.school.students), 'there should be 3 students')
        self.assertIn(self.student_1, self.school.students, 'student 1 is missing')
        self.assertIn(self.student_2, self.school.students, 'student 2 is missing')
        self.assertIn(self.student_3, self.school.students, 'student 3 is missing')

    def test_find_students(self):
        st = self.school.find_student('ccc', 'ddd')
        self.assertEqual(self.student_2, st, 'student not found')

        with self.assertRaises(ValueError, msg='exception not raised when not finding student'):
            self.school.find_student('zzz', 'ppp')
