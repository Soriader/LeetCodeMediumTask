import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.RotateImageTask import rotate

class RotateImageTests(unittest.TestCase):

    def test_first_case(self):
        matrix = [[1,2],[3,4]]
        expected_output = [[3,1],[4,2]]
        result = rotate(self, matrix)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected_output = [[7,4,1],[8,5,2],[9,6,3]]
        result = rotate(self, matrix)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        expected_output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        result = rotate(self, matrix)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
