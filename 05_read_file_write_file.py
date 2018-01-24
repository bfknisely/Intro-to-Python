# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:38:08 2018

@author: Brian
"""

# Reading a 1D list of numbers as a list

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


# Writing to a file

a = list(range(10))

f = open('results.txt', 'w')
for n in range(len(a)):
    f.write(str(a[n])+'\n')  # one method is to write strings to files
# the .write method requires a string as input
# note: .write will overwrite an existing file
# to append to a file instead, use .append
f.close()  # close the file

# Using ".format" to write more elegantly to a file

x = [1., 10., 100., 1000., 10000.]
y = [1., 2., 3., 4., 5.]
z = [0.123, 0.456, 0.789, 0.135, 0.246]

f = open('results2.txt', 'w')
f.write('{}, {}, {}\n'.format('x', 'y', 'z'))
for n in range(len(x)):
    f.write('{}, {}, {}\n'.format(x[n], y[n], z[n]))
f.close()

# Now make it even nicer by specifying field widths

f = open('results2_nicer.txt', 'w')
f.write('{:5}, {:5}, {:5}\n'.format('x', 'y', 'z'))
# gives characters 5 spaces each
for n in range(len(x)):
    f.write('{:5}, {:5}, {:5}\n'.format(x[n], y[n], z[n]))
    # gives characters 5 spaces each
f.close()

# Further, you can specify the (maximum) number of decimals
# this example goes to using the print function so we stop making so many files

print('{:5}, {:5}, {:5}\n'.format('x', 'y', 'z'))
for n in range(len(x)):
    print('{:10}, {:10.0}, {:10.1}\n'.format(x[n], y[n], z[n]))

# Or choose which substitute belongs in each position by putting a number
# before the colon

print('{1:5}, {2:5}, {0:5}\n'.format('x', 'y', 'z'))
# this places 'y' first, then 'z', then 'x'
for n in range(len(x)):
    print('{1:10.0}, {2:10}, {0:10}\n'.format(x[n], y[n], z[n]))
