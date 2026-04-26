import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.DetectCyclesIn2DGridTask import containsCycle


class DetectCyclesIn2DGridTests(unittest.TestCase):

    def test_first_case(self):
        n = [
        ["a", "a", "a", "a"],
        ["a", "b", "b", "a"],
        ["a", "b", "b", "a"],
        ["a", "a", "a", "a"]
    ]
        expected_output = True
        result = containsCycle(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [
        ["c", "c", "c", "a"],
        ["c", "d", "c", "c"],
        ["c", "c", "e", "c"],
        ["f", "c", "c", "c"]
    ]
        expected_output = True
        result = containsCycle(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = [
        ["a", "b", "b"],
        ["b", "z", "b"],
        ["b", "b", "a"]
    ]
        expected_output = False
        result = containsCycle(self, n)
        self.assertEqual(result, expected_output)
