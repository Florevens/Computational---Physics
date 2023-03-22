# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:07:56 2022

@author: flore
"""
import numpy as np
from scipy.integrate import trapz, simps, quad
import matplotlib.pyplot as plt

def Heat(x):
    return x**4*((np.exp(x))/(np.exp(x)-1)**2)





def CV(T):
    intg = quad(Heat, 0 , 428/T)
    return (9*0.001*(6.022*10**28)*(1.381*10**-28)*(T/428)**3)*intg[0]


T = np.linspace(5,500,495)


cT = 495
cvList = []


for i in range(cT):
    cvList.append(CV(T[i]))
    

plt.plot(T, cvList, 'ro')
plt.xlabel('Temperature (K)')
plt.ylabel('Cv (J/K)')
plt.title('Aluminiums Heat Capacity with Temperature')
plt.show()
    