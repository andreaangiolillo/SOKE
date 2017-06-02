from __future__ import division
import logging
import math
import operator

import numpy as np

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

from active_ranking_interface import *

import warnings
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)


class RankSVMActiveLearner(ActiveRankingInterface):
    def __init__(self, model):
        super(RankSVMActiveLearner, self).__init__(model)
        #logging.info("Init RankSVM")
        self.lamb = 1
        self.min_r = 0
        self.max_r = 2
        self.other_threshold = 0
        self.index_threshold = 0
        self.threshold_rank = 0

    def get_rank_and_active(self, tr_data_x, tr_data_y, rank_data, max_to_rank=11, max_best_scored=11):
        start = time.time()
        self.ra_model.fit(tr_data_x, tr_data_y) # fitting model
        predicting = self.rank(rank_data.astype('float')) # ranking active with sampled dataset
        predicting = self.find_to_label(predicting) # with the dataset above we compute the active score
        best_scored = predicting.sort('rank', ascending=[False]).index.values
        to_rank = predicting.sort('active_learning_score', ascending=[False]).index.values
        end = time.time()
        elapsed = end - start
        #logging.info("\tElapsed Time " + str(elapsed) + " seconds")

        return to_rank[0: max_to_rank], best_scored[0: max_best_scored], predicting

    def fit(self, training_X, training_y):
        #logging.info("Fitting RankSVM")
        self.ra_model.fit(training_X, training_y)

    def rank(self, X):
        #logging.info("Ranking RankSVM")
        rank = self.ra_model.rank(X)
        rank = np.array(rank)
        index_of_threshold = (np.array(rank) < 0).argmax()
        #print rank
        #raw_input()
        X['f_value'] = np.array(rank)
        X = X.sort("f_value", ascending=[True])
        array_length = rank.size
        X['rank'] = np.arange(1, array_length + 1)
        self.other_threshold = X.iloc[index_of_threshold]["rank"] + 1/2
        #raw_input(self.other_threshold)
        self.max_r = len(rank) + 1
        return X

    @staticmethod
    def compute_threshold(X):
        """
        :param X:
        :return: indice, k dell'associazione e valore
        """
        K = X.sort("rank", ascending=[True]) #ordine crescente
        row = K["f_value"].values
        indexes = K.index.values
        possible = {}
        for i in range(0, row.size - 1):
            possible[i] = (np.absolute(row[i] - row[i+1]))
        key, value = max(possible.iteritems(), key=operator.itemgetter(1))
        return key, indexes[key], row[key]

    def posterior_estimation(self, X):
        pos_estimation = []
        neg_estimation = []
        X = X.sort("f_value")
        self.index_threshold, observation_index, valore_corretto= self.compute_threshold(X)
        #print X.loc[self.index_threshold]["rank"]
        self.threshold_rank = X.ix[observation_index]["f_value"]

        for index, row in X.iterrows():
            pos_estimation.append(self.inner_posterior_estimation(1, row["f_value"]))
            neg_estimation.append(self.inner_posterior_estimation(-1, row["f_value"]))
        X["pos_estimation"] = np.array(pos_estimation)
        X["neg_estimation"] = np.array(neg_estimation)

        return X

    def inner_posterior_estimation(self, y, value):
        return 1/(1 + math.exp(-y * value + self.threshold_rank))

    def find_to_label(self, X):
        scores = []
        X = self.posterior_estimation(X)
        for index, row in X.iterrows():
            scores.append(self.compute_estimation(row["pos_estimation"],  row["neg_estimation"], row["rank"]))
        X["active_learning_score"] = np.array(scores)
        return X

    def compute_estimation(self, pos_estimation, neg_estimation, r_k):
        pos_multiplier = (1/2 - (r_k - self.index_threshold))
        neg_multiplier = (1/2 + (r_k - self.index_threshold))

        if pos_multiplier < 0:
            pos_multiplier = 0
        if neg_multiplier < 0:
            neg_multiplier = 0

        pos_multiplier = pos_multiplier/(np.absolute(self.min_r - self.index_threshold))
        neg_multiplier = neg_multiplier/(np.absolute(self.max_r -  self.index_threshold))

        final_score = pos_estimation*pos_multiplier*(1-self.lamb) + neg_estimation*neg_multiplier*self.lamb
        return final_score

