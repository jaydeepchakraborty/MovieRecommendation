#reverse

import glob
import os
import random
import numpy
from sklearn import linear_model
from numpy import size, ones
from sklearn.cluster import KMeans
# import pprint

my_data = numpy.genfromtxt('text_big.csv', delimiter=',')
my_data = numpy.delete(my_data, (0), axis=0)

total_rows = numpy.size(my_data, 0)
total_cols = numpy.size(my_data, 1)
train_rows = int(total_rows * 0.7)

numpy.random.shuffle(my_data)
training, test = my_data[:train_rows,:], my_data[train_rows:,:]

XTrain = training[:,1:total_cols-1];
YTrain = training[:,total_cols-1];

XTest = test[:,1:total_cols-1];
YTest = test[:,total_cols-1];

# print(XTrain)
# print(YTrain)
#   
# print(XTest)
# print(YTest)

km = KMeans(n_clusters=5, random_state=0).fit(XTrain)
pred_Y = km.predict(XTest)
x = [1 for i in range(size(XTest, 0))]
print(x)
print(pred_Y)
pred_Y = numpy.add(x, pred_Y)

print(pred_Y)

error = numpy.sum(YTest != pred_Y);
nb_accuracy = (float(total_rows - error) / total_rows) * 100;

print(nb_accuracy)


print("--------------DONE--------------")
