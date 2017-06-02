from __future__ import division

from sklearn import svm

from active_learning.rank_learning import *
from active_learning.active_learning_rank_svm.rank_learning_uncertainty import *

__author__ = 'vinid'


class CustomSvm:

    def __init__(self):
        self.model = 0
        """:type : svm.LinearSVC """
    # train method
    def fit(self, x, y):
        panda = pd.DataFrame()

        for index, row in x.iterrows():
            for jndex, jrow in x.iterrows():
                if(y.ix[[index]].values[0] !=  y.ix[[jndex]].values[0]):
                    rows = row - jrow
                    rows["score"] = np.sign(y.ix[[index]].values[0] - y.ix[[jndex]].values[0])
                    panda = panda.append(rows, ignore_index=True)

        training_y = panda["score"].as_matrix()
        training = panda.drop("score", 1).as_matrix()

        cls = svm.LinearSVC(loss="hinge")

        self.model = cls.fit(training, training_y)

    def rank(self, x, y=0):
        prediction = np.dot(x, self.model.coef_.T)
        return prediction

def data_frame_to_matrix_permutation_difference(x):
    association_ids = x.index.values
    x = x.as_matrix()
    diff = []
    id_one = []
    id_two = []
    for i, val in enumerate(x):
        for j, dal in enumerate(x):
            if(association_ids[i]!=association_ids[j]):
                id_one.append(association_ids[i])
                id_two.append(association_ids[j])
                diff.append(val - dal)
    return id_one, id_two, diff
