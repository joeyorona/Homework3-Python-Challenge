import os
import csv

pltotal = 0
change = 0
avgchg = 0
pllist = []
month_list = []
change_list = []
totalchg = 0
highest = 0
lowest = 0
value = 0
lM = 0
hM = 0

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    #print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        
        pltotal += int(row[1])
        month_list.append(row[0])
        pllist.append(row[1])
    
    for value in range(len(pllist)):        
        #print(value)
        if value == 0:
            change = 0
            change_list.append(change)
        else:
            change = int(pllist[value]) - int(pllist[value-1])
            totalchg += change
            change_list.append(change)
    
    for value in range(len(change_list)):
        highest = max(change_list)
        lowest = min(change_list)

hM = (change_list.index(highest))
lM = (change_list.index(lowest))
hMonth = (month_list[hM])
lMonth = (month_list[lM])        
    
avgchg = totalchg/(len(change_list)-1)

print("Financial Analysis ")
print("----------------------------")
##outside of the For loop, it gives the final count
print("Total Months: " + str(len(month_list)))
print("Total: " + str(pltotal))
print("Average Change: " + str("%.2f" % avgchg))
print("Greatest Increase: " + (hMonth +" "+ str(highest)))
print("Greatest Decrease: " + (lMonth +" "+ str(lowest)))

import sys
file = open('budget_data.txt', 'w')
sys.stdout = file

print("Financial Analysis ")
print("----------------------------")
##outside of the For loop, it gives the final count
print("Total Months: " + str(len(month_list)))
print("Total: " + str(pltotal))
print("Average Change: " + str("%.2f" % avgchg))
print("Greatest Increase: " + (hMonth +" "+ str(highest)))
print("Greatest Decrease: " + (lMonth +" "+ str(lowest)))

file.close()