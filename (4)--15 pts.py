# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:17:34 2022

@author: flore
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import sqrt,exp


data = np.loadtxt('decay1.txt', float, skiprows = 1)
data2 = np.loadtxt('decay2.txt', float, skiprows = 1)

x1 = data[:,0]
y1 = data[:,1]

x2 = data2[:,0]
y2 = data2[:,1]

plt.plot(x1,y1, "*", label = "decay1", color = "r")
plt.plot(x2,y2, ".", label = "decay2")
plt.legend(loc='upper right')
plt.show()

yerr1 = sqrt(y1)

    

yerr2 = sqrt(y2)
    
 #Plotting the errorbars   
'''plt.errorbar(x1,y1,yerr1, label = "decay1", color = "r")
plt.title("Decay1 errorbar")
plt.show()
plt.errorbar(x2,y2,yerr2, label = "decay2")
plt.title("Decay2 errorbar")
plt.show()'''

plt.errorbar(x1,y1,yerr1, label = "decay1", fmt = "r.")
plt.semilogy(x1, y1)
plt.title("Decay1 errorbar")
plt.show()


plt.errorbar(x1,np.log(y1),yerr1, label = "decay1", fmt = "r.")
plt.title("Decay1 errorbar")
plt.show()


plt.errorbar(x2,y2,yerr2, label = "decay2", fmt = "g.")
plt.semilogy(x2,y2)
plt.title("Decay2 errorbar")
plt.show()

#A straight line on a semi-log graph means that the original x and y sets have
#an exponential relationship.









    

    
