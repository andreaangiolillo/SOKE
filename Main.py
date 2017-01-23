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
from theano.scalar.basic import InRange


        
#http://stackoverflow.com/questions/23056460/does-the-svm-in-sklearn-support-incremental-online-learning
def learning() :
    article = 130
    user = 1
    score_eval = Preprocessing.extract_user_evaluated_association()
    #print score_eval
    ids= np.sort(clustering(article, user))
    #print ids, "ids"
    print "ciao ", ids
    
    
    score = []
    for id in ids:
        for row in score_eval:
            if row[0] == user and row[1] == id and row[3] == article:
                score.append(row[2])
                #print score, "score"
                break
                
    data = []
    assoc = Preprocessing.extract_association_score()
    for id in ids:
        for row in assoc:
            if row[0] == id and row[1] == article:
                data.append(row)
                np.delete(assoc, row, 0)
                #print row, "data"
                break
            
            

    clf = SGDClassifier(loss="log", penalty="l2")
    
    
    #training
    for row in range(0, len(score)):
        x = np.array(data[row])
        y = np.array([score[row]])
        #print np.array([score[row]])
        #print y 
        #print x
        clf.partial_fit(x, y, classes=np.unique(score_eval))
        
    
    
    
    predictions = clf.predict(assoc)    
    
    print predictions  
        
        
        
#     d = {}
#     for prediction in predictions:
#         pass
#                     
#                 #test



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
        print df.head(10)
        diri = Clustering_dirichlet.DirichletClustering()
        print "\n", user, ": ", article
        diri.dirichlet(df, user, article)
        ids = diri.predict(df, user, article)
        print ids
        return ids




if __name__ == '__main__':
    
    learning()


 
        