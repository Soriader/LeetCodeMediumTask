import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.RepeatedDNASequencesTask import findRepeatedDnaSequences


class GreatestSumDivisibleByThreeTests(unittest.TestCase):

    def test_first_case(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        expected_output = ["AAAAACCCCC","CCCCCAAAAA"]
        result = findRepeatedDnaSequences(self, s)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        s = "AAAAAAAAAAAAA"
        expected_output = ["AAAAAAAAAA"]
        result = findRepeatedDnaSequences(self, s)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
