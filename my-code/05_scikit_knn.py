'''
CLASS: Introduction to scikit-learn with iris data
'''

# read in iris data
import pandas as pd
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                   names=col_names)

# create numeric column for the response
#  .map() takes a specified dictionary, and maps the data to the new variable
iris['species_num'] = iris.species.map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})

# create X (features) two different ways
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
X = iris.loc[:, 'sepal_length':'petal_width'] # selects all rows, and the columns 'sepal_length' through 'petal_width'
X = iris.iloc[:, 0:4] # selects all rows, and selects columns 0 - 3 (the 4 is not included)

# create y (response)
y = iris.species_num

# predict y with KNN
from sklearn.neighbors import KNeighborsClassifier  # import class ~~> nobody does 'import sklearn'
                                                    # from A import B brings in less info and makes program run faster (less memory)
knn = KNeighborsClassifier(n_neighbors=1)           # instantiate the estimator ~~> skl call models 'estimators'
knn.fit(X, y)                                       # fit with data
knn.predict([1, 1, 1, 1])                           # predict for a new observation

# predict for multiple observations at once
X_new = [[3, 5, 4, 2], [3, 5, 2, 2]]
knn.predict(X_new)

# try a different value of K
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
knn.predict(X_new)              # predictions
knn.predict_proba(X_new)        # predicted probabilities
knn.kneighbors([3, 5, 4, 2])    # distances to nearest neighbors (and identities)

# calculate Euclidian distance manually for nearest neighbor
import numpy as np
np.sqrt(((X.values[106] - [3, 5, 4, 2])**2).sum())
