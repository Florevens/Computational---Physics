# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 03:46:47 2022

@author: flore
"""

from scipy.integrate import trapz, simps, quad
import scipy.special
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint


m = 1 #mass
gl = 1
l = 9.8
g = 9.8
tpts = 1000
tmax = 50
t = np.linspace(0,tmax,tpts)
dt = tmax/tpts

theta = np.zeros(len(t))
omega = np.zeros(len(t))

theta[0] = 1/6
omega[0] = 0


def deriv(theta, omega):
    dTheta = omega
    domega = -1*theta
    
    return dTheta, domega

for i in range(tpts-1):
    
    xmid = theta[i] + (dt/2) * deriv(theta[i],omega[i])[0]
    ymid = omega[i] + (dt/2) * deriv(theta[i],omega[i])[1]
    
    theta[i+1] = theta[i] + dt*deriv(xmid,ymid)[0]
    omega[i+1] = omega[i] + dt*deriv(xmid,ymid)[1]
    
E = (m*l*g*(1-np.cos(theta)))+(.5*m*(l*omega)**2)

plt.plot(t,theta)
plt.title("Theta vs Time")
plt.show()
plt.plot(t, omega)
plt.title("Omega vs Time")
plt.show()
plt.plot(theta, omega)
plt.title("Phase plot")
plt.show()
plt.plot(t,E)
plt.title("Energy vs time")



