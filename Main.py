# encoding=utf8
import numpy as np
from sklearn.utils.testing import assert_almost_equal
import Preprocessing
import Clustering_dirichlet
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics 
import matplotlib.pyplot as plt
import math
import os


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
    #print x, "x"
     
    for row in x:
        id = row[0]
        prob = row[1]
        entropy = 0
        #print "id: ", id ,"prob:",prob 
        for i in range(0, len(prob)):
            if prob[i] != 0:
                #print prob[i], "prob"
                entropy += -prob[i] * np.log2(prob[i])
                #print entropy, " entropy ", "prob[i]", prob[i] , " log ",  np.log2(prob[i])
        
#         if entropy > 1:
#             print prob, "id ", id    
#                 
        entropy_list[id] = entropy
         
    return entropy_list



'''
    @param  id_score    - matrix with a user id, user value and cluster probability score
    @return A matrix ordered for each field

''' 

def radix_sort(id_score, start, stop):
    for i in reversed(range(start, stop)):
        if i==1 :
            id_score = sorted(id_score, key=lambda x: x[i], reverse = True)
        else:
            id_score = sorted(id_score, key=lambda x: x[i])
    return id_score

'''
    @param  l       -  input list
    @return flatten list

''' 
def flat_list(l):
    return [i[0] for i in l]

'''
    @param  ndcg_data       -  association with it's user score
    @return l               -  list with ndcg values for each i| 1 <= i < #of input elements

''' 

def ndcg(ndcg_data):
    dcg_values = dcg1(ndcg_data, len(ndcg_data) - 1)
    #print sorted(ndcg_data, reverse=True), "lista ordinata per rilevanza" # stampate questo per vedere che effettivamente è corretto
    idcg_values = dcg1(sorted(ndcg_data, reverse=True), len(ndcg_data) - 1)
    print idcg_values, "idcg_values"
    print dcg_values, "dcg_values"
    
    
    
    return np.divide(dcg_values, idcg_values)


'''
    @param  G       -  array with user association score per association
    @param  i       -  index for recursion
    @return l       -  list with dcg values for each i| 1 <= i < #of input elements

''' 

def dcg(G, i):
    if (i == 0):
        return [G[i]]
    else:
        list = dcg(G, i - 1)
        list.append(list [i - 1] + (G[i] / np.log2(i + 1)))   
        return list 

'''
    @param  G       -  array with user association score per association
    @param  i       -  index for recursion
    @return l       -  list with dcg values for each i| 1 <= i < #of input elements

'''     
def dcg1(G, i):
    if (i == 0):
        return [((math.pow(2, G[i]) - 1) / math.log(i + 2, 2))]
    else:
        list = dcg1(G, i - 1)
        list.append(list [i - 1] + ((math.pow(2, G[i]) - 1) / math.log(i + 2, 2)))   
        return list 


'''
    @param  item    -
    @return list    - 

''' 

def getKey(item):
    return item[1]
  
    
'''
    @param  prob - list of tuples. The first position of each tuple is an association name and the second is an array of probabilities
    @return list - Association names ordered by their relevance
'''    
def sort_prob(prob):
    sort_list_1 = []
    sort_list_2 = []
    sort_list_3 = []
    sort_list_4 = []
    sort_list_5 = []
    sort_list_6 = []
    
    #print "START SORT"
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
    #print prob, "prob"
    #print sort_list_6,"lista 6"
    #print sort_list_1,"lista 1"
    
    sort = sort_list_6 + sort_list_5 + sort_list_4 + sort_list_3 + sort_list_2 + sort_list_1 
    #print sort, "print sort"
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
        #print df.head(10)
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
    ids= np.sort(clustering(article, user))
    print ids, "ids"
    ndcg_data = score_eval[:, 1:3]
    ndcg_list = []
    ndcg_values = []
    j = 0

    clf = MultinomialNB()
    for i in range (0, t):
        score_eval = get_score_from_ids(user, ids, score_eval)
        score = score_eval["score"]
        score_eval = score_eval["score_eval"]
         
        assoc = get_features_from_ids(article, ids, assoc) 
        data = assoc["data"]
        assoc = assoc["assoc"]
        
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
        #print assoc_, "input prediction"
        prediction = clf.predict(assoc_)  
        #print prediction
           
        prob = clf.predict_proba(assoc_)  
                  
        name_assoc = assoc[:,0]
        #print name_assoc 
          
        id_score = []
        len_p = len(prediction)
        if len_p == len(name_assoc):
            for i in range (0, len_p):
                #id_score.append((prediction[i], name_assoc[i], prob[i]))
                id_score.append((name_assoc[i], prob[i]))
        
                
        sorted_associations = sort_prob(id_score)#first associations are those we will select
                
        entropies = entropy(id_score)  
        
        entropies = sorted(entropies.items(), key=lambda x: x[1], reverse=True)
        
        to_be_evalueted = entropies[:k]
            
        print to_be_evalueted, "to_be_evaluated"
        ids = []
        ndcg_list = []
        for item in to_be_evalueted:
            ids.append(item[0])
           
        print ids 
        #np.asarray(np.column_stack([id_score_name, prediction, id_score_prob]))
        
        ndcg_list.extend(sorted_associations[0:11])
        
            
            
        print ndcg_list, "ndcg_list"
        user_assoc_score = []
        for i in range(0, len(ndcg_list)):
            for item in range(0, ndcg_data.shape[0] - 1):
                if(ndcg_data[item, 0] == ndcg_list[i]):
                    user_assoc_score.append(ndcg_data[item, 1])
            
        print user_assoc_score, "score associazioni selezionate"
        print sorted(user_assoc_score, reverse = True), "score associazioni selezionate ordinati"
        ndcg_values.append(ndcg(user_assoc_score)[len(user_assoc_score) - 1])
        j += 1
        
    return ndcg_values
    


if __name__ == '__main__':
    ndcg_list_article130 = []
    #article 130
    
    ndcg_list_article130.extend(learning(130, 8, 5, 2))
    
    
    ndcg_list_article133 = []
    #article 133
    
    ndcg_list_article133.extend(learning(133, 8, 5, 2))
    
    ndcg_list_article139 = []
    #article 139
    
    ndcg_list_article139.extend(learning(139, 8, 5, 2))
    
    #provate con 10 iterazioni.. si nota come le performance sono molto buone
    
    print ndcg_list_article130, "130"
    print ndcg_list_article133, "133"
    print ndcg_list_article139, "139"
    
    articles_mean = []
    
    articles_mean.append(ndcg_list_article130)
    articles_mean.append(ndcg_list_article133)
    articles_mean.append(ndcg_list_article139)
    
    articles_mean = [sum(x)/float(len(x)) for x in zip(*articles_mean)]
    
    print articles_mean, "performance media sui 3 articoli"
    ALC = metrics.auc([0, 1, 2, 3, 4], articles_mean) / metrics.auc([0, 1, 2, 3, 4], [1, 1, 1, 1, 1]) 
    print ALC
    #normalizzato su intervallo [0,1]
    
    fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
    plt.xlabel("Iterazione")
    plt.ylabel("nDCG value")
    plt.autoscale(enable = True, axis = 'y')
    ax.plot([0, 1, 2, 3, 4], ndcg_list_article130, 'bo--', label = "Articolo 130")
    ax.plot([0, 1, 2, 3, 4], ndcg_list_article133, 'ro--', label = "Articolo 133")
    ax.plot([0, 1, 2, 3, 4], ndcg_list_article139, 'go--', label = "Articolo 139")
    ax.plot([0, 1, 2, 3, 4], articles_mean, 'yo--', label = "Media Articoli")
    title = "Valutazione performance \n ALC = ", ALC
    plt.title(title[0] + str(title[1]))
    plt.legend(loc='best')
    fig.savefig('Data/plot/plot.png')   #change pathname
    plt.close(fig) 
    


        