# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:36:22 2015
@author: jward
"""

# K-Nearest Neighbors 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics

# only include the NUMERIC features that we want: Pclass, sx, etc.
# include the response

# map categorical variables to numeric


def create_features(df):
    """takes a dataframe and adds and removes necessary data"""
    df['sx'] = np.where(df.Sex=='female',0,1)
    df = df[df.embk.isnull()==False]    
    df['embk'] = df.Embarked.map({'S':0, 'C':1, 'Q':2})
    df['Age_Fill'] = df.groupby(['Sex', 'Pclass']).Age.transform(lambda x: x.fillna(x.median()))
    df['Num_on_ticket'] = df.groupby('Ticket').Ticket.transform(lambda x: x.value_counts())
    df['Price_per_passenger'] = df.Fare / df.Num_on_ticket
    X = df[['Pclass', 'sx', 'embk', 'Age_Fill', 'Num_on_ticket', 'Price_per_passenger']]
    return X


tr = pd.read_csv('train.csv', index_col='PassengerId')  
X = create_features()
y = tr['Survived']

# use train_test_split, with random_state = 4 to train and test our model
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

xx, yy = [], []
for k in range(1,25):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = metrics.accuracy_score(y_test, y_pred)
    xx.append(k)
    yy.append(acc)
    
plt.plot(xx, yy)
plt.show()

# create kaggle submission with k = 5

# load and process data
test = pd.read_csv('test.csv', index_col='PassengerId')
test['sx'] = np.where(test.Sex=='female',0,1)
test['embk'] = test.Embarked.map({'S':0, 'C':1, 'Q':2})
X_test = test[['Pclass', 'sx']]
    
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)
y_pred = knn.predict(X_test)
X_test['Survived'] = y_pred

X_test.reset_index(inplace=True)
output = X_test[['PassengerId', 'Survived']]

output.to_csv('knn5_simple.csv', index=False)


