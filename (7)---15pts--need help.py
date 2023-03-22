# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 02:43:25 2022

@author: flore
"""

#importing the necessary libraries.
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt,exp

#Number of points
N = 200

#Setting up the grid

x_points = np.linspace(-20,20,N) 
y_points = np.linspace(-20,20,N)


#The surface function
def psi(x,y):
    
    #defining the radius for every single combination of x and y
    r = sqrt(x**2+y**2)
    
    #Returning the surface
    return x*(6-r)*exp(-r/3)
    
#Creating the grid usin numpys "meshgrid"
X,Y= np.meshgrid(x_points,y_points)

#Computing Z for every x and y combination on the grid
z_points= psi(X,Y)

#Plotting the surface plot for the x, y and z data

#Creating a 3d axes using projection
ax = plt.axes(projection = '3d')

#Using "plot_surface" to plot the surface
ax.plot_surface(X,Y,z_points)

#setting the x axis label
ax.set_xlabel('x')

#setting the y axis label
ax.set_ylabel('y')

#setting the z axis label
ax.set_zlabel('$\psi(x,y)$')






