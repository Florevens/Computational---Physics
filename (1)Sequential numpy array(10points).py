# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:40:41 2022

@author: flore
"""

import numpy as np

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of colums: "))
list2d = []
number = 1
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(number)
        number+=1
    list2d.append(row)

array1 = np.array(list2d)

print(array1, "\n")

print("Column three: ", array1[:,2],"\n") 

print("Row four: ", array1[3], "\n")

print( "3 by 3 left: ", array1[0:3,0:3], "\n")

print("3 by 3 right: ", array1[0:3,-3:], "\n")


print("transpose array1: ", np.transpose(array1))








    
        
        
        
