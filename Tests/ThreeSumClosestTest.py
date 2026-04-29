import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.ThreeSumClosestTask import threeSumClosest


class ThreeSumClosestTests(unittest.TestCase):

    def test_first_case(self):
        n = [-1,2,1,-4]
        target = 1
        expected_output = 2
        result = threeSumClosest(self, n, target)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [0,0,0]
        target = 1
        expected_output = 0
        result = threeSumClosest(self, n, target)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()