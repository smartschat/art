import unittest

from art import aggregators
from art.scores import Score
from art.scores import Scores

__author__ = 'smartschat'


class TestAggregators(unittest.TestCase):
    def test_average(self):
        scores_for_average = Scores(
            [
                Score([1]),
                Score([5]),
                Score([3]),
                Score([0]),
            ]
        )
        self.assertEqual(9.0 / 4, aggregators.average(scores_for_average))

    def test_enum_sum_div_by_denom_sum(self):
        scores_for_enum_sum_div_by_denom_sum = Scores(
            [
                Score([2, 3]),
                Score([4, 12]),
                Score([22, 500]),
                Score([3.1, 4.355]),
            ]
        )
        self.assertEqual(31.1 / 519.355,
                         aggregators.enum_sum_div_by_denom_sum(
                             scores_for_enum_sum_div_by_denom_sum))

    def test_f_1(self):
        scores_for_f_1 = Scores(
            [
                Score([2, 3, 7, 8]),
                Score([4, 12, 33, 50]),
                Score([22, 500, 12.3, 15.9]),
                Score([3.1, 4.355, 1, 2]),
            ]
        )

        recall = 31.1 / 519.355
        precision = 53.3 / 75.9
        f_1 = 2 * recall * precision / (recall + precision)

        self.assertEqual(f_1, aggregators.f_1(scores_for_f_1))

if __name__ == '__main__':
    unittest.main()
