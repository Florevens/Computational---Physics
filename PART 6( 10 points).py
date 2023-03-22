# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:02:04 2022

@author: flore
"""

from scipy.integrate import trapz, simps, quad
import numpy as np
import math
import matplotlib.pyplot as plt


x = np.linspace(0,3,7)


def errf(t):
    return np.exp(-t**2)

y = errf(x)

trap = trapz(y, x) #Trap

simp = simps(y, x) #Simp

print("trap:  ",trap)
print()
print("simp:  ",simp)
print()
print("QUAD: ", quad(errf, 0, 3))



    
    

