"""
Created on Fri Jan 19 19:13:04 2018

@author: Brian

The purpose of this code is to learn plotting using MatPlotLib and Numpy
"""

import matplotlib.pyplot as plt  # imports MatPlotLib module
import numpy as np  # import Numpy
import os  # imports OS module - used for saving/reading files

# Standard 2D plots require data with two coordinates
# Assume we have the following data:
xData = np.array([12.5, 25, 37.5, 50, 62.5, 75])  # x data
yData = np.array([20, 59, 118, 197, 299, 420])  # y data
# The data doesn't have to be numpy arrays - lists work too for plotting

# Making your own lists/arrays is useful for plotting
list(range(10))  # make a list from 0 to 9 in increments of 1
np.array(range(10))  # make a 1D array from 0 to 9 in increments of 1

# Useful functions to create linear or logarithmic 1D arrays

# linspace inputs are (Start, Stop, num=NumberOfElements)
np.linspace(0, 10, num=21)  # create linear array from 0 to 10 with 51 elements
np.linspace(10, -10, num=51)  # Start can be greater than Stop
np.linspace(0, 1e5, num=100)  # create linear array from 0 to 100,000 with 100
#                               elements

# Similarly, logspace can be used to make an array with log spacing
xLog = np.logspace(0, 10, num=21)
# create log array from 0 to 10 with 21 elements
print(xLog)

# If you are using an IDE with the IPython console (e.g. Spyder), figures can
# be displayed in line in the console. If you'd rather have your figures as
# separate popups a la Matlab, check your IDE's settings.
# In Spyder, this can be configured through:
# Tools --> Preferences --> IPython console --> Graphics --> Backend: Automatic
# Set Backend to Inline (default) if you want graphics in the Console instead

# Making a basic plot:
# (Note, you must run all lines together in order to make one plot with all
# of the specified elements)

fig, ax = plt.subplots()  # define figure object and axis object
plt.plot(xData, yData)  # plots the x-y data on the current figure

# Sometimes you need to define figure and axis objects to edit other settings
# For basic usage, you don't need to define them:
plt.plot(xData, yData)  # plots the x-y data on the current figure

# Save your plot with the plt.savefig function
plt.plot(xData, yData)  # plots the x-y data on the current figure
fname = 'MyPlotImage.png'  # choose filename & extension (e.g. png, jpg, pdf)
plt.savefig(fname)  # save current figure as filename

# The file will save in the working directory if only a filename is specified
# Check the current working directory with getcwd
os.getcwd()  # check current working directory
os.startfile(fname)  # open file with the OS's default program

# Save as higher-quality image by increasing the dpi
plt.plot(xData, yData)  # plots the x-y data on the current figure
plt.savefig(fname, dpi=320)

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

# Line styles
# - = solid line
# -. = dash-dot line
# -- = dashed line
# : = dotted line
# For more lines (and general options for 2D lines) go to:
# https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html

# The color, marker, and line format can be specified in any order
# e.g. 'ko-' or 'o-k'

plt.plot(xData, yData, 'ko')  # plots with black (k) circles (o) and no line

# Good plots need axis labels. Axis labels are added with xlabel and ylabel

plt.plot(xData, yData, 'ko')  # plots the x-y data with black (k) circles (o)
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot

# Multiple data sets can be plotted together
# We need another data set
xData2 = [11.25, 22.5, 33.75, 45.0, 60, 72]
yData2 = [30., 60, 100., 150, 270, 410]

# Elements can be plotted together either on the same line of code:
# The first data set is in black circles with no line
# The second data set is plotted with blue triangles and a dotted line
plt.plot(xData, yData, 'ko', xData2, yData2, 'b:^')
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot

# Or on separate lines of code:
plt.plot(xData, yData, 'rx')  # red X markers
plt.plot(xData2, yData2, 'bs')  # blue square markers
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot

# You can add a legend with the legend function; input is an array of strings
plt.plot(xData, yData, 'md')  # magenta diamond markers
plt.plot(xData2, yData2, 'y.')  # yellow dot markers
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot
plt.legend(['Test 1', 'Test 2'])

# More on legends here: https://matplotlib.org/users/legend_guide.html

# Set the axis limits using xlim(xmin, xmax) and ylim(ymin, ymax)
plt.plot(xData, yData, 'ko')
plt.plot(xData2, yData2, 'bs')
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot
plt.legend(['Test 1', 'Test 2'])
plt.xlim(0, 80)
plt.ylim(0, 500)

# Plot on log-log axes using the "loglog" function in place of "plot"
plt.loglog(xData, yData, 'ko')
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot

# Or plot with a logarithmic x-axis and linear y axis with "semilogx"
plt.semilogx(xData, yData, 'ko')
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot

# Or vise versa with "semilogy"
plt.semilogy(xData, yData, 'ko')
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot

# Turn on the grid with the grid function
plt.plot(xData, yData, 'ko')
plt.grid(True)  # Turns on major gridlines

# Simple polynomial regression for (xData, yData)

degree = 2  # Choose order of polynomial
# create fit object with inputs (x, y, degree)
fit = np.polyfit(xData, yData, degree)
yFit = np.polyval(fit, xData)  # Calculate y_fit for each x data point
R = np.corrcoef(xData, yData)[0, 1]  # Get correlation coefficient (R)
print(R)  # Print correlation coefficient
Rsq = R**2  # Calculate R^2 value
print('The R-squared value is {0:0.6}'.format(Rsq))  # Print R^2 value

plt.plot(xData, yData, 'ko', xData, yFit, 'r')  # Plot data with regression
plt.xlabel("Velocity [mph]")  # add x-label to plot
plt.ylabel("Stopping Distance [ft]")  # add y-label to plot


# Small note on data types:
# Most (if not all) Numpy functions use 64-bit floating-point numbers (aka
# float64) by default. This means calculations are more precise compared to
# default Python numbers (which are 32-bit) at the cost of speed. If speed is
# of high importance, consider using 32-bit numbers with Numpy. These can be
# specified in most functions with "dtype"; e.g. linspace:

x1 = np.linspace(4, 100, 25)  # this creates an array of float64s (default)
type(x1[0])  # data type is float64 for individual elements

x2 = np.linspace(4, 100, 25, dtype='float32')  # array of float32s
type(x2[0])  # data type is float32 for individual elements

# Read more on data types here:
# https://docs.scipy.org/doc/numpy/user/basics.types.html
