#Leap Years, Precisely (15 points)
#author-Florevens Petithomme
#January 27, 2022---9:39AM

#This program takes in a user integer that represents a year and decide wether it is a leap year or not.

year = int(input("Enter your year: "))
print(year)
if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print("The given year is not a leap year")
elif (year % 4 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
    print("The given year is a leap year")
elif year % 4 != 0 or year % 100 != 0 or year % 400 != 0 :
    print("The given year is not a leap year")
        
