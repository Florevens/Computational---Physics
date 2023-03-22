#Radius of a circle (15 points)
#This program ask the user for the radius of a circle
#And then prints out the radius, area, and circumference of that circle
#author Florevens PH
#February 1, 2022---9:43am
import math

radius = float(input("What is the radius of your circle: "))
area = math.pi*(radius**2)
roundedArea = round(area, 1)
circumference = 2*math.pi*radius
roundedCircumference = round(circumference, 1)
print("Your radius is: " + str(radius))
print("Your area is: " + str(roundedArea))
print("Your circumference is: " + str(roundedCircumference))
