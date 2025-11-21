import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.LongestSubstringWithoutRepeatingCharactersTask import lengthOfLongestSubstring


class LongestSubstringWithoutRepeatingCharactersTests(unittest.TestCase):

    def test_first_case(self):
        n = "abcabcbb"
        expected_output = 3
        result = lengthOfLongestSubstring(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = "bbbbb"
        expected_output = 1
        result = lengthOfLongestSubstring(n)
        self.assertEqual(result, expected_output)
    def test_third_case(self):
        n = "pwwkew"
        expected_output = 3
        result = lengthOfLongestSubstring(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()