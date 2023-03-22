# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 02:34:07 2022

@author: flore
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp
import os
from scipy import special


n = 0

xmax =2*math.sqrt(n+1)

x=np.linspace(-xmax,xmax,100)

p=np.exp(-(x)**2)*(sp.eval_hermite(n,x))**2

plt.subplot(2,2,1)
plt.plot(x, p)
plt.title('n = 0')


n = 1

xmax =2*math.sqrt(n+1)

x=np.linspace(-xmax,xmax,100)

#p = math.exp(-x**2)*(special.hermite(n,x)**2)

p=np.exp(-(x)**2)*(sp.eval_hermite(n,x))**2

plt.subplot(2,2,2)
plt.plot(x, p)
plt.title('n = 1')

n = 2

xmax =2*math.sqrt(n+1)

x=np.linspace(-xmax,xmax,100)

#p = math.exp(-x**2)*(special.hermite(n,x)**2)

p=np.exp(-(x)**2)*(sp.eval_hermite(n,x))**2

plt.subplot(2,2,3)
plt.plot(x, p)
plt.title('n = 2')

n = 50

xmax =2*math.sqrt(n+1)

x=np.linspace(-xmax,xmax,1000)

#p = math.exp(-x**2)*(special.hermite(n,x)**2)

p=np.exp(-(x)**2)*(sp.eval_hermite(n,x))**2

plt.subplot(2,2,4)
plt.plot(x, p)
plt.title('n = 50')

plt.show()







