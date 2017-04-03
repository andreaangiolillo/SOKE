import socket
import pickle
import numpy as np
from sklearn.utils.testing import assert_almost_equal
import Preprocessing
import Clustering_dirichlet
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics 
import math
import os


'''
@attention: 
This method takes in input a list of associations' id and finds in
association_score.csv their info. 
If flag is True the info are:
     (source, first property, middle_one, second_property, destination)
Else If flag is False the info are:   
    id, article_id, length, relevance_score, rarity_score, localPageRankMean
    localHubMean, dbpediaPageRankMean, path_informativeness,path_pattern_informativeness
    localPageViewMean)
'''

def find(list,article, flag):
    output = []
    all_score = Preprocessing.extract_association_score(article,flag)
    for i in list:
        for j in all_score:
            #print j, "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
            if int(i) == int(j[0]):
                output.append(j)

    return output

"""
@attention:
This method deletes ids from list.
"""
def delete_from(list, ids):
    output = []
    for i in list:
        if int(i[0]) not in ids : 
            output.append(i)
            #print i, "sono in delete from"
    return output


'''
    @attention: This method executes a clutering of the associations to get the centroids 
    @param  article - article ID
    @return ids     - list of associations id (centroid)

'''     
           
def clustering(article,user):
                    
        all_score = Preprocessing.extract_association_score(article)
        associations_score = all_score[:, [0, 5, 8, 9, 6, 3, 4]]
         
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
    
        diri.dirichlet(df,user, article)
        ids = diri.predict(df, user, article)
        
        
        #print ids
        return find(np.sort(ids), article, True), np.sort(ids) 
        


def learning(ids, eval, article,learner):
    
    #getting info about association evaluated
    data = find(ids, article, False)
    
    #test
    print ids, "!!!!!! IDS !!!!!!"
    print data, "data"
    

    #Learning stage
    for row in range(0, len(eval)):
        x = np.array(data[row])
        x = x[2:] # remove ID, article 
        y = np.array([eval[row]])
        print "in the for "
        print np.array([eval[row]])
        print y, " _y"
        print x, " x"
        
        if row == 0:           
            learner.partial_fit(x, y, [1, 2, 3, 4, 5, 6])
        else:
            learner.partial_fit(x, y)
    
    #getting all the article's associations for the prediction
    all_assoc = Preprocessing.extract_association_score(article, False)
    #deleting associations used for learning from all_assoc
    all_assoc = delete_from(all_assoc, ids)
    all_assoc = np.asarray(all_assoc)
    
    #removing ID and article from associations
    assoc_for_prediction = np.zeros((54,9))
    assoc_name = []
    for i in range (0, all_assoc.shape[0]):
        assoc_for_prediction[i] = all_assoc[i][2:]
        assoc_name.append(all_assoc[i][0])
        
        #test
        #print all_assoc[i][2:]
    prediction = learner.predict(assoc_for_prediction)
    
    return prediction, assoc_name
    
    #prediction
#     prediction = learner.predict(all_assoc)
#     print prediction
#     
    


def main():
    host = "127.0.0.1"
    port = 5000
    
    s = socket.socket()
    s.bind((host, port))#bind the socket to address and port
    
    s.listen(5)#Listen for connections made to the socket.
    
    
    #Accept a connection. The socket must be bound to an address
    #and listening for connections. 
    #The return value is a pair (conn, address) 
    #where conn is a new socket object usable to 
    #send and receive data on the connection, 
    #and address is the address bound to the socket 
    #on the other end of the connection.
    c, addr = s.accept();
    print "Connection from: " + str(addr);
    learner = MultinomialNB()
    while True:
        
        ''' FIRST STEP: getting user and article from Client'''
        #get user
        user  = (c.recv(1024))
        if not user:
            break
        print "From connected user: " + str(user)
        c.send("OK")
        
        #get article
        article = int(c.recv(1024))
        if not article:
            break
        print "From connected user: " + str(article)
        
        '''SECOND STEP: executing the cluster for finding the 
        associations to evaluate for the first loop'''
        data, ids = clustering(article,user)
        
        
        #test
        for i in data:
            print i
        
            
        print data
        #sending the associations to evaluate
        assoc = pickle.dumps(data)#serialization
        c.send(assoc)
        
        '''THIRD STEP: getting the evaluation from the Client
        '''
        #getting the evaluation 
        eval = pickle.loads(c.recv(1024))
        
        #test
        for i in eval:
            print i
        
        
        ''' FORTH STEP: executing online learning '''
        sort, selected_association_name = learning(ids, np.asarray(eval), article,learner)
        
        associations_properties = find(selected_association_name, article, True)
        
        
        data = pickle.dumps(sort)
        c.send(data)
        data = pickle.dumps(find(selected_association_name, article, True))
        c.send(data)
        
        
        
        
        
        
    c.close()
    
if __name__ == '__main__':
    main()