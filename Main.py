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
    assoc_evals = {} #dictionary containing {association_score_id: "scores..scores.., target"}
    current_user_id = evaluations[0][0]
    for evaluation in evaluations: #we learn from each user independently
        if evaluation[0] == current_user_id:
            for association in associations:
                if association[0] == evaluation[1]: #the two IDs are the same: we found the right row
                    temp = []
                    temp.append(associations[1:])
                    temp.append(evaluation[2])
                    assoc_evals[int(association[0])] = temp
                    
        else:
            assoc_evals = {}
            current_user_id = evaluation[0]
            for association in associations:
                if association[0] == evaluation[1]: #the two IDs are the same: we found the right row
                    temp = []
                    temp.append(associations[1:])
                    temp.append(evaluation[2])
                    assoc_evals[int(association[0])] = temp
            
         
    print assoc_evals
#         
#         
#         
#         if evaluation[0] == current_user_id:
#             targets.append(evaluation[2])
#             for association in associations: #we want to find the right row among the associations
#                 if association[0] == evaluation[1]: #the two IDs are the same: we found the right row
#                     data.append(association)
#                     continue #exits this for loop without having to check all the associations
#          
#         else:
#             print "user" + str(evaluation[0])
#             if data: #means: if data is not empty
#                 data = np.array(data)
#                 targets = np.array(targets)
#                 print data
#                 print "data"
#                 print data
#                 print "target"
#                 print targets



#         clf = SGDClassifier(loss="log", penalty="l2")
#         clf.partial_fit(data[i],targets[i], classes=np.unique(targets))
#         predictions = clf.predict(data[i+1: len(data)])
#         d = {}
#         for prediction in predictions:
#             pass
                    
                #test    

         
                 
#             current_user_id = evaluation[0]
#             data = []
#             targets = []
#             targets.append(evaluation[2])
#             for association in associations: 
#                 if association[0] == evaluation[1]: 
#                     data.append(association)
#                     pass
    
    



if __name__ == '__main__':
    
    linear_model()




 
        