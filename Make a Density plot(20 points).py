# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:28:11 2022

@author: flore
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import random


def f(x,y):
    R = math.sqrt(x**2+y**2)
    #ans = math.sin(R)
    theta = math.atan2(y,x)
    ans = math.sin(R+theta)
    
    
    return ans


nx = 100
ny = 100
myf = np.empty((nx, ny), float) 
print(myf)


'''for i, j in zip(x, y):
    answer = f(i,j)
    List.append(answer)'''
    
print(myf)
for i in range(nx):
    x = -50 + i
    for j in range(ny):
        y = -50 + j
        myf[i,j] = f(x,y)
        
plt.imshow(myf)
plt.colorbar()
plt.show()


    



    