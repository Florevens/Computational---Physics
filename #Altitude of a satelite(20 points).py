#Altitude of a satelite
import math
G = 6.67*10**-11 # Gravitation constant, m3/kgs2
M = 5.97*10**24 #Mass of the earth, in KG
R  = 6371*1000  #radius of the earth, km


T = float(input("Please enter a period of rotation: "))

h = (((G*M*T**2)/(4*math.pi**2))**(1/3))-R
rounded_h = "{:.2f}".format(h)


if h < 0:
    print("Period not allowed")
else: 
    print("Your height is: " + rounded_h + " meters")
    

    
