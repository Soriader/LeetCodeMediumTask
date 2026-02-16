import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MultiplyStringsTask import multiply


class MultiplyStringsTests(unittest.TestCase):

    def test_first_case(self):
        num1 = "2"
        num2 = "3"
        expected_output = "6"
        result = multiply(self, num1, num2)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        num1 = "123"
        num2 = "456"
        expected_output = "56088"
        result = multiply(self, num1, num2)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
