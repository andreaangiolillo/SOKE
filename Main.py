import numpy as np
from sklearn.utils.testing import assert_almost_equal
import Preprocessing
import Clustering_dirichlet
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
#from dataset_creation import DataSetCreator
#from lightning.ranking import KernelPRank

#from svmlight import *
#from active_global_local_uncertainty import *
import logging
import time
from theano.scalar.basic import InRange


def get_score_from_ids(user, ids, score_eval):
    score = []
    for id in ids:
        for row in score_eval:
            if row[1] == id:
                score.append(row[2])
                mask = score_eval[:, 1] != id
                score_eval = score_eval[mask]
                #print score, "score"
                break


    return {
            "user_evaluations": score_eval,
            "ids_user_evaluations": score 
            }

def get_features_from_ids(article, ids, assoc):
    
    data = []
    for id in ids:
        for row in assoc:
            if row[0] == id:
                data.append(row)
                mask = assoc[:, 0] != id
                assoc = assoc[mask]
                #print row, "data"
                break
         
    return {
            "feature_vector": assoc,
            "ids_feature_vector": data 
            }
        
#http://stackoverflow.com/questions/23056460/does-the-svm-in-sklearn-support-incremental-online-learning
def learning() :
    article = 130
    user = 1
    feature_vector = Preprocessing.extract_association_score(article)
     
    user_evaluations = Preprocessing.extract_user_evaluated_association(user)
    
     
    ids= clustering(article, user)
    print ids, "ids"
    t = 11
    k = 2
    clf = MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)
    
     
     
    for i in range (0, t):
        user_evaluations = get_score_from_ids(user, ids, user_evaluations)
        ids_user_evaluations = user_evaluations["ids_user_evaluations"]
        user_evaluations = user_evaluations["user_evaluations"]
         
        feature_vector = get_features_from_ids(article, ids, feature_vector) 
        ids_feature_vector = feature_vector["ids_feature_vector"]
        feature_vector = feature_vector["feature_vector"]
        
        print ids_feature_vector, "feature vector for centroids"
        print ids_user_evaluations, "ids_user_evaluations" 
     
    #training
        for row in range(0, len(ids_user_evaluations)):
            x = np.array(ids_feature_vector[row])
            y = np.array([ids_user_evaluations[row]])
            #print np.array([ids_user_evaluations[row]])
            print y, " _y"
            print x, " x"           
            clf.partial_fit(x, y, [1, 2, 3, 4, 5, 6])
            
        print len(feature_vector)
        print "t: ", i
        prediction = clf.predict(feature_vector)    
        print prediction, "prediction"
        print clf.predict_proba(feature_vector), "prob"
     
        assocation_name = feature_vector[:,0]
        print assocation_name 
         

        id_score = []
        len_p = len(prediction)
        if len_p == len(assocation_name):
            for i in range (0, len_p):
                id_score.append((prediction[i], assocation_name[i]))
                
        #parte adam#####
        #ordinamento#            
        ######################################################################################
        id_score_name = []
        id_score_prob = []
        
        for i in range(0, len(id_score)):
            id_score_name.append(id_score[i][0]) 
            id_score_prob.append(id_score[i][1])
        
        
        id_score_prob = np.asarray(id_score_prob)
        ndcg_data = np.asarray(np.column_stack([id_score_name, prediction, id_score_prob]))
        ########## copialo nel branch master andre!!##########################################          
        
        id_score_sort = np.array(sorted(id_score,key=lambda x: x[0]))
        print id_score_sort, " id_score sort"
         
        id_score_sort = id_score_sort[:k,:]
        print id_score_sort, " prendo solo i k"
        ids_ = []
        
        ids = id_score_sort[:, 1].tolist()
        print ids 
        
         
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
        #print ids
        return ids




if __name__ == '__main__':
    
    learning()


 
        