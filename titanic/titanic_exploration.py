# -*- coding: utf-8 -*-

''' TITANIC DATA EXPLORATION '''

# import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import string as string

# load data from Kaggle training set; 
# ~~> description of data: http://www.kaggle.com/c/titanic-gettingStarted/data
# ~~> will split data later, after exploratory phase
tr = pd.read_csv('train.csv', index_col='PassengerId')

# start exploring the data
tr.describe()

# run pandas scatter matrix function
pd.scatter_matrix(tr)
plt.show()

# look for null values
tr.isnull().sum() # cabin has 687 missing; Age has 177 missing; Embarked has 2 missing

# look further into age variable
tr.Sex.value_counts()
tr[tr.Sex=='male'].isnull().sum() / float(tr[tr.Sex=='male'].Sex.value_counts())
tr[tr.Sex=='female'].isnull().sum() / float(tr[tr.Sex=='female'].Sex.value_counts()) # missing more obs for males

# effects of Sex and Pclass on survival
tr.Survived.hist(by=([tr.Sex, tr.Pclass]), sharex=True, sharey=True, layout=(2,3)) # layout=(2,3)
plt.show() # females in classes 1 and 2 are very likely to survive
tr.groupby(['Sex','Pclass']).Survived.mean()

# effects of Embarked and Pclass
tr.Embarked.value_counts()
tr.groupby('Embarked').Survived.mean()
tr.groupby('Embarked').Pclass.value_counts()
tr.groupby(['Embarked','Pclass']).Survived.mean()


# density plots
tr[(tr.Survived==0) & (tr.Sex=='male')].Age.plot(kind='density')
tr[(tr.Survived==0) & (tr.Sex=='female')].Age.plot(kind='density')
tr[(tr.Survived==1) & (tr.Sex=='male')].Age.plot(kind='density')
tr[(tr.Survived==1) & (tr.Sex=='female')].Age.plot(kind='density')
plt.show() # does not seem to have a large impact, but there are a lot of missing values

# so far, it appears that the biggest indicators of survival are Pclass and Sex
# ASSUMPTION: Fill in missing age values with MEDIAN age for each Pclass and Sex
tr['Age_Fill'] = tr.groupby(['Sex', 'Pclass']).Age.transform(lambda x: x.fillna(x.median()))

# ticket prices should be correlated with class and, therefore, survival
tr.boxplot(column='Fare', by='Pclass')
plt.show()

tr.boxplot(column='Fare', by=['Pclass', 'SibSp'])
plt.show() # it's a bit hard to see, but it looks like ticket price is correlated with number of people on the same ticket

# look at the number of people "per ticket"
tr['Num_on_ticket'] = tr.groupby('Ticket').Ticket.transform(lambda x: x.value_counts())
tr['Price_per_passenger'] = tr.Fare / tr.Num_on_ticket

tr.boxplot(column='Price_per_passenger', by='Pclass')
plt.show()

def remove_numeric(k):
    try:
        temp = string.maketrans('','')
        alf = k.translate(temp, string.digits)
        return alf[0]
    except:
        return 'Z'
    

def remove_alpha(k):
    try:
        temp = string.maketrans('','')
        alf = temp.translate(temp, string.digits)
        k = k.translate(temp, alf)
        if k == '':
            return 999
        else:
            return int(k)
    except:
        return 999

# ASSUMPTION: Some passengers have multiple cabins - it appears that they are all
#   either even numbered or all odd numbered. Therefore, there is no reason to separate 
#   out into multiple rooms for purposes of this analysis
tr['Cabin_lvl'] = tr.Cabin.apply(lambda x: remove_numeric(x))
tr['Cabin_num'] = tr.Cabin.apply(lambda x: remove_alpha(x))
tr['Ship_side'] = np.where(tr.Cabin_num == 999, 0, \
                    np.where(tr.Cabin_num % 2 == 0, 2, 1))

tr['Cabin_level'] = tr.Cabin_lvl.map({'A': 0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'T':7, 'Z':8})

tr.groupby('Cabin_level').Survived.mean().plot(kind='bar')
plt.show()

tr.groupby('Ship_side').Survived.mean().plot(kind='bar')
plt.show()



''' family names and titles??
tr['Name_List'] = tr['Name'].str.split(pat=',')
tr['Family_Name'] = tr.Name_List.str.get(0)
tr['First_Name'] = tr.Name_List.str.get(1)
tr['Title'] = tr['First_Name'].str.split(pat='.')
tr['Title'] = tr['Title'].str.get(0)
del tr['Name_List']
del tr['First_Name']
tr.groupby('Title').Survived.value_counts()
tr.groupby('Survived').Title.value_counts()
tr.groupby('Family_Name').Survived.value_counts()
tr['Solo_Travel'] = np.where( (tr.SibSp==0) & (tr.Parch==0), 1, 0)
tr.groupby(['Survived', 'Sex', 'Pclass']).Solo_Travel.value_counts()
'''