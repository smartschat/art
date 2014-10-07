import os
import aggregators
from approximate_randomization_test import ApproximateRandomizationTest

__author__ = 'smartschat'

import unittest


class TestApproximateRandomizationTest(unittest.TestCase):
    def test_run(self):
        directory = os.path.dirname(os.path.realpath(__file__))
        test = ApproximateRandomizationTest(
            open(directory + "/resources/example_scores"),
            open(directory + "/resources/example_scores_numerator_always_0"),
            aggregators.enum_sum_div_by_denom_sum
        )
        self.assertEqual(1/1001, test.run())


if __name__ == '__main__':
    unittest.main()
