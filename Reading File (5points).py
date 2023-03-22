# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:04:43 2022

@author: flore
"""
import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.loadtxt("Projectile2.txt")


fileObj = open("Projectile4.txt", "r") #opens the file in read mode
fileArray = fileObj.read().splitlines() #puts the file into an array
fileObj.close()
print(fileArray)

    
    