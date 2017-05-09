__author__ = 'vinid'



import time
import random
import string
from rank_svm_interface import *
import os
import numpy as np
import pandas as pd

class LibSvmRank(RankSvmInterface):
    """
    Implements and SVMrank algorithm using libsvmrank code.
    """
    def __init__(self):
        self.location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.filename = str(time.strftime("%H%s")) + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        self.root_dir = self.location + "/tmp/"

    # train method
    def fit(self, x, y):
        x = x.astype('float')
        self.save_svmlight_data(x.as_matrix(), y.as_matrix(), self.filename + ".train", self.root_dir)
        print os.system(self.location + "/../rank_svm_executable/libSVMRank/svm-train " + self.root_dir + self.filename + ".train")

    def rank(self, x, y=0):
        if y == 0:
            y = np.ones(x.shape[0])
        x = x.astype('float')
        self.save_svmlight_data(x, y, self.filename + ".predict", self.root_dir)
        print "ora"
        print os.system(self.location + "/../rank_svm_executable/libSVMRank/svm-predict " + self.root_dir + self.filename + ".predict" + " " + self.filename + ".train.model" + " " + self.root_dir + self.filename + ".out")
        rank = np.loadtxt(self.root_dir + self.filename + ".out")
        return rank

    def save_svmlight_data(self, data, labels, data_filename, data_folder = ''):
        if type(data) is pd.DataFrame:
            data = data.as_matrix()
        if type(labels) is pd.DataFrame:
            labels = labels.as_matrix()
        file = open(data_folder+data_filename,'wr')
        for i,x in enumerate(data):
            indexes = x.nonzero()[0]
            values = x[indexes]

            label = '%i'%(labels[i])
            pairs = ['%i:%f'%(indexes[i]+1,values[i]) for i in xrange(len(indexes))]

            sep_line = [label]
            sep_line.extend(pairs)
            sep_line.append('\n')

            line = ' '.join(sep_line)

            file.write(line)

    def __del__(self):
        os.remove(self.root_dir + self.filename + ".predict")
        os.remove(self.filename + ".train.model")
        os.remove(self.root_dir + self.filename + ".train ")
        os.remove(self.root_dir + self.filename + ".out")

