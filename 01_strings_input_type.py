"""
Created on Fri Jan 19 19:13:04 2018

@author: Brian

The purpose of this code is to practice with strings, input, and data types
"""

# Strings
# Define strings with either single quotes or double quotes

a = 2

str1 = 'hello'  # str1 is a variable with the string type
str2 = "there"
str1 + str2  # combine strings with the plus (+) operator
str1 + ' ' + str2  # combine multiple strings

str3 = str1 + ' ' + str2  # can assign a new string with existing strings

# string can only be combined with other strings when making strings
# trying to combine a string with a number will result in an error
'string' + 2

# you can get around this by converting a number to a string
str(2)  # converts a number, 2, to a string

'string' + str(2)

str1 + ' = ' + str(a)


# can print strings to console with the print function
print('This is a string')

# measure the length (number of characters) in a string with the len function
len('string')

# Indexing a string
# Strings can be indexed using square brackets - indexing starts at 0
str1[0]  # index the 0th element in the string
str1[-1]  # index the last element in the string
str1[0:3]  # index the 0th up to (but not including) the 3rd element

# the .split method can be used to divide a string at a certain character
str1.split('e')  # this splits 'hello' at the e, so you get 'h' and 'llo'
str3 = 'How do you do?'
str3.split(' ')  # splits "How do you do?" at spaces

# specify capitalization of letters
str3.upper()  # make all letters uppercase
str3.lower()  # makes string all lowercase
str3[0].lower()  # make 0th index of string lowercase

# to use an apostrophe in a string, use double quotes to define it
str4 = "The Police are Al's favorite band."

# or if you want to use double quotes in the string, use single quotes outside
str5 = 'She told me, "I love you."'



# Input/Eval Input
# ask the user to enter something in the console
# the prompt for the user is entered as a string inside the parentheses
c = input('Enter a number: ')

type(c)  # the input format is a string

d = eval(input('Enter a number: '))  # evaluating converts a string to a number

type(d)  # using eval(input()) makes a numerical data type, either int or float

type('3')  # this is a string
type(3)  # this ia an int
type(3.1)  # this is a float
int(3.1)  # this converts a float to an int
float(3)  # this converts an int to a float
