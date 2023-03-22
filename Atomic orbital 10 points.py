#atomic orbital, nested for: 10 points

Nmax = int(input("Enter a number n:"))
states = 0
for n in range(Nmax+1):
    for l in range(n):
        for m in range(-l,l+1):
            states+=1
            print("n:",n ,"l: ",l , "m: ", m)
            
print("states: ", states)
        
            
