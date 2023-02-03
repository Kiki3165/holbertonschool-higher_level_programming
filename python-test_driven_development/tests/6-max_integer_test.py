#!/usr/bin/python3
'''unittest'''


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_of_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_list_of_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4, 5])

    def test_list_of_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)

if __name__ == "__main__":
    unittest.main()
