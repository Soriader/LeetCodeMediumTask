import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.RotatedDigitsTask import rotatedDigits


class RotatedDigitsTests(unittest.TestCase):

    def test_first_case(self):
        n = 10
        expected_output = 4
        result = rotatedDigits(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 1
        expected_output = 0
        result = rotatedDigits(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = 2
        expected_output = 1
        result = rotatedDigits(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#RotatetDigitsTask