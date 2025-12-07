import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.FruitIntoBasketsTask import totalFruit


class FruitIntoBasketsTests(unittest.TestCase):

    def test_first_case(self):
        fruits = [1,2,1]
        expected_output = 3
        result = totalFruit(self, fruits)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        fruits = [0,1,2,2]
        expected_output = 3
        result = totalFruit(self, fruits)
        self.assertEqual(result, expected_output)
    def test_third_case(self):
        fruits = [1,2,3,2,2]
        expected_output = 4
        result = totalFruit(self, fruits)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#FruitIntoBasketsTask