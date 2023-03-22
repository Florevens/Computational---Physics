# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:46:06 2022

@author: flore
"""

from scipy.integrate import trapz, simps, quad
import scipy.special
import numpy as np
import math
import matplotlib.pyplot as plt




def E(t):
    return (1-0.9999*math.sin(t)**2)**1/2
 
print("quad:  ", quad(E, 0, math.pi/2))

a = 0.0
b = math.pi/2
N = 100


h = (b-a)/N



t = np.linspace(a, b, N)

Em = (1-0.9999*np.sin(t)**2)**1/2


def E2(m):
    return (1-m*np.sin(t)**2)**1/2

f = 0.0

for i in range(len(t)-1):
    f+= 0.5*((t[i+1]-t[i])*(Em[i+1]+Em[i]))
    
print("TRAP:  ", f)




print("Exact: ", scipy.special.ellipe(0.9999))



k = 1
sum = 0
while k < N:
    x = a + k*h
    if(k%2 == 0):
        sum = sum + 2*E(x)
    else:
        sum = sum + 4*E(x)
    k+=1

Int = (h/3)*(E(a)+E(b)+sum)

print("Simpson: ", Int)
    



    