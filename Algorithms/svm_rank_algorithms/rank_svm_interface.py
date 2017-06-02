__author__ = 'vinid'

class RankSvmInterface:
    """
    Interface class for rank svm algorithms
    """

    def fit(self, x, y):
        raise NotImplementedError("Should have implemented this")

    def rank(self, x):
        raise NotImplementedError("Should have implemented this")
