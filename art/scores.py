""" Contains classes fore managing scores and lists of scores."""

__author__ = 'smartschat'


class Score(object):
    """A score for an individual document.

    Attributes:
        values: A list of floats, which constitutes the score for the document
                under consideration.
    """
    def __init__(self, score):
        """Create a score from a list of numbers.

        Args:
            score: a list of numbers.
        """
        self.values = [float(val) for val in score]

    def __str__(self):
        return ' '.join([str(val) for val in self.values])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.values == other.values
        else:
            return False

    def __hash__(self):
        return hash(self.values)


class Scores(object):
    """A collection of scores for a set of documents (a corpus).

    Attributes:
        scores: A list of Score objects.
    """
    def __init__(self, scores=None):
        """Init from a list of scores.

        Args:
            scores: A list of Score objects.
        """
        if not scores:
            scores = []

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

    def __str__(self):
        return '\n'.join([str(score) for score in self.scores])

    def append(self, score):
        """Append a score.

        Args:
            score: A Score object.
        """
        self.scores.append(score)

    @staticmethod
    def from_file(file):
        """Create a Scores object from a file, where each line in the file
        describes a score for one document.

        The file should contain a list of numbers in each line, seperated by
        white space. The number of entries in each line should match. An
        example file looks like the following:

            1 2 3
            4 3 2.5
            11 1 0

        Args:
            file: A file containing a list of scores.
        """

        scores = []
        for line in file.readlines():
            scores.append(Score(line.split()))
        return Scores(scores)
