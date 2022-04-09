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
proffitloss = []

#link data
budgetdata = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")
print("------------------")

with open(budgetdata) as csvfile:
    csvreader=csv.reader(csvfile)
    next(csvreader, None)    
    

#total months with heading
    for row in csvreader:
        totalmonths+=1
    

#total amount of "Profit/Losses" over the entire period
        totalrev = totalrev + (int(row[1]))
    

#revenue change
        monthlychange = int(row[1])-pastrev
        pastrev = int(row[1])
        revchange.append(monthlychange)
        averagechange = round(sum(revchange)/totalmonths)

#greatest increase in rvenue
        if(monthlychange > highestrev):
            highestmonth = row[0]
            highestrev = monthlychange

    
    print("Total Months:", totalmonths)
    print("Total Revenue:" , totalrev)
    print("Monthly Change:", averagechange)
    print("Greatest Increase in Revenue", highestmonth, highestrev)
    