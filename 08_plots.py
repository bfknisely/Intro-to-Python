"""
Created on Fri Jan 19 19:13:04 2018

@author: Brian

The purpose of this code is to learn plotting using MatPlotLib and Numpy
"""

import matplotlib.pyplot as plt  # imports MatPlotLib module
import numpy as np  # import Numpy

# Standard 2D plots require data with two coordinates
# Assume we have the following data:
xData = [12.5, 25, 37.5, 50, 62.5, 75]  # x data
yData = [20, 59, 118, 197, 299, 420]  # y data

# If you are using an IDE with the IPython console, figures can be displayed in
# line in the console, as shown here:

fig, ax = plt.subplots()  # define figure object and axis object
plt.plot(xData, yData)  # plots the x-y data on the current figure

# Now we have made a basic plot. Notice the default format is a thin,
# continuous, blue line.

# What if you wanted black circles instead?
# The line/marker format can be specified with a color and/or marker style,
# entered immediately after the (x, y) data in the plot.plot() function

# Colors:
# k = black
# b = blue
# r = red
# m = magenta
# c = cyan
# y = yellow
# g = green
# For more colors go to: https://matplotlib.org/api/colors_api.html

# Markers:
# o = circles
# x = x
# . = small dot
# + = plus
# s = square
# d = diamond
# p = pentagon
# ^ = triangle
# For more markers go to: https://matplotlib.org/api/markers_api.html

# The color and line format can be specified in either order; e.g. 'ko' or 'ok'

plt.plot(xData, yData, 'ko')  # plots the x-y data with black (k) circles (o)

# Good plots need axis labels. Axis labels are added with xlabel and ylabel

# Also note, you must run all lines together in order to make one plot with all
# of the specified elements

plt.plot(xData, yData, 'ko')  # plots the x-y data with black (k) circles (o)
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot
