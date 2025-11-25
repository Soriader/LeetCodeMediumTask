import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.LongestConsecutiveSequenceTask import longestConsecutive


class LongestConsecutiveSequenceTests(unittest.TestCase):

    def test_first_case(self):
        n = [100,4,200,1,3,2]
        expected_output = 4
        result = longestConsecutive(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [0,3,7,2,5,8,4,6,0,1]
        expected_output = 9
        result = longestConsecutive(self, n)
        self.assertEqual(result, expected_output)


    def test_third_case(self):
        n = [1,0,1,2]
        expected_output = 3
        result = longestConsecutive(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#LongestConsecutiveSequenceTask