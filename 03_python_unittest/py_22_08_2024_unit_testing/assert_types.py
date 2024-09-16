from unittest import TestCase


class Demo(TestCase):
    def test_1(self):
        self.assertEqual(1 + 1, 2 + 0)

        self.assertNotEqual(1 + 1, 2 + 1)

        self.assertTrue(True)
        self.assertTrue(3)
        self.assertTrue([1, 1, 1])

        self.assertIs(1, 1)

        self.assertIsNot(1, 2)

        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse(None)

        self.assertIsNone(None)

        self.assertIsNotNone(4)

        self.assertIn('b', 'abc')
        self.assertIn(2, (1, 2, 3))

        self.assertNotIn('x', 'abc')
        self.assertNotIn(5, (1, 2, 3))

        print(isinstance(4, int))  # True
        print(isinstance(4, float))  # False
        self.assertIsInstance(4, int)
        self.assertIsInstance(4.5, float)
        self.assertIsInstance(self, TestCase)
        self.assertIsInstance(self, Demo)
        self.assertIsInstance([], list)

        print(not isinstance(1, float))  # True
        print(not isinstance(1.3, float))  # False
        self.assertNotIsInstance(1, float)
        self.assertNotIsInstance(1.4, int)
        self.assertNotIsInstance([], tuple)
