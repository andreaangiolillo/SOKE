import numpy as np
from sklearn.utils.testing import assert_almost_equal
import Preprocessing
from sklearn.linear_model import SGDClassifier
#from lightning.ranking import KernelPRank



        
#http://stackoverflow.com/questions/23056460/does-the-svm-in-sklearn-support-incremental-online-learning
def linear_model() :
    
    associations, evaluations = Preprocessing.extract_association_score(), Preprocessing.extract_user_evaluated_association()
    current_user_id = None
    data = []
    targets = []
    for evaluation in evaluations: #we learn from each user independently
        if evaluation[0] == current_user_id:
            targets.append(evaluation[2])
            for association in associations: #we want to find the right row among the associations
                if association[0] == evaluation[1]: #the two IDs are the same: we found the right row
                    data.append(association)
                    pass #exits this for loop without having to check all the associations
         
        else:
            if data: #means: if data is not empty
                data = np.array(data)
                targets = np.array(targets)
#                 print "data"
#                 print data
#                 print "target"
#                 print targets
                
                length = int(len(data)/5) #split data in 5 sets
                j = 0
                clf = SGDClassifier(loss="log", penalty="l2")
                for i in (0, 4):
                    print targets[j:length]
                    clf.partial_fit(data[j:length],targets[j:length], classes=np.unique(targets))
                    j = length + 1
                    length += length 
                #test    
                print "y ", targets[j:length]
                print "y_ ", clf.predict(data[j:length])#print predict
         
                 
            current_user_id = evaluation[0]
            data = []
            targets = []
            targets.append(evaluation[2])
            for association in associations: 
                if association[0] == evaluation[1]: 
                    data.append(association)
                    pass
    
    



if __name__ == '__main__':
    
    linear_model()




 
        