# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:38:42 2022

@author: flore
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz, simps, quad

x0 = 250e-5
c0 = 100 #ppm
dd = 1.6e-9
ll = 0.001
nn = 200

a = ll/(nn-1) 

x = np.linspace(-ll/2,ll/2,nn)
x[0] = x0
c = np.zeros(nn)

        
for i in range(nn//2-30, nn//2+30):
    c[i] = c0
    
        
xih = 0.4
a = ll/(nn-1) 
h = xih*a**2/dd
hda = h*dd/a**2
tplot=[0,1,3,10,30,100,1000]

def step(tt,hda):
    """Performs one time step, updating array tt."""
    tt[1:-1] += hda*(tt[:-2] + tt[2:] - 2*tt[1:-1])
    
jplot=[]
for t in tplot:
    jplot.append(int(t/h+0.5))
    
plt.rc('font',size=12)
plt.figure(figsize=(6,4))
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$T$ ($^\circ$C)')

for j in range(max(jplot)+1):  # for each time step
    if j in jplot:
        integral = trapz(c,x)
        print(integral)
        # if we are plotting at this time step..
        plt.plot(x,c,label='t=%.1f s'%(j*h)) # ..add a curve to the plot
    step(c,hda)               # do the FTCS step
plt.legend(fontsize=10)
plt.show()
    

    
    

        