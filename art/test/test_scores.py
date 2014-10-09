import os
import unittest

from art.scores import Score
from art.scores import Scores

__author__ = 'smartschat'


class TestScores(unittest.TestCase):
    def test_from_file(self):
        expected_scores = Scores(
            [
                Score([2, 3]),
                Score([4, 12]),
                Score([22, 500]),
                Score([3.1, 4.355]),
            ]
        )
        self.assertEqual(expected_scores, Scores.from_file(open(
            os.path.dirname(os.path.realpath(__file__)) +
        "/resources/example_scores")))


if __name__ == '__main__':
    unittest.main()
