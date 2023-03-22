#Caculate physics equation
#This program asks the user for the distance
#and then figures outputs the time it would take
import math
from cmath import sqrt



distance = float(input("What is the given distance: "))
gravity = 9.8 # Acceleration of gravity
time = sqrt((2*distance)/gravity)
print(time)
print("Your time is: " + str(time) + " seconds")
print ("{0:.2f}".format(time))

