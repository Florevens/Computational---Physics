# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 02:11:10 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import sqrt,exp
from scipy.fftpack import dct, idct
from numpy.random import randn

v1 = 20000#hz
v2 = 25000#hz
N = 1000
tau = 2*10**-6
sd = 0.7
time = np.zeros(N)


for i in range(999):
    time[i+1]+=time[i]+tau
    
    


def Ft(t):
    return np.sin(2*np.pi*v1*t) + np.cos(2*np.pi*v2*t)


fst = Ft(time);

#dtrans = dct(fvt)

fst2 = fst+ sd *randn(N)

plt.plot(time, fst)
plt.title("Time vs Fst")
plt.show()
plt.plot(time,fst2)
plt.title("Time vs FST with SD")
plt.show()

wn = dct(fst2)
plt.plot(time, wn)
plt.title("White noise")
plt.show()

vmax = 30000
new = np.zeros(N)

vk = 1/(2*N*tau)
freq = np.linspace(0, N*vk,N)
print(freq)

for i in range(N):
    if freq[i] > vmax:
        new[i] = 0
    elif freq[i] <= vmax:
        new[i] = wn[i]
  
plt.plot(time,abs(new))
plt.title("Time vs New Trans")
plt.show()

indct = idct(new)
plt.plot(time, indct)
plt.title("Time vs Inverse")





