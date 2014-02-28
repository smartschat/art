import math

__author__ = 'smartschat'


class Score:
    def __init__(self, score):
        self.values = [float(val) for val in score]

    def __str__(self):
        return " ".join([str(val) for val in self.values])


class Scores:
    def __init__(self):
        self.scores = []

    def __iter__(self):
        return iter(self.scores)

    def append(self, score):
        self.scores.append(score)

    def get_f1(self):
        recall = math.fsum(score.values[0] for score in self.scores)/math.fsum(score.values[1] for score in self.scores)
        precision = math.fsum(score.values[2] for score in self.scores)/math.fsum(score.values[3] for score in self.scores)
        f1 = 2*recall*precision/(recall+precision)

        return f1

    def __str__(self):
        return "\n".join([str(score) for score in self.scores])
