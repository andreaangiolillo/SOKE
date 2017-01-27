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
from lightning.ranking import PRank









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
            "score_eval": score_eval,
            "score": score 
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
            "assoc": assoc,
            "data": data 
            }


def entropy(x):
    entropy_list = {}
    print x, "x"
     
    for row in x:
        id = row[0]
        prob = row[1]
        entropy = 0
        #print "id: ", id ,"prob:",prob 
        for i in range(0, len(prob)):
            if prob[i] != 0:
                print prob[i], "prob"
                entropy += -prob[i] * np.log2(prob[i])
                #print entropy, " entropy ", "prob[i]", prob[i] , " log ",  np.log2(prob[i])
        
#         if entropy > 1:
#             print prob, "id ", id    
#                 
        entropy_list[id] = entropy
         
    return entropy_list


#http://stackoverflow.com/questions/23056460/does-the-svm-in-sklearn-support-incremental-online-learning
def learning() :
    article = 130
    user = 1
    assoc = Preprocessing.extract_association_score(article)  
    score_eval = Preprocessing.extract_user_evaluated_association(user)
    
     
    ids= np.sort(clustering(article, user))
    print ids, "ids"
    t = 5
    k = 2
    clf = SGDClassifier(loss="log", penalty="l2")
    
     
     
    for i in range (0, t):
        score_eval = get_score_from_ids(user, ids, score_eval)
        score = score_eval["score"]
        score_eval = score_eval["score_eval"]
         
        assoc = get_features_from_ids(article, ids, assoc) 
        data = assoc["data"]
        assoc = assoc["assoc"]
         
        print data, "data"
        print score, "score" 
      
    #training
        for row in range(0, len(score)):
            x = np.array(data[row])
            x = x[2:] # remove ID, article and length 
            y = np.array([score[row]])
            #print np.array([score[row]])
            print y, " _y"
            print x, " x"           
            clf.partial_fit(x, y, [1, 2, 3, 4, 5, 6])
             
        print len(assoc)
                 
        assoc_ = []#remove ID, article and length from data for the prediction
        [assoc_.append(row[2:]) for row in assoc ]
        assoc_ = np.array(assoc_)
         
        print "t: ", i
        prediction = clf.predict(assoc_)    
        print prediction
         
         
        prob = clf._predict_proba(assoc_)
        
        print prob
       
                
        name_assoc = assoc[:,0]
        print name_assoc 
            
        
            
        id_score = []
        len_p = len(prediction)
        if len_p == len(name_assoc):
            for i in range (0, len_p):
                #id_score.append((prediction[i], name_assoc[i], prob[i]))
                id_score.append((name_assoc[i], prob[i]))
             
                  
         
        #print id_score, " id_score "
        entropies = entropy(id_score)
        #print entropies        
        entropies = sorted(entropies.items(), key=lambda x: x[1], reverse=True)
        
        to_be_evalueted = entropies[:k]
        ids = []
        for item in to_be_evalueted:
            ids.append(item[0])
        
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


 
        