import numpy as np

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib
from sklearn.metrics import *
import os

from sklearn import mixture


class DirichletClustering():

    def __init__(self):
        self.location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) + "/clustering_files/"

    def dirichlet(self, df, user, article):
        df_scaled = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns, index=df.index)
        dpgmm = mixture.DPGMM(n_iter=10000, verbose=False, n_components=10, alpha=1000, covariance_type ='diag', tol=1e-20)
        dpgmm.fit(df_scaled)
        joblib.dump(dpgmm, self.location + 'diri_user_' + user + '_article_' + article + '.pkl')

    def predict(self, df, user, article):
        df_scaled = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns, index=df.index)
        dpgmm = joblib.load(self.location + 'diri_user_' + user + '_article_' + article + '.pkl')
        predict = dpgmm.predict(df_scaled)

        cluster_number = set(predict)
        df_scaled['cluster'] = predict

        clusters = []

        for i in cluster_number:
            clusters.append(df_scaled[df_scaled["cluster"] == i])

        distances = []

        if len(cluster_number) == 1:
            for i in clusters:
                distance_loc_min, _ = (pairwise_distances_argmin_min(np.array(i.mean()), i))
                distances.append((i.iloc[distance_loc_min]).index[0])

                distance_loc_max = pairwise_distances(np.array(i.mean()),  i, metric="euclidean").argmax()
                distance_loc_max = [distance_loc_max]
                distances.append((i.iloc[distance_loc_max]).index[0])

                distance_loc = pairwise_distances((i.var()), i, metric="euclidean").argmin()
                distance_loc = [distance_loc]
                distances.append((i.iloc[distance_loc]).index[0])
        else:
            for i in clusters:
                distance_loc, _ = (pairwise_distances_argmin_min(np.array(i.mean()), i))
                distances.append((i.iloc[distance_loc]).index[0])
        return distances


    def data_frame(self, query, columns):
        """
        Takes a sqlalchemy query and a list of columns, returns a dataframe.
        """
        def make_row(x):
            return dict([(c, getattr(x, c)) for c in columns])
        return pd.DataFrame([make_row(x) for x in query])

