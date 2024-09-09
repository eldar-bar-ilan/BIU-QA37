import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('===================> setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('===================> tearDownClass')

    def setUp(self):
        # the setup method will run before each test
        print("======> setUp")
        self.emp_1 = Employee('John', 'Smith', 30_000)
        self.emp_2 = Employee('Mark', 'Levin', 50_000)

    def tearDown(self):
        print("======> tearDown\n")

    def test_email(self):
        print("======> test_email")
        self.assertEqual(self.emp_1.email, 'john.smith@email.com')
        self.assertEqual(self.emp_2.email, 'mark.levin@email.com')
        # change the first name and check again
        self.emp_1.first = 'Dan'
        self.emp_2.first = 'Ran'
        self.assertEqual(self.emp_1.email, 'dan.smith@email.com')
        self.assertEqual(self.emp_2.email, 'ran.levin@email.com')

    def test_full_name(self):
        print("======> test_full_name")
        self.assertEqual(self.emp_1.full, 'John Smith')
        self.assertEqual(self.emp_2.full, 'Mark Levin')
        # change the first name and check again
        self.emp_1.first = 'Dan'
        self.emp_2.first = 'Ran'
        self.assertEqual(self.emp_1.full, 'Dan Smith')
        self.assertEqual(self.emp_2.full, 'Ran Levin')

    def test_apply_raise(self):
        print("======> test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 31_500)
        self.assertEqual(self.emp_2.pay, 52_500)
