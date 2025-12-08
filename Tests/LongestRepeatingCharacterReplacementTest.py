import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.LongestRepeatingCharacterReplacementTask import characterReplacement


class GreatestSumDivisibleByThreeTests(unittest.TestCase):

    def test_first_case(self):
        n = "ABAB"
        k = 2
        expected_output = 4
        result = characterReplacement(self, n, k)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = "AABABBA"
        k = 1
        expected_output = 4
        result = characterReplacement(self, n, k)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()