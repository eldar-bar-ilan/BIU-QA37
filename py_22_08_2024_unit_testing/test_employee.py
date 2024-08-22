import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('John', 'Smith', 30_000)
        emp_2 = Employee('Mark', 'Levin', 50_000)
        self.assertEqual(emp_1.email, 'john.smith@email.com')
        self.assertEqual(emp_2.email, 'mark.levin@email.com')
        # change the first name and check again
        emp_1.first = 'Dan'
        emp_2.first = 'Ran'
        self.assertEqual(emp_1.email, 'dan.smith@email.com')
        self.assertEqual(emp_2.email, 'ran.levin@email.com')
