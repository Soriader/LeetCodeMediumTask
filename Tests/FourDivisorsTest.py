import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.FourDivisorsTask import sumFourDivisors


class FourDivisorsTests(unittest.TestCase):

    def test_first_case(self):
        n = [21,4,7]
        expected_output = 32
        result = sumFourDivisors(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [21,21]
        expected_output = 64
        result = sumFourDivisors(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = [1,2,3,4,5]
        expected_output = 0
        result = sumFourDivisors(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
#FourDivisorsTest