
import logging
import time

import numpy as np

from active_ranking_interface import *
import inspect
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
import pandas as pd
import warnings
import collections
import itertools as IT
from svmlight import *
from libsvm_rank import *
from svmlight_rank import *
from pysofia_rank import *
from active_sampling import *

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


class RankSVMActiveLearnerUncertainty(ActiveRankingInterface):
    """
    Implementation of an active learning method for RankSVM that order values based on an algorithm defined in
    the papaer Acive Learning to Rank Using Pairwise Supervision, 2013, Buyue Qian
    """

    def __init__(self, model):
        super(RankSVMActiveLearnerUncertainty, self).__init__(model)

    def get_rank_and_active(self, tr_data_x, tr_data_y, rank_data, max_to_rank=10, max_best_scored=10):
        start = time.time()
        self.ra_model.fit(tr_data_x, tr_data_y) # fitting model
        predicting = self.active_rank(rank_data.astype('float')) # ranking active with sampled dataset
        to_rank = self.find_to_label(predicting) # with the dataset above we compute the active score

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

    def active_rank(self, X):
        start  = time.time()
        predicting = X.sample(frac=1, replace=True)

        id_one, id_two, dif = self.data_frame_to_matrix_permutation_difference(predicting)

        panda = pd.DataFrame()
        panda["first_id"] = id_one
        panda["second_id"] = id_two
        start_inside  = time.time()
        panda["rank"] = self.ra_model.rank(np.array(dif))
        end_inside = time.time()

        elapsed = end_inside - start_inside
        panda = panda.sort('rank', ascending=[False])
        end = time.time()

        elapsed = end - start
        return panda

    def find_to_label(self, panda):
        start  = time.time()
        lista = []
        split = {}
        panda = panda.sort('first_id', ascending=[False])
        indexes = np.unique(panda.first_id.values)
        for i in indexes:
            split[i] = (panda[panda.first_id.isin([i])])
        first_start = time.time()

        for i, row in enumerate(panda.itertuples()):
            index, first, _, rank = row

            temp_panda = split[first]

            sum = np.sum(temp_panda["rank"].values)

            value = rank / sum

            lista.append(value * np.log(value))

        first_end = time.time()
        panda["normalized_distance"] = lista
        unique = panda["first_id"].unique()


        global_unc = []
        second_start = time.time()
        for i in unique:
            temp_panda = panda.loc[panda['first_id'] == i]
            global_unc.append(temp_panda["normalized_distance"].sum())
        second_end = time.time()
        global_unc = map(lambda x : x*-1, global_unc)
        dictionary = dict(zip(unique, global_unc))

        final_score = []
        third_start = time.time()
        for row in panda.itertuples():
            first, second, rank, _ = row
            final_score.append((1/rank))
        third_end = time.time()
        panda["final_score"] = final_score
        panda["rank"] = 1/panda["rank"]
        panda = panda.sort('rank', ascending=[False])

        first = panda.first_id.values.tolist()
        second = panda.second_id.values.tolist()
        end = time.time()

        elapsed = end - start

        return np.array(list(set(first + (second))))

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








