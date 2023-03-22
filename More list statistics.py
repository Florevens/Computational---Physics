

import math


voltages = []
voltages2 = []
i = 0
while i == len(voltages):
    volts = float(input("Please enter a voltage reading(enter a negative value to stop): "))
    if volts > 0:
        voltages.append(volts)
        voltages2.append(volts**2)
        i+=1
    else: 
        print(voltages)
        print(voltages2)
        average = sum(voltages)/ len(voltages)
        print(average)
        average2 = sum((l-average)**2 for l in voltages) / len(voltages)
        print(average2)
        standev = math.sqrt(average2)
        print(standev)

        
        
        