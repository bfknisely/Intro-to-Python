# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:38:08 2018

@author: Brian
"""

# opening a 1D list of numbers

fname = 'acc2.dat'  # select name of file
infile = open(fname, "r")  # open file with "read" access
longStr = infile.read()  # read contents of file into one long string
data = longStr.split('\n')  # separate long string into discrete values
# split the string at the "newline" character
infile.close()  # VERY IMPORTANT - close the file when you're done with it

data
len(data)  # look at length of data
min(data)  # find minimum value
max(data)  # find maximum value
