"""Transform CoNLL scorer files into a suitable format."""

from art.scores import Score
from art.scores import Scores

__author__ = 'smartschat'


def get_numerators_and_denominators(score_file):
    """Transform score files obtained by the CoNLL scorer.

    This function transforms files obtained by the reference coreference
    scorer (https://code.google.com/p/reference-coreference-scorers/) into
    a format suitable for performing significance testing for differences in
    F1 score.

    Args
        score_file: A file obtained via running the reference coreference
                    scorer for a single metric, as in
                     $ perl scorer.pl muc key response > conll_score_file

    Returns
        A Scores objects containing numerator/denominator for recall and
        precision for each document described in the score file.
    """
    scores_from_file = Scores()

    temp_mapping = {}

    for line in score_file.readlines():
        if line == '====== TOTALS =======':
            break
        elif line.startswith("("):
            identifier = line.strip()
        elif line.startswith('Recall:'):
            entries = line.split()
            recall_numerator = entries[1].replace("(", "")
            recall_denominator = entries[3].replace(")", "")
            precision_numerator = entries[6].replace("(", "")
            precision_denominator = entries[8].replace(")", "")

            temp_mapping[identifier] = [
                    recall_numerator,
                    recall_denominator,
                    precision_numerator,
                    precision_denominator
            ]

            identifier = None

    for identifier in sorted(temp_mapping.keys()):        
        scores_from_file.append(
            Score(temp_mapping[identifier])
        )

    return scores_from_file
