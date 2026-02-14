import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.ChampagneTowerTask import champagneTower


class GreatestSumDivisibleByThreeTests(unittest.TestCase):

    def test_first_case(self):
        poured = 1
        query_row = 1
        query_glass = 1
        expected_output = 0.00000
        result = champagneTower(self, poured, query_row, query_glass)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        poured = 2
        query_row = 1
        query_glass = 1
        expected_output = 0.50000
        result = champagneTower(self, poured, query_row, query_glass)
        self.assertEqual(result, expected_output)


    def test_third_case(self):
        poured = 100000009
        query_row = 33
        query_glass = 17
        expected_output = 1.00000
        result = champagneTower(self, poured, query_row, query_glass)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#ChampagneTowerTask