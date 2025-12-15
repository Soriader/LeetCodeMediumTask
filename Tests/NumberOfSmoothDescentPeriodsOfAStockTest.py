import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.NumberOfSmoothDescentPeriodsOfAStockTask import getDescentPeriods


class NumberOfSmoothDescentPeriodsOfAStockTests(unittest.TestCase):

    def test_first_case(self):
        n = [3,2,1,4]
        expected_output = 7
        result = getDescentPeriods(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [8,6,7,7]
        expected_output = 4
        result = getDescentPeriods(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = [1]
        expected_output = 1
        result = getDescentPeriods(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
