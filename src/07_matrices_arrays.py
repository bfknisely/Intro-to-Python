"""
Created on Fri Jan 19 19:13:04 2018

@author: Brian

The purpose of this code is to learn matrices and numpy n-dimensional arrays
"""

# Numpy matrix is strictly 2-dimensional, while numpy arrays can be any
# dimension

# Start with matrices

import numpy as np  # imports numpy module and names it "np"

# make 2 x 2 matrix with 4, 3 in first row and 2, 1 in second row
a = np.mat('1, 2; 3, 4')
print(a)  # print matrix

# note that a is a "matrix" object, which is different from an "array" object
type(a)

# Index a matrix by using square brackets and 2 indices [row, column]
a[0, 0]  # python indexing starts at 0 - get element in 0th row, 0th column
# index order is [row, column] for matrices
a[1, 0]  # python indexing starts at 0 - get element in 0th row, 0th column
a[-1, -1]  # get element in last row, last column

# get ALL values in 0th column
a[:, 0]

# get ALL values in last row
a[-1, :]
a[-1]  # same as line above; get all values in last row

a.T  # take transpose of matrix with the "T" method

a.I  # take inverse of matrix with the "I" method
a.i  # methods/functions are case-sensitive; must use uppercase I for inverse

b = np.mat('1, 3; 5, 7')  # create another matrix

a*b  # matrix multiplication is with asterisk (star) operator

a+b  # elementwise addition of matrices
a+2  # elementwise addition of matrix with scalar

a-b  # elementwise subtraction of matrices
a-4  # subtract scalar from matrix

np.multiply(a, 3)  # elementwise multiplication of matrix with scalar
a*3  # elementwise multiplication of matrix with scalar also works with *
np.multiply(a, b)  # elementwise multiply 2 x 2 matrix with 2 x 2 matrix

np.divide(a, 3)  # elementwise division of matrix with scalar
np.divide(a, b)  # elementwise divide 2 x 2 matrix with 2 x 2 matrix

np.power(a, 3)  # elementwise exponentiation with scalar
np.power(a, b)  # elementwise exponentiation with matrix elements

# Alternatively, numpy arrays can be used in lieu of matrices

c = np.array([[1, 2], [3, 4]])  # create 2 x 2 array (note the square brackets)
print(c)  # print out the array
type(c)  # show that it is an ndarray

d = np.array([[1., 3], [5, 7]])  # create another array

# can easily form arrays using lists
np.array(a)  # can convert a matrix into an array easily
np.mat(c)  # and vise versa

np.zeros(5)  # create 1D array of zeros with 5 columns
z = np.zeros([4, 6])  # create 2D array of zeros with 4 rows, 6 columns
print(z)

np.size(z)  # get number of elements in array
np.shape(z)  # get dimensions of array

np.identity(4)  # create identity matrix array of size 4 x 4

np.ones(5)  # create 1D array of ones with 5 columns
np.ones([1, 5])  # create array of ones with 1 row, 5 columns
np.ones([3, 5])  # create 2D array of ones with 3 rows, 5 columns

# Indexing arrays and assignment
c[0, 0]  # get element at 0th row, 0th column of array c
c[:, 1]  # get all rows of 1st column of c

# Indexing a range of values in an array

ar = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(ar)
# indexes the rows in 0th up to but not including 2nd position, and the columns
# in the 1st up to but not including the 3rd position
ar[0:2, 1:3]

ar[:, 0:2]  # index all rows, columns from 0 up to but not including 2
ar[-1, :]  # index the last row, all columns
ar[-1]  # index the last row, all columns

# assigning individual values
z[-1, -1] = 99  # assign last row, last column of z to be 99
d[1, 1] = 'cow'  # note, arrays can only contain one data type (e.g. float)
print(z)
z[0] = 33  # assign all values in first row of z to be 33
print(z)
z[:, -1] = np.ones(4)  # assign all values in last column of z to be 1
print(z)

# When assigning values to an array, the size of the input must be either 1
# (so you assign a scalar to all points) or equal to the indexed area
# Example: these will give an error
z[:, -1] = np.ones(3)  # assign all values in last column of z to be 1
z[0, 0] = np.zeros(3)  # assign all values in last column of z to be 1

# insert array d into array z in rows 1 up to but not including 3
# and in columns 3 up to but not including 5
z[1:3, 3:5] = d
print(z)

# Since matrices are strictly 2D while arrays can be any-D, arrays are more
# flexible. There are many common functions between the two, but some
# differences as well. For example:

# Matrix multiplication
a*b  # matrix multiplication is with asterisk (star) operator
a@b  # array matrix multiplication is with @ operator

# Dot products
np.dot(a, b)
np.dot(c, d)

# Elementwise operations
# All regular math operators (e.g. +, -, *, /, **) are elementwise on arrays
# For matrices, you must use functions like multiply or power
2*c  # elementwise multiply 2 by array
2*a  # elementwise multiply 2 by matrix
# order does not matter with scalar multiplication
c*2  # elementwise multiply array by 2
c+2  # elementwise add array plus two
a+b  # elementwise addition/subtraction works for matrices too
c/7  # elementwise divide array by 7
c**2  # take each element in array to power of two

print(z)  # recall what z looks like
q = z.nonzero()  # get nonzero elements of array
# results are paired row-column coordinates
# returns an empty array if no elements are nonzero
z[q]  # indexes nonzero elements in array

np.linalg.det(a)  # get determinant of square matrix
