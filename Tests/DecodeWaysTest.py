import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.DecodeWaysTask import numDecodings


class GreatestSumDivisibleByThreeTests(unittest.TestCase):

    def test_first_case(self):
        s = "12"
        expected_output = 2
        result = numDecodings(self, s)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        s = "226"
        expected_output = 3
        result = numDecodings(self, s)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        s = "06"
        expected_output = 0
        result = numDecodings(self, s)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
