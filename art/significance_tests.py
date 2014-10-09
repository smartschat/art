"""Contains significance tests for differences between systems."""

from __future__ import division
import math
import random

from art.scores import Scores

__author__ = 'smartschat'


class ApproximateRandomizationTest(object):
    """A paired two-sided approximate randomization test.

    This class allows performing a paired two-sided approximate randomization
    test to assess the statistical significance of the difference in
    performance between two systems which are run and measured on the same
    corpus.

    Attributes:
        system1_scores: A Scores object, which represents the scores of the
                        first system under consideration.
        system2_scores: A Scores object, which represents the scores of the
                        second system under consideration.
        aggregator: An aggregator function, which aggregates all scores for
                        individual documents to obtain a score for the whole
                        corpus.
        trials: The number of iterations during the test.
    """
    def __init__(self,
                 system1_scores,
                 system2_scores,
                 aggregator,
                 trials=10000):
        """Inits a paired two-sided approximate randomization test.

        Args:
            system1_scores: A Scores object, which represents the scores of the
                            first system under consideration.
            system2_scores: A Scores object, which represents the scores of the
                            second system under consideration.
            aggregator: An aggregator function, which aggregates all scores for
                            individual documents to obtain a score for the
                            whole corpus.
            trials: The number of iterations during the test. Defaults to
                            10000.
        """
        self.system1_scores = system1_scores
        self.system2_scores = system2_scores
        self.aggregator = aggregator
        self.trials = trials

    def run(self):
        """Compute the statistical significance of a difference between
        the systems via a paired two-sided approximate randomization test.

        Returns:
            An approximation of the probability of observing corpus-wide
            differences in scores at least as extreme as observed here, when
            there is no difference between the systems.
        """

        absolute_difference = math.fabs(
            self.aggregator(self.system1_scores) -
            self.aggregator(self.system2_scores))
        shuffled_was_at_least_as_high = 0

        for i in range(0, self.trials):
            pseudo_system1_scores = Scores()
            pseudo_system2_scores = Scores()

            for score1, score2 in zip(self.system1_scores,
                                      self.system2_scores):
                if random.randint(0, 1) == 0:
                    pseudo_system1_scores.append(score1)
                    pseudo_system2_scores.append(score2)
                else:
                    pseudo_system1_scores.append(score2)
                    pseudo_system2_scores.append(score1)

            pseudo_difference = math.fabs(
                self.aggregator(pseudo_system1_scores) -
                self.aggregator(pseudo_system2_scores))

            if pseudo_difference >= absolute_difference:
                shuffled_was_at_least_as_high += 1

        significance_level = (shuffled_was_at_least_as_high + 1) / (
            self.trials + 1)

        return significance_level
