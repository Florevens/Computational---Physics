# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 03:44:37 2022

@author: flore
"""

import numpy as np
import matplotlib.pyplot as plt
import math



#Setting the radius
r = 4

#Setting the theta range
theta = np.linspace(0, math.pi, 25)

#setting the phi range
phi = np.linspace(0, 2*math.pi, 25)

#setting the empty lists to calculate the the 
xlist = []
ylist = []
zlist = []

for i in theta:
    for j in phi:
        
        #converting from spherical to rectangular
       xlist.append(r*np.sin(i) * np.cos(j))
       ylist.append((r*np.sin(i) * np.sin(j)))
       zlist.append(r*np.cos(i))
    
ax = plt.axes(projection='3d') 
ax.scatter3D(xlist,ylist,zlist)

#setting the x axis label
ax.set_xlabel('x')

#setting the y axis label
ax.set_ylabel('y')

#setting the z axis label
ax.set_zlabel('z')

