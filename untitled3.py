# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:48:25 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, sqrt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

A = 10
B = 12
tau = 365
D = 0.1

def T0(t):
	return A + B*np.sin(2*np.pi*(t/tau-(1/4)))

L = 20    
D = 0.1   
N = 100       
a = L/N       
h = 0.01     


T = np.zeros(N+1,float)
T[1:N]=10


def iterate(T,t_min,t_max):
	# Main loop
	t = t_min
	c = h*D/a**2

	while t<t_max:
	
	    # Calculate the new values of T
		T[0] = T0(t)
		T[N] = 11
		T[1:N] = T[1:N] + c*(T[2:N+1]+T[0:N-1]-2*T[1:N])
	    
		
		t += h
	return T


T9 = iterate(T,0,365*9)

T9_i = T9
t_min = 365*9
for t_max in [365*9 + i*(365//4) for i in range(4)]:
	T9_i = iterate(T9_i,t_min,t_max)
	plt.plot(T9_i,label=t_max%365/(365//4))
	t_min = t_max

plt.legend()
plt.xlabel("x")
plt.ylabel("T")
plt.show()