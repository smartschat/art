"""Contains functions to aggregate scores over a corpus."""

import math

__author__ = 'smartschat'


def average(scores):
    """Compute the average of all scores.

    Args:
        scores: A Scores object. Each score in scores should contain only one
                number.

    Returns:
        The average of all numbers in scores.
    """
    return math.fsum([score.values[0] for score in scores])/len(scores)


def enum_sum_div_by_denom_sum(scores):
    """Sum up the first entry of all scores, then sum up the second entry.
    Divide the first sum by the second sum.

    Args:
        scores: A Scores object. Each score in scores should contain two
                numbers.

    Returns:
        The sum of the first entry of each score in scores, divided by the sum
        of the second entry of each score in scores.
    """
    return math.fsum([score.values[0] for score in scores])/math.fsum(
        [score.values[1] for score in scores])


def f_1(scores):
    """Compute the corpus-wide F1 score represented by the scores.

    Each score should contain four entries. Consider:
        - first/second entry numerator/denominator for recall,
        - third/fourth entry numerator and denominator for precision.

    Then define r = sum(first entries)/sum(second entries) and
    p = sum(third entries)/sum(fourth entries)

    The F1 score is then computed as F1 = 2pr/(p+r).

    Args:
        scores: A Scores object. Each score in scores should contain four
                numbers.

    Returns:
        The corpus-wide F1 score.
    """
    first_component = math.fsum(
        [score.values[0] for score in scores]
    )/math.fsum(
        [score.values[1] for score in scores])

    second_component = math.fsum(
        [score.values[2] for score in scores]
    )/math.fsum(
        [score.values[3] for score in scores])

    return 2 * first_component * second_component / (
        first_component + second_component)
