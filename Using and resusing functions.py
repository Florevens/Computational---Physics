# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:10:20 2022

@author: flore
"""
import numpy as np
import matplotlib.pyplot as plt
from random import choice
import math

xVals = np.linspace(-10, 10,500)
yVals = 0
yValsl1 = []
yValsl2 = []
yValsl3 = []
def f(x):
    func1 = x + 2*math.cos(x**2)
    yVals = func1
    
    
    return yVals

 
for i in xVals:
    ans = f(i)
    yValsl1.append(ans)
    
for j in xVals:
    ans2 = f(j)+10
    yValsl2.append(ans2)

for k in xVals:
    k = k+5
    ans3 = f(k)
    yValsl3.append(ans3)
    
    
print(yValsl1)
print(yValsl2) 
print(yValsl3)

plt.plot(xVals, yValsl1, label = "f(x)")
plt.plot(xVals, yValsl2, label = "f(x)+10")
plt.plot(xVals, yValsl3, label = "f(x+5)")
plt.legend()

plt.xlabel("X values")
plt.ylabel("f(x) values")
plt.title("X vs (f(x), f(X+5), f(x) + 10")