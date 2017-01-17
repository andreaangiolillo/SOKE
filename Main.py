import numpy as np
from sklearn.utils.testing import assert_almost_equal
import Preprocessing
import Clustering_dirichlet
from sklearn.linear_model import SGDClassifier
import pandas as pd
#from dataset_creation import DataSetCreator
#from lightning.ranking import KernelPRank

#from svmlight import *
#from active_global_local_uncertainty import *
import logging
import time


        
#http://stackoverflow.com/questions/23056460/does-the-svm-in-sklearn-support-incremental-online-learning
def learning() :
    
    score_eval = Preprocessing.extract_user_evaluated_association()
    
    ids = clustering(130, 1)
    clf = SGDClassifier(loss="log", penalty="l2")
    clf.partial_fit(data[i],targets[i], classes=np.unique(targets))
    predictions = clf.predict(data[i+1: len(data)])
    d = {}
    for prediction in predictions:
        pass
                    
                #test


def ranking(user, article):
        
        all_score_eval = Preprocessing.extract_user_evaluated_association() 
        associations_score_eval = []
        [associations_score_eval.append(row) for row in all_score_eval if ((int(row[0]) == int(user)) and (int(row[3]) == int(article))) ]
        associations_score_eval = np.array(associations_score_eval)# list to numpy array

                     
        #associations_score = s.query(AssociationScore).filter(AssociationScore.article_id == article)
        all_score = Preprocessing.extract_association_score()
        associations_score = []
        [associations_score.append(row) for row in all_score if int(row[1]) == int(article)]
        associations_score = np.array(associations_score) #list to numpy array
        associations_score = associations_score[:, [0, 3, 4, 5, 6, 8, 9]]
        print associations_score
        #TODO
        ##http://stackoverflow.com/questions/20763012/creating-a-pandas-dataframe-from-a-numpy-array-how-do-i-specify-the-index-colum
#         df = data_frame(associations_score,
#                             [c for c in ["association_id",
#                                          "localPageRankMean",
#                                          "path_informativeness",
#                                          "path_pattern_informativeness",
#                                          "localHubMean",
#                                          "relevance_score",
#                                          "rarity_score"]])
#         df = df.set_index("association_id")
    


def clustering(article, user):
        all_score_eval = Preprocessing.extract_user_evaluated_association() 
        associations_score_eval = []
        [associations_score_eval.append(row) for row in all_score_eval if ((int(row[0]) == int(user)) and (int(row[3]) == int(article))) ]
        associations_score_eval = np.array(associations_score_eval)# list to numpy array

                     
        #associations_score = s.query(AssociationScore).filter(AssociationScore.article_id == article)
        all_score = Preprocessing.extract_association_score()
        associations_score = []
        [associations_score.append(row) for row in all_score if int(row[1]) == int(article)]
        associations_score = np.array(associations_score) #list to numpy array
        associations_score = associations_score[:, [0, 5, 8, 9, 6, 3, 4]]
        #print associations_score
        
        df = pd.DataFrame(data = associations_score[0:, 0:],
                        index = associations_score[0:, 0],
                        columns = ["association_id",
                                         "localPageRankMean",
                                         "path_informativeness",
                                         "path_pattern_informativeness",
                                         "localHubMean",
                                         "relevance_score",
                                         "rarity_score"])
        df = df.set_index("association_id")
        print df
        diri = Clustering_dirichlet.DirichletClustering()
        diri.dirichlet(df, user, article)
        ids = diri.predict(df, user, article)
        print ids
        return {"ids": ids }




if __name__ == '__main__':
    
    learning()


 
        