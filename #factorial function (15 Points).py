#fatorial funtcion

from sqlalchemy import false, true


n = float(input("Please enter a number: "))

if n<0 or not(n.is_integer()):
    print("Please enter a positive number")
elif n==0 or n==1:
    print("The factorial is 1")
else:
    factor = 1
    while(n>1):
        factor*=n
        n-=1
    
print(factor)
    
    

    
     
    
    