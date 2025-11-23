import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.SubarraySumsDivisibleByKTask import subarraysDivByK


class SubarraySumsDivisibleByKTests(unittest.TestCase):

    def test_first_case(self):
        n = [4,5,0,-2,-3,1]
        k = 5
        expected_output = 7
        result = subarraysDivByK(self, n, k)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [5]
        k = 9
        expected_output = 0
        result = subarraysDivByK(self, n, k)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

#SubarraySumsDivisibleByKTask