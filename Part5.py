# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:04:46 2022

@author: flore
"""

import numpy as np
import matplotlib.pyplot as plt

Vbtmright = 0
Vtopleft = 100
target = 1e-4
L = 1
M = 50
a = L/M

phi = np.zeros([M+1,M+1], float) # initial guess is all V = 0 except at
phinew = np.empty([M+1,M+1], float)

phi[0,:] = Vtopleft
phi[-1,:] = Vbtmright
phi[:,0] = Vtopleft
phi[:,-1] = Vbtmright

ra = np.zeros([M+1,M+1], float)
ra[15:30, 15:30] = 10**4

deltaphi = Vtopleft


while deltaphi > target:
    for i in range(M+1):
        for j in range(M+1):
            if i ==0 or i == M or j == 0 or j == M:
                phinew[i,j] = phi[i,j]
            else:
                phinew[i,j] = 0.25*(phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])+(ra[i,j]*a/4)
                
    phidiff = phi - phinew
    deltaphi = np.max(np.abs(phidiff))
    phi = np.array(phinew)   

#plt.imshow(phi, origin='lower', extent=(0,1,0,1))
#plt.colorbar()
#plt.show()
plt.contour(phi)
plt.title("Equipotential")

 




