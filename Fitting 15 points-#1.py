# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:14:19 2022

@author: flore
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os


def f2(x, p0, p1, p2):
    return p0 + p1*x + p2*x**2


data = np.loadtxt('data1.txt', float, skiprows = 1)
x = data[:, 0]
y = data[:, 1]
yerr = data[:, 2]
nn = len(x)
plt.errorbar(x, y, yerr, fmt = 'bo')

pp = 3
guesses = (1, 1, 1)
(p0, p1, p2), cc = curve_fit(f2, x, y, p0 = guesses, sigma = yerr)

(up0, up1, up2) = np.sqrt(np.diag(cc))
 
print(f'p0 = {p0:.3f} +/- {up0:.3f}')
print(f'p1 = {p1:.3f} +/- {up1:.3f}')
print(f'p2 = {p2:.3f} +/- {up2:.3f}')

xmod = np.linspace(x[0], x[-1], 100)

ymod = f2(xmod, p0, p1, p2)

yfit = f2(x, p0, p1, p2)  

yys = (y-yfit)**2/yerr**2

chisquared = sum(yys)/(nn-pp)
print(f'Reduced Chisquared = {chisquared:.3f}')

plt.plot(xmod, ymod, 'r')





