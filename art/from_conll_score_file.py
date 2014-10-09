import sys

from art.scores import Score
from art.scores import Scores

__author__ = 'smartschat'


def get_numerators_and_denominators(score_file):
    scores_from_file = Scores()

    for line in score_file.readlines():
        if line == "====== TOTALS =======":
            break
        elif line.startswith("Recall:"):
            entries = line.split()
            recall_numerator = entries[1].replace("(", "")
            recall_denominator = entries[3].replace(")", "")
            precision_numerator = entries[6].replace("(", "")
            precision_denominator = entries[8].replace(")", "")

            scores_from_file.append(
                Score([
                    recall_numerator,
                    recall_denominator,
                    precision_numerator,
                    precision_denominator])
            )

    return scores_from_file


if __name__ == "__main__":
    conll_scores = get_numerators_and_denominators(open(sys.argv[1]))
    print(conll_scores)
