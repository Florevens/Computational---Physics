# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:18:49 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import sqrt,exp


data = np.loadtxt('wavedata.txt', float, skiprows = 1)

t = data[:,0]
y = data[:,1]
yerr = np.ones(len(t))*.20

def sinF(x,p0,p1,p2,p3):
    
    return p0*np.sin(p1*x + p2) + p3

plt.plot(t, y)
plt.title('t(sec) vs y(V)')
plt.xlabel("t (sec)")
plt.ylabel('y (V)')
plt.show()

pp = 4
nn = len(t)

guesses = (1,1,2,1)

(p0, p1,p2,p3), cc = curve_fit(sinF, t, y, p0 = guesses, sigma = yerr)
(up0, up1,up2,up3) = np.sqrt(np.diag(cc))

xmod = np.linspace(t[0], t[-1], 100)

ymod = sinF(xmod, p0, p1, p2,p3)


#Plotting the best quadratic fit
plt.errorbar(t, y, yerr, fmt = 'bo')
plt.plot(xmod, ymod,'r')

yfit = sinF(t, p0, p1, p2,p3) 
yys = (y-yfit)**2/yerr**2

plt.title('Quadratic fit(Time vs Average')
plt.xlabel('Time starting at 0')
plt.ylabel('Montly average')

yfit = sinF(t, p0, p1, p2,p3)  

yys = (y-yfit)**2/yerr**2

chisquared = sum(yys)/(nn-pp)
print(f'Reduced Chisquared = {chisquared:.3f}')




