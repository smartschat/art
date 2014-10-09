import math

__author__ = 'smartschat'


def average(scores):
    return math.fsum([score.values[0] for score in scores])/len(scores)


def enum_sum_div_by_denom_sum(scores):
    return math.fsum([score.values[0] for score in scores])/math.fsum(
        [score.values[1] for score in scores])


def f1(scores):
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