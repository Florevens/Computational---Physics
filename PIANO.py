# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:58:20 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, sqrt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

time = 0.1
L = 1   # Length of wire in metres
v = 100 # velocity in m/s
d = 0.1 # distance of hammer
C = 1   # 1 m/s
sigma = 0.03  # sigma in metres
N = 200 # grid spacings
a = L/N

alpha = float(input('Enter a value of alpha: '))
h = sqrt(alpha)*a/v
Nt = int(time/h)
scale = 40
Nplot = int(Nt/scale)

def stringvelprofile(x):
 """Returns initial df/dt."""
 return (x*(L - x)/L**2)

x = np.linspace(0,L,N)
f = np.zeros([N,Nt])
g0 = stringvelprofile(x)

f[:,1] = g0*h

for t in range(1, Nt - 1):
# keep two ends of string fixed, so loop over points that exclude the ends
 for i in range(1, N - 1):
     f[i,t+1] = 2*(1 - alpha)*f[i,t] + alpha*(f[i+1,t]+f[i-1,t])-f[i,t-1]

for t in range(Nplot):
 plt.plot(x,f[:,t*scale])
plt.xlabel('x')






