# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:29:08 2022

@author: flore
"""

from scipy.integrate import quad
import numpy as np
import math
import matplotlib.pyplot as plt

x = 5.0
y = 0.2

z = x + y*1j
t = np.linspace(0, 10, 1000)

def f(t):
    return np.exp(z*t*1j)

plt.plot(t, f(t).real)
plt.plot(t, f(t).imag)
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
plt.plot(f(t).real, f(t).imag)



