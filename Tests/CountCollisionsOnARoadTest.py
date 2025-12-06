import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CountCollisionsOnARoadTask import countCollisions


class CountCollisionsOnARoadTests(unittest.TestCase):

    def test_first_case(self):
        directions = "RLRSLL"
        expected_output = 5
        result = countCollisions(self, directions)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        directions = "LLRR"
        expected_output = 0
        result = countCollisions(self, directions)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
