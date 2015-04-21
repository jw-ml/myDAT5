# -*- coding: utf-8 -*-

'''
Let's use the glass identification dataset again.   We've previously run knn
on this dataset.  Now, let's try logistic regression.  Access the dataset at
http://archive.ics.uci.edu/ml/datasets/Glass+Identification.  Complete the 
following tasks or answer the following questions.

1. Read the data into a pandas dataframe.
2. Explore the data and look at what columns are available.
3. Convert the 'glass type' column into a binary response.
    * If type of class = 1/2/3/4, binary=0.
    * If type of glass = 5/6/7, binary=1.
4. Create a feature matrix and a response vector.  
5. Split the data into the appropriate training and testing sets.
6. Create and fit a logistic regression model.
7. Make predictions with your new model.
8. Calculate the accuracy rate of your model and compare it to the null accuracy.
9. Generate a confusion matrix for your predictions.  Use this to calculate the
sensitivity and specificity of your model.
'''

# import relevant modules and methods
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

# read data into dataframe; add column names (col_names) and set index column
col_names = ['id','ri','na','mg','al','si','k','ca','ba','fe','glass_type']
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data', \
                 names=col_names, index_col='id')

# convert 'glass_type' to a binary variable
df['binary'] = np.where(df.glass_type < 5, 0, 1)

# create a feature matrix (X) and a response vector (y)
X = df.iloc[:,:9]
y = df['binary']

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y)

# create and fit a logistic regression model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# make predictions
y_pred = logreg.predict(X_test)

# test the accuracy
print metrics.accuracy_score(y_test, y_pred)

# confusion matrix
con_mat = metrics.confusion_matrix(y_test, y_pred)
print con_mat

# Let's define our true posititves, false positives, true negatives, and false negatives
true_neg = con_mat[0][0]
false_neg = con_mat[1][0]
true_pos = con_mat[1][1]
false_pos = con_mat[0][1]

# Sensitivity: percent of correct predictions when reference value is 'default'
sensitivity = float(true_pos)/(false_neg + true_pos)
print sensitivity

# Specificity: percent of correct predictions when reference value is 'not default'
specificity = float(true_neg) / (true_neg + false_pos)
print specificity


