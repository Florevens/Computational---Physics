# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 02:13:17 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import sqrt,exp

def f(t,N0,tau):
    return N0*exp(-t/tau) + 25
    

data = np.loadtxt('decay1.txt', float, skiprows = 1)
data2 = np.loadtxt('decay2.txt', float, skiprows = 1)

x1 = data[:,0]
y1 = data[:,1]

x2 = data2[:,0]
y2 = data2[:,1]


yerr1 = []
for i in y1:
    yerr1.append(sqrt(i))
    

yerr2 = []
for i in y2:
    yerr2.append(sqrt(i))

#fitting for decay1

pp = 2
nn = len(x1)
guesses = (1,1)
(N0,tau), cc = curve_fit(f, x1, y1, p0 = guesses, sigma = yerr1)
(uN0,utau) = np.sqrt(np.diag(cc))

yfit = f(x1,N0,tau)
yys = (y1-yfit)**2

xmod1 = np.linspace(x1[0], x1[-1], 100)
ymod1 = f(xmod1,N0,tau)

plt.errorbar(x1,y1, yerr1, fmt = 'bo') # plot the data
plt.plot(xmod1,ymod1,'b') # plot the model
plt.xlabel('t (min)')
plt.ylabel('y (Counts/min)')
plt.show()

chisqr = sum(yys)/(nn-pp)
print()
print(f'reduced chi-squared for Two parameter(decay1) = {chisqr:.3f}')

print()
print("The result for tau(decay1):")
print('tau = %.3f +/- %.3f'%(tau,utau))


#fitting for decay2


nn = len(x2)
guesses2 = (1,2)

(N0,tau), cc = curve_fit(f, x2, y2, p0 = guesses2, sigma = yerr2)
(uN0,utau) = np.sqrt(np.diag(cc))

yfit = f(x2,N0,tau)
yys = (y2-yfit)**2


xmod2 = np.linspace(x2[0], x2[-1], 100)
ymod2 = f(xmod2,N0,tau)



plt.errorbar(x2,y2, yerr2, fmt = 'bo') # plot the data
plt.plot(xmod2,ymod2,'b') # plot the model
plt.xlabel('t (min)')
plt.ylabel('y (Counts/min)')
plt.title("min vs Counts/min")
plt.show()

chisqr = sum(yys)/(nn-pp)
print()
print(f'reduced chi-squared for Two parameter(decay2) = {chisqr:.3f}')

print()
print("The result for tau(decay2):")
print('tau = %.3f +/- %.3f'%(tau,utau))








    
     