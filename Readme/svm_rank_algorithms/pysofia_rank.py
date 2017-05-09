__author__ = 'vinid'


from pysofia.compat import RankSVM
import numpy as np
from sklearn.cross_validation import ShuffleSplit
from sklearn.grid_search import GridSearchCV

class PySofiaRank():
    """
    Implements and SVMrank algorithm using pysofia that is a python wrapper for ml-sofia lib.
    Uses cross validation internally
    """
    # train method
    def fit(self, x, y):
        rs = RankSVM(max_iter=200)
        cv = ShuffleSplit(x.shape[0], n_iter=10, test_size=0.2, random_state=0)
        classifier = GridSearchCV(estimator=rs, param_grid={"max_iter" : [200]},  cv=cv)
        #print training_X, training_y
        classifier.fit(x, y)
        self.model = classifier.best_estimator_

    def rank(self, x):
        rank = self.model.predict(x)
        rank = np.array(rank)
        return rank




