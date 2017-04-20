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

    def find(self, list, article, flag):
        output = []
        all_score = Preprocessing.extract_association_score(article,flag)
        for i in list:
            for j in all_score:
                #print j, "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
                if int(i) == int(j[0]):
                    output.append(j)
    
        return output

    def getKey(self, item):
        return item[1]

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



    def sort_prob(self, prob):
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
        
    
        sort_list_1 = sorted(sort_list_1, key=self.getKey,  reverse=True)
        sort_list_2 = sorted(sort_list_2, key=self.getKey,  reverse=True)
        sort_list_3 = sorted(sort_list_3, key=self.getKey,  reverse=True)
        sort_list_4 = sorted(sort_list_4, key=self.getKey,  reverse=True)
        sort_list_5 = sorted(sort_list_5, key=self.getKey,  reverse=True)
        sort_list_6 = sorted(sort_list_6, key=self.getKey,  reverse=True)
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

    def entropy(self, x):
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
        assoc_ids = []
        for i in range (0, all_assoc.shape[0]):
            assoc_for_prediction[i] = all_assoc[i][2:]
            assoc_ids.append(all_assoc[i][0])
            
            
        predictions = learner.predict(assoc_for_prediction)
        
        return predictions, assoc_ids
        
  
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
            
            '''SECOND STEP: executing the cluster to find the 
            associations to evaluate in the first loop'''
            data, ids = self.clustering(article, user)
            
            
            
                
            print data
            #sending the associations to evaluate
            assoc = pickle.dumps(data)#serialization
            client.send(assoc)
            
            '''THIRD STEP: getting the evaluation from the Client
            '''
            #getting the evaluation 
            eval = pickle.loads(client.recv(1024))
            
            
            ''' FOURTH STEP: executing online learning '''
            predictions, assoc_ids = self.learning(ids, np.asarray(eval), article, learner)
            assoc_properties = self.find(assoc_ids, article, True)
                        
            data = pickle.dumps(predictions)
            client.send(data)
            data = pickle.dumps(assoc_properties)
            client.send(data)
            
            ''' FIFTH STEP: find new associations to evaluate '''
            assoc_measures_ids = self.find(assoc_ids, article, False) #get the measures for all assoc_ids (contains id and article_id)
            #now remove ids and article_id from assoc_measures_ids
            assoc_measures = []
            for item in assoc_measures_ids:
                assoc_measures.append(item[2:])
            
            prob = learner.predict_proba(assoc_measures)  
            #name_assoc = assoc_ids[:,0]
               
            id_score = []
            len_p = len(predictions)
            if len_p == len(assoc_ids):
                for i in range (0, len_p):
                    #id_score.append((predictions[i], name_assoc[i], prob[i]))
                    id_score.append((assoc_ids[i], prob[i]))
             
                     
            sorted_associations = self.sort_prob(id_score)#first associations are those we will select
                     
            entropies = self.entropy(id_score)  
             
            entropies = sorted(entropies.items(), key=lambda x: x[1], reverse=True)
             
            to_be_evalueted = entropies[:k]
                 
            print to_be_evalueted, "to_be_evaluated"
            ids = []
            ndcg_list = []
            for item in to_be_evalueted:
                ids.append(item[0])
            
            assoc_to_evaluate = find(ids, article, True)
            print assoc_to_evaluate
            serialized_data = pickle.dumps(assoc_to_evaluate)
            client.send(serialized_data)

            

if __name__ == "__main__":
    #port_num = input("Port? ")
    host = "127.0.0.1"
    port_num = 6000
    ThreadedServer('',port_num).listen() #assigns a free port to client's thread
    