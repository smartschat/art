__author__ = 'smartschat'


class Score:
    def __init__(self, score):
        self.values = [float(val) for val in score]

    def __str__(self):
        return " ".join([str(val) for val in self.values])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.values == other.values
        else:
            return False

    def __hash__(self):
        return hash(self.values)


class Scores:
    def __init__(self, scores):
        self.scores = scores

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.scores == other.scores
        else:
            return False

    def __hash__(self):
        return hash(self.scores)

    def __len__(self):
        return len(self.scores)

    def __iter__(self):
        return iter(self.scores)

    def append(self, score):
        self.scores.append(score)

    @staticmethod
    def from_file(file):
        scores = []
        for line in file.readlines():
            scores.append(Score(line.split()))
        return Scores(scores)

    def __str__(self):
        return "\n".join([str(score) for score in self.scores])
