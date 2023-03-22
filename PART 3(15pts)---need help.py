# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:43:56 2022

@author: flore
"""

from scipy.integrate import quad
import numpy as np
import math
import matplotlib.pyplot as plt



L = 150*(10**-6) #(henry)
C = 12*(10**-9) #(Farad)
R = 33 #(Coulomb)
V = 30 #(Volts)

f = np.linspace(10,250*1000,250) #(Kilo-Hertz)


def I(f):
    w = f*2*math.pi
    
    zL = w*L*1j
    zC = 1/(w*C*1j)
    Zt = R + zL + zC
    
    return V/Zt

plt.plot(f, I(f).real)
plt.plot(f, I(f).imag)











    


