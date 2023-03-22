# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 01:29:43 2022

@author: flore
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import sqrt,exp

def f(t,N0,tau,B):
    return N0*exp(-t/tau) + B
    

data = np.loadtxt('decay1.txt', float, skiprows = 1)
data2 = np.loadtxt('decay2.txt', float, skiprows = 1)

x1 = data[:,0]
y1 = data[:,1]

x2 = data2[:,0]
y2 = data2[:,1]

plt.plot(x1,y1, "*", label = "decay1", color = "r")
plt.plot(x2,y2, "--", label = "decay2")
plt.legend(loc='upper right')
plt.show()

yerr1 = []
for i in y1:
    yerr1.append(sqrt(i))
    

yerr2 = []
for i in y2:
    yerr2.append(sqrt(i))

#fitting for decay1
plt.plot(x1,y1)
plt.title("min vs Counts/min")
plt.xlabel("min")
plt.ylabel("Counts/min")
plt.show()

pp = 3
nn = len(x1)
guesses = (1,2,1)
(N0,tau,B), cc = curve_fit(f, x1, y1, p0 = guesses, sigma = yerr1)
(uN0,utau,uB) = np.sqrt(np.diag(cc))

yfit = f(x1,N0,tau, B)
yys = (y1-yfit)**2

xmod1 = np.linspace(x1[0], x1[-1], 100)
ymod1 = f(xmod1,N0,tau,B)

plt.errorbar(x1,y1, yerr1, fmt = 'bo') # plot the data
plt.plot(xmod1,ymod1,'b') # plot the model
plt.xlabel('t (min)')
plt.ylabel('y (Counts/min)')
plt.show()

chisqr = sum(yys)/(nn-pp)
print()
print(f'reduced chi-squared for Three parameter(decay1) = {chisqr:.3f}')

print()
print("The result for tau(decay1):")
print('tau = %.3f +/- %.3f'%(tau,utau))


#fitting for decay2
plt.plot(x2,y2)
plt.title("min vs Counts/min")
plt.xlabel("min")
plt.ylabel("Counts/min")
plt.show()

nn = len(x2)
guesses2 = (2,1,1)

(N0,tau,B), cc = curve_fit(f, x2, y2, p0 = guesses2, sigma = yerr2)
(uN0,utau,uB) = np.sqrt(np.diag(cc))

yfit = f(x2,N0,tau,B)
yys = (y2-yfit)**2

xmod2 = np.linspace(x2[0], x2[-1], 100)
ymod2 = f(xmod2,N0,tau,B)



plt.errorbar(x2,y2, yerr2, fmt = 'bo') # plot the data
plt.plot(xmod2,ymod2,'b') # plot the model
plt.xlabel('t (min)')
plt.ylabel('y (Counts/min)')
plt.title("min vs Counts/min")
plt.show()

chisqr = sum(yys)/(nn-pp)
print()
print(f'reduced chi-squared for Three parameter(decay1) = {chisqr:.3f}')

print()
print("The result for tau(decay2):")
print('tau = %.3f +/- %.3f'%(tau,utau))







    
     