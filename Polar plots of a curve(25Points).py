# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:46:44 2022

@author: flore
"""
import numpy as np
import matplotlib.pyplot as plt
from random import choice
import math

Theta = np.linspace(int(input("Please enter Your min: ")),int(input("Please enter your max: ")), int(input("please enter your steps: ")))
setTheta = []
setValX = []
setValY = []
setR = []
'''for i in Theta:
    if(0 <= i < 2*math.pi):
        
        x = 2*math.cos(i) + math.cos(2*i)
        y = 2*math.sin(i) - math.sin(2*i)
        setTheta.append(i)
        setValX.append(x)
        setValY.append(y)
    while(0 > i or i > 2*math.pi):
            print(setValX)
            print(setValY)
            print(list(Theta))
            break;
    
    plt.plot(setValX,setValY)
    plt.xlabel("X values")
    plt.ylabel("Y(X) values")
    plt.title("X vs Y values")'''
    

'''##Galilean spiral
for i in Theta:
    if(0 <= i < 10*math.pi):
        R = i**2
        setR.append(R)
        x = R*math.cos(i)
        y = R*math.sin(i)
        setValX.append(x)
        setValY.append(y)
    if(0 > i or i > 10*math.pi):
            print(setValX)
            print(setValY)
            print(list(Theta))
            print(setR)
            break;
            
    plt.plot(setValX,setValY)
    plt.xlabel("X values")
    plt.ylabel("Y(X) values")
    plt.title("X vs Y values")'''
    
#Feys Function
for i in Theta:
    if(0 <= i < 24*math.pi):
        R = math.exp(math.cos(i))-(2*math.cos(4*i))+math.sin(i)**5*(i/12)
        setR.append(R)
        x = R*math.cos(i)
        y = R*math.sin(i)
        setValX.append(x)
        setValY.append(y)
    if(0 > i or i > 24*math.pi):
        print(setValX)
        print(setValY)
        print(list(Theta))
        print(setR)
        break;
    
    plt.plot(setValX,setValY)
    plt.xlabel("X values")
    plt.ylabel("Y(X) values")
    plt.title("Feys")   
    
    
    
    
    
            

        
    
    

