# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:43:21 2015

@author: jward
"""
'''
1. petal_width < .75 then assign Iris-setosa (alternatively, petal_length < 2 then Iris-setosa)
2. if petal_area < 8 then Iris-versicolor
3. otherwise Iris-virginica

'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                   names=col_names)

# check for null values                
iris.isnull().sum()
               
pd.scatter_matrix(iris)
plt.show()

iris.groupby('species').describe()


iris.boxplot(column='petal_width', by='species')

iris.boxplot(column='petal_width', by='species')

iris.boxplot(column='sepal_width', by='species')

iris.boxplot(column='sepal_length', by='species')

iris.boxplot(by='species')

iris['pedal_area'] = iris.petal_length * iris.petal_width # key diff
plt.show()
iris['psw_ratio'] = iris.petal_width / iris.sepal_width
iris['sepal_area'] = iris.sepal_length * iris.sepal_width

iris.boxplot(column='pedal_area', by='species')

iris.boxplot(column='sepal_area', by='species')

iris.boxplot(column='psw_ratio', by='species')

colors = np.where(iris.species=='Iris-setosa', 'r', \
         np.where(iris.species=='Iris-versicolor', 'b', 'g'))
iris.plot(kind='scatter', x='petal_width', y='petal_length', c=colors)
plt.show()  

