# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:01:39 2022

@author: flore
"""
import math

def toPolar(X,Y):
    R = math.sqrt(X**2+Y**2)
    Theta = math.atan(Y/X)
    Tlist = [R, Theta]
    
    return Tlist

   
X = int(input("Please enter Your X value: "))
Y = int(input("Please enter your Y value: "))
while(X != 0):
    transPol = toPolar(X,Y)
    print("Your radius is: " + "{:.3f}".format(transPol[0]) + " Your angle is: " + "{:.3f}".format(transPol[1])+u"\N{DEGREE SIGN}")
    X = int(input("Please enter Your X value: "))
    Y = int(input("Please enter your Y value: "))
while(X == 0):
    raise Exception("Not divisible by zero")
    break
    
    