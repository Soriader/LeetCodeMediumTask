import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.LongestBalancedSubstringIITask import longestBalanced


class LongestBalancedSubstringIITests(unittest.TestCase):

    def test_first_case(self):
        n = "abbac"
        expected_output = 4
        result = longestBalanced(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = "aabcc"
        expected_output = 3
        result = longestBalanced(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = "aba"
        expected_output = 2
        result = longestBalanced(self, n)
        self.assertEqual(result, expected_output)

    def test_forth_case(self):
        n = "aaaa"
        expected_output = 4
        result = longestBalanced(self, n)
        self.assertEqual(result, expected_output)
if __name__ == '__main__':
    unittest.main()