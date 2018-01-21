# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 18:08:40 2018

@author: Brian

The purpose of this code is to practice using function definitions in Python
"""


def main():
    # do something within function
    # According to Pep8 guidelines, functions should have two returns before
    # and after the definition, as illustrated here
    print('Hello world')  # this is a comment


main()  # run main function


def timesTwo(x):  # value in parentheses is an input
    return 2*x  # variables are outputted using "return" function


timesTwo(10)  # Run "timesTwo" function with 10 as input

a = 5  # Define some variable
b = timesTwo(a)  # Run function and store as new variable


def sumThreeNums(m, n, p):  # use multiple inputs by separating with commas
    return m+n+p  # can perform math operations within "return" statement


sumThreeNums(1, 2, 3)  # test "sumThreeNums" function


def squareRoot(x):  # function to return positive and negative sqrts
    import math  # can import libraries within a function
    root1 = math.sqrt(x)  # take square root
    root2 = -math.sqrt(x)  # take -1*square root
    return root1, root2  # return both values


a, b = squareRoot(9)  # run function and store values as variables
a
b
squareRoot(sumThreeNums(2, 3, 4))  # can do functions within functions


def makeZeroList(x):  # little function to demonstrate making a list of 0s
    return [0]*x


makeZeroArray(5)  # test out the function with 5 as an input
a = makeZeroArray(5)  # assign value to variable a
a

################################################
# Important, "pythonic" way of using functions #

# Note, the functions below don't really do anything, so running them isn't
# super useful. Pay more attention to the structure of this code

# Pretend this code is contained within its own file called "important.py"

"""
Docstring goes here

Created by Brian on Date

The purpose of this code is to use functions in an appropriate, Pythonic way
and to illustrate the "__name__" construct

The functions below can each be imported into another Python code and called.
e.g.
import important
important.main()  # Executes main function by calling it

However, the section at the bottom will execute only when this code is run
directly. This allows the script to be used for this particular purpose, while
the functions themselves can be called for other purposes.
"""


def startFunction(x):  # Define a function that you want to use
    myList = [0]*x  # initialize list of zeros with length x
    return myList  # return list of zeros


def middleFunction(myList):  # Define some other function
    for n in range(len(myList)):
        myList[n] = n  # write index of array into array
    return myList


def lastFunction(myList):  # Define another function
    tot = sum(myList)
    maxVal = max(myList)
    return tot, maxVal


def main():
    myNum = startFunction(5)
    myList = middleFunction(myNum)
    tot, maxVal = lastFunction(myList)
    print('The input value was {}'.format(myNum))
    print('The sum of values up to {} is {}'.format(myNum, tot))


if __name__ == "__main__":
    # This code only runs when "important.py" is run directly
    main():
