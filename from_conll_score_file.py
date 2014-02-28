import sys
from scores import Score, Scores

__author__ = 'smartschat'


def get_numerators_and_demoniators(score_file):
    scores = Scores()

    for line in score_file.readlines():
        if line == "====== TOTALS =======":
            break
        elif line.startswith("Recall:"):
            entries = line.split()
            recall_numerator = entries[1].replace("(", "")
            recall_denominator = entries[3].replace(")", "")
            precision_numerator = entries[6].replace("(", "")
            precision_denominator = entries[8].replace(")", "")

            scores.append(Score([recall_numerator, recall_denominator, precision_numerator, precision_denominator]))

    return scores


if __name__ == "__main__":
    scores = get_numerators_and_demoniators(open(sys.argv[1]))
    print(scores)
