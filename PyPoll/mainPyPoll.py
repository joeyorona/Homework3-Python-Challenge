import os
import csv

vote_total = 0
cand_list = []
cand1_pct = 0
cand2_pct = 0
cand3_pct = 0
cand4_pct = 0
Win = 0
winner = str
winner_index = 0
Counter = 0

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    #print(csv_header)

    # Read each row of data after the header
    for row in csvreader:       
        vote_total += 1
        cand_list.append(row[2])
        #print(vote_total)
    
    string = cand_list
    substring1 = "Khan"
    count1 = string.count(substring1)
    # print count1
    #print("Khan: ", count1)
    substring2 = "Correy"
    count2 = string.count(substring2)
    #print("Correy: ", count2)
    substring3 = "Li"
    count3 = string.count(substring3)
    #print("Li: ", count3)
    substring4 = "O'Tooley"
    count4 = string.count(substring4)
    #print("O'Tooley: ", count4)
    
    cand1_pct = (count1/vote_total)*100
    #print(str("%.3f%%" % cand1_pct))
    cand2_pct = (count2/vote_total)*100
    cand3_pct = (count3/vote_total)*100
    cand4_pct = (count4/vote_total)*100
    
    #winner_index = cand_list.index("Khan")
    #winner = cand_list[0]
    #print(winner)
    
    for value in range(len(cand_list)):
        if count1 > count2 and count3 and count4:
            winner = substring1
        elif count2 > count1 and count3 and count4:
            winner = substring2
        elif count3 > count1 and count2 and count4:
            winner = substring3
        else:
            count4 > count1 and count2 and count3
            winner = substring4

print("Election Results ")
print("------------------------")
print("Total Votes: ", str(vote_total))
print("------------------------")
print("Khan: ", str("%.3f%%" % cand1_pct) , str(count1))
print("Correy: ", str("%.3f%%" % cand2_pct) , str(count2))
print("Li: ", str("%.3f%%" % cand3_pct) , str(count3))
print("O'Tooley: ", str("%.3f%%" % cand4_pct) , str(count4))
print("------------------------")
print("Winner: ", str(winner))
print("------------------------")

import sys
file = open('election_data.txt', 'w')
sys.stdout = file

print("Election Results ")
print("------------------------")
print("Total Votes: ", str(vote_total))
print("------------------------")
print("Khan: ", str("%.3f%%" % cand1_pct) , str(count1))
print("Correy: ", str("%.3f%%" % cand2_pct) , str(count2))
print("Li: ", str("%.3f%%" % cand3_pct) , str(count3))
print("O'Tooley: ", str("%.3f%%" % cand4_pct) , str(count4))
print("------------------------")
print("Winner: ", str(winner))
print("------------------------")

file.close()