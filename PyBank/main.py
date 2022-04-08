#modules
import os
import csv

#trackers
totalmonths = 0
totalrev = 0
pastrev = 0
highestrev = 0
lowestrev = 0

#create revenue bucket
revchange = []

#link data
budgetdata = os.path.join("Resources", "budget_data.csv")

with open(budgetdata) as csvfile:
    csvreader=csv.reader(csvfile)
    print(csvreader)

#total months with heading
    for row in csvreader:
        totalmonths+=1
    print("Total Months:", totalmonths)




