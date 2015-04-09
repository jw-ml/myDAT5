# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:02:57 2015

@author: jward
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split

'''
ABOUT THE DATA

https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.names

   1. Id number: 1 to 214
   2. RI: refractive index
   3. Na: Sodium (unit measurement: weight percent in corresponding oxide, as 
                  are attributes 4-10)
   4. Mg: Magnesium
   5. Al: Aluminum
   6. Si: Silicon
   7. K: Potassium
   8. Ca: Calcium
   9. Ba: Barium
  10. Fe: Iron
  11. Type of glass: (class attribute)
      -- 1 building_windows_float_processed
      -- 2 building_windows_non_float_processed
      -- 3 vehicle_windows_float_processed
      -- 4 vehicle_windows_non_float_processed (none in this database)
      -- 5 containers
      -- 6 tableware
      -- 7 headlamps
'''
col_names = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type_of_glass']
glass = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data', names=col_names, index_col='Id')

glass['binary'] = np.where( (glass.Type_of_glass == 1) \
                            | (glass.Type_of_glass == 2) \
                            | (glass.Type_of_glass == 3) \
                            | (glass.Type_of_glass == 4), 0, 1)

X = glass.iloc[:, 0:-2]
y = glass.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)

def run_knn(kay_nay):
    knn = KNeighborsClassifier(n_neighbors=kay_nay)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return accuracy_score(y_test, y_pred)

xs = []
ys = []
for i in range(1,20):
    acc = run_knn(i)
    xs.append(i)
    ys.append(acc)
    print i, acc
  

plt.plot(xs, ys)
plt.show()