# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 23:01:47 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os
import math


data = np.loadtxt('co2_data.txt', float, skiprows = 2)

#The decimal date, 1959-1961
Time = data[10:46:,2]

#Monthly average/Co2 concentration--including seasonal variations
#1959-1961
Co2Level = data[10:46:,3]

#ERROR
yerr = data[10:46,7]

plt.plot(Time, Co2Level)
plt.show()



def quad(x,p0,p1,p2,p3,p4):
    
    return np.sin(x*p1 + p2)*p0 + p3*x + p4

pp = 5
nn = len(Time)

guesses = (1, 1, 1, 1, 1)

(p0, p1, p2, p3, p4), cc = curve_fit(quad, Time, Co2Level, p0 = guesses, sigma = yerr)
(up0, up1, up2, up3, up4) = np.sqrt(np.diag(cc))

xmod = np.linspace(Time[0], Time[-1], 100)

ymod = quad(xmod, p0, p1, p2, p3, p4)


#Plotting the best quadratic fit
plt.errorbar(Time, Co2Level, yerr, fmt = 'bo')
plt.plot(xmod, ymod,'r')

yfit = quad(Time, p0, p1, p2, p3, p4) 
yys = (Co2Level-yfit)**2/yerr**2

plt.title('Quadratic fit(Time vs Average')
plt.xlabel('Time starting at 0')
plt.ylabel('Montly average')

yfit = quad(Time, p0, p1, p2,p3,p4)  

yys = (Co2Level-yfit)**2/yerr**2

chisquared = sum(yys)/(nn-pp)
print(f'Reduced Chisquared = {chisquared:.3f}')
print(p0)



    



