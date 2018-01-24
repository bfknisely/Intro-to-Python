# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:38:08 2018

@author: Brian
"""

###########################################
# Reading a 1D list of numbers as a list
###########################################

fname = 'acc2.dat'  # select name of file
infile = open(fname, "r")  # open file with "read" access
longStr = infile.read()  # read contents of file into one long string
data = longStr.split('\n')  # separate long string into discrete values
# split the string at the "newline" character
infile.close()  # VERY IMPORTANT - close the file when you're done with it

data = list(filter(None, data))  # remove empty strings from list

data
data = list(map(float, data))

len(data)  # look at length of data
min(data)  # find minimum value
max(data)  # find maximum value

############################################
# Writing to a file
############################################

a = list(range(10))

f = open('results.txt', 'w')  # opens (and creates) file object
#                               with write access
for n in range(len(a)):
    f.write(str(a[n])+'\n')  # one method is to write strings to files
#                              \n is a "newline" character

# the .write method requires a string as input
# note: .write will overwrite an existing file
# to append to a file instead, use .append

f.close()  # close the file


# Intro to the .format method

# The .format method uses curly brackets to specify where you would like to
# insert a value, and then within the parentheses you specify what to insert
# into the curly brackets. You can insert many data types into a string with
# the .format method.

# Create string to say Gal is a good dog
'{} is a good dog'.format('Gal')

# This string does the same thing. Notice how you can insert multiple values
'{} is a good {}'.format('Gal', 'dog')

# You can insert numbers using .format as well
'{} is {} years old'.format('Gal', 11)

# Adding numbers into the curly brackets lets you specify where you would like
# to insert the inputs specified in the parentheses
'{0} is the 0th index'.format('A', 'B')
'{1} is the 1st index'.format('A', 'B')
'{0} {1} {1} {0}'.format('A', 'B')
'{1}{0}{1}{2}'.format('A', 'B', 'E')

# .format can be used to specify number formats
pi = 3.141592653589793
'Pi is equal to {}'.format(pi)  # this uses default number formatting
'Pi is equal to {:.5}'.format(pi)  # this limits the number to 5 digits
'{0} is equal to {1:.5}'.format('Pi', pi)  # same result as line above

# Using .format to write more elegantly to a file

x = [1., 10., 100., 1000., 10000.]  # float format
y = [1, 2, 3, 4, 5]  # integer format
z = [0.123, 0.456, 0.789, 0.135, 0.246]  # float format

f = open('results2.txt', 'w')

f.write('{}, {}, {}\n'.format('x', 'y', 'z'))
for n in range(len(x)):
    f.write('{}, {}, {}\n'.format(x[n], y[n], z[n]))
f.close()  # close the file

# Now make it even nicer by specifying field widths

f = open('results2_nicer.txt', 'w')
# give characters 5 spaces each
f.write('{:5}, {:5}, {:5}\n'.format('x', 'y', 'z'))
for n in range(len(x)):
    # gives characters 5 spaces each
    f.write('{:5.0}, {:5}, {:5}\n'.format(x[n], y[n], z[n]))
f.close()

# Further, you can specify the (maximum) number of decimals
# this example goes to using the print function so we stop making so many files

print('{:10}, {:10}, {:10}'.format('x', 'y', 'z'))
for n in range(len(x)):
    print('{:10}, {:10}, {:10.1}'.format(x[n], y[n], z[n]))

# Or choose which substitute belongs in each position by putting a number
# before the colon

print('{1:5}, {2:5}, {0:5}'.format('x', 'y', 'z'))
# this places 'y' first, then 'z', then 'x'
for n in range(len(x)):
    print('{1:10.0}, {2:10}, {0:10}'.format(x[n], y[n], z[n]))
