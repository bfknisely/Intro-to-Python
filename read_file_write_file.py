# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:38:08 2018

@author: Brian
"""

fname = 'acc2.dat'
infile = open(fname, "r")
longStr = infile.read()
data = longStr.split('\n')
infile.close()  # VERY IMPORTANT

data
len(data)
min(data)
max(data)