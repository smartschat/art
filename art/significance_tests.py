from __future__ import division
import math
import random

from art.scores import Scores


__author__ = 'smartschat'


class ApproximateRandomizationTest:
    def __init__(self, system1_file, system2_file, aggregator, trials=1000):
        self.system1_scores = Scores.from_file(system1_file)
        self.system2_scores = Scores.from_file(system2_file)
        self.aggregator = aggregator
        self.trials = trials

    def run(self):
        absolute_difference = math.fabs(self.aggregator(self.system1_scores) - self.aggregator(self.system2_scores))
        shuffled_was_at_least_as_high = 0

        for i in range(0, self.trials):
            pseudo_system1_scores = Scores([])
            pseudo_system2_scores = Scores([])

            for score1, score2 in zip(self.system1_scores, self.system2_scores):
                if random.randint(0, 1) == 0:
                    pseudo_system1_scores.append(score1)
                    pseudo_system2_scores.append(score2)
                else:
                    pseudo_system1_scores.append(score2)
                    pseudo_system2_scores.append(score1)

            pseudo_difference = math.fabs(self.aggregator(pseudo_system1_scores)
                                          - self.aggregator(pseudo_system2_scores))

            if pseudo_difference >= absolute_difference:
                shuffled_was_at_least_as_high += 1

        significance_level = (shuffled_was_at_least_as_high + 1) / (self.trials + 1)

        return significance_level