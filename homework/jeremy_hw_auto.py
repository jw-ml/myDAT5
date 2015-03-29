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
#import matplotlib.pyplot as plt

'''
Part 1
Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
into a DataFrame.  Try looking at the "head" of the file in the command line
to see how the file is delimited and how to load it.
Note:  You do not need to turn in any command line code you may use.
'''
# use pandas to load data from url
# auto = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep='|')
auto = pd.read_table('auto_mpg.txt', sep='|')   # read_table is more general


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

# Dropping 3 and 5 cylinder cars because low number of observations
auto_dropped = auto[(auto.cylinders == 3) | (auto.cylinders == 5)]
auto = auto[(auto.cylinders != 3) & (auto.cylinders != 5)]

# mpg gallon by cylinders and origin
auto.groupby('cylinders').mpg.mean() # 4 cylinder autos get the best mpg
auto.groupby('origin').mpg.mean() # Europe and Japan produce cars with better mpg (but why?)
auto.groupby('model_year').mpg.mean() # # mpg sees a big jump starting in 1980

# why do Europe and Japan produce cars with greater mileage?
auto.groupby('origin').cylinders.describe() # US only producer of cars with 8 cylinders
auto.groupby(['origin','cylinders']).cylinders.count() # US produces A LOT of cars with 6 and 8 cylinders (relative to JP and EU)
auto[auto.cylinders == 4].groupby('origin').mpg.mean() # US on par with Europe
auto[auto.cylinders == 6].groupby('origin').mpg.mean() # US on par with Europe

# how does mpg relate to model year?
auto.groupby(['origin', 'model_year']).mpg.mean() # jump might be driven by change in US mpg
auto.groupby(['origin', 'model_year']).cylinders.mean() # US moves towards more 4 cylinder cars starting in 1980

# what about displacement?
auto.groupby('cylinders').displacement.mean() # displacement increases with number of cylinders
auto.groupby(['origin', 'cylinders']).displacement.mean() # both US 4 and 6 cylinders have greater displacement on average than JP or EU

# is weight a factor?
auto.groupby('cylinders').weight.describe()
bn = pd.cut(auto.weight, 20) # create bins to help analyze weight
auto.groupby(bn).mpg.mean() # mpg decreases with weight
auto.groupby(bn).cylinders.mean() # num cylinders increases with weight
auto.groupby(bn).displacement.mean() # displacement increases with weight
auto.groupby('cylinders').weight.mean() # number of cylinders increases with weight (or vice versa ... ?)

# lastly, what is the impact of horsepower
auto.groupby('cylinders').horsepower.mean()
auto.groupby(bn).horsepower.mean()
hpbn = pd.cut(auto.horsepower, 20)
auto.groupby(hpbn).mpg.mean()
auto.groupby(hpbn).weight.mean()
auto.groupby(hpbn).cylinders.mean()

# WHAT ARE SOME KEY TAKEAWAYS
#   1. The US makes larger cars with more engines, and those cars have the lowest mpg
#   2. There is very high correlation between num of cylinders, weight, horsepower, and displacement
#       - all of which lead to lower mpg
#   3. The US started a shift towards more 4 cylinder cars around 1980 which have better mpg





