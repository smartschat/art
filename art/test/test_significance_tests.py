import os
import unittest

from art import aggregators
from art import scores
from art import significance_tests


__author__ = 'smartschat'


class TestApproximateRandomizationTest(unittest.TestCase):
    def test_run(self):
        directory = os.path.dirname(os.path.realpath(__file__))
        test = significance_tests.ApproximateRandomizationTest(
            scores.Scores.from_file(open(directory +
                                         "/resources/example_scores")),
            scores.Scores.from_file(open(
                directory + "/resources/example_scores_numerator_always_0")),
            aggregators.enum_sum_div_by_denom_sum
        )
        self.assertGreater(test.run(), 0)

    def test_run_with_same(self):
        directory = os.path.dirname(os.path.realpath(__file__))
        test = significance_tests.ApproximateRandomizationTest(
            scores.Scores.from_file(open(directory +
                                         "/resources/example_scores")),
            scores.Scores.from_file(open(directory +
                                         "/resources/example_scores")),
            aggregators.enum_sum_div_by_denom_sum
        )
        self.assertEqual(1.0, test.run())


if __name__ == '__main__':
    unittest.main()
