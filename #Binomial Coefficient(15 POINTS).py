#Binomial Coefficient


import numpy

def binomial(n, k):
    n = int(input("Enter a number n:"))
    k = int(input("Enter a number k:"))
    listN = list(range(1, n+1))
    print(listN)
    factN = numpy.prod(listN)
    print(factN)
    
    listK = list(range(1, k+1))
    print(listK)
    factK = numpy.prod(listK)
    print(factK)
    listnk = list(range(1, (n-k)+1))
    print(listnk)
    factnk = numpy.prod(listnk)
    

    return factN/factK/factnk


