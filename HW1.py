# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:01:12 2022

@author: flore
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import random;
from random import choice
import pandas as pd


def Walk():
    x = -40
    x2 = 40
    stepsInt = 0
    stepsA = [];
    i = x
    stepsPoint = []
    while(x <= i < x2):
        if i == -40:
            i+=1
            stepsInt+=1
            stepsPoint.append(i)
            stepsA.append(stepsInt)
        elif i < x2:
            i+= choice([i for i in range(-1,2) if i not in [0]])
            stepsInt+=1
            stepsPoint.append(i)
            stepsA.append(stepsInt)
    
        elif i == 40:
                break;
                
        plt.plot(stepsPoint,stepsA)
        plt.xlabel("Position")
        plt.ylabel("Step Number")
        plt.title("Position Vs. Steps")
        info = "StepsArray: ", stepsA, "Steps: ", stepsInt, "count: ", i, "Point: ", stepsPoint
    
    return print(info)

##Walk()

def WalkTwoD():
    X = -40
    Y = 0
    Z = 40
    step2d = 0
    I = -40
    Ylist = []
    Xlist = []
    stepsA = []
   
    
    while(I <= X <= Z and I <= Y <= Z):
        while(X == -40 and Y == 0):
            leftEdge = random.choice([X, Y])
            if leftEdge == Y:
                Y+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
                Xlist.append(X)
                stepsA.append(step2d)
                while  X == -40 and I < Y < Z:
                    leftEdge2 = random.choice([X, Y])
                    if leftEdge2 == Y:
                        Y+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Ylist.append(Y)
                        Xlist.append(X)
                        stepsA.append(step2d)
                    elif leftEdge2 == X:
                        X+=1
                        step2d+=1
                        Xlist.append(X)
                        Ylist.append(Y)
                        stepsA.append(step2d)
            elif leftEdge == X:
                X+=1
                step2d+=1
                Xlist.append(X)
                Ylist.append(Y)
                stepsA.append(step2d)
                
        while(I < X < Z and I < Y < Z ):
            allSteps = random.choice([X,X,Y])
            if allSteps == X:
                X+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Xlist.append(X)
                Ylist.append(Y)
                stepsA.append(step2d)
            elif allSteps == Y:
                Y+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
                Xlist.append(X)
                stepsA.append(step2d)
                
        while(Y == -40 and I < X < Z):
            bottomEdge = random.choice([X, Y])
            if bottomEdge == Y: 
                X+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
                Xlist.append(X)
                stepsA.append(step2d)
                while Y == -40 and I < X < Z:
                    bottomEdge2 = random.choice([X, Y])
                    if bottomEdge2 == X:
                        X+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Xlist.append(Y)
                        Xlist.append(X)
                        stepsA.append(step2d)
                    elif bottomEdge2 == Y:
                        Y+=1
                        step2d+=1
                        Ylist.append(X)
                        Ylist.append(Y)
                        stepsA.append(step2d)
            elif bottomEdge == Y:
                        Y+=1
                        step2d+=1
                        Ylist.append(Y)
                        Xlist.append(X)
                        stepsA.append(step2d)
                
        while (Y == 40 and I < X < Z):
            topEdge = random.choice([X, Y])
            if topEdge == X: 
                X+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Xlist.append(X)
                Ylist.append(Y)
                stepsA.append(step2d)
                while Y == 40 and I < X < Z:
                    topEdge2 = random.choice([X, Y])
                    if topEdge2 == X:
                        X+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Xlist.append(X)
                        Ylist.append(Y)
                        stepsA.append(step2d)
                    elif topEdge2 == Y:
                        Y-=1
                        step2d+=1
                        Ylist.append(Y)
                        Xlist.append(X)
                        stepsA.append(step2d)
                    
            elif topEdge == Y:
                Y-=1
                step2d+=1
                Ylist.append(Y)
                Xlist.append(X)
                stepsA.append(step2d)
            
        
        while(X == 40 and I < Y < Z and Y != 0):
            edgeControl1 = random.choice([X, Y])
            if edgeControl1 == Y:
                Y+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
                Xlist.append(X)
                stepsA.append(step2d)
                while X == 40 and I < Y < Z:
                    subEdge1 = random.choice([X, Y])
                    if subEdge1 == Y:
                        Y+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Ylist.append(Y)
                        Xlist.append(X)
                        stepsA.append(step2d)
                    elif subEdge1 == X:
                        X-=1
                        step2d+=1
                        Xlist.append(X)
                        Ylist.append(Y)
                        stepsA.append(step2d)
            elif edgeControl1 == X:
                X-=1
                step2d+=1
                Xlist.append(X)
                Ylist.append(Y)
                stepsA.append(step2d)
                
        while(X == -40 and I < Y < Z):
            edgeControl3 = random.choice([X, Y])
            if edgeControl3 == Y:
                Y+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
                Xlist.append(X)
                stepsA.append(step2d)
                while X == -40 and I < Y < Z:
                    subEdge3 = random.choice([X, Y])
                    if subEdge3 == Y:
                        Y+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Ylist.append(Y)
                        Xlist.append(X)
                        stepsA.append(step2d)
                    elif subEdge3 == X:
                        X+=1
                        step2d+=1
                        Xlist.append(X)
                        Ylist.append(Y)
                        stepsA.append(step2d)
            elif edgeControl3 == X:
                X+=1
                step2d+=1
                Xlist.append(X)
                Ylist.append(Y)
                stepsA.append(step2d)
                
        while(X== -40 and Y == -40):
            vert1 = random.choice([X, Y])
            if vert1 == X:
                X+=1
                Xlist.append(X)
                Ylist.append(Y)
                step2d+=1
                stepsA.append(step2d)
            elif vert1 == Y:
                Y+=1
                Ylist.append(Y)
                Xlist.append(X)
                step2d+=1
                stepsA.append(step2d)
        
        while(X == 40 and Y == 40):
            vert2 = random.choice([X, Y])
            if vert2 == X:
                X-=1
                Xlist.append(X)
                Ylist.append(Y)
                step2d+=1
                stepsA.append(step2d)
            elif vert2 == Y:
                Y-=1
                Ylist.append(Y)
                Xlist.append(X)
                step2d+=1
                stepsA.append(step2d)
            
        while(X == -40 and Y == 40):
            vert3 = random.choice([X, Y])
            if vert3 == X:
                X+=1
                Xlist.append(X)
                Ylist.append(Y)
                step2d+=1
                stepsA.append(step2d)
            elif vert3 == Y:
                Y-=1
                Ylist.append(Y)
                Xlist.append(X)
                step2d+=1
                stepsA.append(step2d)
        
        while(X == 40 and Y == -40):
            vert4 = random.choice([X, Y])
            if vert4 == X:
                X-=1
                Xlist.append(X)
                Ylist.append(Y)
                step2d+=1
                stepsA.append(step2d)
            elif vert4 == Y:
                Y+=1
                Ylist.append(Y)
                Xlist.append(X)
                step2d+=1
                stepsA.append(step2d)
    
        if(X == 40 and Y == 0):
            break;
            
            print ("Done")
            
    '''plt.plot(Xlist, Ylist)
    plt.xlabel("X- position")
    plt.ylabel("Y-Postion")
    plt.title("Trajectory")
    plt.annotate("Starting Position", (-40,0))
    plt.annotate("($^\circ$C)", (40,0))'''
    
    
            
    return print("Steps: " + str(step2d), "Xlist:\n\n\n\n "  + str(Xlist) + "\n\n\n\n\n" + "Ylist:\n\n\n\n\n "+ str(Ylist) + "\n\n\n\n"+str(stepsA))
    ##return step2d
WalkTwoD()
'''def Instances():
    I = 1
    listN = []
    while I <= 1000:
        listN.append(WalkTwoD())
        I+=1
        
    
    average = sum(listN)/ len(listN)
        
    
    plt.hist(listN, density=True, bins=100, label = "Time Vs Occurence") 
    plt.title()
    plt.ylabel("Number of Occurances")
    plt.xlabel("Residence Time")
    return print(str(listN) + " Average: " + str(average))

Instances()
        '''


        
        
       

        
        
        
    
    
        
        
        
        
        
        
    



    
    



    

    

 
    

