from __future__ import division
import logging
import time

import numpy as np

from active_learning.active_learning_rank_svm.active_ranking_interface import *
import inspect
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
import pandas as pd
import warnings
import collections
import itertools as IT
from active_learning.svm_rank_algorithms.svmlight import *
from active_learning.svm_rank_algorithms.libsvm_rank import *
from active_learning.svm_rank_algorithms.svmlight_rank import *
from active_learning.svm_rank_algorithms.pysofia_rank import *
from active_learning.active_learning_rank_svm.active_sampling import *

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


class RankSVMActiveLearnerFUncartain(ActiveRankingInterface):
    """
    Implementation of an active learning method for RankSVM that order values based on f(x_i - x_j) value measuring how
    much the ranking function is unsure on the ordering of pairs
    """

    def __init__(self, model):
        super(RankSVMActiveLearnerFUncartain, self).__init__(model)

    def get_rank_and_active(self, tr_data_x, tr_data_y, rank_data, max_to_rank=10, max_best_scored=10):
        start = time.time()
        self.ra_model.fit(tr_data_x, tr_data_y) # fitting model
        to_rank = self.generate_matrix_data(rank_data) # with the dataset above we compute the active score

        x = self.rank_data(rank_data)  # ranking
        best_scored = x.sort('rank', ascending=[False]).index.values
        end = time.time()

        elapsed = end - start
        logging.info("\tElapsed Time of " + inspect.stack()[0][3] + " " + str(elapsed) + " seconds")
        return to_rank[0: max_to_rank], best_scored[0: max_best_scored], x



    def fit(self, training_X, training_y):
        start  = time.time()
        logging.info("Fitting RankSVM")
        self.ra_model.fit(training_X, training_y)
        end = time.time()

        elapsed = end - start

    def rank_data(self, X):
        start  = time.time()

        X["rank"] = self.ra_model.rank(X)
        end = time.time()

        elapsed = end - start
        logging.info("\tElapsed Time of " + inspect.stack()[0][3] + " " + str(elapsed) + " seconds")
        return X

    def data_frame_to_matrix_permutation_difference(self, x):
        start  = time.time()
        association_ids = x.index.values
        x = x.as_matrix()
        diff = []
        id_one = []
        id_two = []
        for i, val in enumerate(x):
            for j, dal in enumerate(x):
                if(j<i):
                    continue
                if(i!=j):
                    id_one.append(association_ids[i])
                    id_two.append(association_ids[j])
                    diff.append(val - dal)
        end = time.time()

        elapsed = end - start
        logging.info("\tElapsed Time of " + inspect.stack()[0][3] + " " + str(elapsed) + " seconds")
        return id_one, id_two, diff

    def generate_matrix_data(self, predicting):
        predicting = predicting.sample(frac=1, replace=True)

        id_one, id_two, matrix = self.data_frame_to_matrix_permutation_difference(predicting)
        #rank the matrix to get the w_x
        rank = self.ra_model.rank(pd.DataFrame(matrix))
        df = pd.DataFrame(matrix)
        df["first_index"] = id_one
        df["second_index"] = id_two

        df["rank"] = rank
        df = df.sort('rank', ascending=[True])

        first = df.first_index.values.tolist()
        second = df.second_index.values.tolist()
        return np.array(list(set(first + (second))))





