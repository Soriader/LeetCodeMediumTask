import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CountMentionsPerUserTask import countMentions


class CountMentionsPerUserTests(unittest.TestCase):

    def test_first_case(self):
        number_of_users = 2
        events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
        expected_output = [2,2]
        result = countMentions(self, number_of_users, events)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        number_of_users = 2
        events = [["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "12", "ALL"]]
        expected_output = [2,2]
        result = countMentions(self, number_of_users, events)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
        number_of_users = 2
        expected_output = [0,1]
        result = countMentions(self, number_of_users, events)
        self.assertEqual(result, expected_output)
if __name__ == '__main__':
    unittest.main()


#CountMentionsPerUserTask