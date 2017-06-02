from __future__ import division

import random
import os
import time
import string
import numpy as np
import pandas as pd
import inspect
import logging
__author__ = 'vinid'

class SvmLight():
    """
    Implements and SVMrank algorithm using svmlight code.
    """
    def __init__(self):
        self.location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.filename = "SVMLIGHT_" + str(time.strftime("%H%s")) + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        self.root_dir = self.location + "/tmp/"

    # train method
    def fit(self, x, y):
        start = time.time()
        x = x.astype('float')
        start_save = time.time()
        self.save_svmlight_data(x.as_matrix(), y.as_matrix(), self.filename + ".train", self.root_dir)
        end_save = time.time()

        elapsed = end_save - start_save
        logging.info("\tElapsed Time of saving in " + inspect.stack()[0][3] + " " + str(elapsed) + " seconds")
        os.system(self.location + "/../rank_svm_executable/svm_light/svm_learn -z p -x 1 -v 0 " + self.root_dir + self.filename
                        + ".train " + self.filename + ".train.model")
        end = time.time()

        elapsed = end - start
        logging.info("\tElapsed Time of " + inspect.stack()[0][3] + " " + str(elapsed) + " seconds")

    def rank(self, x, y=0):
        if y == 0:
            y = np.ones(x.shape[0])
        x = x.astype('float')
        self.save_svmlight_data(x, y, self.filename + ".predict", self.root_dir)
        start_time = time.time()
        os.system(self.location + "/../rank_svm_executable/svm_light/svm_classify -v 0 " + self.root_dir + self.filename + ".predict"
                        + " " + self.filename + ".train.model" + " " + self.root_dir + self.filename + ".out")
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
        os.remove(self.root_dir + self.filename + ".train")
        os.remove(self.root_dir + self.filename + ".out")

