# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:02:30 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os

#Linear fit
def first(x,p0,p1):
    return p0 + p1*x

data = np.loadtxt('data2.txt', float, skiprows = 1)
x = data[:, 0]
y = data[:, 1]
yerr = data[:, 2]
nn = len(x)

plt.errorbar(x, y, yerr, fmt='bo')

pp = 2 
guesses = (1, 1)


(p0, p1), cc = curve_fit(first, x, y, p0 = guesses, sigma = yerr)

(up0, up1) = np.sqrt(np.diag(cc)) 

print(f'p0 = {p0:.3f} +/- {up0:.3f}')
print(f'p1 = {p1:.3f} +/- {up1:.3f}')
print()

xmod = np.linspace(0, 10, 100)  
ymod = first(xmod, p0, p1)        


plt.plot(xmod, ymod, 'g')
plt.title('Linear Function fit')
plt.show()

yfit = first(x, p0, p1)   

yys = (y - yfit)**2/yerr**2

#PLOTTING RESIDUALS FIRST ORDER
yres = y - yfit
plt.errorbar(x, yres, yerr, fmt = 'b^')
plt.title("Residuals first order")
plt.axhline(y=0.0, color='g', linestyle='--')
plt.show()

chisquared = sum(yys)/(nn-pp)
print(f'Reduced Chisquared Linear = {chisquared:3.3f}')
print()




#Quadratic fit
def second(x,p0,p1,p2):
    return p0+p1*x + p2*x**2

pp = 3 

guesses = (1, 1, 1)

(p0, p1, p2), cc = curve_fit(second, x, y, p0 = guesses, sigma = yerr)

(up0, up1, up2) = np.sqrt(np.diag(cc)) 
print(f'p0 = {p0:.3f} +/- {up0:.3f}')
print(f'p1 = {p1:.3f} +/- {up1:.3f}')
print(f'p2 = {p2:.3f} +/- {up2:.3f}')
print()

xmod = np.linspace(x[0], x[-1], 100) 
ymod = second(xmod, p0, p1, p2)

yfit = second(x, p0, p1, p2)   

yys = (y-yfit)**2/yerr**2


chisquared = sum(yys)/(nn-pp)
print(f'Reduced Chisquared Quadratic = {chisquared:.3f}')
print()

plt.errorbar(x, y, yerr, fmt = 'bo')
plt.plot(xmod, ymod, 'r')
plt.title('Quadratic Function fit')
plt.show()

#PLOTTING RESIDUALS SECOND ORDER
yres = y - yfit
plt.errorbar(x, yres, yerr, fmt = 'b^')
plt.title("Residuals second order")
plt.axhline(y=0.0, color='g', linestyle='--')
plt.show()



#3rd order polynomial
def third(x, p0, p1, p2, p3):
    return p0 + p1*x + p2*x**2 + p3*x**3

pp = 4  
guesses = (1, 1, 1, 1)

(p0, p1, p2, p3), cc = curve_fit(third, x, y, p0 = guesses, sigma = yerr)
(up0, up1, up2, up3) = np.sqrt(np.diag(cc)) 
print(f'p0 = {p0:.3f} +/- {up0:.3f}')
print(f'p1 = {p1:.3f} +/- {up1:.3f}')
print(f'p2 = {p2:.3f} +/- {up2:.3f}')
print(f'p3 = {p3:.6f} +/- {up3:.6f}')
print()

xmod = np.linspace(x[0], x[-1], 100)
ymod = third(xmod, p0, p1, p2, p3)

yfit = third(x, p0, p1, p2, p3)  
yys = (y-yfit)**2/yerr**2



chisquared = sum(yys)/(nn-pp)

print(f'Reduced Chisquared 3rd order = {chisquared:.3f}')
print()

plt.errorbar(x, y, yerr, fmt = 'bo')
plt.plot(xmod, ymod, 'r')
plt.title('3rd order function fit')
plt.show()

#PLOTTING RESIDUALS THIRD ORDER
yres = y - yfit
plt.errorbar(x, yres, yerr, fmt = 'b^')
plt.title("Residuals third order")
plt.axhline(y=0.0, color='g', linestyle='--')
plt.show()


print("The order that fits the data the best is the Linear function as it is the one with the closes Chisquared to One")

