import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.SubarrayProductLessThanKTask import numSubarrayProductLessThanK


class SubarrayProductLessThanKTests(unittest.TestCase):

    def test_first_case(self):
        nums = [10,5,2,6]
        k = 100
        expected_output = 8
        result = numSubarrayProductLessThanK(self, nums, k)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        nums = [1,2,3]
        k = 0
        expected_output = 0
        result = numSubarrayProductLessThanK(self, nums, k)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
