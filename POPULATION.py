# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:16:28 2022

@author: flore
"""

from scipy.integrate import trapz, simps, quad
import scipy.special
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

gamma = 0.5
beta = 0.5

alpha = 1
delta = 2


R = 2
F = 2

t = np.linspace(0,15,100)

dt = 15/len(t)






def Rabbits(vect,t):
    (R,F) = vect
    
    drdt = alpha*R - beta*R*F
    dfdt = gamma*R*F - delta*F
    
    return drdt,dfdt
    

vect1 = (R,F)
Rab = odeint(Rabbits,vect1,t)




plt.plot(t,Rab[:, 0],"-r", label = "DR/DT")
plt.plot(t, Rab[:, 1], "-b", label = "DF/DT")
plt.legend(loc = "upper right")

#If I increase alpha, I expect both populations to rise
#There are more rabbits, and there are more food for the foxes.

#If I increase Gamma, I expect the wolf population to grow, and the 
#rabbits to decrease as there are more predators now.

#If I increase beta, the rabbit population decreases

#If I even out delta, the populations also evens out





    





