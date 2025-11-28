import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MinimumSizeSubarraySumTask import minSubArrayLen


class MinimumSizeSubarraySumTests(unittest.TestCase):

    def test_first_case(self):
        n = [2,3,1,2,4,3]
        target = 7
        expected_output = 2
        result = minSubArrayLen(self, target, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [1,4,4]
        target = 4
        expected_output = 1
        result = minSubArrayLen(self, target, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = [1,1,1,1,1,1,1,1]
        target = 11
        expected_output = 0
        result = minSubArrayLen(self, target, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()



#MinimumSizeSubarraySumTask