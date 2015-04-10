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
from sklearn.metrics import accuracy_score

# only include the NUMERIC features that we want: Pclass, sx, etc.
# include the response

# map categorical variables to numeric


def create_features(df):
    """takes a dataframe and adds and removes necessary data"""
    df['sx'] = np.where(df.Sex=='female',0,1)  
    df['embk'] = df.Embarked.map({'S':0, 'C':1, 'Q':2})
    #df['Age_Fill'] = df.groupby(['Sex', 'Pclass']).Age.transform(lambda x: x.fillna(x.median()))
    df['Num_on_ticket'] = df.groupby('Ticket').Ticket.transform(lambda x: x.value_counts())
    df['Price_per_passenger'] = df.Fare / df.Num_on_ticket
    df['Price_per_passenger'] = df.groupby(['Sex', 'Pclass']).Price_per_passenger.transform(lambda x: x.fillna(x.mean()))
    X = df[['Pclass', 'sx', 'embk','Price_per_passenger']]
    return X


train = pd.read_csv('train.csv', index_col='PassengerId')  
train = train[train.Embarked.isnull()==False]  
X = create_features(train)
y = train.iloc[:,0]

# use train_test_split, with random_state = 4 to train and test our model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=4)

xx, yy = [], []
for k in range(1,25):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    xx.append(k)
    yy.append(accuracy_score(y_test, y_pred))
    
plt.plot(xx, yy)
plt.show()

# create kaggle submission with k = 5

# load and process data
test = pd.read_csv('test.csv', index_col='PassengerId')
X_test = create_features(test)
    
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)
y_pred = knn.predict(X_test)

X_test['Survived'] = y_pred
X_test.reset_index(inplace=True)
output = X_test[['PassengerId', 'Survived']]
output.to_csv('../titanic_knn_.csv', index=False)


