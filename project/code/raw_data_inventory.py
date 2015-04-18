# -*- coding: utf-8 -*-

import os
import csv

# get Current Working Directory
cwd = os.getcwd()

# set new working directory
raw_data_path = '../raw_data/'
os.chdir(raw_data_path)
cwd = os.getcwd()
 
# empty list
list_of_files = []
 
# create a list of files using os.walk()
for (dirpath, dirname, files) in os.walk(cwd):
    for filename in files:
        thefile = os.path.join(dirpath, filename)
        list_of_files.append(thefile)

# remove non-project related portion of the path (in other words, change to relative path instead of absolute)
# this will also allow the files to be accessed from the 'code' subdirectory of the project directory
for ii in xrange(len(list_of_files)):
    jj = list_of_files[ii].find('/raw_data')
    list_of_files[ii] = '..' + list_of_files[ii][jj:]
 
# print output to csv file
with open('raw_email_inventory.csv', 'wb') as f:
    wr = csv.writer(f)
    for item in list_of_files:
        wr.writerow([item]) # put item in list so that it will be written as a whole and not parsed
 
 
# make sure csv was written correctly
with open('raw_email_inventory.csv', 'rb') as f:
    new_list = f.readlines()

for j in new_list:
    print j

