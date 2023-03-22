# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 18:20:37 2022

@author: flore
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import sqrt,exp

def f(x,p1,p2,p3,p4):
 # Model function: Gaussian plus linear background
 return exp(-(x-p1)**2/(2*p2**2)) + p3 + p4*x


#Reading in the text file
data = np.loadtxt('peak4.txt', float, skiprows = 1)

x = data[:,0]
y = data[:,1]
yerr = np.ones(len(x))*.1
nn = len(x)
#Number of parameters in the fit function
pp = 4

guesses = (1,1,1,1)
#Most sensitive to the first two guesses

(p1,p2,p3,p4),cc = curve_fit(f,x,y,p0=guesses)

#1-sigma uncertainties in fit parameters
(up1,up2,up3,up4) = sqrt(np.diag(cc)) 

yfit = f(x,p1,p2,p3,p4)
yys = (y-yfit)**2
chisqr = sum(yys)/(nn-pp) 

    
    
xmod = np.linspace(x[0], x[-1], 100)
ymod = f(xmod,p1, p2, p3,p4) 


plt.plot(x,y,'bo') # plot the data
plt.plot(xmod,ymod,'r') # plot the model
plt.title("linear graph")
plt.xlabel('x (cm)')
plt.ylabel('y (mV)')
plt.show()
 

chisquared = sum(yys)/(nn-pp)

print()
print('LINEAR INFO')
print(f'reduced chi-squared = {chisqr:.3f}')
print('parameters and 1-sigma parameter uncertainties:')
print('p1 = %.3f +/- %.3f'%(p1,up1))
print('p2 = %.3f +/- %.3f'%(p2,up2))
print('p3 = %.3f +/- %.3f'%(p3,up3))
print('p4 = %.3f +/- %.3f'%(p4,up4))



def f2(x,p0,p1,p2,p3,p4):
 # Model function: Gaussian plus linear background
 return p0*exp(-(x-p1)**2/(2*p2**2)) + p3 + p4*x


#Reading in the text file
data = np.loadtxt('peak4.txt', float, skiprows = 1)

x = data[:,0]
y = data[:,1]
yerr = np.ones(len(x))*.1
nn = len(x)

#Number of parameters in the fit function
pp = 5

guesses = (1,1,1,1,1)


(p0,p1,p2,p3,p4),cc = curve_fit(f2,x,y,p0=guesses)

#1-sigma uncertainties in fit parameters
(up0,up1,up2,up3,up4) = sqrt(np.diag(cc)) 

yfit = f2(x,p0,p1,p2,p3,p4)
yys = (y-yfit)**2
chisqr = sum(yys)/(nn-pp) 

    
    
xmod = np.linspace(x[0], x[-1], 100)
ymod = f2(xmod,p0,p1, p2, p3,p4) 


plt.plot(x,y,'bo') # plot the data
plt.plot(xmod,ymod,'r') # plot the model
plt.title("Quadratic graph")
plt.xlabel('x (cm)')
plt.ylabel('y (mV)')
plt.show()
 

chisquared = sum(yys)/(nn-pp)

print()
print('QUADRATIC INFO')
print(f'reduced chi-squared = {chisqr:.3f}')
print('parameters and 1-sigma parameter uncertainties:')
print('p0 = %.3f +/- %.3f'%(p0,up0))
print('p1 = %.3f +/- %.3f'%(p1,up1))
print('p2 = %.3f +/- %.3f'%(p2,up2))
print('p3 = %.3f +/- %.3f'%(p3,up3))
print('p4 = %.3f +/- %.3f'%(p4,up4))

#Based on the chisquared, the additional parameter might not be needed



#CONSTANT FIT

def f3(x,p0,p1,p2):
 # Model function: Gaussian plus linear background
 return exp(-(x-p0)**2/(2*p1**2)) + p2


#Reading in the text file
data = np.loadtxt('peak4.txt', float, skiprows = 1)

x = data[:,0]
y = data[:,1]
yerr = np.ones(len(x))*.1
nn = len(x)
#Number of parameters in the fit function
pp = 3

guesses = (1,2,1)
#Most sensitive to the second guess

(p0,p1,p2),cc = curve_fit(f3,x,y,p0=guesses)

#1-sigma uncertainties in fit parameters
(up0,up1,up2) = sqrt(np.diag(cc)) 

yfit = f3(x,p0,p1,p2)
yys = (y-yfit)**2
chisqr = sum(yys)/(nn-pp) 

    
    
xmod = np.linspace(x[0], x[-1], 100)
ymod = f3(xmod,p0, p1, p2) 


plt.plot(x,y,'bo') # plot the data
plt.plot(xmod,ymod,'r') # plot the model
plt.title("Constant graph")
plt.xlabel('x (cm)')
plt.ylabel('y (mV)')
plt.show()
 

chisquared = sum(yys)/(nn-pp)

print('Constant info')
print(f'reduced chi-squared = {chisqr:.3f}')
print('parameters and 1-sigma parameter uncertainties:')
print('p0 = %.3f +/- %.3f'%(p0,up0))
print('p1 = %.3f +/- %.3f'%(p1,up1))
print('p2 = %.3f +/- %.3f'%(p2,up2))

#The reduced chisquared for this one is better than the quadratic but worst for the linear







