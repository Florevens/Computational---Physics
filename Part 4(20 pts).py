# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:18:40 2022

@author: flore
"""


from pylab import imshow,show
from numpy import zeros,linspace


N = 1000
Nmax = 32


#Creating NxN array of zeros
arr = zeros([N,N])

#Creating x component and y component to iterate over of same size of 2d array
x_arr = linspace(-2, 1, N)
y_arr = linspace(-1.5, 1.5, N)

# Using counters i and j to count current index, as well as x and y to keep track
# of the current values at the [i,j] indices.
for i,x in enumerate(x_arr):
    for j,y in enumerate(y_arr):
        
        #setting the initial value of the complex number Z
        Zo = 0 + 0j
        
        #setting the initial value of complex constant C to x and imag y
        C = x + y*1j
        
        #using step to count the iterations until maximum N is reached
        step = 0
        while(step <= Nmax):
            step+=1
            
            #The formula that will be used and reused again until the if statement
            #becomes true i.e Mandelbrot formula
            Zo = Zo**2 + C
            
            #Checks to see if the  absoluta value of Z is reached after many rinse
            #and repeat iterations, while keeping C constant.
            # if it reached, the program is stopped and we move on to the next value
            #of C
            if abs(Zo) > 2.0:
                #Adds the value we get for the amount of iteration it took
                #to reach the condition to the 2d array at indices i,j
                arr[i,j] += step
                break
            
            #If the previous condition is never reached, the pixel is then just zero
            else:
                arr[i,j] += 0
                
           
                
print(arr)

        
