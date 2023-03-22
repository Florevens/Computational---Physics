#Leap years, rough
#This program takes in a user input
#and calculate if it is a leap year
#author-Florevens Petithomme
#February 1, 2022 10:41
year = int(input("What is the year: "))
if year%4 ==0:
    print(str(year) +" is a leap year")
else:
    print(str(year) + " is not a leap year")
    
