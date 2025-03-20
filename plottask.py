# This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

#author: gerry callaghan

import matplotlib.pyplot as plt
import numpy as np

#I'm going to seed my random numbers so i get the same numbers each time
np.random.seed(1)
#the first number is the mean, the second is the standard deviaton, third number is the number of observations
# so my normal distribution is expressed as follows
normal_data= np.random.normal(5, 2,size=1000)

# my linegraph is going to be an array containing values between 0 and 10, these will be my horiztonal axis points
xpoints=np.array([0,1,2,3,4,5,6,7,8,9,10])
#print(f"xpoints are: {xpoints}")

#my vertical axis points will then be the x-axis value cubed
ypoints=xpoints*xpoints*xpoints

# i plot my line graph by passing the x points, y points, and the label
plt.plot(xpoints, ypoints,label="X^3")

# i plot my line graph by passing the normal distribution data and the label
plt.hist(normal_data,label="Normal Distribution")

#I want to put a title on my chart as follows
plt.title("Normal Distribtion vs. X^3")

# i want to add a legend as follows
plt.legend()

#now to show it
plt.show()

#now to save the chart
plt.savefig("Norm_Dis_vs_X-cubed")