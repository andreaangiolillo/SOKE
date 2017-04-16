import socket
import threading
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

class ThreadedServer(object):
    
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

    def find(self, list,article, flag):
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
    def delete_from(self, list, ids):
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
           
    def clustering(self,article,user):
                        
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
            return self.find(np.sort(ids), article, True), np.sort(ids) 
            


    def learning(self, ids, eval, article,learner):
        
        #getting info about association evaluated
        data = self.find(ids, article, False)
        
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
        all_assoc = self.delete_from(all_assoc, ids)
        all_assoc = np.asarray(all_assoc)
        
        #removing ID and article from associations
        assoc_for_prediction = np.zeros((54,9))
        assoc_name = []
        for i in range (0, all_assoc.shape[0]):
            assoc_for_prediction[i] = all_assoc[i][2:]
            assoc_name.append(all_assoc[i][0])
            
            
        prediction = learner.predict(assoc_for_prediction)
        
        return prediction, assoc_name
        
  
    #Init of server 
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
    
    #listen to clients
    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()
    
    #similar to main
    def listenToClient(self, client, address):
        #----------------------------------------------------------- size = 1024
        #----------------------------------------------------------- while True:
            #-------------------------------------------------------------- try:
                #-------------------------------------- data = client.recv(size)
                #------------------------------------------------------ if data:
                    #--------- # Set the response to echo back the recieved data
                    #------------------------------------------- response = data
                    #------------------------------------- client.send(response)
                #--------------------------------------------------------- else:
                    #------------------------ raise error('Client disconnected')
            #----------------------------------------------------------- except:
                #------------------------------------------------ client.close()
                #-------------------------------------------------- return False
        #s = socket.socket()
        #s.bind((host, port_num))#bind the socket to address and port
        
        #s.listen(5)#Listen for connections made to the socket.
        
        
        #Accept a connection. The socket must be bound to an address
        #and listening for connections. 
        #The return value is a pair (conn, address) 
        #where conn is a new socket object usable to 
        #send and receive data on the connection, 
        #and address is the address bound to the socket 
        #on the other end of the connection.
        #c, addr = self.sock.accept();
        print "Connection from: " + str(address);
        learner = MultinomialNB()
        while True:
            
            ''' FIRST STEP: getting user and article from Client'''
            #get user
            user  = (client.recv(1024))
            if not user:
                break
            print "From connected user: " + str(user)
            client.send("User received")
            
            #get article
            article = int(client.recv(1024))
            if not article:
                break
            print "From connected user: " + str(article)
            
            '''SECOND STEP: executing the cluster for finding the 
            associations to evaluate for the first loop'''
            data, ids = self.clustering(article, user)
            
            
            #test
            for i in data:
                print i
            
                
            print data
            #sending the associations to evaluate
            assoc = pickle.dumps(data)#serialization
            client.send(assoc)
            
            '''THIRD STEP: getting the evaluation from the Client
            '''
            #getting the evaluation 
            eval = pickle.loads(client.recv(1024))
            
            #test
            for i in eval:
                print i
            
            
            ''' FOURTH STEP: executing online learning '''
            prediction, selected_association_name = self.learning(ids, np.asarray(eval), article, learner)
            
            assoc_properties = self.find(selected_association_name, article, True)
            
            
            data = pickle.dumps(prediction)
            client.send(data)
            data = pickle.dumps(assoc_properties)
            client.send(data)
              
            ''' FIFTH STEP: find new associations to evaluate '''     
            assoc_ = []#remove ID, article and length from data for the prediction
            [assoc_.append(row[2:]) for row in assoc ]
            assoc_ = np.array(assoc_)
               
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

            

if __name__ == "__main__":
    #port_num = input("Port? ")
    host = "127.0.0.1"
    port_num = 6000
    ThreadedServer('',port_num).listen() #assigns a free port to client's thread
    