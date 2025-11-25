import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.SmallestIntegerDivisibleByKTask import smallestRepunitDivByK


class SmallestIntegerDivisibleByKTests(unittest.TestCase):

    def test_first_case(self):
        k = 1
        expected_output = 1
        result = smallestRepunitDivByK(self, k)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        k = 2
        expected_output = -1
        result = smallestRepunitDivByK(self, k)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        k = 3
        expected_output = 3
        result = smallestRepunitDivByK(self, k)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()