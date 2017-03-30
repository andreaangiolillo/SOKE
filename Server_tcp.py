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
@attention: This method takes in input a list of associations' id and finds in
association_score.csv their info (source, first property, middle_one, second_property, destination)
            
'''

def find(list,article):
    output = []
    all_score = Preprocessing.extract_association_score(article,True)
    for i in list:
        for j in all_score:
            #print j
            if int(i) == int(j[0]):
                output.append(j)

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
        return find(np.sort(ids), article)



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
        data = clustering(article,user)
        for i in data:
            print i 
        #sending the associations to evaluate
        assoc = pickle.dumps(data)#serialization
        c.send(assoc)

        
    c.close()
    
if __name__ == '__main__':
    main()