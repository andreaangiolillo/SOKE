import numpy as np
from sklearn.utils.testing import assert_almost_equal
import Preprocessing
from sklearn.linear_model import SGDClassifier
from dataset_creation import DataSetCreator
#from lightning.ranking import KernelPRank

from svmlight import *
from active_global_local_uncertainty import *
import logging
import time


        
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
                    temp.append(association[2:])
                    temp.append(evaluation[2])
                    assoc_evals[int(association[0])] = temp
                    continue
                    
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



#         clf = SGDClassifier(loss="log", penalty="l2")
#         clf.partial_fit(data[i],targets[i], classes=np.unique(targets))
#         predictions = clf.predict(data[i+1: len(data)])
#         d = {}
#         for prediction in predictions:
#             pass
                    
                #test





def ranking(article, user):
        """
        This method expose the functionality for ranking data. It assumes that some associations have already been
        evaluated
        :param article: article to rank
        :param user: user that is asking for ranked data
        :return: json result with the best ordered associations, the associations to rank
        """
       # db = create_engine('mysql+mysqlconnector://root:federico92@localhost/dacena')
       # db.echo = False  # false beacuse I don't need logging (now)
       # session = sessionmaker()
       # session.configure(bind=db)
       # Base.metadata.create_all(db)
        #s = session()

        #associations_score_eval = s.query(UserEvaluatedAssociation).filter(UserEvaluatedAssociation.article_id == article and
                                                                  #UserEvaluatedAssociation.user_id == user)
                                                                  
        all_score_eval = Preprocessing.extract_user_evaluated_association() 
        associations_score_eval = []
        [associations_score_eval.append(row) for row in all_score_eval if ((int(row[0]) == int(user)) and (int(row[3]) == int(article))) ]
        associations_score_eval = np.array(associations_score_eval)# list to numpy array

                
                 
        
        #associations_score = s.query(AssociationScore).filter(AssociationScore.article_id == article)
        all_score = Preprocessing.extract_association_score()
        associations_score = []
        [associations_score.append(row) for row in all_score if int(row[1]) == int(article)]
        associations_score = np.array(associations_score) #list to numpy array
        
#         for row in all_score_eval:
#             if ((int(row[1]) == int(article))):
#                 associations_score.append(row)
                
        # features to use for the prediction. TODO: make global
        features =["association_id",
                   "localPageRankMean",
                   "path_informativeness",
                   "path_pattern_informativeness",
                   "localHubMean",
                   "relevance_score",
                   "rarity_score"]

        dc = DataSetCreator()
        training, training_y, predi = dc.create_dataset(associations_score_eval, associations_score, features)

        model = SvmLight()
        rs = RankSVMActiveLearnerUncertainty(model)

        to_rank, best_scored, _ = rs.get_rank_and_active(training, training_y, predi)

        return {'to_rank': to_rank.tolist(),
                'best_scored': best_scored.tolist(),
                'prediction_complete': 0}






if __name__ == '__main__':
    
   # linear_model()

    ranking(130, 1)


 
        