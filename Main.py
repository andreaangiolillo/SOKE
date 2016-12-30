import numpy as np
from sklearn.utils.testing import assert_almost_equal
from lightning.ranking import PRank
import Preprocessing
#from lightning.ranking import KernelPRank

associations, evaluations = Preprocessing.extract_association_score(), Preprocessing.extract_user_evaluated_association()
print "X: " + str(associations)
print "y: "+str(evaluations)


#y = np.round(y, decimals=-2)


# TODO: Add more rankers.
rankers = PRank(n_iter=10, shuffle=False, random_state=0),
#            KernelPRank(kernel="sigmoid",
#                    n_iter=10,
#                        shuffle=True,
#                        random_state=0))

#Now we want to group the evaluations by user_id
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
            for ranker in rankers:
                print data
                print targets
                print ranker.__class__.__name__
                ranker.fit(data, targets)
                print ranker.score(data, targets)
        current_user_id = evaluation[0]
        data = []
        targets = []
        targets.append(evaluation[2])
        for association in associations: 
            if association[0] == evaluation[1]: 
                data.append(association)
                pass
            

        
        