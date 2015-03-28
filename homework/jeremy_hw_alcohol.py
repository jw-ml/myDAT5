# jeremy - pandas homework

##########################################
#############    Homework    #############
##########################################
'''
Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.csv) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''
# import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Part 1
Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
into a DataFrame.  Try looking at the "head" of the file in the command line
to see how the file is delimited and how to load it.
Note:  You do not need to turn in any command line code you may use.
'''
# use pandas to load data from url
auto = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep='|')


'''
Part 2
Get familiar with the data.  Answer the following questions:
- What is the shape of the data?  How many rows and columns are there?
- What variables are available?
- What are the ranges for the values in each numeric column?
- What is the average value for each column?  Does that differ significantly
  from the median?
'''
# returns the number of rows and number of columns
auto.shape # 392 rows by 9 columns

# returns the column names (i.e., the header row); u denotes type of encoding
auto.columns #[u'mpg', u'cylinders', u'displacement', u'horsepower', u'weight', u'acceleration', u'model_year', u'origin', u'car_name'

# return range of value for each column
auto.min() # returns min value for each column
auto.max() # returns max value for each column

# stores the mean in 'mn', the median in 'md', and calculates the difference
mn = auto.mean()
md = auto.median()
mn - md # absolute difference
abs(mn - md) / (0.5*(mn + md)) # percent difference

# takeaway: Cylinders and Displacement and have the largest differences.
#   this suggests that the data is somewhat skewed by some large values

'''
Part 3
Use the data to answer the following questions:
- Which 5 cars get the best gas mileage?  
- Which 5 cars with more than 4 cylinders get the best gas mileage?
- Which 5 cars get the worst gas mileage?  
- Which 5 cars with 4 or fewer cylinders get the worst gas mileage?
'''
# returns the cars with the best gas mileage (mpg)
auto[['car_name', 'mpg']].sort_index(by='mpg', ascending=False).head()

# returns the 5 cars with > 4 cylinders that have the best mpg
auto[['car_name', 'mpg', 'cylinders']][auto.cylinders > 4].sort_index(by='mpg', ascending=False).head()

# returns the 5 cars with the worst gas mileage
auto[['car_name', 'mpg']].sort_index(by='mpg').head()

# returns the 5 cars with <= 4 cylinders that get the worst mpg
auto[['car_name', 'mpg', 'cylinders']][auto.cylinders <= 4].sort_index(by='mpg').head()

'''
Part 4
Use groupby and aggregations to explore the relationships 
between mpg and the other variables.  Which variables seem to have the greatest
effect on mpg?
Some examples of things you might want to look at are:
- What is the mean mpg for cars for each number of cylindres (i.e. 3 cylinders,
  4 cylinders, 5 cylinders, etc)?
- Did mpg rise or fall over the years contained in this dataset?
- What is the mpg for the group of lighter cars vs the group of heaver cars?
Note: Be creative in the ways in which you divide up the data.  You are trying
to create segments of the data using logical filters and comparing the mpg
for each segment of the data.
'''

# mpg gallon by cylinders, model year, and origin
auto.groupby('cylinders').mpg.mean() # 4 and 5 cylinder autos get the best mpg
auto.groupby('model_year').mpg.mean() # mpg sees a big jump starting in 1980
auto.groupby('origin').mpg.mean() # Europe and Japan produce cars with better mpg (but why?)

# cylinders by origin
auto.groupby('origin').cylinders.describe() # US only producer of cars with 8 cylinders
auto[auto.cylinders == 4].groupby('origin').mpg.mean() # US on par with Europe
auto[auto.cylinders == 6].groupby('origin').mpg.mean() # US on par with Europe

# what is displacement?
auto.groupby('cylinders').displacement.mean()
auto.groupby('origin').displacement.mean()
auto[auto.cylinders == 4].groupby('origin').displacement.mean() # US produces autos with greater displacement
auto[auto.cylinders == 6].groupby('origin').displacement.mean() # US produces 6 cyl autos with much greater displacement

# is weight a factor?
auto.groupby('cylinders').weight.describe()
bn = pd.cut(auto.weight, 10) # create bins to help analyze weight
auto.groupby(bn).mpg.mean() # mpg decreases with weight
auto.groupby(bn).cylinders.mean() # num cylinders increases with weight
auto.groupby(bn).displacement.mean() # displacement increases with weight
auto.groupby('cylinders').weight.mean()

# lastly, what is the impact of horsepower
auto.groupby('cylinders').horsepower.mean()
auto.groupby(bn).horsepower.mean()
hpbn = pd.cut(auto.horsepower, 10)
auto.groupby(hpbn).mpg.mean()
auto.groupby(hpbn).weight.mean()
auto.groupby(hpbn).cylinders.mean()





