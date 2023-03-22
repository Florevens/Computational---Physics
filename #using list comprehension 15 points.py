#using list comprehension 15 points

from pyparsing import AtLineStart


to20 = [i for i in range(21)]
print(to20)

omit5 = [i for i in range(0,21)]
for i in omit5:
    if i%5 == 0:
        omit5.remove(i)
print(omit5)

Div5 = [i for i in range(0,20,5)]
print(Div5)

aList = [10, 20, 30]
bList = [3, 7, 9]

cList =[]
for j in aList:
    for k in bList:
        cList.append(j+k)
        
print(cList)
        
        



