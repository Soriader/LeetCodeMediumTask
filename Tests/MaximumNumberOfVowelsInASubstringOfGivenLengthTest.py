import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MaximumNumberOfVowelsInASubstringOfGivenLengthTask import maxVowels


class MaximumNumberOfVowelsInASubstringOfGivenLengthTests(unittest.TestCase):

    def test_first_case(self):
        s = "abciiidef"
        k = 3
        expected_output = 3
        result = maxVowels(self, s,k)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        s = "aeiou"
        k = 2
        expected_output = 2
        result = maxVowels(self, s,k)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        s = "leetcode"
        k = 3
        expected_output = 2
        result = maxVowels(self, s,k)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#MaximumNumberOfVowelsInASubstringOfGivenLengthTask