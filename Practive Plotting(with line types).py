# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:14:48 2022

@author: flore
"""
import math
import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams.update({'font.size': 22})

x = int(input("Enter your chosen range: "))
#arr = np.linspace(0,x,200)
arr = np.linspace(0,x,20)
f1 = arr**2 + 8
f2 = arr**3 + 8
print(arr, '\n')

print(f1, '\n')
print(f2, '\n')

#plots using color and linetypes(5pts)
plt.xlim(0,16)
plt.ylim(0,72)

font1 = {'Time', 'size = 20',}
font2 = {'serif', 'size = 20'}


fig1, func1 = plt.subplots()
func1.plot(arr, f1, color = "blue", linestyle = "dotted", label = "$x^2$") 
func1.set_xlabel("Range", fontsize = 20.0)
func1.set_ylabel("function 1")
func1.set_title("\ast Range x Function")
func1.legend(loc = "upper left")
func1.plot(1,0, marker = "")

fig2, func2 = plt.subplots()
func2.plot(arr, f2, "r-", linestyle = "dashed", label = "$x^3$")
func2.set_xlabel("Range")
func2.set_ylabel("function 2")
func2.set_title("Range x Function")
func2.legend(loc = "upper left")

fig3, combFunc = plt.subplots()
combFunc.plot(arr, f1, color = "b", linestyle = "dotted", label = "$x^2$")
combFunc.plot(arr, f2, "r-", linestyle = "dashed", label = "$x^3$")
combFunc.set_xlabel("Range")
combFunc.set_ylabel("function 2 and 1")
combFunc.set_title("Range x Functions")
combFunc.legend(loc = "upper left")







#Plot using lines in shapes connected(5pts)
#combFunc.plot(arr, f2,"b-s", linewidth = 1) 
c#ombFunc.plot(arr, f1, "r-o", linewidth = 1)




