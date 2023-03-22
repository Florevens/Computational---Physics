#Building a List 15 Points

voltages = []
i = 0
while i == len(voltages):
    volts = float(input("Please enter a voltage reading(enter a negative value to stop): "))
    if volts > 0:
        voltages.append(volts)
        i+=1
    else: 
        print(voltages)
        totReading = len(voltages)
        print("Total Reading: ", totReading)
        Largest = max(voltages)
        print ("The max of the list: ", "{0:.3f}".format(Largest))
        Smallest = min(voltages)
        print("The min of the list is: ", "{0:.3f}".format(Smallest))
        Average = sum(voltages)/len(voltages)
        print("The average of the list is: ", "{0:.3f}".format(Average))

    
