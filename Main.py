# encoding=utf8
import numpy as np
from sklearn.utils.testing import assert_almost_equal
import Preprocessing
import Clustering_dirichlet
import pandas as pd
from sklearn.naive_bayes import MultinomialNB



'''
    @param  user       - user ID
    @param  ids        - list of associations ID
    @param  score_eval - list of users' evaluation
    @return score_eval - list of users' evaluation without association in ids
    @return score      - list of users' evaluation for association in ids

''' 

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


'''
    @param  article    - article ID
    @param  ids        - list of associations ID
    @param  assoc      - 
    @return assoc      - 
    @return data       - 

''' 

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
    

'''
    @param  x       -
    @return list    - 

''' 

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


'''
    @param  id_score    -
    @return list        - 

''' 

def radix_sort(id_score):
    maxcol = id_score.shape[1]
    for i in reversed(range(1, maxcol)):
        id_score = sorted(id_score, key=lambda x: x[i])
    return id_score

def flat_list(l):
    return [item for sublist in l for item in sublist]
    

'''
    @param  data_for_prediction       -  feature vector for each association.
    @param  ndcg_data       -  association with it's user score
    @return l       -  list with ndcg value for each association 

''' 

def ndcg(data_for_prediction, ndcg_data, clf):
    prob = clf.predict_proba(data_for_prediction[:, 2:])
    #dcg on not ordered list
    dcg_list = dcg(ndcg_data[:, 1], len(ndcg_data[:, 1]) - 1)
    data_to_order = np.asarray(np.column_stack([ndcg_data, prob]))
    
    ndcg_data = np.asmatrix(radix_sort(data_to_order))
    
    ndcg_list = np.asarray(dcg1(ndcg_data[:,1], len(ndcg_data[:,1]) - 1)).tolist()
    ndcg_list = flat_list(flat_list(ndcg_list))
    return np.divide(ndcg_list, dcg_list)
    #print ndcg_list / dcg_list
    
    #return np.divide(ndcg_list, dcg_list)

'''
    @param  G       -  matrix with user association score per association
    @param  i       -  index for recursion
    @return l       -  list with dcg value for each association 

''' 

def dcg1(G, i):
    l = []
    if (i == 0):
        return [G[i, 0]]
    else:
        l = dcg(G, i - 1)
        sum = l[i - 1] + (G[i, 0] / np.log2(i + 1))
        l.append(sum)
    return l

'''
    @param  G       -  array with user association score per association
    @param  i       -  index for recursion
    @return l       -  list with dcg value for each association 

''' 
#recursive algorithm that calculates the dcg measure
def dcg(G, i):
    l = []
    if (i == 0):
        return [G[i]]
    else:
        l = dcg(G, i - 1)
        sum = l[i - 1] + (G[i] / np.log2(i + 1))
        l.append(sum)
    return l
        


'''
    @param  item    -
    @return list    - 

''' 

def getKey(item):
    return item[1]
  
    
'''
    @param  prob - list of probability  
    @return list - list sorted
'''    
def sort_prob(prob):
    sort_list_1 = []
    sort_list_2 = []
    sort_list_3 = []
    sort_list_4 = []
    sort_list_5 = []
    sort_list_6 = []
    print "START SORT"
    for row in prob:
        name = row[0]
        feasibility = row[1]
        cl = 0
        max = 0
        for col in range(0,6):
            if max < feasibility[col]:
                max = feasibility[col]
                cl = col
        if cl == 0:
            sort_list_1.append((name, max))
        elif cl == 1:
             sort_list_2.append((name, max))
        elif cl == 2:
            sort_list_3.append((name, max))
        elif cl == 3:
             sort_list_4.append((name, max))
        elif cl == 4:
            sort_list_5.append((name, max))
        elif cl == 5:
            sort_list_6.append((name, max))
        
#     print sort_list_1, "1 ", len(sort_list_1)
#     print sort_list_2, "2 ", len(sort_list_2)
#     print sort_list_3, "3 ", len(sort_list_3)
#     print sort_list_4, "4 ", len(sort_list_4)
#     print sort_list_5, "5 ", len(sort_list_5)
#     print sort_list_6, "6 ", len(sort_list_6)
#     print len(prob)
    

    sort_list_1 = sorted(sort_list_1, key=getKey,  reverse=True)
    sort_list_2 = sorted(sort_list_2, key=getKey,  reverse=True)
    sort_list_3 = sorted(sort_list_3, key=getKey,  reverse=True)
    sort_list_4 = sorted(sort_list_4, key=getKey,  reverse=True)
    sort_list_5 = sorted(sort_list_5, key=getKey,  reverse=True)
    sort_list_6 = sorted(sort_list_6, key=getKey,  reverse=True)
    
    sort = sort_list_1 + sort_list_2 + sort_list_3 + sort_list_4 + sort_list_5 + sort_list_6 
    sort = np.array(sort)[:,:1]
    
    sort_id = []
    
    for element in sort:
        sort_id.append(int(element[0]))
    
    return sort_id
    
    
    
    
    
'''
    @attention: This method executes a clutering of the associations to get the centroids 
    @param  article - article ID
    @param  user    - user ID
    @return ids     - list of associations id (centroid)

'''     
           
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

   
#http://stackoverflow.com/questions/23056460/does-the-svm-in-sklearn-support-incremental-online-learning
''' 
    @attention: This method executes a MultinomialNB - Online Learning to predict a list of interested associations for the user  
    @param  article - article ID
    @param  user    - user ID
    @param  t       - number of iterations
    @param  k       - number of associations to be evaluated  
    @return list    - list of associations' id sorted by online learning algorithm
'''
def learning(article, user, t, k) :
    assoc = Preprocessing.extract_association_score(article)  
    score_eval = Preprocessing.extract_user_evaluated_association(user)
    print score_eval, "score_eval"
    ids= np.sort(clustering(article, user))
    print ids, "ids"
    flag_ndcg = True

    clf = MultinomialNB()
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
#             print np.array([score[row]])
#             print y, " _y"
#             print x, " x"
            if row == 0:           
                clf.partial_fit(x, y, [1, 2, 3, 4, 5, 6])
            else:
                clf.partial_fit(x, y)
        print len(assoc)
                  
        assoc_ = []#remove ID, article and length from data for the prediction
        [assoc_.append(row[2:]) for row in assoc ]
        assoc_ = np.array(assoc_)
          
        print "t: ", i
        print assoc_, "input predict"
        prediction = clf.predict(assoc_)    
        print prediction
           
        prob = clf.predict_proba(assoc_)  
        #print prob
                  
        name_assoc = assoc[:,0]
        #print name_assoc 
          
        id_score = []
        len_p = len(prediction)
        if len_p == len(name_assoc):
            for i in range (0, len_p):
                #id_score.append((prediction[i], name_assoc[i], prob[i]))
                id_score.append((name_assoc[i], prob[i]))
        
        
        print id_score, " id_score "
        entropies = entropy(id_score)
        print entropies, "entropy"        
        entropies = sorted(entropies.items(), key=lambda x: x[1], reverse=True)
           
        to_be_evalueted = entropies[:k]
        ids = []
        for item in to_be_evalueted:
            ids.append(item[0])
           
        print ids 
        #np.asarray(np.column_stack([id_score_name, prediction, id_score_prob]))
        ndcg_data = score_eval[:, 1:3]
        
        print ndcg(assoc, ndcg_data, clf)#esempio! poi sistemo sul nostro caso!
        
          
    return sort_prob(id_score)
    
    






if __name__ == '__main__':
    
    print learning(130, 3, 5, 2)

 
        