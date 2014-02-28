import random
import sys
import math
from scores import Score, Scores

__author__ = 'smartschat'


def get_scores(system_file):
    scores = Scores()
    for line in system_file.readlines():
        scores.append(Score(line.split()))
    return scores


if __name__ == "__main__":
    system1_file = open(sys.argv[1])
    system2_file = open(sys.argv[2])

    system1_scores = get_scores(system1_file)
    system2_scores = get_scores(system2_file)

    absolute_difference = math.fabs(system1_scores.get_f1() - system2_scores.get_f1())
    trials = 1000
    shuffled_was_higher = 0

    for i in range(0, trials):
        pseudo_system1_scores = Scores()
        pseudo_system2_scores = Scores()

        for score1, score2 in zip(system1_scores, system2_scores):
            if random.randint(0, 1) == 0:
                pseudo_system1_scores.append(score1)
                pseudo_system2_scores.append(score2)
            else:
                pseudo_system1_scores.append(score2)
                pseudo_system2_scores.append(score1)

        pseudo_difference = math.fabs(pseudo_system1_scores.get_f1() - pseudo_system2_scores.get_f1())

        if pseudo_difference >= absolute_difference:
            shuffled_was_higher += 1

    significance_level = (shuffled_was_higher+1)/(trials+1)

    print(significance_level)
