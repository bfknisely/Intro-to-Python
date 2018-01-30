"""
Created on Fri Jan 19 19:13:04 2018

@author: Brian Knisely

The purpose of this code is to learn about assigning variables, displaying
them, doing basic math, and importing modules

This part at the top is called the docstring, where you can put relevant
details about the code like when it was made, who made it, and what the purpose
of the code is.
"""

# %% Lists/indexing lists
# Assign lists using square brackets

q = [1, 2, 3, 4]  # makes a list called q
type(q)  # note that q is a list
len(q)  # length of array
# In Python, lists start at 0! Unlike Matlab or R where lists start at 1
q[0]  # index 0th element
q[3]  # index 3rd element
q[-1]  # index last element
q[-2]  # index second-to-last element
q[-4]  # index fourth-to-last element
q[-5]  # index fifth-to-last element (out of range)
q[0:2]  # index 0th up to but not including 2nd element
q[0:4]  # index 0th up to but not including 4th element
q[0:4:2]  # index from the 0th element up to but not including the 4th element
#           in increments of 2
q[0::2]  # index from the 0th element to the end in increments of 2
q[::2]  # index the entire list in increments of 2

w = list(range(10))  # create list from 0 to 9
print(w)
w[7]  # index 7th element
w[0::3]  # index from 0th element to end in increments of 3
w[2::3]  # index from 2nd element to end in increments of 3
w[3::]  # index from 3rd element to end

z = []  # create empty list
len(z)  # length of an empty list is 0
z.append(3)  # append a 3 to the list
z
z.append(7)  # append a 7 to the list
z
z.remove(7)  # remove the 7 from the list
z.append(1)  # append a 1 to the list
z.append(2)  # append a 2 to the list
z.append(1)  # append another 1 to the list
z
z.remove(1)  # remove the first 1 in the list
z

# Lists may have mixed data types (e.g. integers and strings)
z.append('words')  # append a string to the list
z
z[0]  # index 0th element
z[1]  # index 1st element
z[-1]  # index last element
z[-1][0]  # sub-index 0th element of last element in list

# %% For loops

myList = [2, 3, 5, 8, 13]  # create a list

# loop to print out the list (must select both lines if running line-by-line)
for n in myList:
    print(n)

# Use the range(n) function to make for loops from i = 0 up to i = n-1
for i in range(10):
    print(i)

# Elements in strings may also be used as indices for for loops
for n in 'my string':
    print(n)

# Using integers as indicies for for loops is more useful than strings
str1 = 'my string'  # assign string as variable
len(str1)  # determine length of 'this string'
# since the range operator is used, the index will go from 0 to (11-1)
for n in range(len(str1)):
    print(n, ':', str1[n])  # print formatted number and corresponding string

# When for loops are used for individual operations on a list, a similar
# construct can be used
myList = [2, 3, 5, 8, 13]  # create a list
for j in range(len(myList)):
    print(myList[j])
