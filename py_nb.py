#reverse

import glob
import os
import random
import numpy
from sklearn.naive_bayes import GaussianNB
from numpy import size
# import pprint

def getNBAcc(my_data):
    
    total_rows = numpy.size(my_data, 0)
    total_cols = numpy.size(my_data, 1)
    train_rows = int(total_rows * 0.7)
    
    numpy.random.shuffle(my_data)
    training, test = my_data[:train_rows,:], my_data[train_rows:,:]
    
    XTrain = training[:,1:total_cols-1];
    YTrain = training[:,total_cols-1];
    
    XTest = test[:,1:total_cols-1];
    YTest = test[:,total_cols-1];
    
    gnb = GaussianNB()
    gnb.fit(XTrain, YTrain)
    pred_Y = gnb.predict(XTest)
    
    error = numpy.sum(YTest != pred_Y);
    nb_accuracy = (float(total_rows - error) / total_rows) * 100;
    
    return nb_accuracy

# print(getNBAcc())