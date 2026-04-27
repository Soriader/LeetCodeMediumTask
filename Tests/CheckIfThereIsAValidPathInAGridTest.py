import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CheckIfThereIsAValidPathInAGridTask import hasValidPath


class CheckIfThereIsAValidPathInAGridTests(unittest.TestCase):

    def test_first_case(self):
        n = [[2, 4, 3], [6, 5, 2]]
        expected_output = True
        result = hasValidPath(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [[1]]
        expected_output = True
        result = hasValidPath(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = [[1, 2, 1], [1, 2, 1]]
        expected_output = False
        result = hasValidPath(self, n)
        self.assertEqual(result, expected_output)

    def test_forth_case(self):
        n = [[1, 1, 2]]
        expected_output = False
        result = hasValidPath(self, n)
        self.assertEqual(result, expected_output)
