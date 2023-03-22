# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:21:53 2022

@author: flore
"""
import math
import numpy as np
import matplotlib.pyplot as plt

h = float(input("Enter the starting height: "))
Vo = float(input("Enter the initial speed: "))
theta = float(input("Enter the initial angle: "))

t = np.linspace(0,1,50)
print(t)
projectile_motion = np.ones([100,2],float)

print(projectile_motion)

i=0
y = 1
x = 0
while ( y > 0):
    projectile_motion[i,1] = h + Vo*(math.sin(theta)*t[i]) -  (9.8*t[i]**2)/2
    projectile_motion[i,0] = Vo*math.cos(theta)*t[i]
    y = projectile_motion[i,1]
    x = projectile_motion[i,0]
    
    i+=1
    
    
horiz = []
vert = []
print(projectile_motion)

np.savetxt("Projectile.txt",projectile_motion)

""" r=0
row = len(projectile_motion)
print(row)
while(r < row):
    horiz.append(projectile_motion[r,0])
    vert.append(projectile_motion[r,1])
    r+=1

print(horiz)
print(vert)
plt.plot(horiz,vert) """










        


    
    

