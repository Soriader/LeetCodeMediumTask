import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.SearchInRotatedSortedArrayTask import search


class SearchInRotatedSortedArrayTests(unittest.TestCase):

    def test_first_case(self):
        n = [4,5,6,7,0,1,2]
        target = 0
        expected_output = 4
        result = search(self, n, target)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [4,5,6,7,0,1,2]
        target = 3
        expected_output = -1
        result = search(self, n, target)
        self.assertEqual(result, expected_output)
    def test_third_case(self):
        n = [1]
        target = 0
        expected_output = -1
        result = search(self, n, target)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
