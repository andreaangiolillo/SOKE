from server import Clustering_dirichlet
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd
import pickle
from server import Preprocessing
import threading
import socket

"""
@attention: This class implemented the server
"""
class ThreadedServer(object):
    session = {};
    
    '''
    @attention: This method takes only the associations' data in the variable "associations" from associations_score.csv 
    @param associations: List of association's id
    @param artucle: article's id
    @param graph: Flag. If it is True the method returns the data to use to create the graph 
    @param assoc_data: It contains the association's data from associations_score.csv
    '''
    def find(self, associations, article, graph):
        assoc_data = []
        all_score = Preprocessing.extract_association_score(article, graph)
        for i in associations:
            for j in all_score:
                if int(i) == int(j[0]):
                    assoc_data.append(j)
    
        return assoc_data

    """
    @attention: This method deletes the associations in "ids" from "associations"
    @param associations: list of associations 
    @param ids: list of association's id to remove
    @return new_assoc: new list of associations without the associations in ids
    """
    def delete_from(self, associations, ids):
        new_assoc = []
        for i in associations:
            if int(i[0]) not in ids : 
                new_assoc.append(i)
        return new_assoc


    """
    @attention: This method is used in "sort_prob" to return 
    the value of a item
    @param item
    @return: item value
    """
    def getKey(self, item):
        return item[1]

    """
    @attentions: It sorts the probability
    @param prob:list of probability
    @return sort_id: list of probability sorted 
    """
    def sort_prob(self, prob):
        sort_list_1 = []
        sort_list_2 = []
        sort_list_3 = []
        sort_list_4 = []
        sort_list_5 = []
        sort_list_6 = []
        
        for row in prob:
            name = row[0]
            feasibility = row[1]
            cl = 0
            max_value = 0
            for col in range(0,6):
                if max_value < feasibility[col]:
                    max_value = feasibility[col]
                    cl = col
            if cl == 0:
                sort_list_1.append((name, max_value))
            elif cl == 1:
                sort_list_2.append((name, max_value))
            elif cl == 2:
                sort_list_3.append((name, max_value))
            elif cl == 3:
                sort_list_4.append((name, max_value))
            elif cl == 4:
                sort_list_5.append((name, max_value))
            elif cl == 5:
                sort_list_6.append((name, max_value))
        
        sort_list_1 = sorted(sort_list_1, key=self.getKey,  reverse=True)
        sort_list_2 = sorted(sort_list_2, key=self.getKey,  reverse=True)
        sort_list_3 = sorted(sort_list_3, key=self.getKey,  reverse=True)
        sort_list_4 = sorted(sort_list_4, key=self.getKey,  reverse=True)
        sort_list_5 = sorted(sort_list_5, key=self.getKey,  reverse=True)
        sort_list_6 = sorted(sort_list_6, key=self.getKey,  reverse=True)
        sort = sort_list_6 + sort_list_5 + sort_list_4 + sort_list_3 + sort_list_2 + sort_list_1 
        sort = np.array(sort)[:,:1]
        sort_id = []
        
        for element in sort:
            sort_id.append(int(element[0]))
        
        return sort_id
    
    """
    @attention: It calculates the entropy of a prediction, where the entropy shows how much a prediction is unknown
    @param predictions: list of predictions (probabilities)
    @return: entropy_list: list of entropy
    """
    def entropy(self, predictions):
        entropy_list = {}
        for row in predictions:
            id_assoc = row[0]
            prob = row[1]
            entropy = 0
            for i in range(0, len(prob)):
                if prob[i] != 0:
                    entropy += -prob[i] * np.log2(prob[i])
                
            entropy_list[id_assoc] = entropy
             
        return entropy_list
 
    '''
    @attention: This method executes a clutering of the associations to get the centroids 
    @param article: article ID
    @param user: user's id
    @return list of centroids
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
            diri = Clustering_dirichlet.DirichletClustering()
            diri.dirichlet(df,user, article)
            ids = diri.predict(df, user, article)
            return self.find(np.sort(ids), article, True), np.sort(ids) 
            
    """
    @attention: This method executes the online learning 
    @param ids: id of the associations used in the learning phase
    @param valuation: valuation of the associations in "ids"
    @param article: article's id
    @param learner: instance of the class MultinomialNB
    @return predictions: predictions 
    @return assoc_ids: id of the predictions   
    """
    def learning(self, ids, valuation, article,learner):
        #getting info about association evaluated
        data = self.find(ids, article, False)
        
        #Learning stage
        for row in range(0, len(valuation)):
            x = np.array(data[row])
            x = x[2:] # remove ID, article 
            y = np.array([valuation[row]])
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
        assoc_for_prediction = np.zeros((len(all_assoc),9))
        assoc_ids = []
        for i in range (0, all_assoc.shape[0]):
            assoc_for_prediction[i] = all_assoc[i][2:]
            assoc_ids.append(all_assoc[i][0])
            
            
        predictions = learner.predict(assoc_for_prediction)  
        return predictions, assoc_ids
        
    """
    @attention: This method initializes the server
    @param host: IP address
    @param port: port number  
    """ 
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        
    """
    @attention: listening method
    """
    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(300000) #wait up to 5 minutes
            threading.Thread(target = self.listenToClient,args = (client,address)).start()
    
    """
    @attention: This method executes the first step of the online learning 
    @param client: client's instance
    @param article: article's id
    @param user: user's id
    """
    #fist loop (clustering)
    def first_step(self,client, article, user):
        learner = MultinomialNB()
        
        '''SECOND STEP: executing the cluster to find the associations to evaluate in the first loop'''
        data, ids = self.clustering(article, user)
        string_assoc_to_evaluate = ""
        for i in data:
            for j in i:
                string_assoc_to_evaluate = string_assoc_to_evaluate + ","  + j 
         
            string_assoc_to_evaluate = string_assoc_to_evaluate + "."
            
        #sending the associations to evaluate
        assoc = pickle.dumps(string_assoc_to_evaluate)#serialization
        client.send(assoc)
        
        '''THIRD STEP: getting the evaluations from the Client
        '''
        evaluate = client.recv(1024)
        evaluate = eval("[" + evaluate + "]")
        
        ''' FOURTH STEP: executing online learning '''
        predictions, assoc_ids = self.learning(ids, np.asarray(evaluate), article, learner)
        
        ''' FIFTH STEP: find new associations to evaluate '''
        assoc_measures_ids = self.find(assoc_ids, article, False) #get the measures for all assoc_ids (contains id and article_id)
        
        #now remove ids and article_id from assoc_measures_ids
        assoc_measures = []
        for item in assoc_measures_ids:
            assoc_measures.append(item[2:])
        
        prob = learner.predict_proba(assoc_measures)             
        id_score = []
        len_p = len(predictions)
        if len_p == len(assoc_ids):
            for i in range (0, len_p):
                id_score.append((assoc_ids[i], prob[i]))
                
        sorted_associations = self.sort_prob(id_score)#first associations are those we will select
        data= ', '.join(str(x) for x in sorted_associations[:10])
        self.session[user + str(article) + "learner"] =  learner # saving the learner
        self.session[user + str(article)  + "id_score"] = id_score #saving the id_score for the second step
        client.send(data)
    
    """
    @attention: This method executes the second step of the online learning 
    @param client: client's instance
    @param article: article's id
    @param user: user's id      
    """
    def second_step(self, client, article, user):
        id_score = self.session[user + str(article) + "id_score"]
        learner = self.session[user + str(article) + "learner"]
        entropies = self.entropy(id_score)         
        entropies = sorted(entropies.items(), key=lambda x: x[1], reverse=True)
        to_be_evalueted = entropies[:2]
        ids = []
        for item in to_be_evalueted:
            ids.append(item[0])
          
        assoc_to_evaluate = self.find(ids, article, True)
        string_assoc_to_evaluate = ""
        for i in assoc_to_evaluate[0:2]:
            for j in i:
                string_assoc_to_evaluate = string_assoc_to_evaluate + ","  + j 
         
            string_assoc_to_evaluate = string_assoc_to_evaluate + "."
        
        serialized_data = pickle.dumps(string_assoc_to_evaluate)
        client.send(serialized_data)#sending the 2 association to be evaluated
        evaluate = (client.recv(1024))
        evaluate = eval("[" + evaluate + "]")
        predictions, assoc_ids = self.learning(ids, np.asarray(evaluate), article, learner)
            
        ''' FIFTH STEP: find new associations to evaluate '''
        assoc_measures_ids = self.find(assoc_ids, article, False) #get the measures for all assoc_ids (contains id and article_id)
        
        #now it removes ids and article_id from assoc_measures_ids
        assoc_measures = []
        for item in assoc_measures_ids:
            assoc_measures.append(item[2:])
        
        prob = learner.predict_proba(assoc_measures)  
        id_score = []
        len_p = len(predictions)
        if len_p == len(assoc_ids):
            for i in range (0, len_p):
                id_score.append((assoc_ids[i], prob[i])) 
                 
        sorted_associations = self.sort_prob(id_score)#first associations are those we will select
        data= ', '.join(str(x) for x in sorted_associations[:10])
        self.session[user + str(article) + "learner"] =  learner # saving the learner
        self.session[user + str(article) + "id_score"] = id_score #saving the id_score for the second step
        client.send(data)
    
    """
    @attention: Main method
    @param client: client's instance
    @param address: IP address  
    """
    def listenToClient(self, client, address):
        while True:
            
            #getting a flag to know if is the first iteration
            clustering = (client.recv(1024))
            
            ''' FIRST STEP: getting user and article from Client'''
            #get user
            user  = (client.recv(1024))
            if not user:
                break
            
            #get article
            article = int(client.recv(1024))
            if not article:
                break
            
            if clustering == "true":
                self.first_step(client, article, user) 
            else:
                self.second_step(client, article,user)
            
    
if __name__ == "__main__":
    host = "127.0.0.1"
    port_num = 6000
    ThreadedServer('',port_num).listen() #assigns a free port to client's thread
    