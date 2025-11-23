import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.GreatestSumDivisibleByThreeTask import maxSumDivThree


class GreatestSumDivisibleByThreeTests(unittest.TestCase):

    def test_first_case(self):
        n = [3,6,5,1,8]
        expected_output = 18
        result = maxSumDivThree(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [4]
        expected_output = 0
        result = maxSumDivThree(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = [1,2,3,4,4]
        expected_output = 12
        result = maxSumDivThree(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()