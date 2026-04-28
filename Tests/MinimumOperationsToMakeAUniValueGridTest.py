import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MinimumOperationsToMakeAUniValueGridTask import minOperations


class MinimumOperationsToMakeAUniValueGridTests(unittest.TestCase):

    def test_first_case(self):
        n = [[2, 4], [6, 8]]
        x = 2
        expected_output = 4
        result = minOperations(self, n, x)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n =  [[1, 5], [2, 3]]
        x = 1
        expected_output = 5
        result = minOperations(self, n, x)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = [[1, 2], [3, 4]]
        x = 2
        expected_output = -1
        result = minOperations(self, n, x)
        self.assertEqual(result, expected_output)


