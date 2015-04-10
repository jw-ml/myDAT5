# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:02:57 2015

HOMEWORK 6: KNN AND TYPES OF GLASS
@author: jward
"""
# import necessary modules and methods
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split

'''
ABOUT THE DATA
https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.names
'''

# Read in the data from the url; store in a dataframe named glass
col_names = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type_of_glass']
glass = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data', names=col_names, index_col='Id')

# create new binary variable where type_of_glass in (1, 2, 3, 4) = 0, and = 1 otherwise
glass['Glass_type_b'] = np.where( (glass.Type_of_glass == 1) \
                            | (glass.Type_of_glass == 2) \
                            | (glass.Type_of_glass == 3) \
                            | (glass.Type_of_glass == 4), 0, 1)

# create feature set and response
X = glass.iloc[:, 0:-2] # drops last two columns: Type_of_glass and Glass_type_b
y = glass.iloc[:,-1]    # drops all columns except for the response: Glass_type_b
del glass               # removes glass dataframe from memory


# loop through several random states in order to get a sense of model variance
for j in range(1,4):
    xs, ys = [], []
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=j) 
    
    # loop through different values of k to find best predictor for KNN model
    for k in range(1,20):
        # instantiate, fit, and predict KNN classifier model
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        # get accuracy of predictions
        acc = accuracy_score(y_test, y_pred)
        # store number of neighbors (k) and accuracy for plotting         
        xs.append(k)
        ys.append(acc)
    # plot results of random state experiment
    plt.plot(xs, ys)

# display results  
plt.show()

# TAKEAWAY: k = 1 seems to consistently perform the best

'''
for sake of comparison, compute the "null accuracy" (i.e., the classification 
accuracy that could be achieved by always predicting the majority class.)
'''
# if the mean of y is less than 0.5, then the majority of the glass types must be 0
# create a list of 0's equal to the length of y
if y.mean() < 0.5:
    y_pred = [0]*len(y)
else:
    y_pred = [1]*len(y)

# predicts and accuracy of 76.2 percent
print "the null accuracy is {0:.3f}".format(accuracy_score(y, y_pred))
