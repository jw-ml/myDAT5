"""
HOMEWORK:  Visualization
"""

##########################################
#############    Homework    #############
##########################################
'''
Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''
# imports modules to be used
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# loads the data from the url provided
auto = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep='|')

'''
Part 1
Produce a plot that compares the mean mpg for the different numbers of cylinders.
'''

# plots the mean mpg for differnt cylinders
auto.groupby('cylinders').mpg.mean().plot(kind='bar', title='Average MPG by number of cylinders', ylim=(0,40))
plt.xlabel('Number of cylinders')
plt.ylabel('Miles per gallon')
plt.show()

# takeaway: 4 cylinder cars get the best gas mileage on average, mpg appears to decrease as
# the number of cylinders increase (with the exception of 3 cylinder cars)

'''
Part 2
Use a scatter matrix to explore relationships between different numeric variables.
'''
pd.scatter_matrix(auto)
plt.show()

# takeaway 1: weight, horsepower, and displacement have very similar relationships with mpg - that is, (not quite linearly) negatively correlated
# takeaway 2: similarly, weight, horsepower, and displacement are positively correlated with each other
# takeaway 3: mpg seems to improve slightly over time

'''
Part 3
Use a plot to answer the following questions:
-Do heavier or lighter cars get better mpg?
-How are horsepower and displacement related?
-What does the distribution of acceleration look like?
-How is mpg spread for cars with different numbers of cylinders?
-Do cars made before or after 1975 get better average mpg? (Hint: You need to 
create a new column that encodes whether a year is before or after 1975.)
'''
# drop 3 and 5 cylinder cars because of low observations
auto = auto[(auto.cylinders != 3) & (auto.cylinders != 5)]

# creates a color map for key cylinder categories (includes white category for 3 & 5 cylinders in case they are kept in data)
cyl = np.where(auto.cylinders==4, 'r', np.where(auto.cylinders==6,'b',np.where(auto.cylinders==8,'g', 'w')))
orgn = np.where(auto.origin==1, 'b', np.where(auto.origin==2,'y','r'))

# choose your color map!
cmap = cyl

# creates a scatter plot of weight and mpg
auto.plot(kind='scatter', x='weight', y='mpg', c=cmap)
plt.title('Weight and MPG')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()

# takeaway 1: mpg decreases as weight increase
# takeaway 2: adding the colormap by cylinder, we see that 4 cylinders get the best mpg and weight less
# takeaway 3: adding the colormap by origin, we see that the US makes cars that weigh more and get lower mpg

# creates a scatter plot of horsepower and displacement
auto.plot(kind='scatter', x='horsepower', y='displacement', c=cmap)
plt.show()

# takeaway: displacement is positively correlated with horsepower. US cars have greater displacement
#    and horsepower than most EU and JP autos; same with 8 vs 6 and 4 cylinder cars

# Histogram of acceleration
auto.acceleration.hist(bins=10)
plt.show()

auto.acceleration.hist(bins=10, by=auto.cylinders, sharex=True, sharey=True, layout=(3,1))
plt.show()

# Density of acceleration
auto.groupby('cylinders').acceleration.plot(kind='density', sharex=True, sharey=True)
plt.show()

# how is mpg spread for cars with different number of cylinders
auto.boxplot(column='mpg', by='cylinders')
plt.show()

auto[auto.cylinders==4].mpg.plot(kind='density', label='4')
auto[auto.cylinders==6].mpg.plot(kind='density', label='6')
auto[auto.cylinders==8].mpg.plot(kind='density', label='8')
plt.legend(borderaxespad=1.)
plt.show();

# takeaway: there is a wider distribution for autos with 4 cylinders, but those cars tend to get much better mpg
# QUESTION - IS THERE A BETTER WAY TO GENERATE THE LEGEND FOR THE DENSITY PLOT ABOVE?

# 
auto['after_75'] = np.where(auto.model_year <= 75, 0, 1)

auto.boxplot(column='mpg', by='after_75')
plt.show()

auto[auto.after_75==0].mpg.plot(kind='density', label='75 and before')
auto[auto.after_75==1].mpg.plot(kind='density', label='after 75')
plt.legend(borderaxespad=0.5)
plt.show()

# takeaway: cars made are likely to have better mpg than cars made before

