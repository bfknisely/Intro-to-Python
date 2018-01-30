"""
Created on Fri Jan 19 19:13:04 2018

@author: Brian Knisely

The purpose of this code is to learn about assigning variables, displaying
them, doing basic math, and importing modules

This part at the top is called the docstring, where you can put relevant
details about the code like when it was made, who made it, and what the purpose
of the code is.

The recommended way to go through this file is on a line-by-line basis. Using
an IDE like Spyder, you can run a single line at a time (with F9 in Spyder).
"""

# Assigning variables

a = 2
b = 3

# Displaying variables

print(a)  # Display in console

# Doing math

a+b  # Addition
a-b  # Subtraction
a*b  # Multiplication
a/b  # Division
a**b  # Exponent (power)
2a  # Note that without any operator, this will return an error
2*a  # This will multiply 2 times a without any problems
round(3.1)  # Round to nearest integer (3)
round(3.5)  # Rounds up to 4
sqrt(a)  # if a function name does not exist, it will return an error

import math  # modules contain additional functions for a specific purpose

# functions within a module are used with the dot (.) character
math.sqrt(a)  # square root
math.cos(a)  # cosine (argument is in radians)
math.ceil(3.1)  # ceiling; increases to nearest integer
math.floor(3.5)  # floor: reduces to nearest integer
math.floor(3.99999)
round(3.999999)  # round is not in the math module, so no "math." is needed

import math as m  # you can rename modules for convenience
m.sqrt(a)  # the functions in a module are used with the module as imported

# using "from module import function" lets you call that function directly
from math import sqrt, cos  # can import specific functions

sqrt(a)  # take square root - no module name needed because "from" was used

sqrt(-1)  # function is not defined for values less than zero


import cmath  # complex math function
cmath.sqrt(-1)

# sometimes different modules can have overlapping names of functions
from cmath import sqrt

sqrt(-1)  # square root with complex math function returns complex (imag) value
# 1j is the imaginary number, defined as square root of -1