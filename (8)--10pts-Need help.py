# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 03:39:27 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import sqrt,exp
from matplotlib import cm




def psi(x,y):
    r = sqrt(x**2+y**2)
    return x*(6-r)*exp(-r/3)


'''nx = 100
ny = 100
myf = np.empty((nx, ny), float) 
print(myf)
for i in range(nx):
    x = i
    for j in range(ny):
        y = j
        myf[i,j] = psi(x,y)
        
plt.imshow(myf)
plt.colorbar()
plt.show()'''

xs = np.linspace(-20,20,200) 
ys = np.linspace(-20,20,200)

X,Y = np.meshgrid(xs,ys)

myf = psi(X,Y)

plt.imshow(myf)









