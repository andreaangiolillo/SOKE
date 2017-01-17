__author__ = 'vinid'

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class DataSetCreator():

    def data_frame(self, query, columns):
        """
        Takes a sqlalchemy query and a list of columns, returns a dataframe.
        """
        def make_row(x):
            return dict([(c, getattr(x, c)) for c in columns])
        return pd.DataFrame([make_row(x) for x in query])

    def create_dataset(self, associations_score_eval, associations_score, features):
        #original_data_frame = self.data_frame(associations_score_eval, [c for c in ["association_score_id", "score"]])
        #print associations_score_eval
        associations_score_eval = associations_score_eval[:, [2]]
        #original_data_frame = original_data_frame.rename(columns={'association_score_id': 'association_id'})

        #print associations_score_eval, "a1"
        #temp_data_frame = self.data_frame(associations_score, [c for c in features])
        #print associations_score
        associations_score = associations_score[:, [0, 3, 4, 5, 6, 8, 9]]
        #print associations_score
        #print len(associations_score), " ", len(associations_score_eval)

#                         
#         temp_data_frame = temp_data_frame.set_index('association_id')
#         temp_data_frame = pd.DataFrame(MinMaxScaler().fit_transform(temp_data_frame.astype("float")),
#                                        columns=temp_data_frame.columns, index=temp_data_frame.index)
# 
#         kernelized = temp_data_frame #(rbf_kernel(asdf, asdf, -1))
# 
#         kernelized = (pd.DataFrame(kernelized, index=temp_data_frame.index))
#         original_data_frame = original_data_frame.set_index('association_id')
# 
#         #training = pd.merge(dfta, kernelized,left_index=True,left_on='association_id')
#         training = original_data_frame.join(kernelized)
# 
#         predicting = kernelized[~kernelized.index.isin(original_data_frame.index)]
#         training = training.drop('score', 1)
#         training_y = original_data_frame["score"]
# 
        return associations_score, associations_score_eval, [1,2,3,4,5,6]
   
 
       
   
   