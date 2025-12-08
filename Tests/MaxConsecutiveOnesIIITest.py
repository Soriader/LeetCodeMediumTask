import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MaxConsecutiveOnesIIITask import longestOnes


class MaxConsecutiveOnesIIITests(unittest.TestCase):

    def test_first_case(self):
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        k = 2
        expected_output = 6
        result = longestOnes(self, nums, k)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        k = 3
        expected_output = 10
        result = longestOnes(self, nums, k)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()