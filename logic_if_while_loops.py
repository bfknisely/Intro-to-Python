# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:13:04 2018

@author: Brian

The purpose of this code is to practice with logical statements, if
statements, and while loops.
"""

2 == 3
2 == 2
2 > 3
2 >= 2
2 != 3
2 != 3 and 2 < 3
2 != 3 or 2 > 3
True
False
True and False
True or False
False and False

# Checking if a string is in another string
str1 = 'hello'
'h' in str1
'hell' in str1
'q' in str1
'q' not in str1

# Checking if a value is in a list
primes = [2, 3, 5, 7, 11, 13, 17]
3 in primes
4 in primes
4 not in primes

a = input('Enter 2 or any other number: ')  # Ask user for some number
if a == 2:
    print('a is equal to 2')

if a == 2:
    print('a is equal to 2')
else:
    print('a is not equal to 2')

# While loops

a = 1
while a != 8:
    print(a)
    a = a + 1
    print('...')
print('Congratulations.')

a = 2
while a < 7:
    a += 1
    print(a)

a = 1
while a <= 32:
    a *= 2
    print(a)
