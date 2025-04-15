# This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

#author: gerry callaghan

import matplotlib.pyplot as plt # this library has some functions that make plotting data easier
import numpy as np # this library allows us perform functions on our arrays

# I'm going to seed my random numbers so i get the same set of random numbers each time
np.random.seed(1)

# initialise my variable normal_data equal to the normal distribution of random numbers
normal_data= np.random.normal(5, 2,size=1000)
# the first number 5 is the mean, the second number 2 is the standard deviaton, 
# and the third number 1000 is the number of observations

# Now to plot my series of numbers
# my line graph is going to be a numpy array containing values between 0 and 10, 
# these will be my horizontal axis points
xpoints=np.array([0,1,2,3,4,5,6,7,8,9,10])
# print(f"x-axis points are: {xpoints}")


# my vertical y-axis points will then be equal to values of the x-axis (see the array xpoints above) cubed
# we cube the array by multiplying it by itself again and again
# Note our numpy array xpoints with square brackets is not like a matrix which also has square brackets
# we don't have to transpose it to multiply by itself as in matrices, forget row vs columns, 
# we can think of the array as just a vertical column of numbers inside square brackets
ypoints=xpoints*xpoints*xpoints
# think of mulitplying across each of the three instances of our xpoints array
# ypoints = [0x0x0, 1x1x1, 2x2x2, 3x3x3, 4x4x4, 5x5x5, 6x6x6, 7x7x7, 8x8x8, 9x9x9, 10x10x10]
# ypoints = [0,1,8,27,64,125,216,343,512,729,1000]
# print(f"y-axis points are: {ypoints}")


# i plot my line graph by passing the x points, y points, and the label
plt.plot(xpoints, ypoints,label="$X^3$") # this is where matplotlib does the heavy lifting for us, we pass three variables
# the first variable is our array containing the x-axis coordinates, 
# the second variable is our array containing the y-axis coordinates, 
# the third variable is name of the series for the legend,
# the dollar symbols either side of X^3 are latex 
# - examples of latext from here https://stackoverflow.com/questions/4028267/how-to-render-latex-markup-using-python
# it just displays the  3 as a superscript so it's visually easier to read

# i plot my line graph by passing the normal distribution 
# comprising of random numbers with mean 5, stddev of 2) 
# and the name of the series for the legend
plt.hist(normal_data,label="Normal Distribution")

# addition of labels and titles as per lab session and here https://www.w3schools.com/python/matplotlib_labels.asp

# I want to labels. 
plt.xlabel('x axis') 
plt.ylabel('y axis')

#I want to put a title on my chart as follows
plt.title("Normal Distribtion vs. $X^3$")

# i want to add a legend as follows
# it shows you how to add a legend here https://www.w3schools.com/python/matplotlib_pie_charts.asp
# of course in their case on w3schools, they didn't explicity explain that their labels array were for BOTH on the piechart 
# and for the legend - thanks to trial and error it worked
plt.legend()

# now to show it
#plt.show()

# or alternatively to save the chart
plt.savefig("Norm_Dis_vs_X-cubed")