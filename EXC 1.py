# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 00:37:00 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import sqrt,exp
from scipy.fftpack import dct

v1 = 20000#hz
v2 = 25000#hz
N = 1000
tau = 2*10**-6
time = np.zeros(N)

for i in range(N-1):
    time[i+1]+=time[i]+tau
    
    


def Ft(t):
    return np.sin(2*np.pi*v1*t) + np.cos(2*np.pi*v2*t)




vk = 1/(2*N*tau)
#freq = np.zeros(N)
freq = np.linspace(0, N*vk,N)
print(freq)
#for i in range(999):
 
    #freq[i] = i/(2*N*tau)

    

fst = Ft(time);
dtrans = dct(fst)


plt.plot(time, fst)
plt.show()
plt.plot(dtrans)
plt.show()


plt.plot(freq, abs(dtrans))





