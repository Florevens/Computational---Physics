# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:14:48 2022

@author: flore
"""
import math
import numpy as np
import matplotlib.pyplot as plt

x = int(input("Enter your chosen range: "))
#arr = np.linspace(0,x,200)
arr = np.linespace(0,x,20)
f1 = arr**2 + 8
f2 = arr**2 - 8
print(arr, '\n')

print(f1, '\n')
print(f2, '\n')

#plots using color and linetypes(5pts)
plt.xlim(0,20)
plt.ylim(0,72)
#plt.plot(arr, f2, color = "blue", linestyle = "dotted") 
#plt.plot(arr, f1, "r-", linestyle = "dashed")
#plt.plot(f1,f2,"black", linestyle = "dashdot")

#Plot using lines in shapes connected(5pts)
plt.plot(arr, f2, color = "blue", linestyle = "-*") 
plt.plot(arr, f1, "r-", linestyle = "-@")
plt.plot(f1,f2,"black", linestyle = "--&")




