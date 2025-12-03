import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.BullsAndCowsTask import getHint


class BullsAndCowsTaskTests(unittest.TestCase):

    def test_first_case(self):
        secret = "1807"
        guess = "7810"
        expected_output = "1A3B"
        result = getHint(self, secret, guess)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        secret = "1123"
        guess = "0111"
        expected_output = "1A1B"
        result = getHint(self, secret, guess)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

#BullsAndCowsTask