# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:01:12 2022

@author: flore
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import random
from random import choice


def Walk():
    x = -40
    x2 = 40
    steps = 0;
    i = x
    stepsPoint = []
    while(x <= i < x2):
        if i == -40:
            i+=1
            steps+=1
            stepsPoint.append(i)
        elif i < x2:
            i+= choice([i for i in range(-1,2) if i not in [0]])
            steps+=1
            stepsPoint.append(i)
    
        elif i == 40:
                break;
                #stepsPoint.append(i)
                
        plt.plot(i,steps)
        info = "Steps: ", steps, "count: ", i, "Point: ", stepsPoint
    
    return print(info)

Walk()

def WalkTwoD():
    X = -40
    Y = 0
    Z = 40
    step2d = 0
    I = -40
    Ylist = []
    Xlist = []
    
    while I <= X < Z and I <= Y < Z:
        while(X == -40 and Y == 0):
            leftEdge = random.choice([X, Y])
            if leftEdge == Y:
                Y+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
                while Y != 0:
                    leftEdge2 = random.choice([X, Y])
                    if leftEdge2 == Y:
                        Y+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Ylist.append(Y)
                    elif leftEdge2 == X:
                        X+=1
                        step2d+=1
                        Xlist.append(X)
                        
            elif leftEdge == X:
                X+=1
                step2d+=1
                Xlist.append(X)
                
        while(I < X < Z and I < Y < Z):
            allSteps = random.choice([X,Y])
            if allSteps == X:
                X+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Xlist.append(X)
            elif allSteps == Y:
                Y+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
              
        while(Y == -40 and X == 0):
                bottomEdge = random.choice([X, Y])
                if bottomEdge == Y: 
                    X+=choice([i for i in range(-1,2) if i not in [0]])
                    step2d+=1
                    Ylist.append(Y)
                    while X != 0:
                        bottomEdge2 = random.choice([X, Y])
                        if bottomEdge2 == X:
                            X+=choice([i for i in range(-1,2) if i not in [0]])
                            step2d+=1
                            Xlist.append(Y)
                        elif leftEdge2 == Y:
                            Y+=1
                            step2d+=1
                            Ylist.append(X)
                            break
                elif bottomEdge == Y:
                    Y+=1
                    step2d+=1
                    Ylist.append(Y)
            
        while (Y == 40 and X == 0):
            topEdge = random.choice([X, Y])
            if topEdge == X: 
                X+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Xlist.append(X)
                while X != 0:
                    topEdge2 = random.choice([X, Y])
                    if topEdge2 == X:
                        X+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Xlist.append(Y)
                    elif topEdge2 == Y:
                        Y-=1
                        step2d+=1
                        Ylist.append(Y)
                        break;
            elif topEdge == Y:
                Y-=1
                step2d+=1
                Ylist.append(Y)
        
        while(X == 40 and Y !=0):
            edgeControl1 = random.choice([X, Y])
            if edgeControl1 == Y:
                Y+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
                while Y != 0:
                    subEdge1 = random.choice([X, Y])
                    if subEdge1 == Y:
                        Y+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Ylist.append(Y)
                    elif subEdge1 == X:
                        X-=1
                        step2d+=1
                        Xlist.append(X)
                        break;
            elif edgeControl1 == X:
                X-=1
                step2d+=1
                Xlist.append(X)
                
        while(Y == 40 and X != 0):
            edgeControl2 =  random.choice([X, Y])
            if edgeControl2 == X:
                X+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Xlist.append(X)
                while X != 0:
                    subEdge2 = random.choice([X, Y])
                    if subEdge2 == X:
                        X+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Xlist.append(X)
    
                    elif subEdge2 == Y:
                        Y-=1
                        step2d+=1
                        Ylist.append(Y)
                        break;
            
            elif edgeControl2 == Y:
                Y-=1
                step2d+=1
                Ylist.append(Y)
            
        while(X == -40 and Y != 0):
            edgeControl3 = random.choice([X, Y])
            if edgeControl3 == Y:
                Y+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Ylist.append(Y)
                while Y != 0:
                    subEdge3 = random.choice([X, Y])
                    if subEdge3 == Y:
                        Y+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Ylist.append(Y)
                    elif subEdge3 == X:
                        X+=1
                        step2d+=1
                        Xlist.append(X)
                        break;
            elif edgeControl3 == X:
                X+=1
                step2d+=1
                Xlist.append(X)
                
        while(Y == -40 and X != 0):
            edgeControl4 = random.choice([X, Y])
            if edgeControl4 == X:
                X+=choice([i for i in range(-1,2) if i not in [0]])
                step2d+=1
                Xlist.append(X)
                while X != 0:
                    subEdge4 = random.choice([X, Y])
                    if subEdge4 == X:
                        X+=choice([i for i in range(-1,2) if i not in [0]])
                        step2d+=1
                        Xlist.append(X)
                    elif subEdge4 == Y:
                        Y+=1
                        step2d+=1
                        Ylist.append(Y)
                        break;
            elif edgeControl4 == Y:
                Y+=1
                step2d+=1
                Ylist.append(Y)
        
        while(X == -40 and Y == -40):
            vert1 = random.choice([X, Y])
            if vert1 == X:
                X+=1
                Xlist.append(X)
                step2d+=1
            elif vert1 == Y:
                Y+=1
                Ylist.append(Y)
                step2d+=1
        
        while(X == 40 and Y == 40):
            vert2 = random.choice([X, Y])
            if vert2 == X:
                X-=1
                Xlist.append(X)
                step2d+=1
            elif vert2 == Y:
                Y-=1
                Ylist.append(Y)
                step2d+=1
            
        while(X == -40 and Y == 40):
            vert3 = random.choice([X, Y])
            if vert3 == X:
                X+=1
                Xlist.append(X)
                step2d+=1
            elif vert3 == Y:
                Y-=1
                Ylist.append(Y)
                step2d+=1
        
        while(X == 40 and Y == -40):
            vert4 = random.choice([X, Y])
            if vert4 == X:
                X-=1
                Xlist.append(X)
                step2d+=1
            elif vert4 == Y:
                Y+=1
                Ylist.append(Y)
                step2d+=1
    
        while(X == 40 and Y == 0):
            Xlist.append(X)
            Ylist.append(Y)
            break;
        
                
        
                
            
    info = "Steps: " + str(step2d) + " Xlist: " +str(Xlist) + "\n" +  "Ylist: " + str(Ylist)
            
    return print(info)
                
WalkTwoD()



        
        
       

        
        
        
    
    
        
        
        
        
        
        
    



    
    



    

    

 
    

