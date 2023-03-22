# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 12:01:45 2022

@author: flore
"""

from scipy.integrate import trapz, simps, quad
import scipy.special
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint



r = 0
xo = 1e-5

t = np.linspace(0,50,1000)

def Nt(x,t):
    global r 
    
    dndt = r*x*(1-x)
    
    return dndt
def Nt2(x,t):
    return r*x


plt.figure(0)
plt.ylim(0,1.2)

for i in range(3):
    r+=0.5
   
    
    pop = odeint(Nt,xo,t)
    plt.plot(t,pop, label = str(r))

    pop2 = odeint(Nt2,xo,t)
    plt.plot(t,pop2, label = str(r))
    
    for j in range(len(pop)):
        if abs(pop[j]-pop2[j]) >= 0.05:
            print(r,t[j])
            break
   
    
plt.legend()




    
    






