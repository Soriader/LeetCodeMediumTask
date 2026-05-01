import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.RotateFunctionTask import maxRotateFunction


class RotateFunctionTests(unittest.TestCase):

    def test_first_case(self):
        n = [4,3,2,6]
        expected_output = 26
        result = maxRotateFunction(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [100]
        expected_output = 0
        result = maxRotateFunction(self, n)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()