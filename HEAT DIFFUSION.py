# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:15:27 2022

@author: flore
"""

import numpy as np
import matplotlib.pyplot as plt

ll = 0.1                      
dd = 4.25e-6                  
tt_l = 100.0                  
tt_r = 400.0 
tt0 = 100 
          
   

nn = 100
xih = 0.4
tplot=[1,3,10,30,100, 1000]

a = ll/(nn-1)  
h = xih*a**2/dd

x = np.linspace(0,ll,nn)
tt = tt0*np.ones(nn)
tt[0] = tt_l
tt[-1] = tt_r

hda = h*dd/a**2
def step(tt,hda):
    """Performs one time step, updating array tt."""
    tt[1:-1] += hda*(tt[:-2] + tt[2:] - 2*tt[1:-1])

jplot=[]
for t in tplot:
    jplot.append(int(t/h+0.5))

plt.rc('font', size=12)
plt.figure(figsize=(6, 4))
plt.xlabel(r'$x$ (m)')
plt.ylabel(r'$T$ ($^\circ$C)')

for j in range(max(jplot) + 1):  # for each time step
    if j in jplot:  # if we are plotting at this time step..
        plt.plot(x, tt, label='t=%.1f s' % (j * h))  # ..add a curve to the plot
    step(tt, hda)  # do the FTCS step
plt.legend(fontsize=10)
plt.show()

    


